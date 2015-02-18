#include "homescreen.h"
#include "imageacquisition.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    HomeScreen w;
    //imageacquisition w;
    w.show();

    return a.exec();
}
