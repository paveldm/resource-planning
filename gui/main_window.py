# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 791)
        MainWindow.setStyleSheet(u"background-color: #f0f0f0;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 80, 1131, 681))
        self.Employees = QWidget()
        self.Employees.setObjectName(u"Employees")
        self.groupBox = QGroupBox(self.Employees)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(100, 0, 401, 51))
        self.groupBox.setStyleSheet(u"background-color: #fffafa;")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 10, 241, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.groupBox_2 = QGroupBox(self.Employees)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(100, 70, 401, 101))
        self.groupBox_2.setStyleSheet(u"background-color: #fffafa;")
        self.pushButtonAdd = QPushButton(self.groupBox_2)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(280, 50, 101, 31))
        self.pushButtonAdd.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonAdd.setAutoFillBackground(False)
        self.pushButtonAdd.setStyleSheet(u"QPushButton#pushButtonAdd {\n"
"    background-color: #4CAF50; /* \u0417\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonAdd:hover {\n"
"    background-color: #45A049; /* \u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPush"
                        "Button#pushButtonAdd:pressed {\n"
"    background-color: #3E8E41; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.chooseDirection = QComboBox(self.groupBox_2)
        self.chooseDirection.addItem("")
        self.chooseDirection.addItem("")
        self.chooseDirection.addItem("")
        self.chooseDirection.setObjectName(u"chooseDirection")
        self.chooseDirection.setEnabled(True)
        self.chooseDirection.setGeometry(QRect(130, 50, 81, 24))
        self.chooseDirection.setAcceptDrops(False)
        self.chooseDirection.setEditable(False)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 101, 20))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 101, 20))
        self.addEmployee = QLineEdit(self.groupBox_2)
        self.addEmployee.setObjectName(u"addEmployee")
        self.addEmployee.setGeometry(QRect(130, 20, 151, 22))
        self.tableWidget = QTableWidget(self.Employees)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(120, 180, 361, 431))
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.deleteEmployee = QComboBox(self.Employees)
        self.deleteEmployee.setObjectName(u"deleteEmployee")
        self.deleteEmployee.setEnabled(True)
        self.deleteEmployee.setGeometry(QRect(210, 620, 131, 24))
        self.deleteEmployee.setAcceptDrops(False)
        self.deleteEmployee.setEditable(False)
        self.pushButtonDeleteEmployee = QPushButton(self.Employees)
        self.pushButtonDeleteEmployee.setObjectName(u"pushButtonDeleteEmployee")
        self.pushButtonDeleteEmployee.setGeometry(QRect(350, 620, 131, 31))
        self.pushButtonDeleteEmployee.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonDeleteEmployee.setAutoFillBackground(False)
        self.pushButtonDeleteEmployee.setStyleSheet(u"QPushButton#pushButtonDeleteEmployee {\n"
"    background-color: #FF4D4D; /* \u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;        /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonDeleteEmployee:hover {\n"
"    background-color: #FF1A1A; /* \u0422\u0435\u043c\u043d\u043e-\u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 "
                        "*/\n"
"}\n"
"\n"
"QPushButton#pushButtonDeleteEmployee:pressed {\n"
"    background-color: #B30000; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.groupBox_6 = QGroupBox(self.Employees)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(570, 70, 441, 161))
        self.groupBox_6.setStyleSheet(u"background-color: #fffafa;")
        self.pushButtonAddDateProject = QPushButton(self.groupBox_6)
        self.pushButtonAddDateProject.setObjectName(u"pushButtonAddDateProject")
        self.pushButtonAddDateProject.setGeometry(QRect(330, 110, 101, 31))
        self.pushButtonAddDateProject.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonAddDateProject.setAutoFillBackground(False)
        self.pushButtonAddDateProject.setStyleSheet(u"QPushButton#pushButtonAddDateProject {\n"
"    background-color: #4CAF50; /* \u0417\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonAddDateProject:hover {\n"
"    background-color: #45A049; /* \u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 *"
                        "/\n"
"}\n"
"\n"
"QPushButton#pushButtonAddDateProject:pressed {\n"
"    background-color: #3E8E41; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 110, 191, 20))
        self.dateStartProject = QDateEdit(self.groupBox_6)
        self.dateStartProject.setObjectName(u"dateStartProject")
        self.dateStartProject.setGeometry(QRect(210, 110, 111, 24))
        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 10, 401, 71))
        self.label_20.setWordWrap(True)
        self.groupBox_7 = QGroupBox(self.Employees)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(570, 0, 441, 51))
        self.groupBox_7.setStyleSheet(u"background-color: #fffafa;")
        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(100, 10, 241, 31))
        self.label_21.setFont(font)
        self.stackedWidget.addWidget(self.Employees)
        self.Tasks = QWidget()
        self.Tasks.setObjectName(u"Tasks")
        self.groupBox_3 = QGroupBox(self.Tasks)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(100, 0, 251, 51))
        self.groupBox_3.setStyleSheet(u"background-color: #fffafa;")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 10, 201, 31))
        self.label_5.setFont(font)
        self.pushButtonDeleteTask = QPushButton(self.Tasks)
        self.pushButtonDeleteTask.setObjectName(u"pushButtonDeleteTask")
        self.pushButtonDeleteTask.setGeometry(QRect(900, 630, 131, 31))
        self.pushButtonDeleteTask.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonDeleteTask.setAutoFillBackground(False)
        self.pushButtonDeleteTask.setStyleSheet(u"QPushButton#pushButtonDeleteTask {\n"
"    background-color: #FF4D4D; /* \u041a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;        /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonDeleteTask:hover {\n"
"    background-color: #FF1A1A; /* \u0422\u0435\u043c\u043d\u043e-\u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}"
                        "\n"
"\n"
"QPushButton#pushButtonDeleteTask:pressed {\n"
"    background-color: #B30000; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.groupBox_4 = QGroupBox(self.Tasks)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(100, 70, 911, 131))
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 61, 16))
        self.addTask = QLineEdit(self.groupBox_4)
        self.addTask.setObjectName(u"addTask")
        self.addTask.setGeometry(QRect(80, 20, 261, 22))
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 70, 71, 16))
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 20, 101, 20))
        self.chooseDirection_2 = QComboBox(self.groupBox_4)
        self.chooseDirection_2.addItem("")
        self.chooseDirection_2.addItem("")
        self.chooseDirection_2.addItem("")
        self.chooseDirection_2.setObjectName(u"chooseDirection_2")
        self.chooseDirection_2.setEnabled(True)
        self.chooseDirection_2.setGeometry(QRect(460, 20, 81, 24))
        self.chooseDirection_2.setAcceptDrops(False)
        self.chooseDirection_2.setEditable(False)
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(570, 20, 141, 20))
        self.pushButtonAddTask = QPushButton(self.groupBox_4)
        self.pushButtonAddTask.setObjectName(u"pushButtonAddTask")
        self.pushButtonAddTask.setGeometry(QRect(800, 50, 101, 31))
        self.pushButtonAddTask.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonAddTask.setAutoFillBackground(False)
        self.pushButtonAddTask.setStyleSheet(u"QPushButton#pushButtonAddTask {\n"
"    background-color: #4CAF50; /* \u0417\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonAddTask:hover {\n"
"    background-color: #45A049; /* \u0422\u0435\u043c\u043d\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
""
                        "QPushButton#pushButtonAddTask:pressed {\n"
"    background-color: #3E8E41; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0437\u0435\u043b\u0435\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.taskDescription = QTextEdit(self.groupBox_4)
        self.taskDescription.setObjectName(u"taskDescription")
        self.taskDescription.setGeometry(QRect(80, 50, 261, 64))
        self.chooseEmployee = QComboBox(self.groupBox_4)
        self.chooseEmployee.setObjectName(u"chooseEmployee")
        self.chooseEmployee.setEnabled(True)
        self.chooseEmployee.setGeometry(QRect(510, 70, 131, 24))
        self.chooseEmployee.setAcceptDrops(False)
        self.chooseEmployee.setEditable(False)
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(360, 70, 151, 20))
        self.durationInput = QSpinBox(self.groupBox_4)
        self.durationInput.setObjectName(u"durationInput")
        self.durationInput.setGeometry(QRect(710, 20, 67, 24))
        self.durationInput.setMinimum(1)
        self.durationInput.setMaximum(365)
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(660, 50, 131, 20))
        self.dependenciesInput = QLineEdit(self.groupBox_4)
        self.dependenciesInput.setObjectName(u"dependenciesInput")
        self.dependenciesInput.setGeometry(QRect(660, 70, 131, 22))
        self.deleteTask = QComboBox(self.Tasks)
        self.deleteTask.setObjectName(u"deleteTask")
        self.deleteTask.setEnabled(True)
        self.deleteTask.setGeometry(QRect(760, 630, 131, 24))
        self.deleteTask.setAcceptDrops(False)
        self.deleteTask.setEditable(False)
        self.tableWidgetTasks = QTableWidget(self.Tasks)
        if (self.tableWidgetTasks.columnCount() < 7):
            self.tableWidgetTasks.setColumnCount(7)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidgetTasks.setHorizontalHeaderItem(6, __qtablewidgetitem8)
        self.tableWidgetTasks.setObjectName(u"tableWidgetTasks")
        self.tableWidgetTasks.setGeometry(QRect(90, 220, 941, 401))
        self.tableWidgetTasks.setMinimumSize(QSize(441, 0))
        self.tableWidgetTasks.setTabletTracking(False)
        self.tableWidgetTasks.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetTasks.setShowGrid(True)
        self.tableWidgetTasks.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetTasks.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetTasks.horizontalHeader().setHighlightSections(True)
        self.tableWidgetTasks.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetTasks.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetTasks.verticalHeader().setVisible(True)
        self.tableWidgetTasks.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTasks.verticalHeader().setHighlightSections(True)
        self.tableWidgetTasks.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetTasks.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.Tasks)
        self.Diagram = QWidget()
        self.Diagram.setObjectName(u"Diagram")
        self.stackedWidgetDiagrams = QStackedWidget(self.Diagram)
        self.stackedWidgetDiagrams.setObjectName(u"stackedWidgetDiagrams")
        self.stackedWidgetDiagrams.setGeometry(QRect(0, 0, 1071, 671))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.webEngineViewDiagramEmployee = QWebEngineView(self.page)
        self.webEngineViewDiagramEmployee.setObjectName(u"webEngineViewDiagramEmployee")
        self.webEngineViewDiagramEmployee.setGeometry(QRect(0, 0, 1061, 691))
        self.webEngineViewDiagramEmployee.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetDiagrams.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.webEngineViewDiagramTasks = QWebEngineView(self.page_2)
        self.webEngineViewDiagramTasks.setObjectName(u"webEngineViewDiagramTasks")
        self.webEngineViewDiagramTasks.setGeometry(QRect(0, 0, 1061, 691))
        self.webEngineViewDiagramTasks.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetDiagrams.addWidget(self.page_2)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.webEngineViewCriticalPath = QWebEngineView(self.page_7)
        self.webEngineViewCriticalPath.setObjectName(u"webEngineViewCriticalPath")
        self.webEngineViewCriticalPath.setGeometry(QRect(0, 0, 1061, 691))
        self.webEngineViewCriticalPath.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetDiagrams.addWidget(self.page_7)
        self.pushButtonDiagram1 = QPushButton(self.Diagram)
        self.pushButtonDiagram1.setObjectName(u"pushButtonDiagram1")
        self.pushButtonDiagram1.setGeometry(QRect(1080, 290, 31, 31))
        self.pushButtonDiagram1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonDiagram1.setAutoFillBackground(False)
        self.pushButtonDiagram1.setStyleSheet(u"QPushButton#pushButtonDiagram1 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonDiagram1:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonDiagram1:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.pushButtonDiagram1.setIcon(icon)
        self.pushButtonDiagram2 = QPushButton(self.Diagram)
        self.pushButtonDiagram2.setObjectName(u"pushButtonDiagram2")
        self.pushButtonDiagram2.setGeometry(QRect(1080, 330, 31, 31))
        self.pushButtonDiagram2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonDiagram2.setAutoFillBackground(False)
        self.pushButtonDiagram2.setStyleSheet(u"QPushButton#pushButtonDiagram2 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonDiagram2:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonDiagram2:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.pushButtonDiagram2.setIcon(icon1)
        self.stackedWidget.addWidget(self.Diagram)
        self.ActualDates = QWidget()
        self.ActualDates.setObjectName(u"ActualDates")
        self.listWidgetTasks = QListWidget(self.ActualDates)
        self.listWidgetTasks.setObjectName(u"listWidgetTasks")
        self.listWidgetTasks.setGeometry(QRect(20, 40, 211, 641))
        self.pushButtonSaveActualDuration = QPushButton(self.ActualDates)
        self.pushButtonSaveActualDuration.setObjectName(u"pushButtonSaveActualDuration")
        self.pushButtonSaveActualDuration.setGeometry(QRect(770, 0, 121, 31))
        self.pushButtonSaveActualDuration.setStyleSheet(u"QPushButton#pushButtonSaveActualDuration {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 2px 5px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonSaveActualDuration:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438"
                        " */\n"
"}\n"
"\n"
"QPushButton#pushButtonSaveActualDuration:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.label_11 = QLabel(self.ActualDates)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(410, 10, 281, 20))
        self.label_13 = QLabel(self.ActualDates)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, -10, 221, 51))
        self.label_13.setWordWrap(True)
        self.tableWidgetActualDates = QTableWidget(self.ActualDates)
        if (self.tableWidgetActualDates.columnCount() < 10):
            self.tableWidgetActualDates.setColumnCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidgetActualDates.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidgetActualDates.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidgetActualDates.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetActualDates.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidgetActualDates.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        self.tableWidgetActualDates.setObjectName(u"tableWidgetActualDates")
        self.tableWidgetActualDates.setGeometry(QRect(240, 50, 881, 631))
        self.tableWidgetActualDates.setMinimumSize(QSize(441, 0))
        self.tableWidgetActualDates.setTabletTracking(False)
        self.tableWidgetActualDates.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetActualDates.setShowGrid(True)
        self.tableWidgetActualDates.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetActualDates.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetActualDates.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetActualDates.horizontalHeader().setHighlightSections(True)
        self.tableWidgetActualDates.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetActualDates.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetActualDates.verticalHeader().setVisible(True)
        self.tableWidgetActualDates.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetActualDates.verticalHeader().setHighlightSections(True)
        self.tableWidgetActualDates.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetActualDates.verticalHeader().setStretchLastSection(False)
        self.actualDurationInput = QSpinBox(self.ActualDates)
        self.actualDurationInput.setObjectName(u"actualDurationInput")
        self.actualDurationInput.setGeometry(QRect(690, 10, 67, 24))
        self.actualDurationInput.setMinimum(1)
        self.actualDurationInput.setMaximum(365)
        self.stackedWidget.addWidget(self.ActualDates)
        self.Analysis = QWidget()
        self.Analysis.setObjectName(u"Analysis")
        self.progressBarCompletion = QProgressBar(self.Analysis)
        self.progressBarCompletion.setObjectName(u"progressBarCompletion")
        self.progressBarCompletion.setGeometry(QRect(540, 30, 118, 23))
        self.progressBarCompletion.setStyleSheet(u"    QProgressBar {\n"
"        border: 2px solid #007BFF;\n"
"        border-radius: 10px;\n"
"        background-color: #E9ECEF;\n"
"        height: 20px;\n"
"        text-align: center;\n"
"        color: #333333;\n"
"        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* \u0422\u0435\u043d\u044c */\n"
"    }\n"
"    QProgressBar::chunk {\n"
"        background-color: #007BFF;\n"
"        border-radius: 8px;\n"
"    }")
        self.progressBarCompletion.setValue(24)
        self.labelAvgPlannedDuration = QLabel(self.Analysis)
        self.labelAvgPlannedDuration.setObjectName(u"labelAvgPlannedDuration")
        self.labelAvgPlannedDuration.setGeometry(QRect(540, 120, 411, 16))
        self.labelAvgActualDuration = QLabel(self.Analysis)
        self.labelAvgActualDuration.setObjectName(u"labelAvgActualDuration")
        self.labelAvgActualDuration.setGeometry(QRect(540, 140, 411, 20))
        self.label_12 = QLabel(self.Analysis)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(540, 10, 171, 16))
        self.label_14 = QLabel(self.Analysis)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(540, 70, 151, 16))
        self.labelQuantityTasks = QLabel(self.Analysis)
        self.labelQuantityTasks.setObjectName(u"labelQuantityTasks")
        self.labelQuantityTasks.setGeometry(QRect(690, 70, 49, 16))
        self.label_16 = QLabel(self.Analysis)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(790, 10, 231, 16))
        self.labelProjectDuration = QLabel(self.Analysis)
        self.labelProjectDuration.setObjectName(u"labelProjectDuration")
        self.labelProjectDuration.setGeometry(QRect(1030, 10, 71, 16))
        self.labelQuantityEmployees = QLabel(self.Analysis)
        self.labelQuantityEmployees.setObjectName(u"labelQuantityEmployees")
        self.labelQuantityEmployees.setGeometry(QRect(730, 90, 49, 16))
        self.label_17 = QLabel(self.Analysis)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(540, 90, 191, 16))
        self.stackedWidgetBarCharts = QStackedWidget(self.Analysis)
        self.stackedWidgetBarCharts.setObjectName(u"stackedWidgetBarCharts")
        self.stackedWidgetBarCharts.setGeometry(QRect(539, 159, 591, 281))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.webEngineViewBarChartQuantityEmployee = QWebEngineView(self.page_3)
        self.webEngineViewBarChartQuantityEmployee.setObjectName(u"webEngineViewBarChartQuantityEmployee")
        self.webEngineViewBarChartQuantityEmployee.setGeometry(QRect(0, 0, 591, 271))
        self.webEngineViewBarChartQuantityEmployee.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetBarCharts.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.webEngineViewBarChartDuration = QWebEngineView(self.page_4)
        self.webEngineViewBarChartDuration.setObjectName(u"webEngineViewBarChartDuration")
        self.webEngineViewBarChartDuration.setGeometry(QRect(0, 0, 591, 271))
        self.webEngineViewBarChartDuration.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetBarCharts.addWidget(self.page_4)
        self.pushButtonBarChart2 = QPushButton(self.Analysis)
        self.pushButtonBarChart2.setObjectName(u"pushButtonBarChart2")
        self.pushButtonBarChart2.setGeometry(QRect(1100, 120, 31, 31))
        self.pushButtonBarChart2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonBarChart2.setAutoFillBackground(False)
        self.pushButtonBarChart2.setStyleSheet(u"QPushButton#pushButtonBarChart2 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonBarChart2:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonBarChart2:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pushButtonBarChart2.setIcon(icon2)
        self.pushButtonBarChart1 = QPushButton(self.Analysis)
        self.pushButtonBarChart1.setObjectName(u"pushButtonBarChart1")
        self.pushButtonBarChart1.setGeometry(QRect(1060, 120, 31, 31))
        self.pushButtonBarChart1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonBarChart1.setAutoFillBackground(False)
        self.pushButtonBarChart1.setStyleSheet(u"QPushButton#pushButtonBarChart1 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonBarChart1:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonBarChart1:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.pushButtonBarChart1.setIcon(icon3)
        self.tableWidgetDirectionAnalysis = QTableWidget(self.Analysis)
        if (self.tableWidgetDirectionAnalysis.columnCount() < 4):
            self.tableWidgetDirectionAnalysis.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidgetDirectionAnalysis.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetDirectionAnalysis.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetDirectionAnalysis.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetDirectionAnalysis.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.tableWidgetDirectionAnalysis.setObjectName(u"tableWidgetDirectionAnalysis")
        self.tableWidgetDirectionAnalysis.setGeometry(QRect(540, 440, 591, 121))
        self.tableWidgetDirectionAnalysis.setMinimumSize(QSize(441, 0))
        self.tableWidgetDirectionAnalysis.setTabletTracking(False)
        self.tableWidgetDirectionAnalysis.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetDirectionAnalysis.setShowGrid(True)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setHighlightSections(True)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetDirectionAnalysis.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDirectionAnalysis.verticalHeader().setVisible(True)
        self.tableWidgetDirectionAnalysis.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDirectionAnalysis.verticalHeader().setHighlightSections(True)
        self.tableWidgetDirectionAnalysis.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetDirectionAnalysis.verticalHeader().setStretchLastSection(False)
        self.stackedWidgetPieCharts = QStackedWidget(self.Analysis)
        self.stackedWidgetPieCharts.setObjectName(u"stackedWidgetPieCharts")
        self.stackedWidgetPieCharts.setGeometry(QRect(0, 50, 531, 311))
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.webEngineViewPieChart = QWebEngineView(self.page_5)
        self.webEngineViewPieChart.setObjectName(u"webEngineViewPieChart")
        self.webEngineViewPieChart.setGeometry(QRect(0, 0, 531, 311))
        self.webEngineViewPieChart.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetPieCharts.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.webEngineViewPieChart2 = QWebEngineView(self.page_6)
        self.webEngineViewPieChart2.setObjectName(u"webEngineViewPieChart2")
        self.webEngineViewPieChart2.setGeometry(QRect(0, 0, 531, 311))
        self.webEngineViewPieChart2.setUrl(QUrl(u"about:blank"))
        self.stackedWidgetPieCharts.addWidget(self.page_6)
        self.pushButtonPieChart2 = QPushButton(self.Analysis)
        self.pushButtonPieChart2.setObjectName(u"pushButtonPieChart2")
        self.pushButtonPieChart2.setGeometry(QRect(500, 10, 31, 31))
        self.pushButtonPieChart2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonPieChart2.setAutoFillBackground(False)
        self.pushButtonPieChart2.setStyleSheet(u"QPushButton#pushButtonPieChart2 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonPieChart2:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonPieChart2:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.pushButtonPieChart2.setIcon(icon2)
        self.pushButtonPieChart1 = QPushButton(self.Analysis)
        self.pushButtonPieChart1.setObjectName(u"pushButtonPieChart1")
        self.pushButtonPieChart1.setGeometry(QRect(460, 10, 31, 31))
        self.pushButtonPieChart1.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonPieChart1.setAutoFillBackground(False)
        self.pushButtonPieChart1.setStyleSheet(u"QPushButton#pushButtonPieChart1 {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonPieChart1:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
""
                        "\n"
"QPushButton#pushButtonPieChart1:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.pushButtonPieChart1.setIcon(icon3)
        self.label_18 = QLabel(self.Analysis)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(130, 370, 271, 16))
        self.tableWidgetDirectionQuality = QTableWidget(self.Analysis)
        if (self.tableWidgetDirectionQuality.columnCount() < 3):
            self.tableWidgetDirectionQuality.setColumnCount(3)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidgetDirectionQuality.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetDirectionQuality.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidgetDirectionQuality.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        self.tableWidgetDirectionQuality.setObjectName(u"tableWidgetDirectionQuality")
        self.tableWidgetDirectionQuality.setGeometry(QRect(0, 390, 531, 121))
        self.tableWidgetDirectionQuality.setMinimumSize(QSize(441, 0))
        self.tableWidgetDirectionQuality.setTabletTracking(False)
        self.tableWidgetDirectionQuality.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetDirectionQuality.setShowGrid(True)
        self.tableWidgetDirectionQuality.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDirectionQuality.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetDirectionQuality.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetDirectionQuality.horizontalHeader().setHighlightSections(True)
        self.tableWidgetDirectionQuality.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetDirectionQuality.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDirectionQuality.verticalHeader().setVisible(True)
        self.tableWidgetDirectionQuality.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidgetDirectionQuality.verticalHeader().setHighlightSections(True)
        self.tableWidgetDirectionQuality.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidgetDirectionQuality.verticalHeader().setStretchLastSection(False)
        self.labelProjectDeviation = QLabel(self.Analysis)
        self.labelProjectDeviation.setObjectName(u"labelProjectDeviation")
        self.labelProjectDeviation.setGeometry(QRect(1030, 30, 91, 20))
        self.label_19 = QLabel(self.Analysis)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(790, 30, 231, 16))
        self.stackedWidget.addWidget(self.Analysis)
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 791, 61))
        self.groupBox_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"    color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-radius: 5px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 8px 16px; /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: bold; /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    text-align: center; /* \u0422\u0435\u043a\u0441\u0442 \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435"
                        "\u043d\u0438\u0438 */\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QPushButton:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0438\u043a\u043e\u043d\u043e\u043a */\n"
