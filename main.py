# -*- coding: utf-8 -*-
# -*- encode: utf-8 -*-
import time

__author__ = 'Anton'
import cv2
import struct
import os
import numpy as np


class Gluer:
    def __init__(self, path, fps=24, out_name='out.mp4'):
        self.path = path
        self.fps = fps
        self.out_name = out_name
        self.minutes = []
        self.total = None
        self.size = []

    def check_size(self):
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
                        #raise Exception('Image size error', path, size, temp_size)
                        if temp_size[0] > size[0]: size[0] = temp_size[0]
                        if temp_size[1] > size[1]: size[1] = temp_size[1]
        self.size = size

    def get_minutes(self):
        self.minutes = os.listdir(self.path)  # 0 to 12, minutes
        total_minutes = len(self.minutes)
        counter = 0  #
        total = 0
        self.minutes = {key: os.listdir(os.path.join(self.path, key)) for key in self.minutes}
        for key, value in self.minutes.iteritems():
            counter2 = 0
            if len(value) < 59 and not (counter == 0 or counter == total_minutes):
                raise Exception('Seconds in minute error')
            counter += 1
            self.minutes[key] = {k2: os.listdir(os.path.join(self.path, key, k2)) for k2 in self.minutes[key]}
            for key2, value2 in self.minutes[key].iteritems():
                self.minutes[key][key2].sort(key=lambda x: len(x))
                if len(value2) < self.fps and not (counter == len(key2)):
                    raise Exception('fps error', len(value2), os.path.join(self.path, key, key2))
                counter2 += 1
            total += counter2
            #if total >= 48:
            #    self.total = 48
            #    return
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
                width, height = 720, 1280
            return [width, height]

h = Gluer(u'G:\\fight')
h.get_minutes()
h.check_size()
fourcc = -1
out = cv2.VideoWriter(u'G:\\out.avi'.encode('utf-8'), fourcc, 12.0, (h.size[1], h.size[0]),  True)
for key, value in h.minutes.iteritems():
    for key2, value2 in value.iteritems():
        for filename in value2:
            frame = cv2.imread(os.path.join(h.path, key, key2, filename).encode("utf-8"),
                               flags=cv2.cv.CV_LOAD_IMAGE_COLOR)
            #frame.resize(h.size)
            time.sleep(1)
            print frame.shape
            out.write(frame)
out.release()