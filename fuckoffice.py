# -*- coding: utf-8 -*-
import ctypes,sys,os,struct

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_YELLOW = 0x0e # yellow.
 
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
#暗天蓝色
#dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()
 
#绿色
#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
 
#红色
#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()
 
#黄色
#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()


printRed(u'欢迎使用：《fuck office》\n')
printDarkSkyBlue(u'还在为第二天交word没有写而悔恨吗？\n还在为excel的任务重时间紧而焦虑吗？\n还在为ppt没有做完而懊恼吗?\n\
试试《fuck office》吧！生成任意大小损坏的office文件，为你争取足够的时间！睡个好觉，第二天萌萌的说：“我发了\
啊！可能压缩的时候损坏了吧!？”\n')
printYellow(u'还支持压缩包哦，亲!!!(#￣～￣#)\n')
printRed(u'使用帮助：\n')
printGreen(u'直接输入命令：fuck excel/ppt/word/rar/zip <name> <size>, size单位：kb\n')
printGreen(u'2007+版本office，请使用:fucknew\n')
printGreen(u'退出：quit\n')

#生成文件函数
def generator(name, size, filetype):
    content = '发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到发送到反反复复发送到方式胜多负少方式发'
    bs = struct.pack('s',content)
    f = open(name+filetype, 'w')
    int_size = int(size)*1024
    for i in range(int_size):  
        f.write(bs)
    f.close()
    print (name+filetype+u'生成成功!\n')

while True:
    name = raw_input()
    cmds = name.split(" ")

    # xlsx xlsx
    # ppt pptx
    # doc docx
    if cmds[0] == 'fuck':
        if cmds[1] == 'excel':
            generator(cmds[2], cmds[3], '.xls')
        elif cmds[1] == 'ppt':
            generator(cmds[2], cmds[3], '.ppt')
        elif cmds[1] == 'word':
            generator(cmds[2], cmds[3], '.doc')
        elif cmds[1] == 'rar':
            generator(cmds[2], cmds[3], '.rar')
        elif cmds[1] == 'zip':
            generator(cmds[2], cmds[3], '.zip')
        else:
            print (u'不包含 '+cmds[1]+' 类型，仅支持 excel, ppt, word, rar, zip\n')
    elif cmds[0] == 'fucknew':
        if cmds[1] == 'excel':
            generator(cmds[2], cmds[3], '.xlsx')
        elif cmds[1] == 'ppt':
            generator(cmds[2], cmds[3], '.pptx')
        elif cmds[1] == 'word':
            generator(cmds[2], cmds[3], '.docx')
        elif cmds[1] == 'rar':
            generator(cmds[2], cmds[3], '.rar')
        elif cmds[1] == 'zip':
            generator(cmds[2], cmds[3], '.zip')
        else:
            printRed (u'不包含 '+cmds[1]+' 类型，仅支持 excel, ppt, word, rar, zip\n')
    elif cmds[0] == 'quit':
        printGreen (u'谢谢您的使用(*^__^*)')
        break
    else:
        printRed (u'命令错误，格式应为： fuck excel/ppt/word/rar/zip <name> <size>\n')


    


