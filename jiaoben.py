from airtest.cli.parser import cli_setup
from airtest.core.api import *
import threading
import logging
import WeiJing_YS_cmd

#logger = logging.getLogger("airtest")
#logger.setLevel(logging.ERROR)
#logger.setLevel(logging.WARNING)

#全局配置
config_device = ""
config_x = 0
config_y = 0
config_sw = False
config_mc = False
config_sc = False
config_jb = False
config_lm = False

def info_Thread():
    while True:
        try:
            sss =  exists(Template(r"C:\weijing_yunshu\堡内.png", record_pos=(-0.444, 0.22), resolution=(960, 540)))
            if sss != False:
                touch(sss)
#                 sleep(1.5)
#                 touch((55,405))
        except:
            print("小错误，将自动处理")
        sleep(5.0)

def err_run():
    try:
        sta = exists(Template(r"C:\weijing_yunshu\确定退出文字.png", record_pos=(-0.004, -0.028), resolution=(960, 540)))
        while sta == False:
            keyevent("BACK")
            sleep(1.0)
            sta = exists(Template(r"C:\weijing_yunshu\确定退出文字.png", record_pos=(-0.004, -0.028), resolution=(960, 540)))
        touch(Template(r"C:\weijing_yunshu\取消.png", record_pos=(-0.114, 0.102), resolution=(960, 540)))
#         sleep(1.0)
#         touch((55,480))
        sleep(1)
        sta = exists(Template(r"C:\weijing_yunshu\堡外.png", record_pos=(-0.442, 0.219), resolution=(960, 540)))
        while sta == False:
            sleep(1.0)
            sta = exists(Template(r"C:\weijing_yunshu\堡外.png", record_pos=(-0.442, 0.219), resolution=(960, 540)))
        x_y_input()
    except:
        err_run()
        
        
def x_y_input():
    global config_lm
    try:
        sta = exists(Template(r"C:\weijing_yunshu\前往.png", record_pos=(0.261, -0.074), resolution=(960, 540)))
        run_num = 0
        while sta == False:
            if run_num >= 5:
                raise ValueError("a 找不到")
            touch(get_xy(Template(r"C:\weijing_yunshu\坐标搜索.png", record_pos=(-0.031, -0.26), resolution=(960, 540))))
            sleep(1.0)
            sta = exists(Template(r"C:\weijing_yunshu\前往.png", record_pos=(0.261, -0.074), resolution=(960, 540)))
            run_num += 1
        sleep(1.0)    
        #输入X
        for x_num in str(config_x):
            if exists(Template(r"C:\weijing_yunshu\删除.png")) == False:
                touch((435,200))
                sleep(1.0)
                touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%("AC"))))
                sleep(0.5)
            touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%(x_num)))) 
            sleep(0.5)
            
        touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%("OK"))))  
        sleep(0.5)
        touch((590,200))   
        sleep(1.0)
        
        for y_num in str(config_y):    
            if exists(Template(r"C:\weijing_yunshu\删除.png")) == False:
                touch((590,200))
                sleep(1.0)
                touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%("AC"))))
                sleep(0.5)
            touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%(y_num)))) 
            sleep(0.5)
        touch(get_xy(Template(r"C:\weijing_yunshu\%s.png"%("OK"))))
        sleep(0.5)
        touch(sta)
        sleep(5.0)
        if config_lm:
            jiaru_bulou()
            print("已加入")
            sleep(1.0)
            keyevent("BACK")
            config_lm = False
        resource_transportation()    
    except:
        err_run()    


