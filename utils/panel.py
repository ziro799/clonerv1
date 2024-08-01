from rich .console import Console #line:1
from rich .table import Table #line:2
from rich .text import Text #line:3
from rich .style import Style #line:4
from rich .panel import Panel as RichPanel #line:5
from rich .align import Align #line:6
import json #line:7
def load_config (file_path ="./utils/config.json"):#line:9
    with open (file_path ,"r")as OOO0O000OO000O0O0 :#line:10
        return json .load (OOO0O000OO000O0O0 )#line:11
def create_table (O00OOO00OOO0OO0OO ,OO0OO000O0OOO0OO0 ,OO00OOOOO00OO000O ,O0O0OO00O0O000000 ,OO0OO00OOOO0O00O0 ):#line:13
    O00O0000OOOOO0OOO =Table (title =O00OOO00OOO0OO0OO ,show_header =True ,header_style ="bold")#line:14
    for OOOO0OO000OO0O000 in OO0OO000O0OOO0OO0 :#line:15
        O00O0000OOOOO0OOO .add_column (OOOO0OO000OO0O000 ["header"],style =OOOO0OO000OO0O000 .get ("style","white"),no_wrap =OOOO0OO000OO0O000 .get ("no_wrap",False ),width =OOOO0OO000OO0O000 .get ("width",None ),justify =OOOO0OO000OO0O000 .get ("justify","left"))#line:22
    for O00000OOOO00OO0OO ,O0OO00O0OO00O0OOO in OO00OOOOO00OO000O .items ():#line:24
        O00O0000OOOOO0OOO .add_row (O00000OOOO00OO0OO .capitalize (),Text ("ON"if O0OO00O0OO00O0OOO else "OFF",style =O0O0OO00O0O000000 if O0OO00O0OO00O0OOO else OO0OO00OOOO0O00O0 ))#line:25
    return O00O0000OOOOO0OOO #line:27
def create_footer (O0O0O0OO00000OO00 ,OO0OO0OO00OOOOOO0 ):#line:29
    O00OO0O00OOO000O0 =Table (show_header =False ,header_style ="bold",show_lines =False ,width =47 )#line:30
    O00OO0O00OOO000O0 .add_column (justify ="center")#line:31
    O00OO0O00OOO000O0 .add_row (f"[bold magenta]Server Cloned: [magenta]{O0O0O0OO00000OO00}")#line:32
    O00OO0O00OOO000O0 .add_row (f"[bold magenta]Logged in as: [magenta]{OO0OO0OO00OOOOOO0}")#line:33
    return O00OO0O00OOO000O0 #line:34
def display_panel (O0OOOOO0O000O00OO ,O0O000OO0OO00000O ):#line:36
    O000000OO0O0O0O0O =Console ()#line:37
    O000000OO0O0O0O0O .print (Align .center (RichPanel (O0OOOOO0O000O00OO ,style ="bold magenta",width =47 )))#line:38
    O000000OO0O0O0O0O .print (Align .center (RichPanel (f"Version: {O0O000OO0OO00000O}",style ="bold magenta",width =47 )))#line:39
