#ifndef HOMESCREEN_H
#define HOMESCREEN_H

#include <QMainWindow>

namespace Ui {
class HomeScreen;
}

class HomeScreen : public QMainWindow
{
    Q_OBJECT

public:
    explicit HomeScreen(QWidget *parent = 0);
    ~HomeScreen();

private slots:
    void on_BtnImageDAQ_clicked();

private:
    Ui::HomeScreen *ui;
};

#endif // HOMESCREEN_H