#资源运输
def resource_transportation():
    zhongxin_x = 230
    while True:
        try:
            touch((460,zhongxin_x))
            sta = exists(Template(r"C:\weijing_yunshu\%s.png"%("查看信息"), resolution=(960, 540)))
            run_num = 0
            while sta == False:
                if run_num >= 6:
                    raise ValueError("a 找不到")
                touch((460,zhongxin_x))
                sleep(1.0)
                sta = exists(Template(r"C:\weijing_yunshu\%s.png"%("查看信息"), resolution=(960, 540)))
                run_num += 1
                zhongxin_x += 20
            sleep(2.0)
            touch(get_xy(Template(r"C:\weijing_yunshu\资源援助.png", resolution=(960, 540))))
            sleep(2.0)
            if config_sw or config_mc or config_sc or config_jb: 
                if config_sw:
                    touch((660,185))
                    sleep(1.0)
                if config_mc:
                    touch((660,240))
                    sleep(1.0)
                if config_sc:
                    touch((660,300))
                    sleep(1.0)
                if config_jb:
                    touch((660,355))
                    sleep(1.0)
                touch(get_xy(Template(r"C:\weijing_yunshu\运输.png", record_pos=(0.118, 0.164), resolution=(960, 540)))) 
            else: 
                keyevent("BACK")
            sleep(5.0)
        except:
            err_run()
        
def jiaru_bulou():
    zhongxin_x = 230
    touch((460,zhongxin_x))
    sta = exists(Template(r"C:\weijing_yunshu\%s.png"%("查看信息"), resolution=(960, 540)))
    run_num = 0
    while sta == False:
        if run_num >= 6:
            raise ValueError("a 找不到")
        touch((460,zhongxin_x))
        sleep(1.0)
        sta = exists(Template(r"C:\weijing_yunshu\%s.png"%("查看信息"), resolution=(960, 540)))
        run_num += 1
        zhongxin_x += 20
    touch(sta)
    sleep(1.0)
    touch(get_xy(Template(r"C:\weijing_yunshu\查看联盟.png", record_pos=(0.399, 0.028), resolution=(960, 540))))
    sleep(1.0)
    ss = exists(Template(r"C:\weijing_yunshu\加入部落.png", record_pos=(0.263, 0.193), resolution=(960, 540)))
    if ss != False:
        touch(ss)
    else:    
        sss = exists(Template(r"C:\weijing_yunshu\部落.png", record_pos=(-0.408, -0.259), resolution=(960, 540)))
        sleep(1.0)
        if sss == False:
            keyevent("BACK")
            sleep(1.0)
            keyevent("BACK")
            sleep(1.0)
            touch(get_xy(Template(r"C:\weijing_yunshu\进入部落.png", record_pos=(0.388, 0.243), resolution=(960, 540))))
            sleep(1.0)
            touch(get_xy(Template(r"C:\weijing_yunshu\部落设置.png", record_pos=(0.411, 0.217), resolution=(960, 540))))
            sleep(1.0)
            touch(get_xy(Template(r"C:\weijing_yunshu\退出部落.png", record_pos=(0.411, 0.217), resolution=(960, 540))))
            sleep(1.0)
            touch(get_xy(Template(r"C:\weijing_yunshu\确定退出.png", record_pos=(0.109, 0.102), resolution=(960, 540))))
            sleep(1)
            jiaru_bulou()
        
    
def get_xy(img):
    for i in range(5):
        sta = exists(img)
        if sta != False:
            return sta
    raise ValueError("a 找不到")     

def run(x,y,sw,mc,sc,jb,lm):
    global config_x
    global config_y
    global config_sw
    global config_mc
    global config_sc
    global config_jb
    global config_lm
    config_x = x
    config_y = y
    config_sw = sw
    config_mc = mc
    config_sc = sc
    config_jb = jb 
    config_lm = lm 
    info_run = threading.Thread(target=info_Thread)  
    info_run.start()
    x_y_input()
       

def run_main(x,y,sw,mc,sc,jb,device):
    if not cli_setup():
        auto_setup(__file__, devices=[device,])
    print(device,"尝试连接运输")
    logger = logging.getLogger("airtest")
    logger.setLevel(logging.ERROR)
    logger.setLevel(logging.WARNING)   
    run(x,y,sw,mc,sc,jb,False)


#if __name__ == "__main__":
    #run_main(x=0,y=0,sw=False,mc=False,sc=False,jb=False,device="emulator-5556")

