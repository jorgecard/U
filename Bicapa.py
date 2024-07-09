import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import queue
import numpy as np
import time
from PyQt5 import QtCore, QtWidgets, QtGui
import pyqtgraph as pg
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QInputDialog, QLineEdit, QFileDialog
import os
import pandas as pd
from scipy.optimize import minimize

dir_actual = os.path.dirname(os.path.abspath(__file__))
dir_interfaz = os.path.join(dir_actual, "Qt")
nombre_interfaz = "interfaz_puestas_a_tierra.ui"
ruta_interfaz = os.path.join(dir_interfaz, nombre_interfaz)
nombre_logo = "nano.png"
ruta_logo = os.path.join(dir_interfaz, nombre_logo)

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = [fig.add_subplot(221), fig.add_subplot(222), fig.add_subplot(223), fig.add_subplot(224)]
        super(MplCanvas, self).__init__(fig)
        fig.tight_layout()

class LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi(ruta_interfaz, self)
        self.resize(888, 600)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(ruta_logo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle('Bicapa')
        
        # Establecer la página predeterminada al arrancar
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_0)
        # self.bt_log_in.clicked.connect(self.log_in)
        # acceder a las paginas
        # self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_login))
        # self.ui.pushButton_gen.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        # self.ui.pushButton_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        # self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # self.ui.pushButton_alarms.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_alarms))
        # self.ui.pushButton_log_ins.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_log_ins))
        self.ui.pushButton_g.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.ui.pushButton_c_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_0))
        self.pushButton_e.clicked.connect(self.open_dialog_box)
        self.pushButton_c.clicked.connect(self.Two_Layer_Parameters)
        
    def open_dialog_box(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Open File', dir_actual, 'All Files (*)')
        self.path_lb.setText(self.filename)
        self.load_data()
        
    def load_data(self):
        df = pd.read_excel(self.filename)
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df.iat[i, j])))
        self.X_a = df.iloc[:, 0].values
        self.Y_a = df.iloc[:, 1].values
        print("X_a:", self.X_a)
        print("Y_a:", self.Y_a)

    def Resistivity_0(self, a=2, ro=[100,200], h=1.5, Np=100):
        a_ro = np.array(ro)
        k = (a_ro[1:] - a_ro[:-1]) / (a_ro[1:] + a_ro[:-1])
        Suma1 = 0
        for q in range(1, Np):
            kn = k[0]**q
            cn = (2*q*h/a)**2
            c1 = kn / np.sqrt(1 + cn)
            c2 = kn / np.sqrt(4 + cn)
            Suma1 += (c1 - c2)
        roc = ro[0] * (1 + 4 * Suma1)
        return roc
    
    def Error_ro1(self, Xd, M_a, M_ro):
        self.p_aj = []
        NN = len(M_a)
        S_errorc = 0
        for q in range(NN):
            ro_aj = self.Resistivity_0(M_a[q], Xd[:2], Xd[2])
            self.p_aj.append(ro_aj)
            ec = ((M_ro[q] - ro_aj) / M_ro[q])**2
            S_errorc += ec
        return S_errorc
    
    def capture(self, x):
        self.x_values.append(x)
    
    def Two_Layer_Parameters(self):
        self.x_values = []
        RES_0 = minimize(self.Error_ro1, [800, 200, 1], (self.X_a, self.Y_a), method='Nelder-Mead', callback=self.capture)
        print("Respuesta: \n", RES_0)
        print('----------------')
        print('X_a (distancias)= ', self.X_a)
        print('Y_a (resistividad)= ', self.Y_a)
        print('----------------')
        print('rho 1=', RES_0.x[0])
        print('rho 2=', RES_0.x[1])
        print('h    =', RES_0.x[2])
        self.h = RES_0.x[2]
        # 'rho 1='
        self.label_rho_1.setText(str(round(RES_0.x[0],3)))
        # 'rho 2='
        self.label_rho_2.setText(str(round(RES_0.x[1],3)))
        # h
        self.label_h.setText(str(round(RES_0.x[2],3)))
        
        # Actualizar labels con nit, nfev y gradiente del error
        self.label_nit.setText(str(RES_0.nit))
        self.label_fev.setText(str(RES_0.nfev))
        if 'jac' in RES_0:
            self.label_grad.setText(str(RES_0.jac))
        else:
            self.label_grad.setText("N/A")
            
        # Llamar a la función para crear las gráficas
        self.create_plots()
    
    def create_plots(self):
        # Convertir los valores capturados a un array
        x_values_array = np.array(self.x_values)
        # Crear un arreglo de gráficas de 3 filas y 1 columna (cada variable en una fila)
        # fig1, axs = plt.subplots(3, 1, figsize=(8, 5))
        fig1, axs = plt.subplots(3, 1)
        # Graficar los valores de rho1 en función de las iteraciones
        iterations = range(len(x_values_array))
        axs[0].plot(iterations, x_values_array[:, 0], marker='.', linestyle='-', color='blue')
        axs[0].set_ylabel("rho 1 [Ohm-m]")
        axs[0].grid(True)
        # Graficar los valores de rho2 en función de las iteraciones
        axs[1].plot(iterations, x_values_array[:, 1], marker='.', linestyle='-', color='green')
        axs[1].set_ylabel("rho 2 [Ohm-m]")
        axs[1].grid(True)
        # Graficar los valores de h en función de las iteraciones
        axs[2].plot(iterations, x_values_array[:, 2], marker='.', linestyle='-', color='red')
        axs[2].set_ylabel("h [m]")
        axs[2].set_xlabel("Iteraciones")
        axs[2].grid(True)
        
        # Mostrar la gráfica en el widget_it
        canvas1 = FigureCanvas(fig1)
        layout1 = QVBoxLayout(self.ui.widget_it)
        layout1.addWidget(canvas1)
        self.ui.widget_it.setLayout(layout1)
        
        # Crear la gráfica de p_aj vs la distancia y Y_a vs distancia
        # fig2, ax = plt.subplots(figsize=(5, 3))
        fig2, ax = plt.subplots()
        ax.plot(self.X_a, self.p_aj, marker='.', linestyle='-', color='purple', label='Resistividad Aparente Calculada')
        ax.plot(self.X_a, self.Y_a, marker='.', linestyle='-', color='green', label='Resistividad Aparente Medida')
        ax.set_xlabel("a [m]")
        ax.set_ylabel("rho [Ohm-m]")
        ax.grid(True)
        # ax.set_title("Comparación entre los datos de Resistividad Aparentes Calculados vs Medidos")
        ax.legend()
        
        # Mostrar la gráfica en el widget_res
        canvas2 = FigureCanvas(fig2)
        layout2 = QVBoxLayout(self.ui.widget_res)
        layout2.addWidget(canvas2)
        self.ui.widget_res.setLayout(layout2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LIVE_PLOT_APP()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()