"QPushButton::icon {\n"
"    margin-right: 8px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u043c\u0435\u0436\u0434\u0443 \u0438\u043a\u043e\u043d\u043a\u043e\u0439 \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */\n"
"}")
        self.layoutWidget = QWidget(self.groupBox_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 759, 37))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonEmployee = QPushButton(self.layoutWidget)
        self.pushButtonEmployee.setObjectName(u"pushButtonEmployee")
        self.pushButtonEmployee.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonEmployee.setAutoFillBackground(False)
        self.pushButtonEmployee.setStyleSheet(u"QPushButton#pushButtonUpdateTable {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonUpdateTable:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
""
                        "}\n"
"\n"
"QPushButton#pushButtonUpdateTable:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonEmployee)

        self.pushButtonTasks = QPushButton(self.layoutWidget)
        self.pushButtonTasks.setObjectName(u"pushButtonTasks")
        self.pushButtonTasks.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonTasks.setAutoFillBackground(False)
        self.pushButtonTasks.setStyleSheet(u"QPushButton#pushButtonUpdateTable {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonUpdateTable:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
""
                        "}\n"
"\n"
"QPushButton#pushButtonUpdateTable:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonTasks)

        self.pushButtonGantt = QPushButton(self.layoutWidget)
        self.pushButtonGantt.setObjectName(u"pushButtonGantt")
        self.pushButtonGantt.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonGantt.setAutoFillBackground(False)
        self.pushButtonGantt.setStyleSheet(u"QPushButton#pushButtonShowDiagram {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 2px 5px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonShowDiagram:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}"
                        "\n"
"\n"
"QPushButton#pushButtonShowDiagram:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonGantt)

        self.pushButtonActualDates = QPushButton(self.layoutWidget)
        self.pushButtonActualDates.setObjectName(u"pushButtonActualDates")
        self.pushButtonActualDates.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonActualDates.setAutoFillBackground(False)
        self.pushButtonActualDates.setStyleSheet(u"QPushButton#pushButtonUpdateTable {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonUpdateTable:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
""
                        "}\n"
"\n"
"QPushButton#pushButtonUpdateTable:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonActualDates)

        self.pushButtonAnalysis = QPushButton(self.layoutWidget)
        self.pushButtonAnalysis.setObjectName(u"pushButtonAnalysis")
        self.pushButtonAnalysis.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.pushButtonAnalysis.setAutoFillBackground(False)
        self.pushButtonAnalysis.setStyleSheet(u"QPushButton#pushButtonUpdateTable {\n"
"    background-color: #007BFF; /* \u0413\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d */\n"
"    color: white;             /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;             /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    padding: 5px 10px;       /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;          /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 5px;       /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"QPushButton#pushButtonUpdateTable:hover {\n"
"    background-color: #0056b3; /* \u0422\u0435\u043c\u043d\u043e-\u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
""
                        "}\n"
"\n"
"QPushButton#pushButtonUpdateTable:pressed {\n"
"    background-color: #004085; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout.addWidget(self.pushButtonAnalysis, 0, Qt.AlignmentFlag.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1150, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.chooseDirection.setCurrentIndex(-1)
        self.deleteEmployee.setCurrentIndex(-1)
        self.chooseDirection_2.setCurrentIndex(-1)
        self.chooseEmployee.setCurrentIndex(-1)
        self.deleteTask.setCurrentIndex(-1)
        self.stackedWidgetDiagrams.setCurrentIndex(2)
        self.stackedWidgetPieCharts.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430", None))
        self.groupBox_2.setTitle("")
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.chooseDirection.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0421\u0423 \u0422\u041f", None))
        self.chooseDirection.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u041c\u041e", None))
        self.chooseDirection.setItemText(2, QCoreApplication.translate("MainWindow", u"\u042d\u0422\u041e", None))

        self.chooseDirection.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430:", None))
        self.addEmployee.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None));
        self.deleteEmployee.setCurrentText("")
        self.pushButtonDeleteEmployee.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox_6.setTitle("")
        self.pushButtonAddDateProject.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0442\u0430\u0440\u0442\u043e\u0432\u0443\u044e \u0434\u0430\u0442\u0443 \u043f\u0440\u043e\u0435\u043a\u0442\u0430:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u2014 \u044d\u0442\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u043d\u0430\u0447\u0430\u043b\u043e\n"
"\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u0442\u0441\u0447\u0435\u0442\u0430 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u0437\u0430\u0434\u0430\u0447 \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435. \u041e\u043d\u0430 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u043f\u043b\u0430\u043d\u043e\u0432\u044b\u0445 \u0434\u0430\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447 (\u0434\u0430\u0442 \u043d\u0430\u0447\u0430\u043b"
                        "\u0430 \u0438 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f) \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0438\u0445 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0435\u0439.", None))
        self.groupBox_7.setTitle("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f \u0434\u0430\u0442\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.groupBox_3.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.pushButtonDeleteTask.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox_4.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.addTask.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.chooseDirection_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0421\u0423 \u0422\u041f", None))
        self.chooseDirection_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0422\u041c\u041e", None))
        self.chooseDirection_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u042d\u0422\u041e", None))

        self.chooseDirection_2.setCurrentText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u043d\u043e\u0432\u0430\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
        self.pushButtonAddTask.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.chooseEmployee.setCurrentText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u043d\u044b\u0439 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u044c \u043e\u0442 \u0437\u0430\u0434\u0430\u0447:", None))
        self.dependenciesInput.setText("")
        self.deleteTask.setCurrentText("")
        ___qtablewidgetitem2 = self.tableWidgetTasks.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tableWidgetTasks.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem4 = self.tableWidgetTasks.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem5 = self.tableWidgetTasks.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None));
        ___qtablewidgetitem6 = self.tableWidgetTasks.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem7 = self.tableWidgetTasks.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem8 = self.tableWidgetTasks.horizontalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438", None));
        self.pushButtonDiagram1.setText("")
        self.pushButtonDiagram2.setText("")
        self.pushButtonSaveActualDuration.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u043d\u0438\u044f:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u0447\u0443 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0434\u043b\u044f\n"
