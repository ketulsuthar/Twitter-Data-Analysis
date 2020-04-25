'''
Author : Ketulkumar
Email : k2lsuthar@gmail.com
_updated : 04-24-2020
'''

import os
import subprocess

_datadir = r'C:\Me\Study\Conestoga\II\PROG8460\Final\twitter_stream_2019_09_30\30'

def bz2_file_process(path):
    '''

    :param path: string
    :return:
    '''
    if not os.path.isfile(path): return
    _cdir = os.getcwd()
    _cpath = os.path.dirname(path)
    _filename = os.path.basename(path)

    _ffile = _filename[0:len(_filename) - 4]
    _ffilepath = os.path.join(_cpath, _ffile)
    if _filename.endswith(".bz2") and not os.path.isfile(_ffilepath):
        os.chdir(_cpath)
        system = subprocess.Popen([r"C:\Program Files\7-Zip\7z.exe", "e", _filename])
        os.chdir(_cdir)
        return (system.communicate())

def process_dir():
    '''
     Thid function get all dir from parent dir and pass that path to bz2_file_process for extraction
    :return: None
    '''
    os.chdir(_datadir)
    hours = os.listdir(".")
    for hour in hours:
        _dest = os.path.join(_datadir, hour)
        _files = os.listdir(_dest)
        for _f in _files:
            bz2_file_process(os.path.join(_dest,_f))


process_dir()

