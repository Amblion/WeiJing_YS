#coding=utf-8
import sys
import threading
import os
import chardet
from os.path import abspath, dirname
from multiprocessing import  Process
import tempfile
import shutil
import smbclient
import airtest
import subprocess
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from tkinter import *
import Fun
import traceback
import dc
import jiaoben
uiName="WeiJing_YS"
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

 #编写bat脚本，删除旧程序，运行新程序
def writeUpgrade(exe_name):
    img_path = 'C:\\updata\\'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    b = open("C:\\updata\\upgrade.bat",'w')
    TempList = "@echo off\n"
    TempList += "if not exist "+r"\\192.168.6.218\\维京崛起\\其它\\工具版本热更新(非专业勿动勿删)\\维京运输工具\\" + exe_name + " exit \n"  #判断是否有新版本的程序，没有就退出更新。
    TempList += "echo 正在更新至最新版本...\n"
    TempList += "timeout /t 10 /nobreak\n"  #等待10秒
    TempList += "del " + os.path.realpath(exe_name) + "\n" #删除旧程序
    TempList += "copy "+r"\\192.168.6.218\\维京崛起\\其它\\工具版本热更新(非专业勿动勿删)\\维京运输工具\\" + exe_name + " " + exe_name + '\n' #复制新版本程序
    TempList += "echo 更新完成\n"
    TempList += "timeout /t 3 /nobreak\n"
    TempList += "exit"
    b.write(TempList)
    b.close()
    os.system('start C:\\updata\\upgrade.bat')  #显示cmd窗口
    sys.exit() #退出主程序

def jiaoben_run(task):
    device = "android://127.0.0.1:5037/"+task[8]+"?cap_method=javacap&touch_method=adb"
    x_y = task[3].split("-")
    jiaoben.run_main(x_y[0],x_y[1],task[4],task[5],task[6],task[7],device)
 
def add_task(data_index,task):
    #[True,task[1],"0-0",True,True,True,True,task[0]]
    Fun.SetCellCheckBox(uiName,'ListView_1',data_index,0,False)
    Fun.SetCellText(uiName,'ListView_1',data_index,1,task[0])
    Fun.SetCellText(uiName,'ListView_1',data_index,2,task[1])
    text = Fun.GetText(uiName,'Entry_1')
    Fun.SetCellText(uiName,'ListView_1',data_index,3,text)
    Fun.SetCellCheckBox(uiName,'ListView_1',data_index,4,False)
    Fun.SetCellCheckBox(uiName,'ListView_1',data_index,5,False)
    Fun.SetCellCheckBox(uiName,'ListView_1',data_index,6,False)
    Fun.SetCellCheckBox(uiName,'ListView_1',data_index,7,False)
    Fun.SetCellText(uiName,'ListView_1',data_index,8,task[10])
    pass
version = 2025051601    
#Form 'Form_1's Load Event :
def Form_1_onLoad(uiName,threadings=0):
    path = os.getcwd()
    if str(path).find("192.168.6.218") != -1:
        Fun.MessageBox("不支持在192.168.6.218共享目录内直接打开","运行错误","error",None)
        sys.exit() #退出主程序
    username = '技术部'  # 用户名
    password = 'Aa123654'  # 密码
    smbclient.reset_connection_cache()
    smbclient.ClientConfig(username=username, password=password)
    
    try:
        with smbclient.open_file("\\192.168.6.218\\技术部\\工具验证设置(非专业勿动勿删)\\维京运输工具\\version.txt",mode='rb') as f:
            raw_data = f.read()        
            result = chardet.detect(raw_data)
            encoding = result["encoding"]
        with smbclient.open_file(r"\\192.168.6.218\\技术部\\工具验证设置(非专业勿动勿删)\\维京运输工具\\version.txt",encoding=encoding) as f:
            new_version = f.read().split("----")
    except:
        Fun.MessageBox("验证异常！联系技术处理","运行错误","error",None)
        sys.exit() #退出主程序
    if(int(new_version[0]) > int(version)):
        if int(new_version[1]) == 1:
            Fun.MessageBox("有新版本，需要更新","更新提醒","info",None)
            writeUpgrade("维京运输工具.exe")
        Fun.SetText(uiName,'Label_2',"有新版本")
        Fun.SetTextColor(uiName,'Label_2','#00B800')
    else:
        pass
        Fun.SetText(uiName,'Label_2',"最新版本")
    
    
    Fun.SetRowBGColor(uiName,'ListView_1','even','lightblue')
    global Dc
    Dc = dc.Dnconsole(r'D:\leidian\LDPlayer9')
    ld_list = Dc.list2().split('\n')
    for i in ld_list:
        ld = i.split(",")
        if len(ld) != 1:
            ld.append("emulator-%s"%(5554+(int(ld[0]) * 2)))
            if Dc.isrunning(int(ld[0])):
                sss = Fun.AddRowText(uiName,'ListView_1','end',"")
                add_task(sss,ld)
    # 源文件夹路径（从哪里复制）
    source_folder = r'\\192.168.6.218\维京崛起\其它\工具版本热更新(非专业勿动勿删)\维京运输工具\weijing_yunshu'
    # 目标文件夹路径（复制到哪里）
    target_folder = r'C:\weijing_yunshu'
    # 判断目标文件夹是否存在
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)
    # 复制源文件夹到目标路径
    shutil.copytree(source_folder, target_folder)
    temp_dir = tempfile.gettempdir()
    source_path = os.path.abspath(r'C:\weijing_yunshu\airtest')
    for item in os.listdir(temp_dir):
        if item.startswith("_MEI"):
            target_path =str(os.path.join(temp_dir, item))+"\\airtest"
            # shutil.rmtree(os.path.join(temp_dir, item))
            # shutil.copy('C:\weijing_yunshu\airtest',os.path.join(temp_dir, item))
            if not os.path.exists(target_path):
                # 如果目标路径不存在原文件夹的话就创建
                os.makedirs(target_path)
    
            if os.path.exists(source_path):
                # 如果目标路径存在原文件夹的话就先删除
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
    
