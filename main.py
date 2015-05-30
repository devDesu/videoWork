# -*- encode: utf-8 -*-
__author__ = 'Anton'
import struct
import os
import exceptions
import io


class Gluer:
    def __init__(self, path, fps=24, out_name='out.mp4'):
        self.path = path
        self.fps = fps
        self.out_name = out_name
        self.minutes = []

    def check(self):
        path = u'1/1/1.bmp'
        self.sze(path, path[path.index('.', len(path)-4)+1:])

    def get_minutes(self):
        self.minutes = os.listdir(self.path)  # 0 to 12, minutes
        total_minutes = len(self.minutes)
        counter = 0
        counter2 = 0
        total = 0
        self.minutes = {key: os.listdir(os.path.join(self.path, key)) for key in self.minutes}
        #  self.minutes = {1: 2, 3: 4}
        for key, value in self.minutes.iteritems():
            if len(value) < 59 and not (counter == 0 or counter == total_minutes):
                raise Exception('Seconds in minute error')
            counter += 1
            self.minutes[key] = {k2: os.listdir(os.path.join(self.path, key, k2)) for k2 in self.minutes[key]}
            for key2, value2 in self.minutes[key].iteritems():
                print self.minutes[key][key2]
                self.minutes[key][key2].sort(key=lambda x: len(x))
                if len(value2) < self.fps and not (counter2 == 0 or counter2 == 59):
                    raise Exception('fps error', len(value2), key2)
                counter2 += 1
            total += counter2
        print self.minutes

    def sze(self, filename, ftype):
        print ftype
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
            print width, height

h = Gluer(u'C:/Users/Public/test2')
#h.check()
h.get_minutes()