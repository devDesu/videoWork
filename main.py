# -*- coding: utf-8 -*-
# -*- encode: utf-8 -*-
import threading
import time

__author__ = 'Anton'
import cv2
import struct
import os
import sys
from PyQt4 import QtGui

from wnd import Ui_MainWindow
import numpy as np


class Gluer:
    def __init__(self, path, fps=24, out_name='out.mp4'):
        self.path = path
        self.fps = fps
        self.out_name = out_name
        self.minutes = []
        self.total = None
        self.size = []
        self.done = 0

    def check_size(self, errorEdit):
        size = None
        for key, value in self.minutes.iteritems():
            for key2, value2 in value.iteritems():
                for filename in value2:
                    path = os.path.join(self.path, key, key2, filename)
                    if not size:
                        size = self.sze(path, path[path.index('.', len(path)-4)+1:])
                        temp_size = size
                    else:
                        temp_size = self.sze(path, path[path.index('.', len(path)-4)+1:])
                    if temp_size[0] != size[0] or temp_size[1] != size[1]:
                        # raise Exception('Image size error', path, size, temp_size)
                        if temp_size[0] > size[0]: size[0] = temp_size[0]
                        if temp_size[1] > size[1]: size[1] = temp_size[1]
        self.size = size
        errorEdit.append("max size is {} {}".format(*size))

    def work(self, clb, errorEdit, preview=False):
        fourcc = -1
        if preview: self.total = 48
        out = cv2.VideoWriter(self.out_name.encode('utf-8'), fourcc, self.fps, (self.size[0], self.size[1]),  True)
        for key, value in sorted(self.minutes.iteritems()):
            for key2, value2 in sorted(value.iteritems()):
                for filename in value2:
                    frame = cv2.imread(os.path.join(self.path, key, key2, filename).encode("utf-8"),
                                       flags=cv2.cv.CV_LOAD_IMAGE_COLOR)
                    out.write(frame)
                    errorEdit.append("{}\{}\{}".format(key, key2, filename))
                    self.done += 1
                    clb(self.done)
                    if self.done >= self.total:
                        out.release()
                        return
        out.release()

    def get_minutes(self, errorEdit):
        self.done = 0
        self.minutes = [x for x in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, x))]  # 0 to 12, minutes
        total_minutes = len(self.minutes)
        counter = 0  #
        total = 0
        self.minutes = {key: os.listdir(os.path.join(self.path, key)) for key in self.minutes}
        for key, value in self.minutes.iteritems():
            counter2 = 0
            counter += 1
            if len(value) != 59 and not counter == total_minutes:
                errorEdit.append('Seconds in minute error: {}: {}'.format(key, value))
            seconds_counter = len(self.minutes[key])
            counter3 = 0
            self.minutes[key] = {k2: os.listdir(os.path.join(self.path, key, k2)) for k2 in self.minutes[key]}
            for key2, value2 in sorted(self.minutes[key].iteritems()):
                errorEdit.append("{}\{}\{}".format(self.path, key, key2))
                self.minutes[key][key2].sort(key=lambda x: len(x))
                counter3 += 1
                print len(value2) != self.fps, counter3 == seconds_counter and counter == total_minutes
                if len(value2) != self.fps and not (counter == total_minutes and counter3 == seconds_counter):
                    errorEdit.append('fps error: {} {}\{}'.format(len(value2), key, key2))
                counter2 += len(value2)
            total += counter2
        self.total = total

    def sze(self, filename, ftype):
        with open(os.path.join(self.path, filename), 'rb') as i:
            if ftype == 'bmp':
                i.seek(18)
                ar = i.read(8)
                width, height = struct.unpack('<II', ar)
            elif ftype == 'png':
                head = i.read(24)
                if len(head) != 24:
                    return
                check = struct.unpack('>i', head[4:8])[0]
                if check != 0x0d0a1a0a:
                    return
                width, height = struct.unpack('>ii', head[16:24])
            else:
                width, height = 1280, 720
            return [width, height]


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # self variables
        self.gluerInstance = Gluer('', 24, '')
        # another part
        app = QtGui.QApplication(sys.argv)
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.selectFolder.clicked.connect(self.clk)
        self.check.clicked.connect(self.chk)
        self.run.clicked.connect(self.rn)
        self.fps.valueChanged.connect(self.chn)
        self.show()
        app.exec_()

    def chn(self):
        self.gluerInstance.fps = self.fps.value()

    def rn(self):
        self.gluerInstance.fps = self.fps.value()
        self.progressBar.setValue(0)
        max = 48 if self.preview.isChecked() else self.gluerInstance.total
        self.progressBar.setMaximum(max)
        threading.Thread(group=None, target=self.gluerInstance.work(self.callback, self.errorEdit, self.preview.isChecked()),
                         name='worker thread').start()

    def callback(self, inp):
        self.progressBar.setValue(inp)

    def clk(self):
        temp = QtGui.QFileDialog.getExistingDirectory(self)
        self.gluerInstance.path = unicode(temp)
        self.check.setEnabled(True)
        self.label.setText(temp)
        self.run.setEnabled(False)
        self.gluerInstance.out_name = os.path.join(self.gluerInstance.path, 'out.avi')

    def chk(self):
            self.gluerInstance.get_minutes(self.errorEdit)
            self.gluerInstance.check_size(self.errorEdit)
            self.run.setEnabled(True)

f = MainWindow(None)