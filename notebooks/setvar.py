# Here we define some utility commands to simplify interaction with the shell.
# You don't need to read or understand this, but it's here in case you want to.
from subprocess import *
import re
import os
def repvar(v):
    """
    repvar() is short for "Replace Variables." The idea is that this
    function looks for strings of the form $VAR or ${VAR} or even
    $(CMD) in the input string and replaces them, either with
    the contents of os.environ[VAR] or os.pipe(CMD), mimicking the
    behavior of bash. If a backslace precedes the $, then the backslash
    will be removed but the string will not be evaluated. Thus:
    ${HOME} becomes "/home/user"
    $HOME becomes "/home/usr"
    $(echo Hello) becomes "Hello"
    \$HOME becomes $HOME
    """
    epos = 0
    buf = ''
    v = str(v)
    for g in re.finditer(r'\$((\w+)|\{([^}]*)\}|\(([^())]*)\))|(\\+\$)',v):
        if g:
            i = 2
            while g.group(i) == None:
                i += 1
            p = g.start(0)
            buf += v[epos:p]
            epos = p + len(g.group(0))
            if i == 4:
                #fh = os.popen(g.group(i),"r")
                fh = Popen(g.group(i),shell=True,close_fds=True,stdout=PIPE,stderr=STDOUT).stdout
                c = repvar(fh.read().decode('utf-8'))
                fh.close()
            elif i == 5:
                c = '$'
            else:
                if not g.group(i) in os.environ:
                    raise Exception("no such environment variable: "+g.group(i))
                c = repvar(os.environ[g.group(i)])
            buf += c
        else:
            break
    buf += v[epos:]
    return buf.strip()
def setvar(e):
    """
    setvar() emulates the ability of BASH to set environment variables.
    Thus, NAME=VALUE will set os.environ["NAME"]="VALUE". Bash-style
    comments will be stripped, and bash-line continuations will be processed.
    """
    e = re.sub(r'#[^\r\n]*','',e)
    e = re.sub(r'\\\n\s*','',e)
    for m in re.finditer(r'(?m)(\w+)=(.*)',e):
        k = m.group(1)
        v = repvar(m.group(2))
        if re.search("PASS",k):
          print(k+"=.....")
        else:
          print(k+"="+v)
        os.environ[k]=v
def readfile(f):
    """
    Reads in a file. repvar() will be applied to the file name.
    """
    n = repvar(f)
    print("Reading file `"+n+"'")
    fh = open(n)
    c = fh.read()
    fh.close()
    return c
def writefile(f,c):
    """
    Writes out a file. repvar() will be applied both to the file name
    and the file contents.
    """
    c = str(c)
    n = repvar(f)
    print("Writing file `"+n+"'")
    fd = os.open(n.encode('utf-8'),os.O_CREAT|os.O_TRUNC|os.O_WRONLY,0o600)
    os.write(fd,repvar(c).encode('utf-8'))
    os.close(fd)
    #fh = open(n,"w")
    #fh.write(repvar(c))
    #fh.close()

import getpass
def readpass(n):
    print("Password or secret: "+n)
    f = n+".txt"
    if os.path.exists(f):
        os.environ[n] = readfile(f)
    else:
        os.environ[n] = getpass.getpass()
        writefile(f,"$"+n)
