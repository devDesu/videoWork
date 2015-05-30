# -*- encode: utf-8 -*-
__author__ = 'Anton'
import struct
import os
import io


class Gluer:
    def __init__(self, path, fps=24, out_name='out.mp4'):
        self.path = path
        self.fps = fps
        self.out_name = out_name

    def check(self):
        path = u'1/1/2.png'
        self.sze(path, path[path.index('.', len(path)-4)+1:])

    def sze(self, filename, ftype):
        print ftype
        with io.open(os.path.join(self.path, filename), 'rb') as i:
            if ftype == 'bmp':
                ar = bytearray(8)
                i.seek(18)
                i.readinto(ar)
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
h.check()