def ListView_1_onCellClicked(uiName,widgetName,rowIndex,columnIndex,threadings=0):
    pass
tasks = []  
def run_all_tasks():
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    global tasks 
    for task in tasks:
        task[1].terminate()
    for ld in listviewTextList:
        if Dc.isrunning(int(ld[1])):
            p = Process(target=jiaoben_run,args=(ld,)) #实例化进程对象
            p.start()
            tasks.append([ld[8],p])
        Fun.Sleep(5)
        
#Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName,widgetName,threadings=0): 
    run_thread = threading.Thread(target=run_all_tasks, args=[])
    run_thread.setDaemon(True)
    run_thread.start()
    
#Button 'Button_2' 's Command Event :
def Button_2_onCommand(uiName,widgetName,threadings=0):
    text = Fun.GetText(uiName,'Entry_1')
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    for ld in range(len(listviewTextList)):
        Fun.SetCellText(uiName,'ListView_1',ld,3,text)
        
#Button 'Button_3' 's Command Event :
def Button_3_onCommand(uiName,widgetName,threadings=0):
    text = Fun.GetText(uiName,'Entry_1')
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    for ld in range(len(listviewTextList)):
        if listviewTextList[ld][0]:
            Fun.SetCellText(uiName,'ListView_1',ld,3,text)
            
#Button 'Button_4' 's Command Event :
def Button_4_onCommand(uiName,widgetName,threadings=0):
    global tasks
    for task in tasks:
        task[1].terminate()
    
#Form 'Form_1's Exit Event :
def Form_1_onExit(uiName,threadings=0):
    print("退出")
    global tasks
    for task in tasks:
        task[1].terminate()
        
def run_sta_tasks():
    global tasks
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    for ld in range(len(listviewTextList)):
        if listviewTextList[ld][0]:
            for task in tasks:
                if listviewTextList[ld][8] == task[0]:
                    task[1].terminate()
            if Dc.isrunning(int(listviewTextList[ld][1])):        
                p = Process(target=jiaoben_run,args=(listviewTextList[ld],)) #实例化进程对象
                p.start()
                tasks.append([listviewTextList[ld][8],p])
        Fun.Sleep(5)
         
#Button 'Button_5' 's Command Event :
def Button_5_onCommand(uiName,widgetName,threadings=0): 
    run_thread = threading.Thread(target=run_sta_tasks, args=[])
    run_thread.setDaemon(True)
    run_thread.start()
            
#Button 'Button_6' 's Command Event :
def Button_6_onCommand(uiName,widgetName,threadings=0):
    global tasks
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    for ld in range(len(listviewTextList)):
        if listviewTextList[ld][0]:
            for task in tasks:
                if listviewTextList[ld][8] == task[0]:
                    task[1].terminate()
                    
#Button 'Button_7' 's Command Event :
def Button_7_onCommand(uiName,widgetName,threadings=0):
    listviewTextList = Fun.GetAllRowTextList(uiName,'ListView_1')
    Fun.DeleteAllRows(uiName,'ListView_1')
    ld_list = Dc.list2().split('\n')
    for i in ld_list:
        ld = i.split(",")
        if len(ld) != 1:
            if Dc.isrunning(int(ld[0])):
                old_list = []
                for new_old_list in listviewTextList:
                    if int(ld[0]) == int(new_old_list[1]):
                        old_list = new_old_list
                if len(old_list) != 0:
                    Fun.AddRowText(uiName,'ListView_1','end',old_list)  
                else: 
                    ld.append("emulator-%s"%(5554+(int(ld[0]) * 2)))        
                    sss = Fun.AddRowText(uiName,'ListView_1','end',"")
                    add_task(sss,ld)
#Button 'Button_8' 's Command Event :
def Button_8_onCommand(uiName,widgetName,threadings=0):
    with smbclient.open_file("\\192.168.6.218\\技术部\\工具验证设置(非专业勿动勿删)\\维京运输工具\\version.txt",mode='rb') as f:
        raw_data = f.read()        
        result = chardet.detect(raw_data)
        encoding = result["encoding"]
    with smbclient.open_file(r"\\192.168.6.218\\技术部\\工具验证设置(非专业勿动勿删)\\维京运输工具\\version.txt",encoding=encoding) as f:
        new_version = f.read().split("----")
    if (int(new_version[0]) > int(version)):
        writeUpgrade("维京运输工具.exe")
 
def get_info_msg():
    value = Fun.GetCurrentValue(uiName,'CheckButton_1')
    return value
