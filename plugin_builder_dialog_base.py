# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plugin_builder_dialog_base.ui'
#
# Created: Wed Apr 16 13:26:49 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PluginBuilderDialogBase(object):
    def setupUi(self, PluginBuilderDialogBase):
        PluginBuilderDialogBase.setObjectName(_fromUtf8("PluginBuilderDialogBase"))
        PluginBuilderDialogBase.resize(908, 601)
        PluginBuilderDialogBase.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(PluginBuilderDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.web_view = QtWebKit.QWebView(PluginBuilderDialogBase)
        self.web_view.setMinimumSize(QtCore.QSize(380, 390))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(",Verdana,sans"))
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.web_view.setFont(font)
        self.web_view.setStyleSheet(_fromUtf8("QWebView{\n"
"    font: Georgia, Verdana, sans;\n"
"    font-size:1.0em;\n"
"    background-color: rgb(210, 255, 217);\n"
"    border-left: solid 2px black;\n"
"}"))
        self.web_view.setObjectName(_fromUtf8("web_view"))
        self.gridLayout.addWidget(self.web_view, 0, 0, 15, 1)
        self.line = QtGui.QFrame(PluginBuilderDialogBase)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 15, 2)
        self.label_10 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 3, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(PluginBuilderDialogBase)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.class_name = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.class_name.setMinimumSize(QtCore.QSize(300, 0))
        self.class_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.class_name.setText(_fromUtf8(""))
        self.class_name.setObjectName(_fromUtf8("class_name"))
        self.horizontalLayout.addWidget(self.class_name)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.title = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.title.setMinimumSize(QtCore.QSize(300, 0))
        self.title.setMaximumSize(QtCore.QSize(300, 16777215))
        self.title.setText(_fromUtf8(""))
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout_2.addWidget(self.title)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.description = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.description.setMinimumSize(QtCore.QSize(300, 0))
        self.description.setMaximumSize(QtCore.QSize(300, 16777215))
        self.description.setText(_fromUtf8(""))
        self.description.setObjectName(_fromUtf8("description"))
        self.horizontalLayout_3.addWidget(self.description)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.version_no = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.version_no.setMinimumSize(QtCore.QSize(60, 0))
        self.version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.version_no.setObjectName(_fromUtf8("version_no"))
        self.horizontalLayout_4.addWidget(self.version_no)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 2, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.min_version_no = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.min_version_no.setMinimumSize(QtCore.QSize(60, 0))
        self.min_version_no.setMaximumSize(QtCore.QSize(60, 16777215))
        self.min_version_no.setObjectName(_fromUtf8("min_version_no"))
        self.horizontalLayout_5.addWidget(self.min_version_no)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 2, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        self.label_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        self.menu_text = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.menu_text.setMinimumSize(QtCore.QSize(300, 0))
        self.menu_text.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_text.setText(_fromUtf8(""))
        self.menu_text.setObjectName(_fromUtf8("menu_text"))
        self.horizontalLayout_6.addWidget(self.menu_text)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 2, 1, 2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_7.setMinimumSize(QtCore.QSize(150, 0))
        self.label_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.company_name = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.company_name.setMinimumSize(QtCore.QSize(300, 0))
        self.company_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.company_name.setText(_fromUtf8(""))
        self.company_name.setObjectName(_fromUtf8("company_name"))
        self.horizontalLayout_7.addWidget(self.company_name)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 2, 1, 2)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_8.setMinimumSize(QtCore.QSize(150, 0))
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.email_address = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.email_address.setMinimumSize(QtCore.QSize(300, 0))
        self.email_address.setMaximumSize(QtCore.QSize(300, 16777215))
        self.email_address.setText(_fromUtf8(""))
        self.email_address.setObjectName(_fromUtf8("email_address"))
        self.horizontalLayout_8.addWidget(self.email_address)
        self.gridLayout.addLayout(self.horizontalLayout_8, 8, 2, 1, 2)
        self.label_14 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 9, 3, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_9 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.tracker = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.tracker.setMinimumSize(QtCore.QSize(300, 0))
        self.tracker.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tracker.setObjectName(_fromUtf8("tracker"))
        self.horizontalLayout_9.addWidget(self.tracker)
        self.gridLayout.addLayout(self.horizontalLayout_9, 10, 3, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_11 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_10.addWidget(self.label_11)
        self.homepage = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.homepage.setMinimumSize(QtCore.QSize(300, 0))
        self.homepage.setMaximumSize(QtCore.QSize(300, 16777215))
        self.homepage.setObjectName(_fromUtf8("homepage"))
        self.horizontalLayout_10.addWidget(self.homepage)
        self.gridLayout.addLayout(self.horizontalLayout_10, 11, 3, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.repository = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.repository.setMinimumSize(QtCore.QSize(300, 0))
        self.repository.setMaximumSize(QtCore.QSize(300, 16777215))
        self.repository.setObjectName(_fromUtf8("repository"))
        self.horizontalLayout_12.addWidget(self.repository)
        self.gridLayout.addLayout(self.horizontalLayout_12, 12, 3, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(PluginBuilderDialogBase)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        self.label_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.tags = QtGui.QLineEdit(PluginBuilderDialogBase)
        self.tags.setMinimumSize(QtCore.QSize(300, 0))
        self.tags.setMaximumSize(QtCore.QSize(300, 16777215))
        self.tags.setObjectName(_fromUtf8("tags"))
        self.horizontalLayout_11.addWidget(self.tags)
        self.gridLayout.addLayout(self.horizontalLayout_11, 13, 3, 1, 1)
        self.experimental = QtGui.QCheckBox(PluginBuilderDialogBase)
        self.experimental.setObjectName(_fromUtf8("experimental"))
        self.gridLayout.addWidget(self.experimental, 14, 3, 1, 1)
        self.line_2 = QtGui.QFrame(PluginBuilderDialogBase)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 15, 0, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(PluginBuilderDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 15, 3, 1, 1)

        self.retranslateUi(PluginBuilderDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), PluginBuilderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginBuilderDialogBase)

    def retranslateUi(self, PluginBuilderDialogBase):
        PluginBuilderDialogBase.setWindowTitle(_translate("PluginBuilderDialogBase", "QGIS Plugin Builder 2.0.3", None))
        self.label_10.setText(_translate("PluginBuilderDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">QGIS Plugin Builder</span></p></body></html>", None))
        self.label.setText(_translate("PluginBuilderDialogBase", "Class name", None))
        self.label_2.setText(_translate("PluginBuilderDialogBase", "Plugin name", None))
        self.label_3.setText(_translate("PluginBuilderDialogBase", "Description", None))
        self.label_4.setText(_translate("PluginBuilderDialogBase", "Version number", None))
        self.version_no.setText(_translate("PluginBuilderDialogBase", "0.1", None))
        self.label_5.setText(_translate("PluginBuilderDialogBase", "Minimum QGIS version", None))
        self.min_version_no.setText(_translate("PluginBuilderDialogBase", "2.0", None))
        self.label_6.setText(_translate("PluginBuilderDialogBase", "Text for the menu item", None))
        self.label_7.setText(_translate("PluginBuilderDialogBase", "Author/Company", None))
        self.label_8.setText(_translate("PluginBuilderDialogBase", "Email address", None))
        self.label_14.setText(_translate("PluginBuilderDialogBase", "Optional Items", None))
        self.label_9.setText(_translate("PluginBuilderDialogBase", "Bug tracker", None))
        self.label_11.setText(_translate("PluginBuilderDialogBase", "Home page", None))
        self.label_13.setText(_translate("PluginBuilderDialogBase", "Repository", None))
        self.label_12.setText(_translate("PluginBuilderDialogBase", "Tags", None))
        self.experimental.setText(_translate("PluginBuilderDialogBase", "Flag the plugin as experimental", None))

from PyQt4 import QtWebKit
