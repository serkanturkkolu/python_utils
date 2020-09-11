import os, tempfile
class sh:  # This utility to use to shell script with python
    _sysout = ''
    def write(cmd):
        global _sysout
        _sysout = ''
        t_file = tempfile.NamedTemporaryFile(mode="r")
        os.system(cmd + "> " + str(t_file.name))
        _sysout = t_file.read()
        t_file.close()
        print(_sysout,end="")
        return _sysout

    def read():
        global _sysout
        return _sysout

