# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(410, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Messenger.setWindowIcon(icon)
        self.central_widget = QtWidgets.QWidget(Messenger)
        self.central_widget.setObjectName("central_widget")
        self.stacked_widget = QtWidgets.QStackedWidget(self.central_widget)
        self.stacked_widget.setGeometry(QtCore.QRect(0, 70, 410, 511))
        self.stacked_widget.setObjectName("stacked_widget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.login_line1 = QtWidgets.QLineEdit(self.login_page)
        self.login_line1.setGeometry(QtCore.QRect(60, 130, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_line1.setFont(font)
        self.login_line1.setObjectName("login_line1")
        self.login_button = QtWidgets.QPushButton(self.login_page)
        self.login_button.setGeometry(QtCore.QRect(140, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_error1 = QtWidgets.QLabel(self.login_page)
        self.login_error1.setGeometry(QtCore.QRect(60, 110, 181, 21))
        self.login_error1.setObjectName("login_error1")
        self.password_error1 = QtWidgets.QLabel(self.login_page)
        self.password_error1.setGeometry(QtCore.QRect(60, 180, 181, 21))
        self.password_error1.setObjectName("password_error1")
        self.go_to_sign_up = QtWidgets.QLabel(self.login_page)
        self.go_to_sign_up.setGeometry(QtCore.QRect(140, 300, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.go_to_sign_up.setFont(font)
        self.go_to_sign_up.setAlignment(QtCore.Qt.AlignCenter)
        self.go_to_sign_up.setObjectName("go_to_sign_up")
        self.stacked_widget.addWidget(self.login_page)
        self.registration_page = QtWidgets.QWidget()
        self.registration_page.setObjectName("registration_page")
        self.login_line2 = QtWidgets.QLineEdit(self.registration_page)
        self.login_line2.setGeometry(QtCore.QRect(60, 130, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_line2.setFont(font)
        self.login_line2.setObjectName("login_line2")
        self.sign_up_button = QtWidgets.QPushButton(self.registration_page)
        self.sign_up_button.setGeometry(QtCore.QRect(140, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setObjectName("sign_up_button")
        self.go_to_login = QtWidgets.QLabel(self.registration_page)
        self.go_to_login.setGeometry(QtCore.QRect(120, 300, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.go_to_login.setFont(font)
        self.go_to_login.setAlignment(QtCore.Qt.AlignCenter)
        self.go_to_login.setObjectName("go_to_login")
        self.login_error2 = QtWidgets.QLabel(self.registration_page)
        self.login_error2.setGeometry(QtCore.QRect(60, 110, 181, 21))
        self.login_error2.setObjectName("login_error2")
        self.password_error2 = QtWidgets.QLabel(self.registration_page)
        self.password_error2.setGeometry(QtCore.QRect(60, 180, 181, 21))
        self.password_error2.setObjectName("password_error2")
        self.stacked_widget.addWidget(self.registration_page)
        self.chat_page = QtWidgets.QWidget()
        self.chat_page.setObjectName("chat_page")
        self.text_browser = QtWidgets.QTextBrowser(self.chat_page)
        self.text_browser.setGeometry(QtCore.QRect(20, 30, 370, 401))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.text_browser.setFont(font)
        self.text_browser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_browser.setObjectName("text_browser")
        self.send_button = QtWidgets.QPushButton(self.chat_page)
        self.send_button.setGeometry(QtCore.QRect(340, 450, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_button.setFont(font)
        self.send_button.setObjectName("send_button")
        self.plain_text_edit = QtWidgets.QPlainTextEdit(self.chat_page)
        self.plain_text_edit.setGeometry(QtCore.QRect(20, 440, 370, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.plain_text_edit.setFont(font)
        self.plain_text_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plain_text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plain_text_edit.setObjectName("plain_text_edit")
        self.text_browser.raise_()
        self.plain_text_edit.raise_()
        self.send_button.raise_()
        self.stacked_widget.addWidget(self.chat_page)
        self.messenger_label = QtWidgets.QLabel(self.central_widget)
        self.messenger_label.setGeometry(QtCore.QRect(70, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.messenger_label.setFont(font)
        self.messenger_label.setObjectName("messenger_label")
        self.server_status = QtWidgets.QLabel(self.central_widget)
        self.server_status.setGeometry(QtCore.QRect(170, 70, 61, 16))
        self.server_status.setObjectName("server_status")
        Messenger.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(Messenger)
        self.status_bar.setObjectName("status_bar")
        Messenger.setStatusBar(self.status_bar)
        self.menu_bar = QtWidgets.QMenuBar(Messenger)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 410, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.menu_bar.setFont(font)
        self.menu_bar.setObjectName("menu_bar")
        self.menu_messenger = QtWidgets.QMenu(self.menu_bar)
        self.menu_messenger.setObjectName("menu_messenger")
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        Messenger.setMenuBar(self.menu_bar)
        self.action_shortcuts = QtWidgets.QAction(Messenger)
        self.action_shortcuts.setObjectName("action_shortcuts")
        self.action_commands = QtWidgets.QAction(Messenger)
        self.action_commands.setEnabled(False)
        self.action_commands.setObjectName("action_commands")
        self.action_about = QtWidgets.QAction(Messenger)
        self.action_about.setObjectName("action_about")
        self.action_close = QtWidgets.QAction(Messenger)
        self.action_close.setObjectName("action_close")
        self.action_logout = QtWidgets.QAction(Messenger)
        self.action_logout.setEnabled(False)
        self.action_logout.setObjectName("action_logout")
        self.action_contacts = QtWidgets.QAction(Messenger)
        self.action_contacts.setStatusTip("")
        self.action_contacts.setObjectName("action_contacts")
        self.action_preferences = QtWidgets.QAction(Messenger)
        self.action_preferences.setObjectName("action_preferences")
        self.menu_messenger.addAction(self.action_preferences)
        self.menu_messenger.addSeparator()
        self.menu_messenger.addAction(self.action_logout)
        self.menu_messenger.addAction(self.action_close)
        self.menu_help.addAction(self.action_shortcuts)
        self.menu_help.addAction(self.action_commands)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_contacts)
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_messenger.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(Messenger)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.login_line1.setPlaceholderText(_translate("Messenger", "Login"))
        self.login_button.setStatusTip(_translate("Messenger", "Log in to your account"))
        self.login_button.setText(_translate("Messenger", "Log in"))
        self.go_to_sign_up.setStatusTip(_translate("Messenger", "Go to registration form"))
        self.go_to_sign_up.setText(_translate("Messenger", "Sign up"))
        self.login_line2.setPlaceholderText(_translate("Messenger", "Enter Your Login"))
        self.sign_up_button.setStatusTip(_translate("Messenger", "Create new account"))
        self.sign_up_button.setText(_translate("Messenger", "Sign Up"))
        self.go_to_login.setStatusTip(_translate("Messenger", "Go to login form"))
        self.go_to_login.setText(_translate("Messenger", "I am already a member"))
        self.text_browser.setHtml(_translate("Messenger", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_button.setText(_translate("Messenger", "Send"))
        self.messenger_label.setText(_translate("Messenger", "Python Messenger"))
        self.menu_messenger.setTitle(_translate("Messenger", "Messenger"))
        self.menu_help.setTitle(_translate("Messenger", "Help"))
        self.action_shortcuts.setText(_translate("Messenger", "Shortcuts"))
        self.action_shortcuts.setStatusTip(_translate("Messenger", "Show available shortcuts"))
        self.action_shortcuts.setShortcut(_translate("Messenger", "Ctrl+S"))
        self.action_commands.setText(_translate("Messenger", "Commands"))
        self.action_commands.setStatusTip(_translate("Messenger", "Show available commands"))
        self.action_commands.setShortcut(_translate("Messenger", "Ctrl+D"))
        self.action_about.setText(_translate("Messenger", "About"))
        self.action_about.setStatusTip(_translate("Messenger", "Show messenger information"))
        self.action_close.setText(_translate("Messenger", "Exit"))
        self.action_close.setStatusTip(_translate("Messenger", "Quit messenger"))
        self.action_close.setShortcut(_translate("Messenger", "Alt+E"))
        self.action_logout.setText(_translate("Messenger", "Logout"))
        self.action_logout.setStatusTip(_translate("Messenger", "Logout from account"))
        self.action_logout.setShortcut(_translate("Messenger", "Ctrl+G"))
        self.action_contacts.setText(_translate("Messenger", "Contacts"))
        self.action_preferences.setText(_translate("Messenger", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Messenger = QtWidgets.QMainWindow()
    ui = Ui_Messenger()
    ui.setupUi(Messenger)
    Messenger.show()
    sys.exit(app.exec_())
