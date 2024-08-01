import subprocess #line:1
import os #line:2
import sys #line:3
import json #line:4
import time #line:5
import discord #line:6
from colorama import Fore ,Style #line:7
from utils .cloner import Cloner #line:8
from utils .panel import Panel ,Panel_Run #line:9
from discord import Client ,Intents #line:10
from rich .prompt import Prompt ,Confirm #line:11
from time import sleep #line:12
pink =Fore .MAGENTA +Style .BRIGHT #line:14
def rename_console (O0OO00000000OOOOO ):#line:16
    if os .name =='nt':#line:17
        import ctypes #line:18
        ctypes .windll .kernel32 .SetConsoleTitleW (O0OO00000000OOOOO )#line:19
    else :#line:20
        sys .stdout .write (f"\x1b]2;{O0OO00000000OOOOO}\x07")#line:21
rename_console ("Discord Server Cloner")#line:23
try :#line:25
    client =Client (intents =Intents .all ())#line:26
except Exception as e :#line:27
    print (f"{pink}> Unable to create Discord client: ",e )#line:28
with open ("./utils/config.json","r")as json_file :#line:30
    data =json .load (json_file )#line:31
os .system ('cls'if os .name =='nt'else 'clear')#line:33
def clear (option =False ):#line:35
    sleep (1 )#line:36
    os .system ('cls'if os .name =='nt'else 'clear')#line:37
    if option :#line:38
        O0O000OO00O00OO0O =client .user #line:39
        OOO0O00OOO0O0OOOO =client .get_guild (int (INPUT_GUILD_ID ))#line:40
        Panel_Run (OOO0O00OOO0O0OOOO ,O0O000OO00O00OO0O )#line:41
    else :#line:42
        Panel ()#line:43
async def clone_server ():#line:45
    OO0000O0OO000000O =time .time ()#line:46
    OOOO0OO0O000OOO00 =client .get_guild (int (INPUT_GUILD_ID ))#line:47
    print (" ")#line:48
    OO00000000O00O0OO =client .get_guild (int (GUILD ))#line:49
    await Cloner .guild_create (OO00000000O00O0OO ,OOOO0OO0O000OOO00 )#line:51
    await Cloner .channels_delete (OO00000000O00O0OO )#line:53
    if data ["copy_settings"]["roles"]:#line:54
        await Cloner .roles_create (OO00000000O00O0OO ,OOOO0OO0O000OOO00 )#line:55
    if data ["copy_settings"]["categories"]:#line:56
        await Cloner .categories_create (OO00000000O00O0OO ,OOOO0OO0O000OOO00 )#line:57
    if data ["copy_settings"]["channels"]:#line:58
        await Cloner .channels_create (OO00000000O00O0OO ,OOOO0OO0O000OOO00 )#line:59
    if data ["copy_settings"]["emojis"]:#line:60
        await Cloner .emojis_create (OO00000000O00O0OO ,OOOO0OO0O000OOO00 )#line:61
    print (f"{pink}\n> Server cloned in "+str (round (time .time ()-OO0000O0OO000000O ,2 ))+" seconds")#line:62
@client .event #line:64
async def on_ready ():#line:65
    clear (True )#line:66
    await clone_server ()#line:67
class ClonerBot :#line:69
    def __init__ (O00OO0O00OOOOO0O0 ):#line:70
        O00OO0O00OOOOO0O0 .INPUT_GUILD_ID =None #line:71
        with open ("./utils/config.json","r")as O0OO00O000OO00OOO :#line:72
            O00OO0O00OOOOO0O0 .data =json .load (O0OO00O000OO00OOO )#line:73
    def clear (OO00OOOO00O0O0OO0 ):#line:75
        sleep (1 )#line:76
        os .system ('cls'if os .name =='nt'else 'clear')#line:77
        Panel ()#line:78
    def edit_config (O0OO00OOO00O00O0O ,O00000OO0OOOOO00O ,OOO000000OO0OOO0O ,copy_settings =False ):#line:80
        if copy_settings :#line:81
            O0OO00OOO00O00O0O .data ["copy_settings"][O00000OO0OOOOO00O ]=OOO000000OO0OOO0O #line:82
        else :#line:83
            O0OO00OOO00O00O0O .data [O00000OO0OOOOO00O ]=OOO000000OO0OOO0O #line:84
        with open ("./utils/config.json","w")as O0OO0OO0O00O000OO :#line:85
            json .dump (O0OO00OOO00O00O0O .data ,O0OO0OO0O00O000OO ,indent =4 )#line:86
    def edit_settings_function (O000OOO000OOO000O ):#line:88
        print (f"{pink}\nYou want to copy:")#line:89
        OO0OOO0O0OOOOOO00 =Confirm .ask ("> Categories?")#line:90
        O00000O00O0O0O000 =Confirm .ask ("> Channels?")#line:91
        O000OOOO00O0000OO =Confirm .ask ("> Roles?")#line:92
        O00O0000O000OOOOO =Confirm .ask ("> Emojis?")#line:93
        for OOO0OOOO000OOOO0O in ["categories","channels","roles","emojis"]:#line:94
            O000OOO000OOO000O .edit_config (OOO0OOOO000OOOO0O ,locals ()[OOO0OOOO000OOOO0O ],copy_settings =True )#line:95
    def main (O0O0OOOOO0OO00O0O ):#line:97
        O0O0OOOOO0OO00O0O .clear ()#line:98
        if O0O0OOOOO0OO00O0O .data ["token"]==False :#line:99
            O0O0OOOOO0OO00O0O .TOKEN =Prompt .ask ("\n> Enter your Token")#line:100
            sleep (0.5 )#line:101
        else :#line:102
            print (f"{pink}> Token found")#line:103
        O0O0OOOOO0OO00O0O .clear ()#line:104
        O0OO0O00000OO00OO =Confirm .ask ("\n> Do you want to edit the settings?")#line:105
        sleep (0.5 )#line:106
        O0O0OOOOO0OO00O0O .clear ()#line:107
        if O0OO0O00000OO00OO :#line:108
            O0O0OOOOO0OO00O0O .edit_settings_function ()#line:109
        sleep (0.5 )#line:110
        O0O0OOOOO0OO00O0O .clear ()#line:111
        O0O0OOOOO0OO00O0O .INPUT_GUILD_ID =Prompt .ask ("\n> Server to copy")#line:113
        sleep (0.5 )#line:114
        O0O0OOOOO0OO00O0O .clear ()#line:115
        O0O0OOOOO0OO00O0O .GUILD =Prompt .ask ("\n> Server to paste")#line:117
        sleep (0.5 )#line:118
        O0O0OOOOO0OO00O0O .clear ()#line:119
        return O0O0OOOOO0OO00O0O .INPUT_GUILD_ID ,O0O0OOOOO0OO00O0O .TOKEN ,O0O0OOOOO0OO00O0O .GUILD #line:121
if __name__ =="__main__":#line:123
    INPUT_GUILD_ID ,TOKEN ,GUILD =ClonerBot ().main ()#line:124
    try :#line:125
        client .run (TOKEN ,bot =False )#line:126
        clear ()#line:127
    except Exception as e :#line:128
        print (e )#line:129
        print (f"{pink}> Invalid Token")#line:130
        data ["token"]=False #line:131
