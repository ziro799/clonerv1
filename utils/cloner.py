import discord #line:1
from colorama import Fore ,init ,Style #line:2
import asyncio #line:3
import sys ,json #line:4
init ()#line:6
with open ("./utils/config.json","r")as json_file :#line:8
  data =json .load (json_file )#line:9
  logs_enabled =data ["logs"]#line:10
def clear_line (n =1 ):#line:12
  OO00OOOO00OOO00OO ='\033[1A'#line:13
  OO0000OOO000O0OOO ='\x1b[2K'#line:14
  for _O0OOOO0O0000OOOOO in range (n ):#line:15
    print (OO00OOOO00OOO00OO ,end =OO0000OOO000O0OOO )#line:16
def logs (OO0O0OOOOOOO0O0OO ,O0O00OOOO000O000O ,number =None ):#line:18
  if logs_enabled :#line:19
    OO000000OOO000O00 ={'add':('[+]',Fore .MAGENTA ),'delete':('[-]',Fore .MAGENTA ),'warning':('[WARNING]',Fore .MAGENTA ),'error':('[ERROR]',Fore .MAGENTA )}#line:25
    OOOOOO0OO0O000O00 ,OOOOO0OO0O000O0OO =OO000000OOO000O00 .get (O0O00OOOO000O000O ,('[?]',Fore .MAGENTA ))#line:26
    if number is not None :#line:28
      print (f" {OOOOO0OO0O000O0OO}{OOOOOO0OO0O000O00}{Style.RESET_ALL} {OO0O0OOOOOOO0O0OO}")#line:29
    else :#line:30
      print (f" {OOOOO0OO0O000O0OO}{OOOOOO0OO0O000O00}{Style.RESET_ALL} {OO0O0OOOOOOO0O0OO}")#line:31
      clear_line ()#line:32