"\u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0444\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        ___qtablewidgetitem9 = self.tableWidgetActualDates.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem10 = self.tableWidgetActualDates.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem11 = self.tableWidgetActualDates.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem12 = self.tableWidgetActualDates.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e (\u041f\u043b\u0430\u043d)", None));
        ___qtablewidgetitem13 = self.tableWidgetActualDates.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 (\u041f\u043b\u0430\u043d)", None));
        ___qtablewidgetitem14 = self.tableWidgetActualDates.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e (\u0424\u0430\u043a\u0442)", None));
        ___qtablewidgetitem15 = self.tableWidgetActualDates.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435 (\u0424\u0430\u043a\u0442)", None));
        ___qtablewidgetitem16 = self.tableWidgetActualDates.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c (\u041f\u043b\u0430\u043d)", None));
        ___qtablewidgetitem17 = self.tableWidgetActualDates.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c (\u0424\u0430\u043a\u0442)", None));
        ___qtablewidgetitem18 = self.tableWidgetActualDates.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438", None));
        self.labelAvgPlannedDuration.setText("")
        self.labelAvgActualDuration.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u0447:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u0434\u0430\u0447:", None))
        self.labelQuantityTasks.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442:", None))
        self.labelProjectDuration.setText("")
        self.labelQuantityEmployees.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432:", None))
        self.pushButtonBarChart2.setText("")
        self.pushButtonBarChart1.setText("")
        ___qtablewidgetitem19 = self.tableWidgetDirectionAnalysis.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem20 = self.tableWidgetDirectionAnalysis.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None));
        ___qtablewidgetitem21 = self.tableWidgetDirectionAnalysis.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u0434\u0430\u043d\u0438\u0439", None));
        ___qtablewidgetitem22 = self.tableWidgetDirectionAnalysis.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0434\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0439, \u0434\u043d\u0438", None));
        self.pushButtonPieChart2.setText("")
        self.pushButtonPieChart1.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447 \u043f\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\u043c", None))
        ___qtablewidgetitem23 = self.tableWidgetDirectionQuality.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem24 = self.tableWidgetDirectionQuality.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043d\u044b\u0445 \u0437\u0430\u0434\u0430\u043d\u0438\u0439", None));
        ___qtablewidgetitem25 = self.tableWidgetDirectionQuality.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u043e\u0442 \u043f\u043b\u0430\u043d\u043e\u0432\u044b\u0445 \u0441\u0440\u043e\u043a\u043e\u0432", None));
        self.labelProjectDeviation.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 \u043e\u0442 \u043f\u043b\u0430\u043d\u043e\u0432\u044b\u0445 \u0441\u0440\u043e\u043a\u043e\u0432:", None))
        self.groupBox_5.setTitle("")
        self.pushButtonEmployee.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.pushButtonTasks.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u044f", None))
        self.pushButtonGantt.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.pushButtonActualDates.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.pushButtonAnalysis.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437", None))
    # retranslateUi

