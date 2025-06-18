#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
import WeiJing_YS_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  WeiJing_YS:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        self.rootZoomed = False
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.Register(uiName,'root',root)
        style = WeiJing_YS_sty.SetupStyle(isTKroot)
        self.UIJsonString ='{"Version": "1.0.0", "UIName": "WeiJing_YS", "Description": "", "WindowSize": [869, 462], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": false, "WindowTitle": "维京运输工具 v2025051601", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": false, "MinSize": [0, 0], "ResolutionScaling": true, "PopupDebugDialog": false, "TransparentColor": null, "RootTransparency": 255, "ICOFile": "E:/App/WeiJing_YS/Resources/ICO_Timer.png", "ICOMode": "File", "WinState": 1, "WinTopMost": false, "BGColor": "#EFEFEF", "GroupList": {"Group_1": "1"}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#EFEFEF", "Size": [869, 462], "PlaceInfo": null, "EventList": {"Load": "Form_1_onLoad", "Exit": "Form_1_onExit"}}, {"Type": "ListView", "Index": 6, "AliasName": "ListView_1", "ParentName": "Form_1", "PlaceInfo": [2, 2, 301, 207, "nw", true, false], "Visible": true, "Size": [654, 451], "SelectMode": "EXTENDED", "RowHeight": 28, "ColumnList": [["口", "center", 35, false], ["ID", "center", 35, false], ["模拟器", "w", 100, false], ["用户坐标", "center", 100, false], ["食物", "center", 45, false], ["木材", "center", 45, false], ["石材", "center", 45, false], ["金币", "center", 45, false], ["操作", "center", 200, false]], "EventList": {"CellClicked": "ListView_1_onCellClicked"}}, {"Type": "Label", "Index": 18, "AliasName": "Label_1", "ParentName": "Form_1", "PlaceInfo": [328, 1, 46, 22, "nw", true, false], "Visible": true, "Size": [100, 48], "BGColor": "#EFEFEF", "Text": "操作面板", "FGColor": "#DA4453", "Font": ["Microsoft YaHei UI", 7, "bold", "roman", 0, 0]}, {"Type": "Button", "Index": 7, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [307, 27, 43, 18, "nw", true, false], "Visible": true, "Size": [95, 40], "BGColor": "#EFEFEF", "ActiveBGColor": "#EEEEEE", "Text": "全部开始", "FGColor": "#000000", "ActiveFGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "LabelFrame", "Index": 9, "AliasName": "LabelFrame_1", "ParentName": "Form_1", "PlaceInfo": [307, 156, 90, 52, "nw", true, false], "Visible": true, "Size": [196, 115], "BGColor": "#EFEFEF", "Text": "坐标设置", "Anchor": "nw", "Relief": "groove", "ScrollRegion": null}, {"Type": "Entry", "Index": 10, "AliasName": "Entry_1", "ParentName": "LabelFrame_9", "PlaceInfo": [3, 2, 81, 16, "nw", true, false], "Visible": true, "Size": [178, 36], "BGColor": "#FFFFFF", "BGColor_ReadOnly": "#EFEFEF", "Text": "0-0", "FGColor": "#000000", "InnerBorderColor": "#000000", "TipFGColor": "#888888", "Relief": "sunken"}, {"Type": "Button", "Index": 11, "AliasName": "Button_2", "ParentName": "LabelFrame_9", "PlaceInfo": [3, 23, 39, 16, "nw", true, false], "Visible": true, "Size": [85, 35], "BGColor": "#EFEFEF", "Text": "全部设置", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_2_onCommand"}}, {"Type": "Button", "Index": 16, "AliasName": "Button_3", "ParentName": "LabelFrame_9", "PlaceInfo": [46, 23, 39, 16, "nw", true, false], "Visible": true, "Size": [85, 35], "BGColor": "#EFEFEF", "Text": "设置选中", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_3_onCommand"}}, {"Type": "LabelFrame", "Index": 23, "AliasName": "LabelFrame_2", "ParentName": "Form_1", "PlaceInfo": [344, 132, 51, 22, "nw", true, false], "Visible": true, "Size": [112, 49], "BGColor": "#EFEFEF", "Text": "版本更新", "Anchor": "nw", "Relief": "groove", "ScrollRegion": null}, {"Type": "Label", "Index": 24, "AliasName": "Label_2", "ParentName": "LabelFrame_23", "PlaceInfo": [2, -5, 46, 22, "nw", true, false], "Visible": true, "Size": [100, 48], "BGColor": "#EFEFEF", "Text": "有新版本", "FGColor": "#000000", "Anchor": "w"}, {"Type": "Button", "Index": 25, "AliasName": "Button_8", "ParentName": "LabelFrame_23", "PlaceInfo": [30, 0, 17, 10, "nw", true, false], "Visible": true, "Size": [38, 23], "BGColor": "#EFEFEF", "Text": "更新", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_8_onCommand"}}, {"Type": "Button", "Index": 17, "AliasName": "Button_4", "ParentName": "Form_1", "PlaceInfo": [353, 27, 43, 18, "nw", true, false], "Visible": true, "Size": [95, 40], "BGColor": "#EFEFEF", "Text": "全部停止", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_4_onCommand"}}, {"Type": "Button", "Index": 19, "AliasName": "Button_5", "ParentName": "Form_1", "PlaceInfo": [307, 47, 43, 18, "nw", true, false], "Visible": true, "Size": [95, 40], "BGColor": "#EFEFEF", "Text": "选中开始", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_5_onCommand"}}, {"Type": "Button", "Index": 20, "AliasName": "Button_6", "ParentName": "Form_1", "PlaceInfo": [353, 47, 43, 18, "nw", true, false], "Visible": true, "Size": [95, 40], "BGColor": "#EFEFEF", "Text": "选中停止", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_6_onCommand"}}, {"Type": "Button", "Index": 21, "AliasName": "Button_7", "ParentName": "Form_1", "PlaceInfo": [308, 136, 33, 18, "nw", true, false], "Visible": true, "Size": [73, 40], "BGColor": "#EFEFEF", "Text": "刷新列表", "FGColor": "#000000", "Relief": "groove", "EventList": {"Command": "Button_7_onCommand"}}, {"Type": "Frame", "Index": 22, "AliasName": "Frame_1", "ParentName": "Form_1", "Layer": "lower", "PlaceInfo": [0, 0, 1.0, 1.0, "nw", true, true], "Visible": true, "Size": [869, 462], "BGColor": "#EFEFEF", "Relief": "flat", "ScrollRegion": null}]}'
        Form_1 = Fun.CreateUIFormJson(uiName,root,isTKroot,style,self.UIJsonString,False)
        #Inital all element's Data 
        Fun.LoadCanvasRecord(uiName,0.46029919447640966)
        #Call Form_1's OnLoad Function
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
            if self.rootZoomed == True and isinstance(self.root,tkinter.Tk) == True:
                self.root.state("zoomed")
                Fun.SetUIState(uiName,"zoomed")
                self.rootZoomed = False
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        #Call Form_1's OnExit Function
        if self.isTKroot == True and Result != False:
            Fun.DestroyUI(self.uiName,0,'')

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget and (self.configure_event is None or self.configure_event[2]!= event.width or self.configure_event[3]!= event.height):
            uiName = self.uiName
            self.configure_event = [event.x,event.y,event.width,event.height]
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            pass
    def ExecuteCode(self,CodeText):
        exec(CodeText)
