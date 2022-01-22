# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 621)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1025, 559))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.CVExplorer = QtWidgets.QLabel(self.centralwidget)
        self.CVExplorer.setObjectName("CVExplorer")
        self.gridLayout.addWidget(self.CVExplorer, 0, 2, 1, 1)
        self.CVTreeWidget = CVTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CVTreeWidget.sizePolicy().hasHeightForWidth())
        self.CVTreeWidget.setSizePolicy(sizePolicy)
        self.CVTreeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.CVTreeWidget.setHeaderHidden(True)
        self.CVTreeWidget.setObjectName("CVTreeWidget")
        self.CVTreeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.CVTreeWidget, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(93, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cvanalysis/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(93, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/minus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.MplCanvas_label = QtWidgets.QLabel(self.centralwidget)
        self.MplCanvas_label.setObjectName("MplCanvas_label")
        self.gridLayout.addWidget(self.MplCanvas_label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.manual_fit_button = QtWidgets.QToolButton(self.centralwidget)
        self.manual_fit_button.setMinimumSize(QtCore.QSize(100, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.manual_fit_button.setIcon(icon2)
        self.manual_fit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.manual_fit_button.setObjectName("manual_fit_button")
        self.horizontalLayout_2.addWidget(self.manual_fit_button)
        self.automatic_fit_button = QtWidgets.QToolButton(self.centralwidget)
        self.automatic_fit_button.setMinimumSize(QtCore.QSize(100, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/auto-flash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.automatic_fit_button.setIcon(icon3)
        self.automatic_fit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.automatic_fit_button.setAutoRaise(False)
        self.automatic_fit_button.setObjectName("automatic_fit_button")
        self.horizontalLayout_2.addWidget(self.automatic_fit_button)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 2, 1, 1)
        self.SCVAData_gridlayout = QtWidgets.QGridLayout()
        self.SCVAData_gridlayout.setContentsMargins(-1, 10, -1, -1)
        self.SCVAData_gridlayout.setObjectName("SCVAData_gridlayout")
        self.cathode_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cathode_label.sizePolicy().hasHeightForWidth())
        self.cathode_label.setSizePolicy(sizePolicy)
        self.cathode_label.setMinimumSize(QtCore.QSize(256, 17))
        self.cathode_label.setMaximumSize(QtCore.QSize(16777215, 17))
        self.cathode_label.setObjectName("cathode_label")
        self.SCVAData_gridlayout.addWidget(self.cathode_label, 0, 2, 1, 1)
        self.cathode_ip_value = QtWidgets.QLineEdit(self.centralwidget)
        self.cathode_ip_value.setReadOnly(True)
        self.cathode_ip_value.setObjectName("cathode_ip_value")
        self.SCVAData_gridlayout.addWidget(self.cathode_ip_value, 1, 2, 1, 1)
        self.anode_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anode_label.sizePolicy().hasHeightForWidth())
        self.anode_label.setSizePolicy(sizePolicy)
        self.anode_label.setMinimumSize(QtCore.QSize(256, 17))
        self.anode_label.setMaximumSize(QtCore.QSize(16777215, 17))
        self.anode_label.setObjectName("anode_label")
        self.SCVAData_gridlayout.addWidget(self.anode_label, 0, 1, 1, 1)
        self.cathode_ippos_value = QtWidgets.QLineEdit(self.centralwidget)
        self.cathode_ippos_value.setText("")
        self.cathode_ippos_value.setReadOnly(True)
        self.cathode_ippos_value.setObjectName("cathode_ippos_value")
        self.SCVAData_gridlayout.addWidget(self.cathode_ippos_value, 3, 2, 1, 1)
        self.anode_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.anode_ip_label.setObjectName("anode_ip_label")
        self.SCVAData_gridlayout.addWidget(self.anode_ip_label, 1, 0, 1, 1)
        self.anode_ip_value = QtWidgets.QLineEdit(self.centralwidget)
        self.anode_ip_value.setText("")
        self.anode_ip_value.setReadOnly(True)
        self.anode_ip_value.setObjectName("anode_ip_value")
        self.SCVAData_gridlayout.addWidget(self.anode_ip_value, 1, 1, 1, 1)
        self.anode_ippos_label = QtWidgets.QLabel(self.centralwidget)
        self.anode_ippos_label.setObjectName("anode_ippos_label")
        self.SCVAData_gridlayout.addWidget(self.anode_ippos_label, 3, 0, 1, 1)
        self.anode_ippos_value = QtWidgets.QLineEdit(self.centralwidget)
        self.anode_ippos_value.setReadOnly(True)
        self.anode_ippos_value.setObjectName("anode_ippos_value")
        self.SCVAData_gridlayout.addWidget(self.anode_ippos_value, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(105, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.SCVAData_gridlayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.SCVAData_gridlayout, 4, 0, 1, 1)
        self.MplCanvas_layout = QtWidgets.QGridLayout()
        self.MplCanvas_layout.setObjectName("MplCanvas_layout")
        self.MplCanvas = MplCanvas(self.centralwidget)
        self.MplCanvas.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplCanvas.sizePolicy().hasHeightForWidth())
        self.MplCanvas.setSizePolicy(sizePolicy)
        self.MplCanvas.setMinimumSize(QtCore.QSize(480, 440))
        self.MplCanvas.setObjectName("MplCanvas")
        self.MplCanvas_layout.addWidget(self.MplCanvas, 0, 0, 1, 1)
        self.MplCanvasButtons_layout = QtWidgets.QVBoxLayout()
        self.MplCanvasButtons_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.MplCanvasButtons_layout.setContentsMargins(-1, 0, -1, 0)
        self.MplCanvasButtons_layout.setSpacing(12)
        self.MplCanvasButtons_layout.setObjectName("MplCanvasButtons_layout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label.setObjectName("label")
        self.MplCanvasButtons_layout.addWidget(self.label)
        self.anode_current_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.anode_current_checkbox.setChecked(True)
        self.anode_current_checkbox.setObjectName("anode_current_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.anode_current_checkbox)
        self.anode_capfit_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.anode_capfit_checkbox.setChecked(True)
        self.anode_capfit_checkbox.setObjectName("anode_capfit_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.anode_capfit_checkbox)
        self.anode_ip_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.anode_ip_checkbox.setChecked(True)
        self.anode_ip_checkbox.setObjectName("anode_ip_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.anode_ip_checkbox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 17))
        self.label_2.setObjectName("label_2")
        self.MplCanvasButtons_layout.addWidget(self.label_2)
        self.cathode_current_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.cathode_current_checkbox.setChecked(True)
        self.cathode_current_checkbox.setObjectName("cathode_current_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.cathode_current_checkbox)
        self.cathode_capfit_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.cathode_capfit_checkbox.setChecked(True)
        self.cathode_capfit_checkbox.setObjectName("cathode_capfit_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.cathode_capfit_checkbox)
        self.cathode_ip_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.cathode_ip_checkbox.setChecked(True)
        self.cathode_ip_checkbox.setObjectName("cathode_ip_checkbox")
        self.MplCanvasButtons_layout.addWidget(self.cathode_ip_checkbox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.MplCanvasButtons_layout.addItem(spacerItem2)
        self.MplCanvas_layout.addLayout(self.MplCanvasButtons_layout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.MplCanvas_layout.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.MplCanvas_layout, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1025, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CVExplorer.setText(_translate("MainWindow", "Explorer"))
        self.toolButton.setText(_translate("MainWindow", "    Add"))
        self.toolButton_2.setText(_translate("MainWindow", " Remove"))
        self.MplCanvas_label.setText(_translate("MainWindow", "Cyclic Voltammetry Plot"))
        self.manual_fit_button.setText(_translate("MainWindow", "Manual fit"))
        self.automatic_fit_button.setText(_translate("MainWindow", " Auto fit"))
        self.cathode_label.setText(_translate("MainWindow", "Cathode"))
        self.anode_label.setText(_translate("MainWindow", "Anode"))
        self.anode_ip_label.setText(_translate("MainWindow", "ip"))
        self.anode_ippos_label.setText(_translate("MainWindow", "ip position"))
        self.label.setText(_translate("MainWindow", "Anode plot"))
        self.anode_current_checkbox.setText(_translate("MainWindow", "Current"))
        self.anode_capfit_checkbox.setText(_translate("MainWindow", "Cap. fit"))
        self.anode_ip_checkbox.setText(_translate("MainWindow", "Peak ip"))
        self.label_2.setText(_translate("MainWindow", "Cathode plot"))
        self.cathode_current_checkbox.setText(_translate("MainWindow", "Current"))
        self.cathode_capfit_checkbox.setText(_translate("MainWindow", "Cap. fit"))
        self.cathode_ip_checkbox.setText(_translate("MainWindow", "Peak ip"))

from cvanalysis.gui.cvtreewidget import CVTreeWidget
from cvanalysis.gui.mplcanvas import MplCanvas
from . import icons_rc