class Cloner :#line:34
  @staticmethod #line:36
  async def guild_create (OOO0OO00O0O0O0OOO :discord .Guild ,O0O0OOO00O00OO00O :discord .Guild ):#line:37
    try :#line:38
      try :#line:39
        OOO0OOOO0O00000O0 =await O0O0OOO00O00OO00O .icon_url_as (format ='jpg').read ()#line:40
      except discord .errors .DiscordException :#line:41
        logs (f"Can't read icon image from {O0O0OOO00O00OO00O.name}",'error')#line:42
        OOO0OOOO0O00000O0 =None #line:43
      await OOO0OO00O0O0O0OOO .edit (name =f'{O0O0OOO00O00OO00O.name}')#line:44
      if OOO0OOOO0O00000O0 is not None :#line:45
        try :#line:46
          await OOO0OO00O0O0O0OOO .edit (icon =OOO0OOOO0O00000O0 )#line:47
          logs (f"Guild Icon Changed: {OOO0OO00O0O0O0OOO.name}",'add')#line:48
        except Exception :#line:49
          logs (f"Error While Changing Guild Icon: {OOO0OO00O0O0O0OOO.name}",'error')#line:50
    except discord .errors .Forbidden :#line:51
      logs (f"Error While Changing Guild Icon: {OOO0OO00O0O0O0OOO.name}",'error')#line:52
    logs (f"Cloned server: {OOO0OO00O0O0O0OOO.name}",'add',True )#line:53
  @staticmethod #line:55
  async def roles_create (OOO00OOO0000000O0 :discord .Guild ,OO000O0OO0000O00O :discord .Guild ):#line:56
    O0O00O00O0OOOOO00 =[OO0O0OOOOOOO0OO00 for OO0O0OOOOOOO0OO00 in OO000O0OO0000O00O .roles if OO0O0OOOOOOO0OO00 .name !="@everyone"]#line:57
    O0O00O00O0OOOOO00 .reverse ()#line:58
    OO0OO00O0O0OOOOO0 =len (O0O00O00O0OOOOO00 )#line:59
    for O00OO0O0O000OO0O0 in O0O00O00O0OOOOO00 :#line:60
      try :#line:61
        OO00000OOOO0O00O0 ={'name':O00OO0O0O000OO0O0 .name ,'permissions':O00OO0O0O000OO0O0 .permissions ,'colour':O00OO0O0O000OO0O0 .colour ,'hoist':O00OO0O0O000OO0O0 .hoist ,'mentionable':O00OO0O0O000OO0O0 .mentionable }#line:68
        await OOO00OOO0000000O0 .create_role (**OO00000OOOO0O00O0 )#line:69
        logs (f"Created Role {O00OO0O0O000OO0O0.name}",'add')#line:70
      except (discord .Forbidden ,discord .HTTPException )as OOO00OO000O00OO0O :#line:71
        logs (f"Error creating role {O00OO0O0O000OO0O0.name}: {OOO00OO000O00OO0O}",'error')#line:72
    logs (f"Created Roles: {OO0OO00O0O0OOOOO0}",'add',True )#line:73
  @staticmethod #line:75
  async def channels_delete (O00O000OOOO0O0OOO :discord .Guild ):#line:76
    OO0O0OOOOO00O0000 =O00O000OOOO0O0OOO .channels #line:77
    OO0OO0O0O0O00O000 =len (OO0O0OOOOO00O0000 )#line:78
    for OOO0OO0O0OO0OO00O in OO0O0OOOOO00O0000 :#line:79
      try :#line:80
        await OOO0OO0O0OO0OO00O .delete ()#line:81
        logs (f"Deleted Channel: {OOO0OO0O0OO0OO00O.name}",'delete')#line:82
      except (discord .Forbidden ,discord .HTTPException )as O00000000OO0O0OO0 :#line:83
        logs (f"Error deleting channel {OOO0OO0O0OO0OO00O.name}: {O00000000OO0O0OO0}",'error')#line:84
    logs (f"Deleted Channels: {OO0OO0O0O0O00O000}",'delete',True )#line:85
  @staticmethod #line:87
  async def categories_create (OOOOO00OO0OO0OOOO :discord .Guild ,OOO0O0OOO00O0OO0O :discord .Guild ):#line:88
    O0OOO00O0O0O000O0 =OOO0O0OOO00O0OO0O .categories #line:89
    for O00000O0OOOOO0OOO in O0OOO00O0O0O000O0 :#line:90
      try :#line:91
        OO0000OOOO000000O ={discord .utils .get (OOOOO00OO0OO0OOOO .roles ,name =O00O00OOOO00000OO .name ):OOOO00OOOO0OO000O for O00O00OOOO00000OO ,OOOO00OOOO0OO000O in O00000O0OOOOO0OOO .overwrites .items ()}#line:95
        OO0O00OOOOO0OOOO0 =await OOOOO00OO0OO0OOOO .create_category (name =O00000O0OOOOO0OOO .name ,overwrites =OO0000OOOO000000O )#line:96
        await OO0O00OOOOO0OOOO0 .edit (position =O00000O0OOOOO0OOO .position )#line:97
        logs (f"Created Category: {O00000O0OOOOO0OOO.name}",'add')#line:98
      except discord .Forbidden :#line:99
        logs (f"Error creating category {O00000O0OOOOO0OOO.name}",'error')#line:100
      except discord .HTTPException :#line:101
        logs (f"Error creating category {O00000O0OOOOO0OOO.name}",'error')#line:102
    logs (f"Created Categories: {len(O0OOO00O0O0O000O0)}",'add',True )#line:103
  @staticmethod #line:105
  async def channels_create (OO0OOOOOO0O00OO00 :discord .Guild ,O0OOO00O000OOOOO0 :discord .Guild ):#line:106
    O0O0O00OO0O00O00O =O0OOO00O000OOOOO0 .text_channels +O0OOO00O000OOOOO0 .voice_channels #line:107
    O00O0OO0000000O0O ={discord .TextChannel :OO0OOOOOO0O00OO00 .create_text_channel ,discord .VoiceChannel :OO0OOOOOO0O00OO00 .create_voice_channel }#line:111
    O0O0O00OOO0O0OOO0 =len (O0O0O00OO0O00O00O )#line:112
    for O0OO0O00O00O00OOO in O0O0O00OO0O00O00O :#line:113
      await asyncio .sleep (0.2 )#line:114
      O000000OO0000O0OO =discord .utils .get (OO0OOOOOO0O00OO00 .categories ,name =getattr (O0OO0O00O00O00OOO .category ,"name",None ))#line:115
      OO000OO0000000OO0 ={}#line:116
      for OO00O0OO0O00OO000 ,OOO000O0OOOO0O00O in O0OO0O00O00O00OOO .overwrites .items ():#line:117
        O00OO00OO00000OOO =discord .utils .get (OO0OOOOOO0O00OO00 .roles ,name =OO00O0OO0O00OO000 .name )#line:118
        OO000OO0000000OO0 [O00OO00OO00000OOO ]=OOO000O0OOOO0O00O #line:119
      try :#line:120
        OOO00OOO0OO0OOO0O =await O00O0OO0000000O0O [type (O0OO0O00O00O00OOO )](name =O0OO0O00O00O00OOO .name ,overwrites =OO000OO0000000OO0 ,position =O0OO0O00O00O00OOO .position )#line:121
        if O000000OO0000O0OO is not None :#line:122
          await OOO00OOO0OO0OOO0O .edit (category =O000000OO0000O0OO )#line:123
        logs (f"Created {'Text' if type(O0OO0O00O00O00OOO) == discord.TextChannel else 'Voice'} Channel: {O0OO0O00O00O00OOO.name}",'add')#line:124
      except (discord .Forbidden ,discord .HTTPException ,Exception )as O0O00OOOOOOOOO00O :#line:125
        logs (f"Error While Creating Channel {O0OO0O00O00O00OOO.name}: {O0O00OOOOOOOOO00O}",'error')#line:126
    logs (f"Created Channels: {O0O0O00OOO0O0OOO0}",'add',True )#line:127
  @staticmethod #line:129
  async def emojis_create (O000O00O00000OO00 :discord .Guild ,O0000O0O0OOOO0OOO :discord .Guild ):#line:130
    OO0OO0O0OOO0O0OOO :discord .Emoji #line:131
    O0OO00000O0000000 =len (O0000O0O0OOOO0OOO .emojis )#line:132
    for OO0OO0O0OOO0O0OOO in O0000O0O0OOOO0OOO .emojis :#line:133
      try :#line:134
        await asyncio .sleep (0.2 )#line:135
        OO0OOOO00OOO0OO00 =await OO0OO0O0OOO0O0OOO .url .read ()#line:136
        await O000O00O00000OO00 .create_custom_emoji (name =OO0OO0O0OOO0O0OOO .name ,image =OO0OOOO00OOO0OO00 )#line:137
        logs (f"Created Emoji {OO0OO0O0OOO0O0OOO.name}",'add')#line:138
      except discord .Forbidden :#line:139
        logs (f"Error While Creating Emoji {OO0OO0O0OOO0O0OOO.name} ",'error')#line:140
      except discord .HTTPException :#line:141
        logs (f"Error While Creating Emoji {OO0OO0O0OOO0O0OOO.name}",'error')#line:142
    logs (f"Created Emojis: {O0OO00000O0000000}",'add',True )#line:143
