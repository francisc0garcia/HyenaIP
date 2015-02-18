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
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_HomeScreen
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *HomeScreen)
    {
        if (HomeScreen->objectName().isEmpty())
            HomeScreen->setObjectName(QStringLiteral("HomeScreen"));
        HomeScreen->resize(400, 300);
        menuBar = new QMenuBar(HomeScreen);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        HomeScreen->setMenuBar(menuBar);
        mainToolBar = new QToolBar(HomeScreen);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        HomeScreen->addToolBar(mainToolBar);
        centralWidget = new QWidget(HomeScreen);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        HomeScreen->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(HomeScreen);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        HomeScreen->setStatusBar(statusBar);

        retranslateUi(HomeScreen);

        QMetaObject::connectSlotsByName(HomeScreen);
    } // setupUi

    void retranslateUi(QMainWindow *HomeScreen)
    {
        HomeScreen->setWindowTitle(QApplication::translate("HomeScreen", "HomeScreen", 0));
    } // retranslateUi

};

namespace Ui {
    class HomeScreen: public Ui_HomeScreen {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HOMESCREEN_H
