#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import threading

class Dnconsole:
    '''
    【雷电控制台类】
    version: 9.0
    import该文件会自动实例化为 Dc
    '''
    def __init__( self, installation_path:str ):
        '''
        【构造方法】
        '''
        # if 模拟器安装路径存在性检测
        if os.path.exists(installation_path) is False:
            print('模拟器安装路径不存在！')
        # 获取模拟器安装路径
        self.ins_path = installation_path
        # Dnconsole程序路径
        self.console_path = self.ins_path + r'\ldconsole.exe '
        # if Dnconsole程序路径检测
        if os.path.exists(self.console_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整或模拟器版本是否不符！')
        # adb程序路径
        self.adb_path = self.ins_path + r'\adb.exe '
        # if adb程序路径检测
        if os.path.exists(self.adb_path) is False:
            print('Dnconsole程序路径不存在！\n请确认模拟器安装文件是否完整！')
        # 模拟器截屏程序路径
        self.screencap_path = r'/system/bin/screencap'
        # 模拟器截图保存路径
        self.devicess_path = r'/sdcard/autosS.png'
        # 本地图片保存路径
        self.images_path = r'D:\PycharmWorkspace\images'
        # 构造完成
        print('Class-Dnconsole is ready.(%s)' % (self.ins_path))

    def CMD( self, cmd:str ):
        '''
        【执行控制台命令语句】
        :param cmd: 命令
        :return: 控制台调试内容
        '''
        CMD = self.console_path + cmd # 控制台命令
        process = os.popen(CMD)
        result = process.read()
        process.close()
        return result

    def ADB( self, cmd:str ):
        '''
        【执行ADB命令语句】
        :param cmd: 命令
        :return: 控制台调试内容
        '''
        CMD = self.adb_path + cmd # adb命令
        process = os.popen(CMD)
        result = process.read()
        process.close()
        return result    

    def list(self):
        '''
        【获取模拟器列表（仅标题）】
        :return: 控制台调试内容
        '''
        cmd = 'list'
        return self.CMD(cmd)    
    
    def list2(self):
        '''
        【取模拟器列表】
        :return: 列表（索引、标题、顶层句柄、绑定句柄、是否进入android、进程PID、VBox进程PID）
        '''
        cmd = 'list2'
        return self.CMD(cmd)

    def runninglist(self):
        '''
        【获取正在运行的模拟器列表（仅标题）】
        :return: 控制台调试内容
        '''
        cmd = 'runninglist'
        return self.CMD(cmd)


    def isrunning( self, index:int = 0 ):
        '''
        【检测模拟器是否启动】
        :param index: 模拟器序号
        :return: True=已启动 / False=未启动
        '''
        cmd = 'isrunning --index %d' %(index)
        if self.CMD(cmd) == 'running': return True
        else: return False


    def actionOfTap( self, index:int, x:int, y:int ):
        '''
        【点击操作】
        :param index: 模拟器序号
        :param x: x
        :param y: y
        :return: 控制台调试内容
        '''
        cmd = 'adb --index %d --command "shell input tap %d %d"' %(index, x, y)
        return self.CMD(cmd)


    def actionOfInput( self, index:int, text:str ):
        '''
        【输入操作】
        :param index: 模拟器序号
        :param text: 文本内容
        :return: 控制台调试内容
        '''
        cmd = 'action --index %d --key call.input --value "%s"' %(index, text)
        return self.CMD(cmd)
    
    def actionOfKeyCode( self, index:int, keycode:int ):
        '''
        【键码输入操作】
        :param index: 模拟器序号
        :param keycode: 键码（0~9，10=空格）
        :return: 控制台调试内容
        '''
        try:
            list = ['KEYCODE_0', 'KEYCODE_1', 'KEYCODE_2', 'KEYCODE_3', 'KEYCODE_4', 'KEYCODE_5',
                    'KEYCODE_6', 'KEYCODE_7', 'KEYCODE_8', 'KEYCODE_9', 'KEYCODE_HOME']
            cmd = 'adb --index %d --command "shell input keyevent %s"' %(index, list[keycode])
            return self.CMD(cmd)
        except Exception as e:
            print(e)
    def actionOfKeyCode2(self, index: int, keycode: str):
        try:
            keycode_map = {
                        "0": 'KEYCODE_0', "1": 'KEYCODE_1', "2": 'KEYCODE_2', "3": 'KEYCODE_3', "4": 'KEYCODE_4',
                        '5': 'KEYCODE_5', '6': 'KEYCODE_6', '7': 'KEYCODE_7', '8': 'KEYCODE_8', '9': 'KEYCODE_9',
                        'A': 'KEYCODE_A', 'B': 'KEYCODE_B', 'C': 'KEYCODE_C', 'D': 'KEYCODE_D', 'E': 'KEYCODE_E',
                        'F': 'KEYCODE_F', 'G': 'KEYCODE_G', 'H': 'KEYCODE_H', 'I': 'KEYCODE_I', 'J': 'KEYCODE_J',
                        'K': 'KEYCODE_K', 'L': 'KEYCODE_L', 'M': 'KEYCODE_M', 'N': 'KEYCODE_N', 'O': 'KEYCODE_O',
                        'P': 'KEYCODE_P', 'Q': 'KEYCODE_Q', 'R': 'KEYCODE_R', 'S': 'KEYCODE_S', 'T': 'KEYCODE_T',
                        'U': 'KEYCODE_U', 'V': 'KEYCODE_V', 'W': 'KEYCODE_W', 'X': 'KEYCODE_X', 'Y': 'KEYCODE_Y',
                        'Z': 'KEYCODE_Z', '@': 'KEYCODE_AT', '.': 'KEYCODE_PERIOD'
                    }
            for i in keycode:
                v = i.upper()
                shift_pressed = False
                
                if i.islower():
                    # 按下 Shift 键
                    shift_cmd = 'adb --index %d --command "shell input keyevent 115"' % index
                    self.CMD(shift_cmd)
                    shift_pressed = True

                if v in keycode_map:
                    cmd = 'adb --index %d --command "shell input keyevent %s"' % (index, keycode_map[v])
                    result = self.CMD(cmd)
                else:
                    print(f"字符 '{i}' 没有对应的 keycode")

                if shift_pressed:
                    # 释放 Shift 键
                    shift_cmd = 'adb --index %d --command "shell input keyevent 115"' % index
                    self.CMD(shift_cmd)
            return result
        except Exception as e:
            print(e)
    def clear_input(self, index: int, length: int):
        '''
        【清空输入框内容】
        :param index: 模拟器序号
        :param length: 输入框内容的长度
        :return: 控制台调试内容
        '''
        # 发送多个退格键来清空输入框内容
        backspace_cmd = 'adb --index %d --command "shell input keyevent 67"' % index
        for _ in range(length):
            self.CMD(backspace_cmd)


  

if __name__ == '__main__':
    global Dc
    Dc = Dnconsole(r'D:\leidian\LDPlayer9')
    ld_list = Dc.list2().split('\n')
    for i in ld_list:
        ld = i.split(",")
        if len(ld) != 1:
            ld.append("emulator-%s"%(5554+(int(ld[0]) * 2)))
            if Dc.isrunning(int(ld[0])):
                print(ld)

