# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
cl = LINETCR.LINE()
cl.login(token="EpWhlumZK46bRyu71l58.6S7B6iV24SxpyyIZPkjUga.S6TstSNeC0w0GxGFge6vC4RnZP/5VihzYkjd0ihCFSw=")
cl.loginResult()

ki1 = LINETCR.LINE()
ki1.login(token="EpKcMD4qjbM0tCDjPmv9.Z2jqcI8fppmz+7xOGNlyEq.32XztUCQ9xEpjpQlwcpyTfYJETgD2ubX9V4Mg31y11E=")
ki1.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EpyCK22hNJVKM0jL36xa.Ql+Iq95c4olkmxSaoadLoG.q6NbdCIrnsVDEhh/QOtjUi6OmvlTn+bDgbgVuHrh09o=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EpGvcG7JkNyEA5wwwLu6.SGby4XQI1gAOTET1lBqQ9G.coIXFC5dgqd75X9kFA2eX500d2R+6PhZf+ARFYs4SUU=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EpWQyd0Ii7JmcSaUdOPa.Q6+YE7DHLRb+4/UXmbKggG.HUGO5X2CGahN6YSosV4M44aGeFXb8tj6vELArbekXzQ=")
ki4.loginResult()

ūki5 = LINETCR.LINE()
ki5.login(token="Eplftwaw4f4ez8k9mdp8.7fLTCfOW6V77bikOdoT16a.HDwV3xjYOQXDUAu+NiB1DsKEjz+lUaH9nHhSgn/fQuo=")
ki5.loginResult()

#ki6 = LINETCR.LINE()
#ki6.login(token="EoxwAg1N3lSmzFfZ0RX3.7f74kMOPgNIBSGT6+sawqW.zNL95ZZiregvvKd9pBWeCNQEvFK8pQVNb3TtBibAGEQ=")
#ki6.loginResult()

#ki7 = LINETCR.LINE()
#ki7.login(token="Eokv7n7uoq4tsmQWREkf.PqUHiCpv2pBtz8Q0TEIqxW.AgPVyVnLoG7UHyzHyQX/ICM4cQapp9zRSY2uGr95du8=")
#ki7.loginResult()

#ki8 = LINETCR.LINE()
#ki8.login(token="EoxWhUuk78IXHPBgYgbe.nMGqEcQDlP6dAl/gilNatG.90ay26S0VfNPti2ZmKGDVlu6FJ3ivCsIUSVDa6kmBEA=")
#ki8.loginResult()

#ki9 = LINETCR.LINE()
#ki9.login(token="EoluRsFVIBC6WfNecGja.XeTFQ55WYwSmXh4n0wOhcG.Zl36VJU8INIcSFmmXsMSXyUZW+gbjmQTgE6LxBQpCa4=")
#ki9.loginResult()

#ki10 = LINETCR.LINE()
#ki10.login(token="EoQW0fWuribDJDJRBTCa.XIBZSHhwVEi2szZJfJwo/G.0Vu2NC0IMsGRgSttKg/vSJz9ngGwx/lGkaqdUqt1GgM=")
#ki10.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""     ─┅═✥FUCK-U-BOT✥═┅─

─┅═✥ᴛʜᴀɪʟᴀɴᴅ✥═┅─
                     
❂͜͡☆➣ 『Me』
❂͜͡☆➣ 『Id』
❂͜͡☆➣ 『Wc』
❂͜͡☆➣ 『Mc:』
❂͜͡☆➣ 『Mid』
❂͜͡☆➣ 『BBc:』
❂͜͡☆➣ 『Gift』
❂͜͡☆➣ 『Mid @』
❂͜͡☆➣ 『Cn: Display Name』
❂͜͡☆➣ 『Cc: Clock Name』
❂͜͡☆➣ 『Hack @』
❂͜͡☆➣ 『Tl: text』
❂͜͡☆➣ 『Auto join: on/off』
❂͜͡☆➣ 『Auto add: on/off』
❂͜͡☆➣ 『Auto leave: on/off』
❂͜͡☆➣ 『Clock: on/off』
❂͜͡☆➣ 『Share on』
❂͜͡☆➣ 『Add message: text』
❂͜͡☆➣ 『Message:』
❂͜͡☆➣ 『Add comment: text』
❂͜͡☆➣ 『Comment: 』
❂͜͡☆➣ 『Cbroadcast text』
❂͜͡☆➣ 『Gbroadcast text』
❂͜͡☆➣ 『Reject』
❂͜͡☆➣ 『Creator 』
❂͜͡☆➣ 『Gn: text 』
❂͜͡☆➣ 『Invite:on 』
❂͜͡☆➣ 『Invite: mid』 
❂͜͡☆➣ 『Allgift 』
❂͜͡☆➣ 『All mid』
❂͜͡☆➣ 『Cancel』
❂͜͡☆➣ 『Link on/off』
❂͜͡☆➣ 『Spam on/off』
❂͜͡☆➣ 『ginfo』
❂͜͡☆➣ 『Myginfo』
❂͜͡☆➣ 『Gurl』
❂͜͡☆➣ 『Glist』
❂͜͡☆➣ 『Set』
❂͜͡☆➣ 『Third: Tag』
❂͜͡☆➣ 『Gcancel:』
❂͜͡☆➣ 『Masuk Join』
❂͜͡☆➣ 『Sa:yang』
❂͜͡☆➣ 『Beb』
❂͜͡☆➣ 『Cinta』
❂͜͡☆➣ 『Sayang: 』
❂͜͡☆➣ 『P:ulang』
❂͜͡☆➣ 『Ban @』
❂͜͡☆➣ 『Uban @』
❂͜͡☆➣ 『Ban 』
❂͜͡☆➣ 『Unban』
❂͜͡☆➣ 『Comment :』
❂͜͡☆➣ 『Banlist』
❂͜͡☆➣ 『Cekban』
❂͜͡☆➣ 『Clear ban』
❂͜͡☆➣ 『Kill @ Fuck @』
❂͜͡☆➣ 『Speed / Sp』
❂͜͡☆➣ 『Hack @2@3@4』
❂͜͡☆➣ 『Ambilin @』
❂͜͡☆➣ 『Sampul @』
❂͜͡☆➣ 『Copy @』
❂͜͡☆➣ 『Mycopy @』
❂͜͡☆➣ 『Keluar :@』
❂͜͡☆➣ 『music』
❂͜͡☆➣ 『.reboot』
❂͜͡☆➣ 『Wikipedia』
❂͜͡☆➣ 『Cleanse』
❂͜͡☆➣ 『Bot Speed』
❂͜͡☆➣ 『P1-P36 link on/off』
❂͜͡☆➣ 『Key』
❂͜͡☆➣ 『Qr on/off』
❂͜͡☆➣ 『Backup on/off』
❂͜͡☆➣ 『Protect On/off』
❂͜͡☆➣ 『Namelock On/off』   
        ─┅═✥ᵀᴴᴬᴵᴸᴬᴺᴰ✥═┅─
