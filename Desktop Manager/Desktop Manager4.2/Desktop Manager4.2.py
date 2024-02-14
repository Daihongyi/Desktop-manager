from random import *
from easygui import*
import time

import os
while True:
    msgbox("欢迎",title="Desktop4.1")
    n = enterbox("请选择功能,打开,质数判断,随机数,加密解密，抛硬币模拟器，退出",title="Desktop4.1")
    if n == "随机数":
        w = enterbox("请输入随机数最小值",title="Desktop4.1")
        v = enterbox("请输入随机数最大值",title="Desktop4.1")
        x = enterbox("请输入生成数量",title="Desktop4.1")
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

        msgbox(msg="结果为" + b,title="Desktop4.1")
        with open("随机数结果.txt", "w") as f:
            f.write("随机数结果为" + b)

    elif n == "打开":
        g = enterbox("请输入文件路径",title="Desktop4.1")
        os.system(g)
    elif n == "质数判断":
        a = enterbox("请输入",title="Desktop4.1")
        a = int(a)
        b = 0
        c = []
        if a == 0 or a == 1:
            msgbox("本数不为质数或合数",title="Desktop4.1")
        else:
            for i in range(1, a + 1):
                if a % i == 0:
                    b = b + 1
                    c.append(i)
            if b == 2:
                msgbox("质数",title="Desktop4.1")
                msgbox("它的约数有"+str(c),title="Desktop4.1")
                with open("质数判断结果.txt", "w") as f:
                    f.write(str(a)+"是质数，它的约数有"+str(c))
            else:
                msgbox("合数",title="Desktop4.1")
                msgbox("它的约数有"+str(c),title="Desktop4.1")
                with open("质数判断结果.txt", "w") as f:
                    f.write(str(a)+"是合数，它的约数有"+str(c))
    elif n == "加密解密":
        a = buttonbox(msg="你需要加密还是解密", choices=["加密", "解密"],title="Desktop4.1")
        if a == "加密":
            b = enterbox("请输入要加密的内容",title="Desktop4.1")
            c = enterbox("请输入要加密的格数（输入数字即可，最大为9，最小为1）",title="Desktop4.1")
            c = int(c)
            d = ""
            for i in b:
                e = ord(i)
                e = e + c
                e = chr(e)
                d = d + e
            d = str(d)
            c = str(c)

            msgbox("加密结果为" + c+d,title="Desktop4.1")
            with open("加密结果为.txt","w")as f:
                f.write("加密结果为" + d)

        if a == "解密":
            b = enterbox("请输入要解密的内容",title="Desktop4.1")

            c = int(b[0])
            d = ""
            for i in range(len(b)-1):
                e = ord(b[i+1])
                e = e - c
                e = chr(e)
                d = d + e
                d = str(d)
            msgbox("解密结果为" + d,title="Desktop4.1")
            with open("解密结果为.txt","w")as f:
                f.write("解密结果为" + d)
    elif n == "抛硬币模拟器":
        a = enterbox("输入抛硬币的次数",title="Desktop4.1")

        a = int(a)
        z = 0
        f = 0
        g = 0
        for i in range(a):
            time.sleep(0.0001)
            with open("desktop.txt","a")as m:

                m.write("这是第" + str(i + 1) + "次模拟\r\n")

                c = randint(0, 1)
                if c == 0:
                    z = z + 1
                    m.write("本次结果为正\r\n")
                if c == 1:
                    f = f + 1
                    m.write("本次结果为反\r\n")

        msgbox("正面有"+str(z)+"次"+","+"反面有"+str(f)+"次",title="Desktop4.1")
        with open("desktop.txt","a")as m:
            m.write("正面有"+str(z)+"次"+","+"反面有"+str(f)+"次\r\n")




    else:
        break



