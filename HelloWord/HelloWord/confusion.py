#!/usr/bin/env python
# encoding=utf8
# -*- coding: utf-8 -*-
# 本脚本用于对源代码中的字符串进行加密
# 替换所有字符串常量为加密的char数组，形式((char[]){1, 2, 3, 0})

import importlib
import os
import re
import sys


# 替换字符串为((char[]){1, 2, 3, 0})的形式，同时让每个字节与0xAA异或进行加密
def replace(match):
    string = match.group(2) + '\x00'
    replaced_string = '((char []) {' + ', '.join(["%i" % ((ord(c) ^ 0xAA) if c != '\0' else 0) for c in list(string)]) + '})'
    return match.group(1) + replaced_string + match.group(3)


# 修改源代码，加入字符串加密的函数
def obfuscate(file):
    with open(file, 'r') as f:
        code = f.read()
        f.close()
        code = re.sub(r'(confusion_NSSTRING\(|confusion_CSTRING\()"(.*?)"(\))', replace, code)
        code = re.sub(r'//#define ggh_confusion', '#define ggh_confusion', code)
        with open(file, 'w') as f:
            f.write(code)
            f.close()


#读取源码路径下的所有.h和.m 文件
def openSrcFile(path):    
    print("开始处理路径： "+ path +"  下的所有.h和.m文件")
    # this folder is custom
    for parent,dirnames,filenames in os.walk(path):
        #case 1:
#        for dirname in dirnames:
#            print((" parent folder is:" + parent).encode('utf-8'))
#            print((" dirname is:" + dirname).encode('utf-8'))
        #case 2
        for filename in filenames:
            extendedName = os.path.splitext(os.path.join(parent,filename))
            if (extendedName[1] == '.h' or extendedName[1] == '.m'):
                print("处理源代码文件: "+ os.path.join(parent,filename))
                obfuscate(os.path.join(parent,filename))


#源码路径工程名
srcPath = '../HelloWord'

if __name__ == '__main__':
    print("本脚本用于对源代码中被标记的字符串进行加密")

    if len(srcPath) > 0:
        openSrcFile(srcPath)
    else:
        print("请输入正确的源代码路径")
        sys.exit()





