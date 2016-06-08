#coding=utf-8

# 参考文章：
#   1. pyqt 使用 Qt Designer 设计的ui文件
#       http://blog.csdn.net/lainegates/article/details/8656145
#   2. PyQt 4.11.4 Reference Guide Using Qt Designer
#       http://pyqt.sourceforge.net/Docs/PyQt4/designer.html
#   3. Create dynamic button in PyQt
#       http://stackoverflow.com/questions/10730131/create-dynamic-button-in-pyqt
#   4. How can I hide the console window in a PyQt app running on Windows?
#       http://stackoverflow.com/questions/466203/how-can-i-hide-the-console-window-in-a-pyqt-app-running-on-windows
#   5. pyqt如何关闭dos窗口
#       http://www.wosoni.com/osk/230860_91298.html
#   6. How do I copy a file in python?
#       http://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
#   7. IOError: [Errno 22] invalid mode ('r') or filename: ''
#       http://stackoverflow.com/questions/14597278/ioerror-errno-22-invalid-mode-r-or-filename

import sys
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )

from PyQt4.QtCore import *
from PyQt4.QtGui import *


from HardwareDialog import HardwareDialog

def getpwd():
    pwd = sys.path[0]
    if os.path.isfile(pwd):
        pwd = os.path.dirname(pwd)
    return pwd

def main():

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(getpwd()+"\logo.ico"))

    hardwareDialog = HardwareDialog()
    hardwareDialog.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
