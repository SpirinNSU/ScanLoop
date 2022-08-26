# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 464)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(490, 10, 51, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 481, 441))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 451, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_31 = QtWidgets.QLabel(self.groupBox_2)
        self.label_31.setGeometry(QtCore.QRect(140, 10, 61, 61))
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.lineEdit_number_of_peaks_to_search = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_number_of_peaks_to_search.setGeometry(QtCore.QRect(200, 20, 31, 31))
        self.lineEdit_number_of_peaks_to_search.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_number_of_peaks_to_search.setObjectName("lineEdit_number_of_peaks_to_search")
        self.lineEdit_min_peak_distance = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_min_peak_distance.setGeometry(QtCore.QRect(410, 20, 31, 31))
        self.lineEdit_min_peak_distance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_min_peak_distance.setObjectName("lineEdit_min_peak_distance")
        self.label_32 = QtWidgets.QLabel(self.groupBox_2)
        self.label_32.setGeometry(QtCore.QRect(350, 10, 61, 61))
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(260, 10, 41, 61))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.lineEdit_min_peak_level = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_min_peak_level.setGeometry(QtCore.QRect(300, 20, 31, 31))
        self.lineEdit_min_peak_level.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_min_peak_level.setObjectName("lineEdit_min_peak_level")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(30, 40, 41, 31))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 41, 31))
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.lineEdit_min_wave = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_min_wave.setGeometry(QtCore.QRect(80, 20, 41, 20))
        self.lineEdit_min_wave.setObjectName("lineEdit_min_wave")
        self.lineEdit_max_wave = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_max_wave.setGeometry(QtCore.QRect(80, 50, 41, 20))
        self.lineEdit_max_wave.setObjectName("lineEdit_max_wave")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 70, 451, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_plot_results_separately = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_plot_results_separately.setGeometry(QtCore.QRect(10, 20, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.checkBox_plot_results_separately.setFont(font)
        self.checkBox_plot_results_separately.setWhatsThis("")
        self.checkBox_plot_results_separately.setTristate(False)
        self.checkBox_plot_results_separately.setObjectName("checkBox_plot_results_separately")
        self.checkBox_find_widths = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_find_widths.setGeometry(QtCore.QRect(10, 50, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.checkBox_find_widths.setFont(font)
        self.checkBox_find_widths.setWhatsThis("")
        self.checkBox_find_widths.setTristate(False)
        self.checkBox_find_widths.setObjectName("checkBox_find_widths")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(170, 10, 271, 91))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setGeometry(QtCore.QRect(30, 10, 81, 21))
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.lineEdit_N_points_for_fitting = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_N_points_for_fitting.setEnabled(True)
        self.lineEdit_N_points_for_fitting.setGeometry(QtCore.QRect(60, 30, 21, 21))
        self.lineEdit_N_points_for_fitting.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_N_points_for_fitting.setObjectName("lineEdit_N_points_for_fitting")
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setEnabled(False)
        self.label_35.setGeometry(QtCore.QRect(60, 60, 81, 31))
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.checkBox_iterate_different_N_points = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_iterate_different_N_points.setEnabled(True)
        self.checkBox_iterate_different_N_points.setGeometry(QtCore.QRect(40, 60, 16, 21))
        self.checkBox_iterate_different_N_points.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.checkBox_iterate_different_N_points.setText("")
        self.checkBox_iterate_different_N_points.setAutoRepeat(False)
        self.checkBox_iterate_different_N_points.setAutoRepeatInterval(-5)
        self.checkBox_iterate_different_N_points.setObjectName("checkBox_iterate_different_N_points")
        self.lineEdit_max_N_points_for_fitting = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_max_N_points_for_fitting.setEnabled(False)
        self.lineEdit_max_N_points_for_fitting.setGeometry(QtCore.QRect(150, 30, 41, 21))
        self.lineEdit_max_N_points_for_fitting.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_max_N_points_for_fitting.setObjectName("lineEdit_max_N_points_for_fitting")
        self.label_34 = QtWidgets.QLabel(self.groupBox_4)
        self.label_34.setGeometry(QtCore.QRect(130, 10, 101, 21))
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.comboBox_iterating_cost_function_type = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_iterating_cost_function_type.setEnabled(False)
        self.comboBox_iterating_cost_function_type.setGeometry(QtCore.QRect(190, 60, 69, 22))
        self.comboBox_iterating_cost_function_type.setObjectName("comboBox_iterating_cost_function_type")
        self.comboBox_iterating_cost_function_type.addItem("")
        self.comboBox_iterating_cost_function_type.addItem("")
        self.label_39 = QtWidgets.QLabel(self.groupBox_4)
        self.label_39.setGeometry(QtCore.QRect(140, 60, 41, 21))
        self.label_39.setWordWrap(True)
        self.label_39.setObjectName("label_39")
        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 270, 451, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setMinimumSize(QtCore.QSize(220, 50))
        self.groupBox_11.setMaximumSize(QtCore.QSize(270000, 50))
        self.groupBox_11.setObjectName("groupBox_11")
        self.lineEdit_FFTFilter_low_freq_edge = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_FFTFilter_low_freq_edge.setGeometry(QtCore.QRect(210, 23, 61, 21))
        self.lineEdit_FFTFilter_low_freq_edge.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_FFTFilter_low_freq_edge.setObjectName("lineEdit_FFTFilter_low_freq_edge")
        self.lineEdit_FFTFilter_high_freq_edge = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_FFTFilter_high_freq_edge.setGeometry(QtCore.QRect(358, 23, 51, 21))
        self.lineEdit_FFTFilter_high_freq_edge.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_FFTFilter_high_freq_edge.setObjectName("lineEdit_FFTFilter_high_freq_edge")
        self.label_40 = QtWidgets.QLabel(self.groupBox_11)
        self.label_40.setEnabled(False)
        self.label_40.setGeometry(QtCore.QRect(150, 18, 81, 31))
        self.label_40.setWordWrap(True)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setEnabled(False)
        self.label_41.setGeometry(QtCore.QRect(306, 18, 81, 31))
        self.label_41.setWordWrap(True)
        self.label_41.setObjectName("label_41")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 330, 451, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy)
        self.groupBox_12.setMinimumSize(QtCore.QSize(220, 50))
        self.groupBox_12.setMaximumSize(QtCore.QSize(270000, 120))
        self.groupBox_12.setObjectName("groupBox_12")
        self.lineEdit_quantum_numbers_fitter_p_max = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_quantum_numbers_fitter_p_max.setGeometry(QtCore.QRect(80, 20, 61, 21))
        self.lineEdit_quantum_numbers_fitter_p_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_quantum_numbers_fitter_p_max.setObjectName("lineEdit_quantum_numbers_fitter_p_max")
        self.label_36 = QtWidgets.QLabel(self.groupBox_12)
        self.label_36.setGeometry(QtCore.QRect(20, 20, 41, 21))
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.checkBox_quantum_numbers_fitter_dispersion = QtWidgets.QCheckBox(self.groupBox_12)
        self.checkBox_quantum_numbers_fitter_dispersion.setGeometry(QtCore.QRect(160, 20, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.checkBox_quantum_numbers_fitter_dispersion.setFont(font)
        self.checkBox_quantum_numbers_fitter_dispersion.setWhatsThis("")
        self.checkBox_quantum_numbers_fitter_dispersion.setChecked(True)
        self.checkBox_quantum_numbers_fitter_dispersion.setTristate(False)
        self.checkBox_quantum_numbers_fitter_dispersion.setObjectName("checkBox_quantum_numbers_fitter_dispersion")
        self.comboBox_quantum_numbers_fitter_polarizations = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_quantum_numbers_fitter_polarizations.setGeometry(QtCore.QRect(370, 20, 69, 22))
        self.comboBox_quantum_numbers_fitter_polarizations.setObjectName("comboBox_quantum_numbers_fitter_polarizations")
        self.comboBox_quantum_numbers_fitter_polarizations.addItem("")
        self.comboBox_quantum_numbers_fitter_polarizations.addItem("")
        self.label_37 = QtWidgets.QLabel(self.groupBox_12)
        self.label_37.setGeometry(QtCore.QRect(270, 20, 81, 21))
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_12)
        self.label_38.setGeometry(QtCore.QRect(250, 60, 101, 21))
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName("label_38")
        self.comboBox_quantum_numbers_fitter_type_of_optimizer = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.setGeometry(QtCore.QRect(370, 60, 69, 22))
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.setObjectName("comboBox_quantum_numbers_fitter_type_of_optimizer")
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.addItem("")
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.addItem("")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 20, 451, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy)
        self.groupBox_13.setMinimumSize(QtCore.QSize(220, 50))
        self.groupBox_13.setMaximumSize(QtCore.QSize(270000, 50))
        self.groupBox_13.setObjectName("groupBox_13")
        self.comboBox_type_of_spectrogram = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_type_of_spectrogram.setGeometry(QtCore.QRect(228, 20, 201, 22))
        self.comboBox_type_of_spectrogram.setObjectName("comboBox_type_of_spectrogram")
        self.comboBox_type_of_spectrogram.addItem("")
        self.comboBox_type_of_spectrogram.addItem("")
        self.comboBox_type_of_spectrogram.addItem("")
        self.comboBox_type_of_spectrogram.addItem("")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.checkBox_iterate_different_N_points.clicked['bool'].connect(self.lineEdit_N_points_for_fitting.setDisabled)
        self.checkBox_iterate_different_N_points.clicked['bool'].connect(self.lineEdit_max_N_points_for_fitting.setEnabled)
        self.checkBox_find_widths.clicked['bool'].connect(self.groupBox_4.setEnabled)
        self.checkBox_iterate_different_N_points.clicked['bool'].connect(self.comboBox_iterating_cost_function_type.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Analyzer options"))
        self.groupBox_2.setTitle(_translate("Dialog", "Find_peaks parameters"))
        self.label_31.setText(_translate("Dialog", "<html><head/><body><p>Number of peaks to be find</p></body></html>"))
        self.lineEdit_number_of_peaks_to_search.setText(_translate("Dialog", "1"))
        self.lineEdit_min_peak_distance.setText(_translate("Dialog", "60"))
        self.label_32.setText(_translate("Dialog", "<html><head/><body><p>Distance between peaks</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p>Peak height, dB</p></body></html>"))
        self.lineEdit_min_peak_level.setText(_translate("Dialog", "3"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p>λ<span style=\" vertical-align:sub;\">max</span>, nm</p></body></html>"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p>λ<span style=\" vertical-align:sub;\">min</span>, nm</p></body></html>"))
        self.lineEdit_min_wave.setText(_translate("Dialog", "1530"))
        self.lineEdit_max_wave.setText(_translate("Dialog", "1590"))
        self.groupBox_3.setTitle(_translate("Dialog", "Advanced"))
        self.checkBox_plot_results_separately.setText(_translate("Dialog", "Plot separately"))
        self.checkBox_find_widths.setText(_translate("Dialog", "find widths"))
        self.groupBox_4.setTitle(_translate("Dialog", "find width parameters"))
        self.label_33.setText(_translate("Dialog", "<html><head/><body><p>N_points for fit</p></body></html>"))
        self.lineEdit_N_points_for_fitting.setText(_translate("Dialog", "0"))
        self.label_35.setText(_translate("Dialog", "<html><head/><body><p>iterating over N_points</p></body></html>"))
        self.lineEdit_max_N_points_for_fitting.setText(_translate("Dialog", "100"))
        self.label_34.setText(_translate("Dialog", "<html><head/><body><p>max N_points for fit</p></body></html>"))
        self.comboBox_iterating_cost_function_type.setItemText(0, _translate("Dialog", "linewidth"))
        self.comboBox_iterating_cost_function_type.setItemText(1, _translate("Dialog", "net error"))
        self.label_39.setText(_translate("Dialog", "<html><head/><body><p>minimize</p></body></html>"))
        self.groupBox_11.setTitle(_translate("Dialog", "FFT filter options"))
        self.lineEdit_FFTFilter_low_freq_edge.setText(_translate("Dialog", "0.00001"))
        self.lineEdit_FFTFilter_high_freq_edge.setText(_translate("Dialog", "0.01"))
        self.label_40.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Min freq</p></body></html>"))
        self.label_41.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Max freq</p></body></html>"))
        self.groupBox_12.setTitle(_translate("Dialog", "Quantum number fitter parameters"))
        self.lineEdit_quantum_numbers_fitter_p_max.setText(_translate("Dialog", "3"))
        self.label_36.setText(_translate("Dialog", "<html><head/><body><p>P_max</p></body></html>"))
        self.checkBox_quantum_numbers_fitter_dispersion.setText(_translate("Dialog", "dispersion"))
        self.comboBox_quantum_numbers_fitter_polarizations.setItemText(0, _translate("Dialog", "both"))
        self.comboBox_quantum_numbers_fitter_polarizations.setItemText(1, _translate("Dialog", "single"))
        self.label_37.setText(_translate("Dialog", "<html><head/><body><p>Polarizations</p></body></html>"))
        self.label_38.setText(_translate("Dialog", "<html><head/><body><p>Type of optimizer</p></body></html>"))
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.setItemText(0, _translate("Dialog", "bruteforce"))
        self.comboBox_quantum_numbers_fitter_type_of_optimizer.setItemText(1, _translate("Dialog", "Nelder-Mead"))
        self.groupBox_13.setTitle(_translate("Dialog", "Plotted value"))
        self.comboBox_type_of_spectrogram.setItemText(0, _translate("Dialog", "insertion losses"))
        self.comboBox_type_of_spectrogram.setItemText(1, _translate("Dialog", "chromatic dispersion"))
        self.comboBox_type_of_spectrogram.setItemText(2, _translate("Dialog", "first polarization"))
        self.comboBox_type_of_spectrogram.setItemText(3, _translate("Dialog", "second polarization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

