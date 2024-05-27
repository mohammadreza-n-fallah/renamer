# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(7200, 480)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Window)
        self.label.setMinimumSize(QtCore.QSize(0, 15))
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.dirEdit = QtWidgets.QLineEdit(Window)
        self.dirEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName("dirEdit")
        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 2)
        self.loadFilesButton = QtWidgets.QPushButton(Window)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout.addWidget(self.loadFilesButton, 1, 2, 1, 1)
        self.splitter = QtWidgets.QSplitter(Window)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(self.layoutWidget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout.addWidget(self.srcFileList)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(self.layoutWidget1)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout_2.addWidget(self.dstFileList)
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 3)
        self.prefixEdit = QtWidgets.QLineEdit(Window)
        self.prefixEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.prefixEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.prefixEdit.setObjectName("prefixEdit")
        self.gridLayout.addWidget(self.prefixEdit, 4, 0, 1, 1)
        self.extensionLabel = QtWidgets.QLabel(Window)
        self.extensionLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.extensionLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.extensionLabel.setObjectName("extensionLabel")
        self.gridLayout.addWidget(self.extensionLabel, 4, 1, 1, 1)
        self.renameFilesButton = QtWidgets.QPushButton(Window)
        self.renameFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameFilesButton.setObjectName("renameFilesButton")
        self.gridLayout.addWidget(self.renameFilesButton, 4, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Window)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "RP Renamer"))
        self.label.setText(_translate("Window", "Last Source Directory:"))
        self.loadFilesButton.setText(_translate("Window", "&Load Files"))
        self.label_2.setText(_translate("Window", "Files to Rename"))
        self.label_3.setText(_translate("Window", "Renamed Files"))
        self.label_4.setText(_translate("Window", "Filename Prefix:"))
        self.prefixEdit.setPlaceholderText(
            _translate("Window", "Rename your files to...")
        )
        self.extensionLabel.setText(_translate("Window", "*.jpg"))
        self.renameFilesButton.setText(_translate("Window", "&Rename"))
