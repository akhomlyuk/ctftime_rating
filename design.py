# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designcbLDsN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QProgressBar, QSizePolicy,
    QSpinBox, QStatusBar, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 732)
        icon = QIcon()
        icon.addFile(u":/icons/res/rht.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(48, 48))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings_box = QGroupBox(self.centralwidget)
        self.settings_box.setObjectName(u"settings_box")
        self.settings_box.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Ubuntu Medium"])
        font.setPointSize(12)
        self.settings_box.setFont(font)
        self.settings_box.setStyleSheet(u"")
        self.settings_box.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.settings_box.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.settings_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.settings_box)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(393, 136))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u":/icons/res/formula.gif"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.team_place = QSpinBox(self.settings_box)
        self.team_place.setObjectName(u"team_place")
        self.team_place.setProperty("showGroupSeparator", True)
        self.team_place.setMinimum(1)
        self.team_place.setMaximum(999999)
        self.team_place.setValue(3)

        self.gridLayout.addWidget(self.team_place, 3, 1, 1, 1)

        self.weight = QDoubleSpinBox(self.settings_box)
        self.weight.setObjectName(u"weight")
        self.weight.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.weight.setProperty("showGroupSeparator", True)
        self.weight.setDecimals(3)
        self.weight.setMaximum(99999.990000000005239)
        self.weight.setValue(22.690000000000001)

        self.gridLayout.addWidget(self.weight, 4, 1, 1, 1)

        self.label_2 = QLabel(self.settings_box)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.teams = QSpinBox(self.settings_box)
        self.teams.setObjectName(u"teams")
        self.teams.setProperty("showGroupSeparator", True)
        self.teams.setMinimum(1)
        self.teams.setMaximum(999999)
        self.teams.setValue(500)

        self.gridLayout.addWidget(self.teams, 5, 1, 1, 1)

        self.label_7 = QLabel(self.settings_box)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_3 = QLabel(self.settings_box)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.rating_spinbox = QDoubleSpinBox(self.settings_box)
        self.rating_spinbox.setObjectName(u"rating_spinbox")
        self.rating_spinbox.setEnabled(True)
        self.rating_spinbox.setCursor(QCursor(Qt.ArrowCursor))
        self.rating_spinbox.setWrapping(False)
        self.rating_spinbox.setFrame(True)
        self.rating_spinbox.setAlignment(Qt.AlignCenter)
        self.rating_spinbox.setReadOnly(True)
        self.rating_spinbox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.rating_spinbox.setAccelerated(False)
        self.rating_spinbox.setKeyboardTracking(False)
        self.rating_spinbox.setProperty("showGroupSeparator", True)
        self.rating_spinbox.setDecimals(3)
        self.rating_spinbox.setMaximum(1000.000000000000000)
        self.rating_spinbox.setValue(22.690000000000001)

        self.gridLayout.addWidget(self.rating_spinbox, 6, 1, 1, 1)

        self.label_6 = QLabel(self.settings_box)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.team_points = QDoubleSpinBox(self.settings_box)
        self.team_points.setObjectName(u"team_points")
        self.team_points.setProperty("showGroupSeparator", True)
        self.team_points.setDecimals(3)
        self.team_points.setMaximum(99999.990000000005239)
        self.team_points.setValue(15927.000000000000000)

        self.gridLayout.addWidget(self.team_points, 2, 1, 1, 1)

        self.label_4 = QLabel(self.settings_box)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.best_team_points = QDoubleSpinBox(self.settings_box)
        self.best_team_points.setObjectName(u"best_team_points")
        self.best_team_points.setMinimumSize(QSize(0, 0))
        self.best_team_points.setProperty("showGroupSeparator", True)
        self.best_team_points.setDecimals(3)
        self.best_team_points.setMaximum(99999.990000000005239)
        self.best_team_points.setValue(16419.000000000000000)

        self.gridLayout.addWidget(self.best_team_points, 1, 1, 1, 1)

        self.label_5 = QLabel(self.settings_box)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.rating_progress = QProgressBar(self.settings_box)
        self.rating_progress.setObjectName(u"rating_progress")
        self.rating_progress.setMaximum(100)
        self.rating_progress.setValue(50)

        self.verticalLayout.addWidget(self.rating_progress)


        self.horizontalLayout.addWidget(self.settings_box)

        self.eventid_box = QGroupBox(self.centralwidget)
        self.eventid_box.setObjectName(u"eventid_box")
        self.eventid_box.setMinimumSize(QSize(0, 0))
        self.eventid_box.setFont(font)
        self.eventid_box.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.eventid_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.event_id = QSpinBox(self.eventid_box)
        self.event_id.setObjectName(u"event_id")
        self.event_id.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.event_id.setProperty("showGroupSeparator", False)
        self.event_id.setMinimum(1)
        self.event_id.setMaximum(999999)
        self.event_id.setValue(1892)

        self.verticalLayout_4.addWidget(self.event_id)

        self.text_result = QTextEdit(self.eventid_box)
        self.text_result.setObjectName(u"text_result")
        font1 = QFont()
        font1.setFamilies([u"Fira Code Medium"])
        font1.setPointSize(10)
        self.text_result.setFont(font1)
        self.text_result.setFrameShape(QFrame.StyledPanel)
        self.text_result.setFrameShadow(QFrame.Sunken)
        self.text_result.setLineWidth(1)
        self.text_result.setMidLineWidth(0)
        self.text_result.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.text_result)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.eventid_box)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.event_info_text = QTextBrowser(self.centralwidget)
        self.event_info_text.setObjectName(u"event_info_text")
        self.event_info_text.setFont(font1)
        self.event_info_text.setReadOnly(True)
        self.event_info_text.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.event_info_text.setOpenExternalLinks(True)
        self.event_info_text.setOpenLinks(True)

        self.horizontalLayout_2.addWidget(self.event_info_text)

        self.rht_info = QTextBrowser(self.centralwidget)
        self.rht_info.setObjectName(u"rht_info")
        self.rht_info.setFont(font1)
        self.rht_info.setOpenExternalLinks(True)

        self.horizontalLayout_2.addWidget(self.rht_info)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.author_label = QLabel(self.centralwidget)
        self.author_label.setObjectName(u"author_label")
        self.author_label.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Medium"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.author_label.setFont(font2)
        self.author_label.setFrameShape(QFrame.NoFrame)
        self.author_label.setTextFormat(Qt.MarkdownText)
        self.author_label.setScaledContents(False)
        self.author_label.setMargin(0)
        self.author_label.setIndent(0)
        self.author_label.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.author_label)

        self.rht_label = QLabel(self.centralwidget)
        self.rht_label.setObjectName(u"rht_label")
        font3 = QFont()
        font3.setFamilies([u"Ubuntu Medium"])
        font3.setPointSize(11)
        self.rht_label.setFont(font3)
        self.rht_label.setTextFormat(Qt.MarkdownText)
        self.rht_label.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.rht_label)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RedHazzarTeam rating", None))
        self.settings_box.setTitle(QCoreApplication.translate("MainWindow", u"Parametres", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Best team pts:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Your rating:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Team pts:", None))
        self.rating_spinbox.setPrefix("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Team place:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Teams:", None))
        self.eventid_box.setTitle(QCoreApplication.translate("MainWindow", u"Event ID", None))
        self.text_result.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Fira Code Medium'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.event_info_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Fira Code Medium'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.author_label.setText(QCoreApplication.translate("MainWindow", u"Author: [Exited3n](https://t.me/exited3n)", None))
        self.rht_label.setText(QCoreApplication.translate("MainWindow", u"Team: [RedHazzarTeam](https://ctftime.org/team/186788)", None))
    # retranslateUi

