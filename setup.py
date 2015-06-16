from cx_Freeze import *
import sys

includefiles = ['ffmpeg/', 'setup.bat', 'wnd.pyc']

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('main.py', base=base, shortcutName="Gluer",
               shortcutDir="Gluer")
]

setup(name='Gluer',
      version='0.1',
      description='Video processing tool',
      executables=executables,
      options={'build_exe': {'include_files': includefiles}}
      )