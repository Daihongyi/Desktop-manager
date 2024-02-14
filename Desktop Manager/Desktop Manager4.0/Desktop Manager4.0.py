from random import *
from easygui import*
import os
while True:
    msgbox("欢迎",title="Desktop4.0")
    n = enterbox("请选择功能,打开,质数判断,随机数,加密解密，退出",title="Desktop4.0")
    if n == "随机数":
        w = enterbox("请输入随机数最小值",title="Desktop4.0")
        v = enterbox("请输入随机数最大值",title="Desktop4.0")
        x = enterbox("请输入生成数量",title="Desktop4.0")
        w = int(w)
        v = int(v)
        x = int(x)
        a = []
        for i in range(x):
            a.append(str(randint(w, v)))
        b = ""
        for i in a:
            b = b + i
            b = b + ","

        msgbox(msg="结果为" + b,title="Desktop4.0")

    elif n == "打开":
        g = enterbox("请输入文件路径",title="Desktop4.0")
        os.system(g)
    elif n == "质数判断":
        a = enterbox("请输入",title="Desktop4.0")
        a = int(a)
        b = 0
        c = []
        if a == 0 or a == 1:
            msgbox("本数不为质数或合数",title="Desktop4.0")
        else:
            for i in range(1, a + 1):
                if a % i == 0:
                    b = b + 1
                    c.append(i)
            if b == 2:
                msgbox("质数",title="Desktop4.0")
                msgbox("它的约数有"+str(c),title="Desktop4.0")
            else:
                msgbox("合数",title="Desktop4.0")
                msgbox("它的约数有"+str(c),title="Desktop4.0")
    elif n == "加密解密":
        a = buttonbox(msg="你需要加密还是解密", choices=["加密", "解密"],title="Desktop4.0")
        if a == "加密":
            b = enterbox("请输入要加密的内容",title="Desktop4.0")
            c = enterbox("请输入要加密的格数（输入数字即可，最大为9，最小为1）",title="Desktop4.0")
            c = int(c)
            d = ""
            for i in b:
                e = ord(i)
                e = e + c
                e = chr(e)
                d = d + e
            d = str(d)
            c = str(c)

            msgbox("加密结果为" + c+d,title="Desktop4.0")

        if a == "解密":
            b = enterbox("请输入要解密的内容",title="Desktop4.0")

            c = int(b[0])
            d = ""
            for i in range(len(b)-1):
                e = ord(b[i+1])
                e = e - c
                e = chr(e)
                d = d + e
            msgbox("解密结果为" + d,title="Desktop4.0")



    else:
        break



