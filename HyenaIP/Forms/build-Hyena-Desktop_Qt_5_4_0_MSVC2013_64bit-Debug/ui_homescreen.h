/********************************************************************************
** Form generated from reading UI file 'homescreen.ui'
**
** Created by: Qt User Interface Compiler version 5.4.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_HOMESCREEN_H
#define UI_HOMESCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_HomeScreen
{
public:
    QAction *actionExit;
    QAction *actionLicense;
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *tab;
    QLabel *label_2;
    QPushButton *BtnCreateLoad;
    QLineEdit *TextEditDirectoryPath;
    QWidget *tab_3;
    QPushButton *BtnImageDAQ;
    QLabel *label_4;
    QWidget *tab_2;
    QPushButton *BtnImageProcessing;
    QLabel *label_6;
    QWidget *tab_4;
    QPushButton *BtnTraining;
    QLabel *label_7;
    QWidget *tab_5;
    QPushButton *BtnTestError;
    QLabel *label_8;
    QLabel *label;
    QLabel *label_3;
    QLabel *label_5;
    QMenuBar *menuBar;
    QMenu *menuFile;
    QMenu *menuAbout;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *HomeScreen)
    {
        if (HomeScreen->objectName().isEmpty())
            HomeScreen->setObjectName(QStringLiteral("HomeScreen"));
        HomeScreen->resize(800, 520);
        HomeScreen->setMinimumSize(QSize(800, 520));
        HomeScreen->setMaximumSize(QSize(800, 520));
        QFont font;
        font.setFamily(QStringLiteral("Century Gothic"));
        HomeScreen->setFont(font);
        QIcon icon;
        icon.addFile(QStringLiteral("../../Media/Images/HyenaLogo.gif"), QSize(), QIcon::Normal, QIcon::Off);
        HomeScreen->setWindowIcon(icon);
        HomeScreen->setDockOptions(QMainWindow::AllowTabbedDocks|QMainWindow::AnimatedDocks);
        actionExit = new QAction(HomeScreen);
        actionExit->setObjectName(QStringLiteral("actionExit"));
        actionLicense = new QAction(HomeScreen);
        actionLicense->setObjectName(QStringLiteral("actionLicense"));
        centralWidget = new QWidget(HomeScreen);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(10, 110, 781, 321));
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        label_2 = new QLabel(tab);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(10, 10, 760, 220));
        BtnCreateLoad = new QPushButton(tab);
        BtnCreateLoad->setObjectName(QStringLiteral("BtnCreateLoad"));
        BtnCreateLoad->setGeometry(QRect(430, 170, 330, 50));
        TextEditDirectoryPath = new QLineEdit(tab);
        TextEditDirectoryPath->setObjectName(QStringLiteral("TextEditDirectoryPath"));
        TextEditDirectoryPath->setGeometry(QRect(10, 230, 751, 41));
        tabWidget->addTab(tab, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QStringLiteral("tab_3"));
        BtnImageDAQ = new QPushButton(tab_3);
        BtnImageDAQ->setObjectName(QStringLiteral("BtnImageDAQ"));
        BtnImageDAQ->setGeometry(QRect(430, 220, 330, 50));
        label_4 = new QLabel(tab_3);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(10, 10, 760, 220));
        tabWidget->addTab(tab_3, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        BtnImageProcessing = new QPushButton(tab_2);
        BtnImageProcessing->setObjectName(QStringLiteral("BtnImageProcessing"));
        BtnImageProcessing->setGeometry(QRect(430, 220, 330, 50));
        label_6 = new QLabel(tab_2);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(10, 10, 760, 220));
        tabWidget->addTab(tab_2, QString());
        tab_4 = new QWidget();
        tab_4->setObjectName(QStringLiteral("tab_4"));
        BtnTraining = new QPushButton(tab_4);
        BtnTraining->setObjectName(QStringLiteral("BtnTraining"));
        BtnTraining->setGeometry(QRect(430, 220, 330, 50));
        label_7 = new QLabel(tab_4);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(10, 10, 760, 220));
        tabWidget->addTab(tab_4, QString());
        tab_5 = new QWidget();
        tab_5->setObjectName(QStringLiteral("tab_5"));
        BtnTestError = new QPushButton(tab_5);
        BtnTestError->setObjectName(QStringLiteral("BtnTestError"));
        BtnTestError->setGeometry(QRect(430, 220, 330, 50));
        label_8 = new QLabel(tab_5);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(10, 10, 760, 220));
        tabWidget->addTab(tab_5, QString());
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(80, 0, 441, 101));
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(620, 10, 171, 91));
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(10, 10, 61, 91));
        label_5->setPixmap(QPixmap(QString::fromUtf8("../../Media/Images/HyenaLogo.gif")));
        HomeScreen->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(HomeScreen);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 800, 31));
        menuFile = new QMenu(menuBar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuAbout = new QMenu(menuBar);
        menuAbout->setObjectName(QStringLiteral("menuAbout"));
        HomeScreen->setMenuBar(menuBar);
        mainToolBar = new QToolBar(HomeScreen);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        HomeScreen->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(HomeScreen);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        HomeScreen->setStatusBar(statusBar);
        QWidget::setTabOrder(tabWidget, BtnCreateLoad);

        menuBar->addAction(menuFile->menuAction());
        menuBar->addAction(menuAbout->menuAction());
        menuFile->addAction(actionExit);
        menuAbout->addAction(actionLicense);

        retranslateUi(HomeScreen);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(HomeScreen);
    } // setupUi

    void retranslateUi(QMainWindow *HomeScreen)
    {
        HomeScreen->setWindowTitle(QApplication::translate("HomeScreen", "Hyena", 0));
        actionExit->setText(QApplication::translate("HomeScreen", "Exit", 0));
        actionLicense->setText(QApplication::translate("HomeScreen", "License", 0));
        label_2->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Project Module</span></p><p><br/><span style=\" font-style:italic;\">Welcome to Hyena!</span></p><p>The first step is define a specific folder as working directory, in which application</p><p>will save the images as well as will perform the training and test process.</p><p><br/>Please select a folder for the project:<br/><br/><br/><br/><br/></p></body></html>", 0));
        BtnCreateLoad->setText(QApplication::translate("HomeScreen", "Select working directory", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("HomeScreen", "Project", 0));
        BtnImageDAQ->setText(QApplication::translate("HomeScreen", "Launch Image Acquisition module", 0));
        label_4->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image acquisition module</span></p><p><br/>This module allows you get and store images for future training or classification processes.</p><p>It is possible get image in real time from the camera or select images from the disk.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QApplication::translate("HomeScreen", "1. Acquisition", 0));
        BtnImageProcessing->setText(QApplication::translate("HomeScreen", "Launch Image Processing module", 0));
        label_6->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image Processing Module</span></p><p><br/></p><p>This module allows you perform different processing task in images such as filtering,</p><p>thresholding, canny detector, gaussian and laplace filters, in order to prepare </p><p>the images for futures process of training and identification.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("HomeScreen", "2. Processing", 0));
        BtnTraining->setText(QApplication::translate("HomeScreen", "Launch Training and clustering module", 0));
        label_7->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Image training module</span></p><p><br/></p><p>This module allow you run training algorithms for learning and clustering of images, like SVM or KNN, </p><p>in order to complete recognition or detection tasks.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_4), QApplication::translate("HomeScreen", "3. Training", 0));
        BtnTestError->setText(QApplication::translate("HomeScreen", "Launch Test and error analysis module", 0));
        label_8->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Test and error analysis module</span></p><p><br/></p><p>This module allows you validate and verify previous process of clustering and </p><p>classification of images, performed with the Training module.</p><p><br/></p><p><br/></p><p><br/></p><p><br/></p><p><br/></p></body></html>", 0));
        tabWidget->setTabText(tabWidget->indexOf(tab_5), QApplication::translate("HomeScreen", "4. Test and error analysis", 0));
        label->setText(QApplication::translate("HomeScreen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Hyena</span></p><p><span style=\" font-size:7pt; color:#535353;\">Acquisition, processing, training and testing process </span></p><p><span style=\" font-size:7pt; color:#535353;\">of images with python and OpenCV.</span></p></body></html>", 0));
        label_3->setText(QApplication::translate("HomeScreen", "<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Developed by</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:600;\">Francisco J Garcia R</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:600;\">2015</span></p></body></html>", 0));
        label_5->setText(QString());
        menuFile->setTitle(QApplication::translate("HomeScreen", "File", 0));
        menuAbout->setTitle(QApplication::translate("HomeScreen", "About", 0));
    } // retranslateUi

};

namespace Ui {
    class HomeScreen: public Ui_HomeScreen {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HOMESCREEN_H
