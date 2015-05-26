#!/usr/bin/python

import os

def replace_in_file(path, a, b):
    f = open(path, 'r')
    s = f.read().replace(a, b)
    f.close()
    f = open(path, 'w')
    f.write(s)
    f.close()

def replace_in_filename(path, a, b):
    j = len(path)-1
    if path[j]!='/':
        j-=1
    while j>0 and path[j]!='/':
        j-=1
    base = path[:j]
    filename = path[j:]
    if a in filename:
        newname = filename.replace(a, b)
        os.rename(path, base+newname)
        return base+newname
    return path

def deepreplace(path, a, b):
    l = []
    if path == '':
        path = '.'
    if path[len(path)-1] == '/':
        path = path[:(len(path)-1)]
    print path
    try:
        l = os.listdir(path)
    except:
        pass
    if l:
        for file in l:
            deepreplace(path + '/' + file, a, b)
    else:
        if path[0] != '.':
            replace_in_file(path, a, b)
    replace_in_filename(path, a, b)

import sys

if len(sys.argv) > 3:
    deepreplace(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print('Arguments: path a b')
    print('Replaces a with b in file or directory at path.  Also replaces a with b in filenames.')

