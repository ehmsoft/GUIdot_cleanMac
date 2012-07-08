"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

NAME = 'Dot Clean'
ICONNAME = 'icono'
VERSION = '0.1'
ICONFILE = 'icono.icns'
plist = dict(
    CFBundleIconFile=ICONNAME,
    CFBundleName=NAME,
    CFBundleShortVersionString=VERSION,
    CFBundleGetInfoString=' '.join([NAME, VERSION]),
    CFBundleExecutable=NAME,
    CFBundleIdentifier='com.ehmsoftware.dotclean',
)

APP = ['GUIdot_cleanMac.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True, 'includes': ['PySide', 'PySide.QtCore', 'PySide.QtGui'],
			'excludes': ['PySide.QtDesigner', 'PySide.QtNetwork', 'PySide.QtOpenGL', 'PySide.QtScript', 'PySide.QtSql', 'PySide.QtTest', 'PySide.QtWebKit', 'PySide.QtXml', 'PySide.phonon'], 'plist':plist, 'iconfile':ICONFILE}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
