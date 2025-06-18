from airtest.cli.runner import AirtestCase, run_script
from airtest.cli.parser import runner_parser

class CustomAirtestCase(AirtestCase):
    def setUp(self):
        # 在air脚本运行之前获取这个自定义的参数
        if self.args.xy:
            self.scope['xy']=self.args.xy
        if self.args.xy:
            self.scope['sw']=self.args.sw    
        if self.args.xy:
            self.scope['mc']=self.args.mc 
        if self.args.xy:
            self.scope['sc']=self.args.sc 
        if self.args.xy:
            self.scope['jb']=self.args.jb  

if __name__ == '__main__':
    ap = runner_parser()
    # 添加自定义的命令行参数
    ap.add_argument("--xy", help="客户坐标")
    ap.add_argument("--sw", help="食物")
    ap.add_argument("--mc", help="木材")
    ap.add_argument("--sc", help="石材")
    ap.add_argument("--jb", help="金币")
    args = ap.parse_args()
    run_script(args, CustomAirtestCase)