──┅═✥============✥═┅──"""
helpMessage2 ="""
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Help〙
╠➩〘sett〙
╠➩〘Help grup〙
╠➩〘Help set〙
╠➩〘Help media〙
╠➩〘Speed〙
╠➩〘Status〙
╚═════════════════
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Protect on/off〙
╠➩〘Qr on/off〙
╠➩〘Invit on/off〙
╠➩〘Cancel on/off〙
╚═════════════════
╔═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Me〙
╠➩〘Myname: 〙
╠➩〘Mybio: 〙
╠➩〘Myname〙
╠➩〘Mybio〙
╠➩〘Mypict〙
╠➩〘Mycover〙
╠➩〘My,copy @〙
╠➩〘Mybackup〙
╠➩〘Getgrup image〙
╠➩〘Getmid @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getbio @〙
╠➩〘Getpict @〙
╠➩〘Getcover @〙
╠➩〘Mention〙
╠➩〘Lurk on/off〙
╠➩〘Lurkers〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Contact on/off〙
╠➩〘Autojoin on/off〙
╠➩〘Autoleave on/off〙
╠➩〘Autoadd on/off〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘Like on〙
╠➩〘Respon on/off〙
╠➩〘Read on/off〙
╠➩〘Simisimi on/off〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Link on/off〙
╠➩〘Url〙
╠➩〘Cancel〙
╠➩〘Gcreator〙
╠➩〘Ki'ck @〙
╠➩〘Ulti @〙
╠➩〘Cancel〙
╠➩〘Gname: 〙
╠➩〘Gbroadcast: 〙
╠➩〘Cbroadcast: 〙
╠➩〘Infogrup〙
╠➩〘Gruplist〙
╠➩〘Friendlist〙
╠➩〘Blocklist〙
╠➩〘Ba'n @〙
╠➩〘U'nban @〙
╠➩〘Clearban〙
╠➩〘Banlist〙
╠➩〘Contactban〙
╠➩〘Midban〙
╠═════════════════
║       ✟ New function ✟
╠═════════════════
╠➩〘Kalender〙
╠➩〘tr-id 〙
╠➩〘tr-en 〙
╠➩〘tr-jp 〙
╠➩〘tr-ko 〙
╠➩〘say-id 〙
╠➩〘say-en 〙
╠➩〘say-jp 〙
╠➩〘say-ko 〙
╠➩〘profileig 〙
╠➩〘checkdate 〙
╚═════════════════
"""
helpMessage3 ="""
╔══════════════════════
║       ✦เปิด/ปิดข้อความต้อนรับ✦
╠══════════════════════
║✰ ต้อนรับ on ➠เปิดข้อความต้อนรับ
║✰ ต้อนรับ off ➠ปิดข้อความต้อนรับ
║✰ ข้อความออก on ➠เปิดข้อความออกกลุ่ม
║✰ ข้อความออก off ➠เปิดข้อความออกกลุ่ม
║✰ ข้อความลบ on ➠เปิดข้อความคนลบ
║✰ ข้อความลบ off ➠เปิดข้อความคนลบ
║✰ Mbot on ➠เปิดเเจ้งเตือนบอท
║✰ Mbot off ➠ปิดเเจ้งเตือนบอท
║✰ M on ➠เปิดเเจ้งเตือนตนเอง
║✰ M off ➠ปิดเเจ้งเตือนตนเอง
║✰ Tag on ➠เปิดกล่าวถึงเเท็ค
║✰ Tag off ➠ปิดกล่าวถึงเเท็ค
║✰ Kicktag on ➠เปิดเตะคนเเท็ค
║✰ Kicktag off ➠ปิดเตะคนเเท็ค
╚══════════════════════
╔══════════════════════
║         ✦โหมดตั้งค่าข้อความ✦
╠══════════════════════
║✰ ตั้งเข้า˓: ➠ไส่ข้อความต้อนรับ
║✰ ตั้งออก˓: ➠ไส่ข้อความออกจากกลุ่ม
║✰ ตั้งลบ˓: ➠ไส่ข้อความเมื่อมีคนลบ
╚══════════════════════
╔══════════════════════
║       ✦โหมดเช็คตั้งค่าข้อความ✦
╠══════════════════════
║✰ เข็คเข้า ➠เช็คข้อความต้อนรับ
║✰ เช็คออก ➠เช็คข้อความคนออก
║✰ เช็คลบ ➠เช็คข้อความคนลบ
╚══════════════════════"""

KAC=[cl,ki1,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
Amid1 = ki1.getProfile().mid
Amid2 = ki2.getProfile().mid
Amid3 = ki3.getProfile().mid
Amid4 = ki4.getProfile().mid
Amid5 = ki5.getProfile().mid
#Amid6 = ki6.getProfile().mid
#Amid7 = ki7.getProfile().mid
#Amid8 = ki8.getProfile().mid
#Amid9 = ki9.getProfile().mid
#Amid10 = ki10.getProfile().mid

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
mid = cl.getProfile().mid
Bots = ["ueacedbe88bf6e2c5cf6188b3a4a26e18",mid,Amid1,Amid2,Amid3,Amid4,Amid5]
self = ["ueacedbe88bf6e2c5cf6188b3a4a26e18",mid,Amid1,Amid2,Amid3,Amid4,Amid]
admin = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
admsa = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
owner = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
adminMID = "ueacedbe88bf6e2c5cf6188b3a4a26e18"
Creator="ueacedbe88bf6e2c5cf6188b3a4a26e18"
wait = {
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"Thanks for add Me THIRD",
    "lang":"JP",
    "comment":"AutoLike by THIRD",
    "commentOn":False,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "Protectcancl":False,
    "pautoJoin":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":",",
    "likeOn":False,
    "pname":False,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":False,
    "Backup":False,
    "protectionOn":False,
    "winvite":False,
    "ainvite":False,
    "binvite":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Hhx1":False,
    "Hhx2":False,
    "Hhx3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
	"posts":False,
	}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


contact = ki1.getProfile()
backup = ki1.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

#contact = ki6.getProfile()
#backup = ki6.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki7.getProfile()
#backup = ki7.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki8.getProfile()
#backup = ki8.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki9.getProfile()
#backup = ki9.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

#contact = ki10.getProfile()
#backup = ki10.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def sendImageWithUrl(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)

def sendImage(self, to_, path):
    M = Message(to=to_, text=None, contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M2 = self._client.sendMessage(0,M)
    M_id = M2.id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendImage2(self, to_, path):
    M = Message(to=to_,contentType = 1)
    M.contentMetadata = None
    M.contentPreview = None
    M_id = self._client.sendMessage(M).id
    files = {
       'file': open(path, 'rb'),
    }
    params = {
       'name': 'media',
       'oid': M_id,
       'size': len(open(path, 'rb').read()),
       'type': 'image',
       'ver': '1.0',
    }
    data = {
       'params': json.dumps(params)
    }
    r = cl.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
    if r.status_code != 201:
       raise Exception('Upload image failure.')
    return True

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki1.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                try:
                                    G = ki3.getGroup(op.param1)
                                except:
                                    try:
                                        G = ki4.getGroup(op.param1)
				    except:
					try:
                                            G = ki5.getGroup(op.param1)
                                        except:
                                            pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki1.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                try:
                                    ki2.updateGroup(G)
                                except:
                                    try:
                                        ki3.updateGroup(G)
                                    except:
                                        try:
                                            ki4.updateGroup(G)
                                        except:
                                            pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ki2.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ki3.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki4.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                                        cl.sendText(op.param1,"Group Name Lock")
                                        ki1.sendText(op.param1,"Haddeuh dikunci Pe'a")
                                        ki2.sendText(op.param1,"Wekawekaweka (Har Har)")
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)



                if op.param3 in mid:
                    if op.param2 in Amid1:
                        G = ki1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid4:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid5:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in mid:
                    if op.param2 in Amid6:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid7:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid8:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid9:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in mid:
                    if op.param2 in Amid10:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)



                if op.param3 in Amid1:
                    if op.param2 in Amid2:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki1.reissueGroupTicket(op.param1)
                        ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Amid2:
                    if op.param2 in Amid3:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Amid3:
                    if op.param2 in Amid4:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)

                if op.param3 in Amid4:
                    if op.param2 in Amid5:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in Amid5:
                    if op.param2 in Amid6:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)

                if op.param3 in Amid6:
                    if op.param2 in Amid7:
                        X = ki7.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki7.reissueGroupTicket(op.param1)

                if op.param3 in Amid7:
                    if op.param2 in Amid8:
                        X = ki8.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki8.updateGroup(X)
                        Ti = ki8.reissueGroupTicket(op.param1)
                if op.param3 in Amid8:
                    if op.param2 in Amid9:
                        X = ki9.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki9.updateGroup(X)
                        Ti = ki9.reissueGroupTicket(op.param1)
                if op.param3 in Amid9:
                    if op.param2 in Amid10:
                        X = ki10.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki7.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki10.updateGroup(X)
                        Ti = ki10.reissueGroupTicket(op.param1)
                if op.param3 in Amid10:
                    if op.param2 in Amid1:
                        X = ki.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        Ti = ki.reissueGroupTicket(op.param1)

#===========================================
        if op.type == 32:
            if not op.param2 in Bots:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "Your invitation was declined\n\n[SELFBOT]]\n\nline.me/ti/p/4bvwOIMft8")
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1, "Your invitation was declined\n\n[SELFBOT]]\n\nline.me/ti/p/4bvwOIMft8")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid1 in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki1.rejectGroupInvitation(op.param1)
                        else:
                            ki1.acceptGroupInvitation(op.param1)
                    else:
                        ki1.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki1.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki1.cancelGroupInvitation(op.param1, matched_list)
            if Amid2 in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki2.rejectGroupInvitation(op.param1)
                        else:
                            ki2.acceptGroupInvitation(op.param1)
                    else:
                        ki2.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki2.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki2.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["qr"] == True:  
                try:
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
        if op.type == 11:
            if not op.param2 in Bots:
              if wait["protectionOn"] == True:
                 try:                    
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist) 
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots:
                if wait["protectionOn"] == True:  
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.1)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl1.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl1.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = ki1.getGroup(op.param1)
                        gs = ki2.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki1.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki1.updateGroup(G)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid1 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki1.updateGroup(X)
                    Ticket = ki1.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


                if Amid2 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ticket = ki2.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid3 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ticket = ki3.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid4 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ticket = ki4.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid5 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ticket = ki5.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid6 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki6.updateGroup(X)
                    Ticket = ki6.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid7 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki8.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki8.updateGroup(X)
                    Ti = ki8.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki7.updateGroup(X)
                    Ticket = ki7.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid8 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki9.updateGroup(X)
                    Ti = ki9.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki8.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki8.updateGroup(X)
                    Ticket = ki8.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid9 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki10.updateGroup(X)
                    Ti = ki10.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki9.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki9.updateGroup(X)
                    Ticket = ki9.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Amid10 in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ki1.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki1.updateGroup(X)
                    Ti = ki1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki1.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.01)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki8.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki9.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki10.acceptGroupInvitationByTicket(op.param1,Ti)

                    X = ki10.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki10.updateGroup(X)
                    Ticket = ki10.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
              if wait["pautoJoin"] == True:
                  cl.acceptGroupInvitation(op.param1)
              else:
                  cl.rejectGroupInvitation(op.param1)


        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to, "error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["แท็กทำไม",cName + " ฝากข้อความไว้นะครับ"]
                     ret_ = "[ข้อความอัตโนมัติ] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["จะแท็กทำไมมากมาย-กูเล่นเกมอยู่",cName + ""]
                     ret_ = "[ข้อความอัตโนมัติ] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '608',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'5507'
                                                        }
                                  cl.sendMessage(msg)
                                  break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithUrl(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")
                        
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Done already")

                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done done aded")
               
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done deleted")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")

               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help","คำสั่ง"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Cmd"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage2 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Help2","Sett"]:
                print "\nHelp pick up..."
                if wait["lang"] == "JP":
                    cl.sendText(msg.to, helpMessage3 + "")
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:"," ")
                klist=[ki7,ki6,ki5,ki1,cl]
                kicker = random.choice(klist)
                kicker.kickoutFromGroup(msg.to,[midd])


        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                     if msg.from_ == admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki1.findAndAddContactsByMid(invite)
                                         ki1.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait['ainvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki1.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki1.findAndAddContactsByMid(target)
                                 ki1.inviteIntoGroup(msg.to,[target])
                                 ki1.sendText(msg.to,"Invite " + _name)
                                 wait['ainvite'] = False
                                 break                              
                             except:             
                                      ki1.sendText(msg.to,"Error")
                                      wait['ainvite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait['binvite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ki2.sendText(msg.to, _name + " สมาชิกอยู่ในกลุ่มเเล้ว")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ki2.findAndAddContactsByMid(target)
                                 ki2.inviteIntoGroup(msg.to,[target])
                                 ki2.sendText(msg.to,"Invite " + _name)
                                 wait['binvite'] = False
                                 break                              
                             except:             
                                      ki2.sendText(msg.to,"Error")
                                      wait['binvite'] = False
                                      break

            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'hack bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                cl.sendMessage(msg)

            elif msg.text.lower() == 'contact bot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid1}
                ki1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid2}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid3}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid4}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid5}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid6}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid7}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid8}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid9}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid10}
                ki10.sendMessage(msg)


            elif "Me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)


            elif "vdo:" in msg.text.lower():
                if msg.toType == 2:
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")



            elif msg.text in ["55"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }

                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "youname " in msg.text.lower():
                txt = msg.text.replace("youname ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"


            elif "Bl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            wait["blacklist"][target] = True
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Banned")
                            print "[Command] Bannad"
                        except:
                            pass
#----------------------------------------------------------------------------
#------------------------------- UNBAN BY TAG -------------------------------
            elif "Wl " in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print "[Command] Unbannad"
                        except:
                            pass
#            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
#                text = msg.text
#                if text is not None:
#                    cl.sendText(msg.to,text)
#                else:
#                    if msg.contentType == 7:
#                        msg.contentType = 7
#                        msg.text = None
#                        msg.contentMetadata = {
#                                             "STKID": "6",
#                                             "STKPKGID": "1",
#                                             "STKVER": "100" }
#                        cl.sendMessage(msg)
#                    elif msg.contentType == 13:
#                        msg.contentType = 13
#                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
#                        cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic:","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic on\n\nเปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already on\n\nเปิดการเลียนเเบบ")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic off\n\nปิดการเลียนเเบบ")
                        else:
                            cl.sendText(msg.to,"Mimic already off\n\nปิดการเลียนเเบบ")
                    elif "add:" in cmd:
                        target0 = msg.text.replace("Mimic:add:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    mimic["target"][target] = True
                                    cl.sendText(msg.to,"Success added target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"โปรเเกรมเลียนเเบบทำงาน")
                                    break
                    elif "del:" in cmd:
                        target0 = msg.text.replace("Mimic:del:","")
                        target1 = target0.lstrip()
                        target2 = target1.replace("@","")
                        target3 = target2.rstrip()
                        _name = target3
                        gInfo = cl.getGroup(msg.to)
                        targets = []
                        for a in gInfo.members:
                            if _name == a.displayName:
                                targets.append(a.mid)
                        if targets == []:
                            cl.sendText(msg.to,"No targets\n\nเกิดข้อผิดพลาด")
                        else:
                            for target in targets:
                                try:
                                    del mimic["target"][target]
                                    cl.sendText(msg.to,"Success deleted target")
                                    cl.sendMessageWithMention(msg.to,target)
                                    break
                                except:
                                    cl.sendText(msg.to,"คุณลบการเลียนเเบบผู้ใช้นี้")
                                    break
                    elif cmd == "list":
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"No target")
                        else:
                            lst = "<<List Target>>"
                            total = len(mimic["target"])
                            for a in mimic["target"]:
                                if mimic["target"][a] == True:
                                    stat = "On"
                                else:
                                    stat = "Off"
                                lst += "\n-> " + cl.getContact(a).displayName + " | " + stat
                            cl.sendText(msg.to,lst + "\nTotal: " + total)


#----------------------------------------------------------------------------
            elif msg.text.lower() in ["botkill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki1.kickoutFromGroup(msg.to,[jj])
                        pass
            elif msg.text.lower() in ["admins","mee"]:
                msg.contentType = 13
                adm = 'ueacedbe88bf6e2c5cf6188b3a4a26e18'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Add Line line.me/ti/p/4bvwOIMft8")


            elif msg.text in ["ของขวัญ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)

            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["vps","kernel","Vps"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif "Gc" == msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"old user")
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")

            elif "#set" in msg.text:
				cl.sendText(msg.to, "Let's see who lazy to type")
				try:
					del wait2['readPoint'][msg.to]
					del wait2['readMember'][msg.to]
				except:
					pass
				wait2['readPoint'][msg.to] = msg.id
				wait2['readMember'][msg.to] = ""
				wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				wait2['ROM'][msg.to] = {}
				print wait2
            elif "#read" in msg.text:
				if msg.to in wait2['readPoint']:
					if wait2["ROM"][msg.to].items() == []:
						chiya = ""
					else:
						chiya = ""
						for rom in wait2["ROM"][msg.to].items():
							print rom
							chiya += rom[1] + "\n"

					cl.sendText(msg.to, "people who reading%s\n is this\n\n\nDate and time I started it:\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
				else:
					cl.sendText(msg.to, "read point not set\nReading point setting you send it it will send an esxisting one")


            elif msg.text in ["Myginfoid"]:
                gid = cl.getGroupIdsJoined()
                g = ""
                for i in gid:
                    g += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,g)

            elif msg.text in ["P1 invite","P1 Invite"]:
                wait["ainvite"] = True
                ki.sendText(msg.to,"Send Contact")
            elif msg.text in ["P2 invite","P2 Invite"]:
                wait["binvite"] = True
                kk.sendText(msg.to,"Send Contact")
#==================================================

            elif "#ประกาศ:" in msg.text:
                bctxt = msg.text.replace("#ประกาศ:", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            elif msg.text.lower() == 'bann':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif "#หำ1:" in msg.text:
                string = msg.text.replace("#หำ1:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
            elif msg.text in ["มาหำ","บอทมา","#kicker","Kicker","kicker","•••"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)

                        ki1.sendText(msg.to,"[SELFBOT]")
                        ki2.sendText(msg.to,"[Do not think  will try.]")
                        ki3.sendText(msg.to,"[FUCK-U-BOT]")
                        ki1.sendText(msg.to,"Hello " + str(ginfo.name) + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["."]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.0)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["ออก","บอทออก","Bye","#bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki1.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki5.leaveGroup(msg.to)
                        ki6.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki6.leaveGroup(msg.to)
                        ki7.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki7.leaveGroup(msg.to)
                        ki8.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki8.leaveGroup(msg.to)
                        ki9.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki9.leaveGroup(msg.to)
                        ki10.sendText(msg.to,"Bye~Bye 􀜁􀄯􏿿"  +  str(ginfo.name)  + "\n\n[By.line.me/ti/p/4bvwOIMft8]")
                        ki10.leaveGroup(msg.to)

                    except:
                        pass

            elif msg.text.lower() == '#byeall':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)

                    except:
                        pass



            elif "#v10" in msg.text:
                cl.sendText(msg.to,"""[FUCK-U-BOT]""")

#==================================================
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif msg.text in ["เชิญ"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")

            elif msg.text in ["Invite off"]:
                if msg.from_ in admin:
                 wait["winvite"] = False
                 cl.sendText(msg.to,"Done..")
            elif msg.text in ["Bot1 invite contact","1เชิญ"]:
                if msg.from_ in admin:
                 wait["ainvite"] = True
                 ki1.sendText(msg.to,"send contact")
            elif msg.text in ["Bot2 invite contact","2เชิญ"]:
                if msg.from_ in admin:
                 wait["binvite"] = True
                 ki2.sendText(msg.to,"send contact")
            
            elif ("Ktc " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif '123zzz' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            elif msg.text in ["ยกเลิก"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["บอทยกเลิก"]:
                if msg.toType == 2:
                    klist=[ki1,ki2,ki3,ki4,ki5,ki6,ki7]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kicker.sendText(msg.to,"No one is inviting")
                        else:
                            kicker.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kicker.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kicker.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["#Link on"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() == 'ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text in ["!Glist","Myginfo"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")


            elif msg.text in ["Selfbot"]:
				msg.contentType = 13
				msg.contentMetadata = {'mid': mid}
				cl.sendMessage(msg)
				cl.sendText(msg.to,"[FUCK-U-BOT]")
            elif "Id" == msg.text:
                key = msg.to
                cl.sendText(msg.to, key)

            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" + key1)

            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif "Keyy" in msg.text:
                cl.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿[{FUCK-U-BOT}] 􀜁􀇔􏿿􀜁􀇔􏿿 \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Kb1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]""")

            elif msg.text.lower() == 'ยกเลิก1':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")
            elif msg.text.lower() == 'บอทยกเลิก1':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki1.cancelGroupInvitation(msg.to,[_mid])

                    ki1.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")
                    cl.sendText(msg.to,"I pretended to cancel and canceled(๑و•̀ω•́)و")

            elif "Me @" in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("Me @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "#cb" in msg.text:
                       nk0 = msg.text.replace("#cb","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"😏")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"😏")
                                except:
                                    cl.sendText(msg.to,"😏")

            elif "#Banall" in msg.text:
                       nk0 = msg.text.replace("#Banall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "#Unbanall" in msg.text:
                       nk0 = msg.text.replace("#Unbanall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)			

            elif msg.text == "กลุ่ม":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ไม่พบผู้สร้างกลุ่ม"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                          u = "[ปิด]"
                        else:
                            u = "[เปิด]"
                        cl.sendText(msg.to,"[ชื่อของกลุ่ม]:\n" + str(ginfo.name) + "\n[Gid]:\n" + msg.to + "\n[ผู้สร้างกลุ่ม:]\n" + gCreator + "\n[ลิ้งค์รูปกลุ่ม]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n[จำนวนสมาชิก]:" + str(len(ginfo.members)) + "คน\n[จำนวนค้างเชิญ]:" + sinvitee + "คน\n[สถานะลิ้งค์]:" + u + "URL [By: THIRD line.me/ti/p/4bvwOIMft8]")
                    else:
                        cl.sendText(msg.to,"Nama Gourp:\n" + str(ginfo.name) + "\nGid:\n" + msg.to + "\nCreator:\n" + gCreator + "\nProfile:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                         cl.sendText(msg.to,"Not for use less than group")
            elif "Bot1@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki1.sendMessage(msg) 
            elif msg.text in ["Bot?","เทส"]:
                ki1.sendText(msg.to,"Bot 1 􀜁􀅔􏿿")
                ki2.sendText(msg.to,"Bot 2 􀜁􀅔􏿿")
                ki3.sendText(msg.to,"Bot 3 􀜁􀅔􏿿")
                ki4.sendText(msg.to,"Bot 4 􀜁􀅔􏿿")
                ki5.sendText(msg.to,"Bot 5 􀜁􀅔􏿿")
                ki6.sendText(msg.to,"Bot 6 􀜁􀅔􏿿")
                ki7.sendText(msg.to,"Bot 7 􀜁􀅔􏿿")
                ki8.sendText(msg.to,"Bot 8 􀜁􀅔􏿿")
                ki9.sendText(msg.to,"Bot 9 􀜁􀅔􏿿")
                ki10.sendText(msg.to,"Bot 10 􀜁􀅔􏿿")

#เทส

            elif "Say " in msg.text:
                                bctxt = msg.text.replace("Say ","")
                                ki1.sendText(msg.to,(bctxt))
                                ki2.sendText(msg.to,(bctxt))
                                ki3.sendText(msg.to,(bctxt))
                                ki4.sendText(msg.to,(bctxt))
                                ki5.sendText(msg.to,(bctxt))
                                ki6.sendText(msg.to,(bctxt))
                                ki7.sendText(msg.to,(bctxt))
                                ki8.sendText(msg.to,(bctxt))
                                ki9.sendText(msg.to,(bctxt))
                                ki10.sendText(msg.to,(bctxt))

            elif "All mid" == msg.text:
                ki1.sendText(msg.to,Amid1)
                ki2.sendText(msg.to,Amid2)
                ki3.sendText(msg.to,Amid3)
                ki4.sendText(msg.to,Amid4)
                ki5.sendText(msg.to,Amid5)
                ki6.sendText(msg.to,Amid6)
                ki7.sendText(msg.to,Amid7)
                ki8.sendText(msg.to,Amid8)
                ki9.sendText(msg.to,Amid9)
                ki10.sendText(msg.to,Amid10)
 
            elif msg.text in ["Protect:on","Protect on","เปิดป้องกัน"]:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:off","Qr off"]:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Qr:on","Qr on"]:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Protect:off","Protect off","ปิดป้องกัน"]:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
					
            elif "Blockinvite:on" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "Blockinvite:off" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif "Cn: " in msg.text:
                string = msg.text.replace("Cn: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Name " + string + " Done Bosqu")
            elif msg.text in ["invite:on"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif "Mc " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Mc: " in msg.text:
                mmid = msg.text.replace("Mc: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                ki1.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                ki10.sendMessage(msg)

            elif msg.text in ["K on","Contact:on","Contact on","K:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["contact v"]:
                if msg.from_ in admin:
                 wait["winvite"] = True
                 random.choice(KAC).sendText(msg.to,"send contact")
            elif msg.text in ["K:off","Contact:off","Contact off","K off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif msg.text in ["Auto join on","Join on","Join:on","Auto join:on","Poin on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
            elif msg.text in ["Join off","Auto join off","Auto join:off","Join:off","Poin off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")

            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

            elif msg.text in ["Leave:on","Auto leave on","Auto leave:on","Leave on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")

            elif msg.text in ["Leave:off","Auto leave off","Auto leave:off","Leave off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")

            elif msg.text in ["共有:オン","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["共有:オフ","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了关断。")
            elif msg.text in ["Auto like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

#========================================
#========================================
            elif msg.text in ["Set"]:
                print "Setting pick up..."
                md = "─┅══THIRD══┅─\n\n"
                if wait["likeOn"] == True: md+="􀬁􀆐􏿿 Auto like : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto like : off 􀜁􀄰􏿿\n"
                if wait["alwayRead"] == True: md+="􀬁􀆐􏿿 Read : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Read : off 􀜁􀄰􏿿\n"
                if wait["detectMention"] == True: md+="􀬁􀆐􏿿 Autorespon : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Autorespon : off 􀜁􀄰􏿿\n"
                if wait["kickMention"] == True: md+="􀬁􀆐􏿿 Autokick: on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Autokick : off 􀜁􀄰􏿿\n"
                if wait["Notifed"] == True: md+="􀬁􀆐􏿿 Notifed : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifed : off 􀜁􀄰􏿿\n"
                if wait["Notifedbot"] == True: md+="􀬁􀆐􏿿 Notifedbot : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifedbot : off 􀜁􀄰􏿿\n"
                if wait["acommentOn"] == True: md+="􀬁􀆐􏿿 Hhx1 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx1 : off 􀜁􀄰􏿿\n"
                if wait["bcommentOn"] == True: md+="􀬁􀆐􏿿 Hhx2 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx2 : off 􀜁􀄰􏿿\n"
                if wait["ccommentOn"] == True: md+="􀬁􀆐􏿿 Hhx3 : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Hhx3 : off 􀜁􀄰􏿿\n"
                if wait["Protectcancl"] == True: md+="􀬁􀆐􏿿 Cancel : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Cancel : off 􀜁􀄰􏿿\n"
                if wait["winvite"] == True: md+="􀬁􀆐􏿿 Invite : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Invite : off 􀜁􀄰􏿿\n"
                if wait["pname"] == True: md+="􀬁􀆐􏿿 Namelock : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Namelock : off 􀜁􀄰􏿿\n"
                if wait["contact"] == True: md+="􀬁􀆐􏿿 Contact : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Contact : off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀬁􀆐􏿿 Auto join : on 􀜁􀄯􏿿\n"
                else: md +="􀬁􀆐􏿿 Auto join : off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀬁􀆐􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿\n"
                else: md+= "􀬁􀆐􏿿 Group cancel : off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀬁􀆐􏿿 Auto leave : on 􀜁􀄯􏿿\n"
                else: md+="􀬁􀆐􏿿 Auto leave : off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀬁􀆐􏿿 Share : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Share : off 􀜁􀄰􏿿\n"
                if wait["clock"] == True: md+="􀬁􀆐􏿿 Clock Name : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Clock Name : off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀬁􀆐􏿿 Auto add : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Auto add : off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀬁􀆐􏿿 Comment : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Comment : off 􀜁􀄰􏿿\n"
                if wait["Backup"] == True: md+="􀬁􀆐􏿿 Backup : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Backup : off 􀜁􀄰􏿿\n"
                if wait["qr"] == True: md+="􀬁􀆐􏿿 Protect QR : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Protect QR : off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
#========================================

#------------------------------------------------
            elif msg.text in ["Gcreator:inv","เชิญเเอทมิน"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif msg.text in ["Backup:on","Backup on","เปิดการเชิญกลับ"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off","ปิดการเชิญกลับ"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Reject","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ปฏิเสฐคำเชิญเข้ากลุ่มเรียบร้อยยย")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Y1 rgroups","Y1 rgroup"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"Bot All invitations is clean")
                else:
                    ki.sendText(msg.to,"拒绝了全部的邀请。")
            elif msg.text in ["Add:on","Auto add on","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","Auto add:off","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        cl.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ok Bosqu")
                    else:
                        cl.sendText(msg.to,"Sudah off Bosqu")
#========================================
#========================================
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message","Com"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Coms set:" in msg.text:
                c = msg.text.replace("Coms set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Com on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Com off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Comment","Coms"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["เช็คเข้า","Hhx1"]:
                cl.sendText(msg.to,"[เช็คข้อความต้อนรับของคุณ]\n\n" + str(wait["acomment"]))

            elif msg.text in ["เช็คออก","Hhx2"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนออกจากกลุ่ม]\n\n" + str(wait["bcomment"]))

            elif msg.text in ["เช็คลบ","Hhx3"]:
                cl.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนลบสมาชิก]\n\n" + str(wait["ccomment"]))

            elif "ตั้งเข้า:" in msg.text:
                c = msg.text.replace("Hhx1:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["acomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)

            elif "ตั้งออก:" in msg.text:
                c = msg.text.replace("Hhx2:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["bcomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนออกจากกลุ่ม👌\n\n" + c)

            elif "ตั้งลบ:" in msg.text:
                c = msg.text.replace("Hhx3:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["ccomment"] = c
                    cl.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนลบสมาชิก👌\n\n" + c)

            elif msg.text in ["ต้อนรับ on"]:
                if wait["acommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["acommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["ข้อความออก on"]:
                if wait["bcommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["bcommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["ข้อความลบ on"]:
                if wait["ccommentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["ccommentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already on")

            elif msg.text in ["ต้อนรับ off"]:
                if wait["acommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["acommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["ข้อความออก off"]:
                if wait["bcommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["bcommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["ข้อความลบ off"]:
                if wait["ccommentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["ccommentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")

            elif "Ambil QR: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Ambil QR: ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Not for use less than group")
            elif "Y1 gurl: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Y1 gurl: ","")
                    x = ki.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(gid)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    ki.sendText(msg.to,"Not for use less than group")
            elif "Y2 gurl: " in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("Y2 gurl: ","")
                    x = kk.getGroup(gid)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(gid)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    kk.sendText(msg.to,"Not for use less than group")
#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "Hack3 @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Hack3 @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithUrl(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Hack2mid:" in msg.text:
                umid = msg.text.replace("Hack2mid:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithUrl(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Hack2 " in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Hack2 ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithUrl(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")

#===============================================
            elif msg.text in ["Sp","sp","Speed"]:
                cl.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                print "[Command]Speed palsu executed"
            elif msg.text in ["Bot Speed"]:
                ki1.sendText(msg.to, "Progress.......")
                start = time.time()
                time.sleep(0.001)
                elapsed_time = time.time() - start
                ki1.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki6.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki7.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki8.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki9.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki10.sendText(msg.to, "%sseconds" % (elapsed_time))    


                print "[Command]Speed palsu executed"

            elif msg.text in ["Keybot"]:
                ki.sendText(msg.to, "[SELFBOT PHET HACK BOT]\n\n❂͜͡☆➣ Namelock on\n❂͜͡☆➣ Namelock off\n❂͜͡☆➣ Blockinvite on\n❂͜͡☆➣ Blockinvite off\n❂͜͡☆➣ Backup on\n❂͜͡☆➣ Backup off\n\n[By.เพชร ทีมทดลองบอท]")

#========================================
            elif msg.text in ["Botbb"]:
                try:
                    ki1.updateDisplayPicture(backup.pictureStatus)
                    ki1.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki5.updateDisplayPicture(backup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki6.updateDisplayPicture(backup.pictureStatus)
                    ki6.updateProfile(backup)
                    ki7.updateDisplayPicture(backup.pictureStatus)
                    ki7.updateProfile(backup)
                    ki8.updateDisplayPicture(backup.pictureStatus)
                    ki8.updateProfile(backup)
                    ki9.updateDisplayPicture(backup.pictureStatus)
                    ki9.updateProfile(backup)
                    ki10.updateDisplayPicture(backup.pictureStatus)
                    ki10.updateProfile(backup)

                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))


            elif msg.text in ["Mebb"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#=================================================
            elif msg.text == "#mid on":
                    cl.sendText(msg.to, "Done..")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "#mid off":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "%s\n\n%s\nReadig point creation:\n [%s]\n"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Lurking dulu dudul Baru bilang result Point.")
						
#========================================
#-------------------Fungsi spam finish----------------------------
            elif "Hackginfo" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithUrl(msg.to,path)
            elif "#Turn off bots" in msg.text:
               if msg.from_ in admsa:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass

#-----------------------------------------------
            elif msg.text in ["Url","url"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"[FUCK-U-BOT]\n\nline://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
            elif msg.text in ["Notifed off","ปิดแจ้งเตือน","M off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")

            elif msg.text in ["Notifedbot on","เปิดเเจ้งเตือนบอท","Mbot on"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
            elif msg.text in ["Notifedbot off","ปิดแจ้งเตือนบอท","Mbot off"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")

#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif msg.text in ["Third All on","third all on"]:
                        cl.sendText(msg.to,"─┅══THIRD══┅─\n\n[FUCK-U-BOT]")
                        cl.sendText(msg.to,"Please wait......")
                        cl.sendText(msg.to,"Turn on all protection")
                        cl.sendText(msg.to,"Qr:on")
                        cl.sendText(msg.to,"Backup:on")
                        cl.sendText(msg.to,"Read:on")
                        cl.sendText(msg.to,"Respon:on")
                        cl.sendText(msg.to,"Responkick:on")
                        cl.sendText(msg.to,"Protect:on")
                        cl.sendText(msg.to,"Namelock:on")
                        cl.sendText(msg.to,"Blockinvite:on")


            elif msg.text in ["Third All off","third all off"]:
                        cl.sendText(msg.to,"─┅══THIRD══┅─\n\n[FUCK-U-BOT]")
                        cl.sendText(msg.to,"Please wait......")
                        cl.sendText(msg.to,"Turn off all protection")
                        cl.sendText(msg.to,"Qr:off")
                        cl.sendText(msg.to,"Backup:off")
                        cl.sendText(msg.to,"Read:off")
                        cl.sendText(msg.to,"Respon:off")
                        cl.sendText(msg.to,"Responkick:off")
                        cl.sendText(msg.to,"Protect:off")
                        cl.sendText(msg.to,"Namelock:off")
                        cl.sendText(msg.to,"Blockinvite:off")
                        cl.sendText(msg.to,"Link off")

 

#========================================
            elif "{}" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to+"',"}
                cl.sendMessage(msg)

            elif '€€€' in msg.text:
                if msg.toType == 2:
                    print "Kickall ok"
                    _name = msg.text.replace("€€€","")
                    gs = ki1.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)

                    ki1.sendText(msg.to, "Hello all...😁😁 {}")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
#                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki1,ki2,ki3,ki4,ki5,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#                                    ki3.sendText(msg,to,"Nuke Finish")
#                                    ki2.sendText(msg,to,"
            elif msg.text.lower() == '#rebootbotall':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)

                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text.lower() == '#boot#':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki1,ki2,ki3,ki4,ki5,ki5,ki6,ki7,ki8,ki9,ki10]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif ("PK4 " in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							ki6.kickoutFromGroup(msg.to,[target])
						except:
							ki6.sendText(msg.to,"Error")
							
            elif "KK2 " in msg.text:
                       nk0 = msg.text.replace("KK2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki2.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki2.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
							
            elif "KK1 " in msg.text:
                       nk0 = msg.text.replace("KK1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki1.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki1.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif "contactjoin:" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("contactjoin:","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

            elif ("PK2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("PK3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")

            elif "Third@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif "แทค" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)


            elif ("PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Success Boss")
                                except:
                                    cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear ban","ล้างดำ"]:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"clear")
				
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist","Mcheck"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Me ban","Cekban","Mcheck mid"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")

#=============================================
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","Read:on"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON")
                
            elif msg.text in ["Read off","Read:off"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider OFF")
                
            elif msg.text in ["Tag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["Tag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon OFF")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"Auto Kick ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"Auto Kick OFF")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
#==============================================================================#
#==============================================================================#

            elif "Thackmid:" in msg.text:
                saya = msg.text.replace("Thackmid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithUrl(msg.to,path)
                except:
                    pass
                
            elif "#Thackgid:" in msg.text:
                saya = msg.text.replace("#Thackgid:","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist","เช็คเพื่อนทั้งหมด","เพื่อนทั้งหมด","Fyall"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist","Nameall"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithUrl(msg.to,path)
                
            elif "#Friendpict:" in msg.text:
                saya = msg.text.replace('#Friendpict:','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            
            elif msg.text in ["Blocklist","บร๊อก","Pbann"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["#Myginfoall"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["#Myginfogidall"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    

            elif "1991258ชื่อกลุ่ม" in msg.text:
                saya = msg.text.replace('1991258ชื่อกลุ่ม','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gid" in msg.text:
                saya = msg.text.replace('Gid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)


            elif msg.text in ["#Meginfoall"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +" ? ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            

            elif "third tag all" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "PHET TAG DONE :\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on\nเปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "เปิดการอ่านอัตโนมัต\nSet reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off\nปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\nDelete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")

            elif msg.text in ["เปิดอ่าน","R on","ตั้งเวลา"]:
                        cl.sendText(msg.to,"lurk on")
            elif msg.text in ["ปิดอ่าน","R off"]:
                        cl.sendText(msg.to,"lurk off")
            elif msg.text in ["อ่าน","Ry"]:
                        cl.sendText(msg.to,"lurkers")
            elif msg.text in ["Ry20"]:
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"llurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
                        cl.sendText(msg.to,"lurkers")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist","Heckmic"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "• "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Thirdmic " in msg.text:
                cmd = msg.text.replace("Thirdmic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithUrl(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithUrl(msg.to,wait["pap"])
#==============================================================================#
            elif msg.text in ["Sk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki1.sendMessage(msg)
            elif msg.text.lower() == 'mymid':
                cl.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Myname","Mename"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio","Mey1"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict","Mey2"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid","Mey3"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithUrl(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict","Mey4"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover","Mey5"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithUrl(msg.to, path)
            elif msg.text in ["Urlcover","Mey6"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "#22Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Ph4" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Ph2" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "mh2" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithUrl(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithUrl(msg.to,path)
                except:
                    pass
            elif "#picall" in msg.text:
                       nk0 = msg.text.replace("#picall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e

            elif "#pictall" in msg.text:
                       nk0 = msg.text.replace("#pictall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    path = str(cu)
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "#phethackall" in msg.text:
                       nk0 = msg.text.replace("#phethackall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"!!..ผิดพลาด")
                           pass
                       else:
                           for target in targets:
                                try:
                                    contact = cl.getContact(target)
                                    cu = cl.channel.getCover(target)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithUrl(msg.to,image)
                                    cl.sendText(msg.to,"Cover " + contact.displayName)
                                    cl.sendImageWithUrl(msg.to, path)
                                except Exception as e:
                                    raise e
            elif "Th3vdo @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Th3vdo @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithUrl(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Th3url @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Th3url @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "2url @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("2url @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithUrl(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Th2url @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Th2url @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "เจ้งเตือน" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithUrl(msg.to,path)
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybb"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
            elif "Botcopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Botcopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki1.CloneContactProfile(target)
                               ki1.sendText(msg.to, "Copied.")
                               ki2.CloneContactProfile(target)
                               ki2.sendText(msg.to, "Copied.")
                               ki3.CloneContactProfile(target)
                               ki3.sendText(msg.to, "Copied.")
                               ki4.CloneContactProfile(target)
                               ki4.sendText(msg.to, "Copied.")
                               ki5.CloneContactProfile(target)
                               ki5.sendText(msg.to, "Copied.")
                               ki6.CloneContactProfile(target)
                               ki6.sendText(msg.to, "Copied.")
                               ki7.CloneContactProfile(target)
                               ki7.sendText(msg.to, "Copied.")
                               ki8.CloneContactProfile(target)
                               ki8.sendText(msg.to, "Copied.")
                               ki9.CloneContactProfile(target)
                               ki9.sendText(msg.to, "Copied.")
                               ki10.CloneContactProfile(target)
                               ki10.sendText(msg.to, "Copied.")

                            except Exception as e:
                                print e
#==============================================================================#
            elif "[Auto Respond]" in msg.text:
                cl.sendImageWithUrl(msg.to, "http://dl.profile.line.naver.jp/0hlGvN3GXvM2hLNx8goPtMP3dyPQU8GSIgJVUpCTpiPVtiA3M2clJ-C2hia11mUn04cAJ-DWljOVBj")
            elif "Fancytext: " in msg.text:
                txt = msg.text.replace("Fancytext: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "Tx: " in msg.text:
                txt = msg.text.replace("Tx: ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
            elif "Bx: " in msg.text:
                txt = msg.text.replace("Bx: ", "")
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)
                ki1.kedapkedip(msg.to,txt)

                print "[Command] Kedapkedip"
            elif "Tx10: " in msg.text:
                txt = msg.text.replace("Tx10: ", "")
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"                    
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "Tr-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO ENGLISH----\n" + "" + result + "\n------SUKSES-----")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM EN----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("ยินดีต้อนรับเข้าสู่กลุ่ม " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('hasil.mp3')
                cl.sendAudioWithUrl(msg.to,'hasil.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudioWithUrl(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudioWithUrl(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudioWithUrl(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudioWithUrl(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudioWithUrl(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudioWithUrl(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudioWithUrl(msg.to,'tts.mp3')
            elif '#dy ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('#dy ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght = ('https://www.youtube.com' + results['href'])
                    cl.sendVideoWithUrl(msg.to, ght)
                except:
                    cl.sendText(msg.to,"Could not find it")            
            elif 'mp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('mp4 ',"").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithUrl(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "/vk " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("/vk ","")
                      wikipedia.set_lang("th")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithUrl(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "#Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithUrl(msg.to,path)
                except:
                    pass           
            elif "#ค้นหารูปภาพ:" in msg.text:
                search = msg.text.replace("ค้นหารูปภาพ:","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithUrl(msg.to,path)
                except:
                    pass           
            
            

            elif "#Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("#Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendImageWithUrl(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): blan = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + blan + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif msg.text in ["Pmcheck","เชคดำ","เช็คดำ"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Mcheckcontact","Cb"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == '1kill':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki1.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            ki1.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
            elif msg.text in ["in on"]:
              if msg.from_ in admin:
                if wait["pautoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["pautoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["in off"]:
              if msg.from_ in admin:
                if wait["pautoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["pautoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif "Hack4" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[profilePicture]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[homePicture]\n" + str(cu))
                except:
                    cl.sendText(msg.to,"[name]\n" + contact.displayName + "\n[mid]\n" + contact.mid + "\n[statusmessage]\n" + contact.statusMessage + "\n[homePicture]\n" + str(cu))
#=============================================
            elif msg.text in ["!Sp"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sTamii Server" % (elapsed_time))
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Bl " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned Bos")
                   except:
                      pass        
       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["#Cinvite"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact 😉")
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 2
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
                        cl.sendText(msg.to, "Done...")
            elif msg.text in ["Mchecky"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user\nมีบัญชีดำของคุณอยู่กลุ่มนี้")
                    xname = ""
                    for mi_d in wait["blacklist"]:
                        xname = cl.getContact(mi_d).displayName + ""
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error

            elif "มอง" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += "@Krampus\n"
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif msg.text in ["Name me","Men"]:
                G = cl.getProfile()
                X = G.displayName
                cl.sendText(msg.to,X)
            elif "siri " in msg.text.lower():
                    query = msg.text.lower().replace("siri ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "siri:" in msg.text.lower():
                    query = msg.text.lower().replace("siri:","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "siri-en " in msg.text.lower():
                    query = msg.text.lower().replace("siri-en ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'en', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif "พูด " in msg.text.lower():
                    query = msg.text.lower().replace("พูด ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                        params = {'language': 'th', 'speed': '1', 'query': query}
                        r    = s.get(url, params=params)
                        mp3  = r.url
                        cl.sendAudioWithUrl(msg.to, mp3)
            elif msg.text in ["1in","Bot1 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki1.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki1.updateGroup(G)
            elif msg.text in ["2in","Bot2 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
            elif msg.text in ["3in","Bot3 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
            elif msg.text in ["4in","Bot4 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki4.updateGroup(G)
            elif msg.text in ["5in","Bot5 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
            elif msg.text in ["6in","Bot6 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
            elif msg.text in ["7in","Bot7 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
            elif msg.text in ["8in","Bot8 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
            elif msg.text in ["9in","Bot9 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
            elif msg.text in ["10in","Bot10 in"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kickers_Ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
            elif '/w ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("/w ","")
                      wikipedia.set_lang("th")
                      pesan="Wikipedia : "
                      pesan+=wikipedia.page(wiki).title
                      pesan+="\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Text Terlalu Panjang Silahkan Click link di bawah ini\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif "/go " in msg.text:
                tanggal = msg.text.replace("/go ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Tanggal Lahir : "+lahir+"\n\nUmur : "+usia+"\n\nUltah : "+ultah+"\n\nZodiak : "+zodiak)
            elif "declined" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)

                    except:
                        pass

            elif "[Auto] " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("[Auto] ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
            elif "☜ʕ•ﻌ•ʔ " in msg.text:
                msg.contentType = 13
                _name = msg.text.replace("☜ʕ•ﻌ•ʔ ","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        msg.contentMetadata = {'mid': g.mid}
                        cl.sendMessage(msg)
                    else:
                         pass
        if op.type == 25:
            msg = op.message
            if msg.text.lower() in ["pheytcg fgtagg all"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "THIRD TAG DONE : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)

        if op.type == 26:
            msg = op.message
            if msg.text.lower() in ["1123"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "THIRD TAG DONE : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
            elif msg.text in [".me","me","Me"]:
                        cl.sendText(msg.to,"You.....")
            elif "/ตั้งเวลา" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on\nเปิดการอ่านอัตโนมัตกรุณาพิมพ์ ➠ /อ่าน")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "โปรเเกรมเปิดการอ่านอัตโนมัต\nSet reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "/ปิดการอ่าน" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off\nปิดการอ่านอัตโนมัต")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ปิดการอ่านอัตโนมัต\nDelete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

                    
            elif "/อ่าน" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "SELFBOT PHET HACK BOT\n\nLurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "กรุณาตั้งเวลาการอ่านใหม่อีกครั้งโปรดพิมพ์ ➠ /ตั้งเวลา")
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to, "[อัตโนมัติ]: " + text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            			"STKID": "6",
            			"STKPKGID": "1",            						"STKVER": "100" }
            			cl.sendMessage(msg)

        if op.type == 15:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀄄􏿿 เเล้วพบใหม่นะ 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " ☜ʕ•ﻌ•ʔ ")
                cl.sendText(op.param1, "􀜁􀄁􏿿 ยินดีต้อนรับครับ 􀜁􀄁􏿿\n􀄃􀅸􏿿 สวัสดีครับผม 􀄃􀅸􏿿\n􂜁􀆄􏿿 อย่าลืมปิดเสียงการเเจ้งเตือนด้วยนะ 􂜁􀆄􏿿\n\n[By.line.me/ti/p/4bvwOIMft8]")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"


        if op.type == 17:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄁􏿿􂘁􀄗􏿿􂘁􀄅􏿿􂘁􀄌􏿿􂘁􀄃􏿿􂘁􀄏􏿿􂘁􀄍􏿿􂘁􀄅􏿿􀜁􀄁􏿿\n\n[By. line.me/ti/p/4bvwOIMft8]")

                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 19:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["bcommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["bcomment"]))
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["acommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["acomment"]))
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["ccommentOn"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["ccomment"]))
                print "MEMBER HAS KICKOUT FROM THE GROUP"


        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)

        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error


def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autolike)
thread1.daemon = True
thread1.start()


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
