contains(QT_VERSION, ^4\.[0-7]\..*) {
    error("Can't build with Qt version $${QT_VERSION}. Use at least Qt 4.8.")
}

TEMPLATE = subdirs
SUBDIRS = repos ssu