def Panel ():#line:41
    O000OOO00OO00OO00 =load_config ()#line:42
    O00000OO0O0O00O0O =Style (color ="magenta",bold =True )#line:43
    OO00O000O0O0OOO00 =Style (color ="magenta",bold =True )#line:44
    O00O0O0OO00000OO0 =[{"header":"Setting","style":"magenta","no_wrap":True ,"width":30 },{"header":"Status","justify":"center","width":10 }]#line:49
    O00O0OOOOO000O0O0 =create_table ("",O00O0O0OO00000OO0 ,O000OOO00OO00OO00 ["copy_settings"],O00000OO0O0O00O0O ,OO00O000O0O0OOO00 )#line:50
    O000000O0O0O00O0O ="""
 ██████████    ███                                          █████      █████████  ████                                        
░░███░░░░███  ░░░                                          ░░███      ███░░░░░███░░███                                        
 ░███   ░░███ ████   █████   ██████   ██████  ████████   ███████     ███     ░░░  ░███   ██████  ████████    ██████  ████████ 
 ░███    ░███░░███  ███░░   ███░░███ ███░░███░░███░░███ ███░░███    ░███          ░███  ███░░███░░███░░███  ███░░███░░███░░███
 ░███    ░███ ░███ ░░█████ ░███ ░░░ ░███ ░███ ░███ ░░░ ░███ ░███    ░███          ░███ ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ 
 ░███    ███  ░███  ░░░░███░███  ███░███ ░███ ░███     ░███ ░███    ░░███     ███ ░███ ░███ ░███ ░███ ░███ ░███░░░   ░███     
 ██████████   █████ ██████ ░░██████ ░░██████  █████    ░░████████    ░░█████████  █████░░██████  ████ █████░░██████  █████    
░░░░░░░░░░   ░░░░░ ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░      ░░░░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░  
                                                made by laxiorr with <3      
"""#line:62
    O0O0OOOOO00O000OO =Console ()#line:64
    O0O0OOOOO00O000OO .print (Align .center (O000000O0O0O00O0O ,style ="bold magenta"))#line:65
    O0O0OOOOO00O000OO .print (Align .center (O00O0OOOOO000O0O0 ))#line:66
def Panel_Run (OO0OO0OO000O0O000 ,OOOO0O00OO0OOO0O0 ):#line:68
    O0000O0O0O0OOO00O =load_config ()#line:69
    O00OO0O00O0OOOOOO =Style (color ="magenta",bold =True )#line:70
    O0OO0O00OO0O00OOO =Style (color ="magenta",bold =True )#line:71
    OO0O000OO000OOOOO =[{"header":"Cloner is Running...","style":"magenta","no_wrap":True ,"width":30 },{"header":"Status","justify":"center","width":10 }]#line:76
    O0000OO00O0O0O000 =create_table ("Discord Server Cloner",OO0O000OO000OOOOO ,O0000O0O0O0OOO00O ["copy_settings"],O00OO0O00O0OOOOOO ,O0OO0O00OO0O00OOO )#line:77
    OO0OOO0O0O000OOO0 =create_footer (OO0OO0OO000O0O000 ,OOOO0O00OO0OOO0O0 )#line:78
    O0O00OO00O000OOOO ="""
 ██████████    ███                                          █████      █████████  ████                                        
░░███░░░░███  ░░░                                          ░░███      ███░░░░░███░░███                                        
 ░███   ░░███ ████   █████   ██████   ██████  ████████   ███████     ███     ░░░  ░███   ██████  ████████    ██████  ████████ 
 ░███    ░███░░███  ███░░   ███░░███ ███░░███░░███░░███ ███░░███    ░███          ░███  ███░░███░░███░░███  ███░░███░░███░░███
 ░███    ░███ ░███ ░░█████ ░███ ░░░ ░███ ░███ ░███ ░░░ ░███ ░███    ░███          ░███ ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ 
 ░███    ███  ░███  ░░░░███░███  ███░███ ░███ ░███     ░███ ░███    ░░███     ███ ░███ ░███ ░███ ░███ ░███ ░███░░░   ░███     
 ██████████   █████ ██████ ░░██████ ░░██████  █████    ░░████████    ░░█████████  █████░░██████  ████ █████░░██████  █████    
░░░░░░░░░░   ░░░░░ ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░      ░░░░░░░░      ░░░░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░  
"""#line:89
    O0O00OOO0O000O000 =Console ()#line:91
    O0O00OOO0O000O000 .print (Align .center (O0O00OO00O000OOOO ,style ="bold magenta"))#line:92
    O0O00OOO0O000O000 .print (Align .center (O0000OO00O0O0O000 ))#line:93
    O0O00OOO0O000O000 .print (Align .center (OO0OOO0O0O000OOO0 ))#line:94
