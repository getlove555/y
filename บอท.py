# -*- coding: utf-8 -*-

import LINETCR
#import wikipedia
from LINETCR.lib.curve.ttypes import *
#from ASUL.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile


cl =LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='EqWi1nv2vwHyDe1xkrX7.MRMd87JLMY8NA0SCe7JEXW.g4Z/y2fTVuDnACB/LEfZbcMGY6n/dRAI8QF/iRgQB4I')
cl.loginResult()

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.login(token='EpIGlBVxGanRsBv2Vj67.MRMd87JLMY8NA0SCe7JEXW.6rSLuuR0D6hGisCn4CpxKtFLn77Jp/0RC1K9CXBwofQ')
#ki.loginResult()

#ki2 = LINETCR.LINE()
#ki2.login(qr=True)
#ki2.login(token='EpzjOp0RaiiUhngYARP7.Cwyg1tG1cekJ45Kzw9aWLW.azTn0Jl5o6VCmK5Wq6RAsnmBSQNdjkRk6o39hKlgU1E')
#ki2.loginResult()

#ki3 = LINETCR.LINE()
#ki3.login(qr=True)
#ki3.login(token='EpzjOp0RaiiUhngYARP7.Cwyg1tG1cekJ45Kzw9aWLW.azTn0Jl5o6VCmK5Wq6RAsnmBSQNdjkRk6o39hKlgU1E')
#ki3.loginResult()

#ki4 = LINETCR.LINE()
#ki4.login(qr=True)
#ki4.login(token='Epmn7crkxUW33Jq7qvod.X1JP/u4+7ITIHBKGuvDQJq.cHGxe0QmdModYXecCDZmIDWI5+OSP3nBtDT+OtexnQ0')
#ki4.loginResult()

#ki5 = LINETCR.LINE()
#ki5.login(qr=True)
#ki5.login(token='Ep16E51AceJ94Szz9Sa2.ZDFEjZ3fY8/74VuPEJeZmG.MSw0xp0JRay0Vd9crrhDo/qIRSmFZKv7itUqY9z5NBU')
#ki5.loginResult()
cl

#ki6 = ASUL.LINE()

#AsulLogged = False


#cl = ASUL.LINE()
#cl.login(token='EoChmq5TXM73ZRg9P8ec.YLgVP2FFH7O3buLlL8m1xa.53z2MiS/devknmPfbJjsBhLEqtWnv6cUujv6wklIJsc')
#cl.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" 
   ╔════☬════♪•●☬●•♪════☬═══╗
                    ✞K̲̲̅̅ ̲̲̅̅I̲̲̅̅ ̲̲̅̅E̲̲̅̅B̲̲̅̅O̲̲̅̅ ̲̲̅̅T̲̲̅̅ ̲̲̅̅L̲̲̅̅O̲̲̅̅V̲̲̅̅E̲̲̅̅L̲̲̅̅IN̲̲̅̅E✞
   ╚════☬════♪•●☬●•♪════☬═══╝
         
||=====☬คำสั่งทั่วไป☬=====||
☬➣ [Me @]➣ดูคอนแทคเพื่อน
☬➣ [Tr-th]➣แปลเป็นไทย
☬➣ [Tr-en]➣แปลเป็นอังกฤษ
☬➣ [Ginfo]➣ดูข้อมูลกลุ่ม
☬➣ [Glist]➣ส่งของขวัญ
☬➣ [Cancel]➣ยกเลิกเชิน
☬➣ [Invite]➣เชินตามคอนแทค
☬➣ [Invite: ]➣เชินด้วยเอมไอดี
☬➣ [Unban @]➣ เพิ่มบันชีขาว @
☬➣ [Unban:]➣ เพิ่มบันชีขาวmid
☬➣ [Unban on]➣ เพิ่มบันชีขาวcontact
☬➣ [Ban @ ]➣ เพิ่มบันชีดำ @
☬➣ [Ban:]➣ เพิ่มบันชีดำmid
☬➣ [Ban on ]➣  เพิ่มบันชีดำcontact
☬➣ [Clear ban]เชคแบนโชว์คอนแทค
☬➣ [Link on]☆เปิดลิ้ง 
☬➣ [Link off]☆ปิดลิ้ง
☬➣ [Gurl]
☬➣ [Url ]➣ลิ้งกลุ่ม
☬➣ [Gname]
☬➣ [Banlist ]
☬➣ [Details grup]
☬➣ [on]➣ เปิดข้อความต้อนรับ
☬➣ [off]➣ ปิดข้อความต้อนรับ
☬➣ [Respon on]➣เปิดกล่างถึงคนแท้ค
☬➣ [Respon off]➣ปิดกล่าวถึงคนแท้ก
☬➣ [Inviteme:]
☬➣ [Info grup]
☬➣ [Gift-Allgift]➣ [ส่งของขวัญ-ทั้งหมด
☬➣ [Clear grup
☬➣️ [Reject]☆ลบรันตัวเอง
☬➣ [Mic:]☆เชคคอนแทค
☬➣️ [Reject1]➣ [ลบรันคิกเก้อ
☬➣ [Nuke]☆ล้างห้อง
☬➣ [Mention,Tagall]➣แทคทั้งห้อง
☬➣ [Kick @]➣ เตะ @
☬➣ [Kick::]➣ เตะmid
☬➣ [Bc:ct ]
☬➣ [Bc:grup]
☬➣ [Block @]
☬➣ [Youtube]➣ยูทูป
☬➣ [vdo]
☬➣ [Blocklist]
☬➣ [Spam on/off]➣รันข้อความแชท
☬➣ [ไวรัส01]
☬➣ [Bot:ct ]
☬➣ [Bot:grup.]
☬➣ [Allname:]
☬➣ [Allbio:]  
☬➣ [Gc]☆ดูผู้สร้างห้อง
☬➣ [Speed]☆สปีดบอท
☬➣ [Conban]➣เชคแบน
☬➣ [Mycopy @] ➣ก้อปปี้โปรไฟล์
☬➣ [Copy1 @] ➣ ก้อปปี้คิกเก้อ1
☬➣ [Copy2 @] ➣ ก้อปปี้คิกเก้อ2
☬➣ [Copy3 @] ➣ ก้อปปี้คิกเก้อ3
☬➣ [Copy4 @] ➣ ก้อปปี้คิกเก้อ4
☬➣ [Copy5 @] ➣ ก้อปปีัคิกเก้อ4
☬➣ [Mybackup @ ]➣กลับคืนค่าก้อปปี้
☬➣ [Like:on/off] ➣ออโต้ไลค์ เปิด/ปิด
☬➣ [Add on/off] ➣ออโต้แอด เปิด/ปิด
☬➣ [Join on/off]➣ออโต้เข้ากลุ่ม เปิด/ปิด
☬➣ [Contact on/off]➣อ่านคอนแทค เปิด/ปิด
☬➣ [Leave on/off] ➣ออโต้ออกแชทรวม เปิด/ปิด
☬➣ [Share on/off]➣โชว์ลิ้งโพส เปิด/ปิด
☬➣ [Getname @]➣เชคชื่อเพื่อน 		   
☬➣ [Getbio @]➣เชคตัสเพื่อน
☬➣ [Getprofile @]➣เชคเสตัสเพื่อน
☬➣ [Jam on/off]➣
☬➣ [Jam say:]
☬➣ [Com on/off]	
☬➣ [Message set:]	
☬➣ [Comment set:]	
☬➣ [Pesan add:]	
||=====☬P R O T E C T☬=====||        
☬➣ [Panick:on/off]      
☬➣ [Allprotect on/off]➣ล้อกทั้งหมด เปิด/ปิด
☬➣ [Protect on]☆ป้องกันเปิด/ปิด
☬➣ [Qrprotect on/off]☆ล้อกคิวอารโค้ตเปิด/ปิด
☬➣ [Inviteprotect on/off]☆เชินเปิด/ปิด			   
☬➣ [Cancelprotect on/off]ยกเชินเปิด/ปิด		   
☬➣[Staff add/remove @]	   
||=======☬FOR ADMIN☬=======||

╔════☬════♪•●☬●•♪════☬═══╗
        Http://line.me/ti/p/~getk3333
╚════☬════♪•●☬●•♪════☬═══╝
        
||=========================||
"""

help2Message =""" ||======== K̲̲̅̅ ̲̲̅̅I̲̲̅̅ ̲̲̅̅E̲̲̅̅B̲̲̅̅O̲̲̅̅ ̲̲̅̅T̲̲̅̅ ̲̲̅̅L̲̲̅̅O̲̲̅̅V̲̲̅̅E̲̲̅̅L̲̲̅̅N̲̲̅̅E̲===========||

☬คท  - ส่งคท.ตัวเอง(Me)
☬ไอดี  - ส่งMidตัวเอง
☬คิกเกอร์  - เชคคท.คิกเกอร์ทั้งหมด
☬คิกมา  - เรียกคิกเกอร์เข้ากลุ่ม
☬คิกออก  - สั่งคิกเกอร์ออกกลุ่ม
☬จุด   - ตั้งจุดเชคคนอ่าน
☬อ่าน  - เชครายชื่อคนอ่าน
☬เชคกลุ่ม  - เชคข้อมูลกลุ่ม
☬ลิสกลุ่ม  - เชคกลุ่มที่มีทั้งหมด
☬ยกเชิญ,ยก  - ยกเลิกเชิญ
☬Mid @  - เชคMidรายบุคคล
☬ดึง  - เชิญคนเข้ากลุ่มด้วยคท.
☬ดึง:  - เชิญคนเข้ากลุ่ม้ดวยMid
☬ขาว  - แก้ดำ(ส่งคท.)
☬ดำ  - เพิ่มบัญชีดำ(ส่งคท.)
☬เชคดำ  - เชคบัญชีดำ
☬ล้างดำ  - ล้างบัญชีดำ
☬เปิดลิ้ง 
☬ปิดลิ้ง
☬ลิ้ง  - เปิดและขอลิ้งกลุ่ม
☬Gname:  - เปลี่ยนชื่อกลุ่ม
☬ลบรัน  - ลบรันตัวเอง
☬ลบรัน1 - ลบรันให้เพื่อน(ขอลิ้งให้ลอคอินก่อน)
☬ขอลิ้ง  - ขอลิ้งให้เพื่อนลอคอิน
☬.  - เชคสถานะลอคอิน
☬Sp  - เชคสปีด
☬Bot sp  - เชคสปีดคิกเกอร์
☬Mycopy @  - กอพปี้โปรไฟล์
☬Copy @  - คิกเกอร์1กอพปี้
☬Mybackup  - กลับร่างเดิม
☬Backup  - คิกเกอร์1กลับร่างเดิม
☬Spam on/off  - ส่งข้อความสแปม
||==============================||
✯★Creator By   ||======== ☬☬☬☬☬☬===========||
"""

helo=""

KAC=[cl]#,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
#kimid = ki.getProfile().mid
#ki2mid = ki2.getProfile().mid
#ki3mid = ki3.getProfile().mid
#ki4mid = ki4.getProfile().mid
#ki5mid = ki5.getProfile().mid
bot1 = cl.getProfile().mid
Bots = [mid]#,kimid,ki2mid,ki3mid,ki4mid,ki5mid]
admsn = "u9ab983f3b8e59b2f276b4b1c13b8dec7"
admin = "u9ab983f3b8e59b2f276b4b1c13b8dec7"

wait = {
    'contact':True,
    'detectMention':True,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"selt bot by=*:K̲̲̅̅ ̲̲̅̅I̲̲̅̅ ̲̲̅̅E̲̲̅̅B̲̲̅̅O̲̅̅T̲̲̅̅ ̲̲̅̅L̲̲̅̅O̲̲̅̅V̲̲̅̅E̲̲̅̅L̲̲̅̅N̲̲̅̅E̲̲̅̅*.:｡ ✿*ﾟ‘ﾟ･✿.｡.:* *.",
    "lang":"JP",
    "comment":"Auto Like By ",
    "welmsg":"welcome to group",
    "commentOn":False,
    "comment1":"Bot Auto Like ©By : Nadya\nContact Me : 👉 line.me/ti/p/~getk9999.",    
    "comment2":"Bot Auto Like ©By : Nadya\nContact Me : 👉 line.me/ti/p/~getk9999",
    "comment3":"Bot Auto Like ©By : Nadya\nContact Me : 👉 line.me/ti/p/~getk9999.",    
    "comment4":"Bot Auto Like ©By : Nadya\nContact Me : 👉 line.me/ti/p/~getk9999.",    
    "commentOn":True,
    "wc":False, 
    "likeOn":True,
    "wc":False,
    "commentBlack":{},
    "wblack":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "dblack":False,
    "clock":False,
    "Sambutan":False,
    "tag":False,
    "pesan":"☺อย่าแท้กบ่อยน่ะเดะจับเยสเรย☺",
    "cNames":"",
    "blacklist":{},
    "group":False,
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}
settings = {
    "simiSimi":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

#contact = ki.getProfile()
#backup = ki.getProfile()
#backup.displayName = contact.displayName
#backup.statusMessage = contact.statusMessage
#backup.pictureStatus = contact.pictureStatus

user1 = mid
user2 = ""

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def bot(op):
    global LINETCRLogged
    global ki
    global user2
    global readAlert
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
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
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
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
                if msg.from_ == "ub8e146e024acdc277a3ba6a7d7a30ca9":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
                            
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = cl.getContact(msg.from_)
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     cName = contact.displayName
                     msg.text1 = "@"+cName+" "
                  #   balas = ["แท็คทำไมครับ(..)รึสนใจจะเอาเราไปใช้\nสนใจติดต่อได้ที่\nLine ID : Kmzaaa\nhttp://line.me/ti/p/eOuAF1hhYx\nటู้ສန้ণს☣နัဂສ૭ບĆĿŰß☣"]
                    balas = ["มีเชลบอทลบรัน พร้อมคิกเก้อ💟\nลบบินกลุ่ม ออโต้ไลค์ และอื่นๆอีกมากมาย\n🔒กันสมาชิกเปิดลิ้งห้อง\n🔒กันรัน\n🔒กันสมาชิกเชิญคนนอกเข้า\n🔒กันสมาชิกเปลี่ยนชื่อกลุ่ม\n🔒กันคนนอกเข้ามาลบคนในกลุ่ม\n👉และมีเชิพเวอร์vpn(เน็ต) มีทั้งรายเดือนและรายวัน👈\n👉สนใจติดต่อลิ้งด้านล่างเรยครับ👈\nโอนเข้าบัญชี💲เทานั้น\nสนใจ แอดมาคุยได้\nhttp://line.me/ti/p/~getk3333\nhttp://line.me/ti/p/~getk9999"]
                     ret_ = msg.text1 + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendImageWithURL(msg.to,image)
                                  break            
                    
            #if "MENTION" in msg.contentMetadata.keys() != None:
            #     if wait['kickMention'] == True:
            #         contact = cl.getContact(msg.from_)
            #         cName = contact.displayName
            #         balas = ["Dont Tag Me!! Im Busy, ",cName + " Ngapain Ngetag?, ",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja, ", "-_-, ","Putra lagi off, ", cName + " Kenapa Tag saya?, ","SPAM PC aja, " + cName, "Jangan Suka Tag gua, " + cName, "Kamu siapa, " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., "]
             #3        ret_ = "[Auto Respond] " + random.choice(balas)
             #        name = re.findall(r'@(\w+)', msg.text)
             #        summon(op.param1,[op.param2])
             #3        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
              #       mentionees = mention['MENTIONEES']
              #       for mention in mentionees:
              #             if mention['M'] in Bots:
              #                    cl.sendText(msg.to,ret_)
                                  
              #                    cl.kickoutFromGroup(msg.to,[msg.from_])
              #                    break

        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)
            print "MEMBER JOIN TO GROUP"


            
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if wait["group"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1, " ยินดีต้อนรับ. เข้ามาแล้วก็อย่าลืมลงแชร์กันน่ะครับ @ " + cl.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈""\nหรือสนใจลงบอทป้องกัน , บอทแท็ก ติดต่อได้ที่Line ID : Kmzaaa\nhttp://line.me/ti/p/eOuAF1hhYx")
            cl.sendImageWithURL(op.param1,image)
            print "ada orang masuk grup"
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if wait['group'] == True:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,"good Bye @  " + cl.getContact(op.param2).displayName + "รีบไปไหนอ่ะ. ไม่เป็นไรไว้เจอกันใหม่น่ะจ๊ะ")
            print ("MEMBER HAS LEFT THE GROUP")
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if wait['group'] == True:
            if op.param2 in bot1:
                return
            ginfo = cl.getGroup(op.param1)
            cl.sendText(op.param1, "😊ยินดีต้อนรับ 😊 @ " + cl.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈""\n\n😃เข้ามาแร้วอย่าดื้อน่ะหนู😄")
            print "MEMBER HAS JOIN THE GROUP"
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
# ----------------- NOTIFED MEMBER JOIN GROUP
#        if op.type == 17:
 #         if wait["group"] == True:
  #          if op.param2 in admin:
   #             return
    #        ginfo = cl.getGroup(op.param1)
     #       contact = cl.getContact(op.param2)
      #      image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
       #     cl.sendImageWithURL(op.param1,image)
        #    print "ada orang masuk grup"
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
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
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break

            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment2"])    
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment3"])
                     cl.like(url[25:58], url[66:], likeType=1005)
                     cl.comment(url[25:58], url[66:], wait["comment4"])                     
                     wait['likeOn'] = True 
                                         
#        if op.type == 25:
 #           msg=op.message
  #          if "@"+cl.getProfile().displayName in msg.text:
   #                 if wait["tag"] == True:
    #                    tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
     #                   jawab = (wait["pesan"])
      #                  jawaban = (jawab)
       #                 contact = cl.getContact(msg.from_)
        #                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
         #               cl.sendImageWithURL(msg.to, path)
          #              cl.sendText(msg.to,jawaban)
           #             print "ada orang tag"
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
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
                        msg.text = "💟ลิ้งโพสอยู่ด้านล้างน้ะจ้ะ💟\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
 
 #--------------------------------------------------                   
#                elif msg.text.lower()  == 'help2':
 #               if wait["lang"] == "JP":
                    cl.sendText(msg.to,help2Message)
  #              else:
   #                 cl.sendText(msg.to,help2Message)

#----------------------------------------------
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
#-----------------------------------------------
            elif msg.text in ["Conban","Contactban","Contact ban"]:
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
#----------------------------------------------------------
            elif "M @" in msg.text:
                _name = msg.text.replace("M @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#----------------------------------------------------------
            elif msg.text in ["group","รายชื่อ"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

#-----------------------------------------------
            elif "Steal dp @" in msg.text:
                nama = msg.text.replace("Steal dp @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        midddd = cl.getContact(linedev.mid)
                        PATH = "http://dl.profile.line-cdn.net/" + midddd.pictureStatus
                    cl.sendImageWithURL(msg.to,PATH)
#================================================
            elif msg.text in ["bot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif "As1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "As2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "As3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "As4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "As5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","As1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","As2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","As3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","As4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)
            elif msg.text in ["Allgift","All Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)

#            if "MENTION" in msg.contentMetadata.keys() != None:
 #                if wait['detectMention'] == True:
  #                   contact = kr.getContact(msg.from_)
   #                  image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
    #                 cName = contact.displayName
     #                msg.text1 = "@"+cName+" "
      #               balas = ["💓อย่าแท้กสิเตง💓"]
       #              ret_ = msg.text1 + random.choice(balas)
        #             name = re.findall(r'@(\w+)', msg.text)
         #            mention = ast.literal_eval(msg.contentMetadata["MENTION"])
          #           mentionees = mention['MENTIONEES']
           #          for mention in mentionees:
            #               if mention['M'] in Bots:
             #                     kr.sendText(msg.to,ret_)
              #                    kr.sendImageWithURL(msg.to,image)
               #                   break 
                              
            


            elif msg.text in ["Cancel","cancel","ยกเชิญ","ยก"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "As1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "As2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "As3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "As4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "As5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
            elif "Mic:" in msg.text:
                mmid = msg.text.replace("Mic:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)

#---------------------------------------------------------
            elif "Name:" in msg.text:
                string = msg.text.replace("Name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
            elif "Name Bot" in msg.text:
                string = msg.text.replace("Name Bot","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    cl.sendText(msg.to,"The name " + string + " I did NI change。")
#---------------------------------------------------------
            elif "K1 upname:" in msg.text:
                string = msg.text.replace("K1 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K2 upname:" in msg.text:
                string = msg.text.replace("K2 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K3 upname:" in msg.text:
                string = msg.text.replace("K3 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K4 upname:" in msg.text:
                string = msg.text.replace("K4 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
            elif "K5 upname:" in msg.text:
                string = msg.text.replace("K5 up name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"The name " + string + " I did NI change。")
#--------------------------------------------------------
#--------------------------------------------------------
            elif msg.text.lower() == 'allin':
                        Ticket = cl.reissueGroupTicket(msg.to)
                        invsend = 0.22222
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.021)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.011)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.011)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.011)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.011)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------------
            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของค���ณเเล้ว")
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
#======================================================#    
#-----------------------------------------------
            elif "Mic: " in msg.text:
                mmid = msg.text.replace("Mic: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟เปิดอ่านคอนแทคสำเร็จ🌟")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off 👈")
                    else:
                        cl.sendText(msg.to,"It is already off 👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off already")
                    else:
                        cl.sendText(msg.to,"🌟ปิดอ่านคอนแทคสำเร็จ🌟")
            elif msg.text.lower() == 'protect on':
              if msg.from_ in admin:
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ��")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ป้องกันเปิดสำเร็จ🌟")
                    else:
                        cl.sendText(msg.to,"It is already On ")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                  if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔��")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka 👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคลิ้งคิวอาร์โค���ตเปิด🌟")
                    else:
                        cl.sendText(msg.to,"It is already On ")
            elif msg.text.lower() == 'inviteprotect on':
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka 👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"��ล็อคการเชิญกลุ่มเปิด🌟")
                    else:
                        cl.sendText(msg.to,"It is already On ")
            elif msg.text.lower() == 'cancelprotect on':
              if msg.from_ in admin:
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka 👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคยกเลิกเชิญสมาชิกเปิด🌟")
                    else:
                        cl.sendText(msg.to,"It is already On ")
                        
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait['detectMention'] = True
                cl.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait['detectMention'] = False
                cl.sendText(msg.to,"Auto respon tag Off")

            elif msg.text in ["on"]:
                wait['group'] = True
                cl.sendText(msg.to,"เปิดต้อนรับแร้ว")

            elif msg.text in ["off"]:
                wait['group'] = False
                cl.sendText(msg.to,"ปิดข้อความ")
                
            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Off(p′︵‵。)")


            elif msg.text.lower() == 'join on':
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ออโต้เข้ากลุ่มเปิด🌟")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคเชิญเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ล็อคเชิญเปิด🌟")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคเชิญเปิด🌟")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคยกเลิกเชิญเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ล็อคยกเลิกเชิญเปิด🌟")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคยกเลิกเชิญเปิด🌟")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ป้องกันเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ป้องกันเปิด🌟")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ป้องกันเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ป้องกันเปิด🌟")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคลิ้งคิวอาร์โค้ตเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ล็อคลิ้งคิวอาร์โค้ตเปิด🌟")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🌟ล็อคลิ้งคิวอาร์โค้ตเปิด🌟")
                    else:
                        cl.sendText(msg.to,"🌟ล็อคลิ้งคิวอาร์โค้ตเปิด🌟")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ล็อคเชิญปิด✨")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคเชิญปิด✨")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
            elif msg.text.lower() == 'join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ออโต้เข้ากลุ่มปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ออโต้เข้ากลุ่มปิด✨")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ออโต้เข้ากลุ่มปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ออโต้เข้ากลุ่มปิด✨")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันปิด���")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันปิด✨")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ล็อคลิ้งคิวอาร์โค้ตปิด✨")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันเชิญปิด✨")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันเชิญปิด✨")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
                    else:
                        cl.sendText(msg.to,"✨ป้องกันยกเลิกเชิญปิด✨")
            elif "Gcancel:" in msg.text:
              if msg.from_ in admin:
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
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif msg.text in ["Welcome:on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomesg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            elif msg.text in ["Welcome:off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'set':
                md = ""       
                if wait["contact"] == True: md+="☞ คอนแทค → ✔\n"
                else: md+="🔚 คอนแทค → ❎\n"
                if wait["autoJoin"] == True: md+="☞ ออโต้เข้ากลุ่ม → ✔\n"
                else: md+="🔚 ออโต้เข้ากลุ่ม → ❎\n"
                if wait["autoCancel"]["on"] == True:md+="☞ ยกเลิกเชิญกลุ่ม: " + str(wait["autoCancel"]["members"]) + " → ✔\n"
                else: md+="🔚 ยกเลิกเชิญกลุ่ม → ❎\n"
                if wait["leaveRoom"] == True: md+="☞ ออโต้ออกแชทรวม → ✔\n"
                else: md+="🔚 ออโต้ออกแชทรวม → ❎\n"
                if wait["timeline"] == True: md+="☞ แชร์ลิ้ง → ✔\n"
                else:md+="🔚 แชร์ลิ้ง → ❎\n"
                if wait["autoAdd"] == True: md+="☞ ออโต้แอด → ✔\n"
                else:md+="🔚 ออโต้แอด → ❎\n"
                if wait["commentOn"] == True: md+="☞ Auto komentar → ✔\n"
                else:md+="🔚 Auto komentar → ❎\n"
                if wait["protect"] == True: md+="☞ ป้องกัน → ✔\n"
                else:md+="🔚 ป้องกัน → ❎\n"
                if wait["linkprotect"] == True: md+="☞ ป้องกันลิ้ง → ✔\n"
                else:md+="🔚 ป้องกันลิ้ง → ❎\n"
                if wait["inviteprotect"] == True: md+="☞ ป้องกันเขิญ → ✔\n"
                else:md+="🔚 ป้องกันเชิญ → ❎\n"
                if wait["cancelprotect"] == True: md+="☞ ป้องกันยกเลิกเชิญ → ✔\n"
                else:md+="🔚 ป้องกันยกเลิกเชิญ → ❎\n"
                if wait["likeOn"] == True: md+="☞ ออโต้ไลค์ → ✔\n"
                else:md+="🔚 ออโต้ไลค์ → ❎\n" 
                if wait["Sambutan"] == True: md+="☞ เปิดโชว์คอนแทค → ✔\n"
                else:md+="🔚 เปิดโชว์คอนแทค → ❎\n" + datetime.now().strftime('\n📅%Y/%m/%d 🕛 %H:%M:%S')
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)

            elif msg.text in ["Like on"]:
                if wait["likeon"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["Like on"] = True
                    if wait["likeon"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Like off"]:
                if wait["likeoff"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeoff"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On👈")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ã‚ªãƒ³ã«ã—ã¾ã—ãŸ👈")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text in ["Point","นับ"]:
                if msg.toType == 2:
                    cl.sendText(msg.to, "ตั้งจุดเช็คคนอ่าน:" + datetime.now().strftime('\n📅%Y/%m/%d 🕛 %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('📅%Y-%m-%d 🕛 %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text in ["Read","อ่าน"]:
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\n Powered By: kieselfbotline" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('📅%Y-%m-%d 🕛 %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n📅%Y-%m-%d 🕛 %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")
#=================================================
            elif msg.text == "แอบ":
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "ออกมา":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Lurking dulu dudul Baru bilang result Point.")
						
#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
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
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","adminlist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------
            elif msg.text in ["Group creator","Gc","Gcreator","gcreator"]:
                ginfo = cl.getGroup(msg.to)
                gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"""╔══════════════
💥ผู้สร้างกลุ่ม Creator 💥Group""")
#staff-----------------------------------------------------------
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"💗ชื่อ💗 :\n" + contact.displayName + "\n\n💗สเตตัส💗 :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
#----------------------------------------------------
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                   cl.cloneContactProfile(target)
                                   cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
#=================================================
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))


#-------------------------------- PP BY TAG ---------------------------------
            elif "Lo @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")
                                
            

            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                                xname = cl.getContact(msg.from_).displayName
                                cl.sendText(msg.to,"Kepo Kaka Yaa "+xname+"\n   (｀・ω・´)\n \n"  +  datetime.now().strftime('%H:%M:%S'))
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/0hQHBfiuxIDmd_HyI5amNxMENaAAoIMQgvBywTVFNIAgRTLk9kRHBCAlkcAFMGKkBiS3hAUQgbBVFU")
#----------------------------------------------------------------------

            elif msg.text in ["Rejectall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Completion。")
                    ki.sendText(msg.to,"Completion。")
                    ki2.sendText(msg.to,"Completion。")
                    ki3.sendText(msg.to,"Completion。")
                    ki4.sendText(msg.to,"Completion。")
                    ki5.sendText(msg.to,"💟ทำการลบห้องรันหมดแล้ว💟")
                else:
                    cl.sendText(msg.to,"key is wrong。")
   #----------------------------------------------------------------
            elif msg.text in ["Reject","ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ปฏิเสทคำเชิญเข้ากลุ่มทั้งหมดเรียบร้อย")
                else:
                    cl.sendText(msg.to,"key is wrong")
            elif msg.text in ["Reject1","ลบรัน1"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"ปฏิเสทค้างเชิญเรียบร้อย")
                else:
                    ki.sendText(msg.to,"key is wrong")
#========================================
            elif msg.text.lower() == 'welcome':
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=========================================
            elif "Say " in msg.text:
                string = msg.text.replace("Say ","")
                if len(string.decode('utf-8')) <= 50:
                    ki.sendText(msg.to," " + string + " ")
                    ki2.sendText(msg.to," " + string + " ")
                    ki3.sendText(msg.to," " + string + " ")
                    ki4.sendText(msg.to," " + string + " ")
                    ki5.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    ki2.sendText(msg.to," " + string + " ")
                    ki3.sendText(msg.to," " + string + " ")
                    ki4.sendText(msg.to," " + string + " ")
                    ki5.sendText(msg.to," " + string + " ")
                    ki.sendText(msg.to," " + string + " ")
                    ki2.sendText(msg.to," " + string + " ")
                    ki3.sendText(msg.to," " + string + " ")
                    ki4.sendText(msg.to," " + string + " ")
                    ki5.sendText(msg.to," " + string + " ")
#-----------------------------------------------
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
            elif 'Youtube ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#==================================================
            elif msg.text in ["ทีมงาน","ทีมทดลองบอท"]:
                msg.contentType = 13
                cl.sendText(msg.to, "[SELFBOT PHET HACK BOT]\n\n[☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢]\n[By.ทีมงานทีมทดลองบอท]")
                cl.sendText(msg.to, "ผู้จัดการทีมงาน:kielovebot")
                msg.contentMetadata = {'mid': 'uca51afa767df87ba3705494b97c3355c'}
                cl.sendMessage(msg)
#=====================================================               
#-----------------------------------------------
#==================================================
#=====================================================               
#=================================================================================
 
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
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
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
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


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
                cl.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
                
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
 
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)

#=========================================
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#=======================================
#========================================
            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
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
                       time.sleep(0.2)
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
                                    Ki5.kickuotFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    Ki5.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    Cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    Cl.updateGroup(gs)
#----------------------------------------------------
            elif msg.text in ["Aslogin","ขอลิ้ง"]:
                    if LINETCRLogged == False:
                        ki.login(qr=True)
                        ki.loginResult()
                        user2 = ki.getProfile().mid
                        LINETCRLogged = True
                        cl.sendText(msg.to,"ล็อคอินสำเร็จ Asul พร้อมใช้งานแล้ว")
                    else:
                        cl.sendText(msg.to,"Asul ได้ทำการล็อคอินไปแล้ว")
            elif msg.text.lower() == ".":
                    gs = []
                    try:
                        gs = cl.getGroup(msg.to).members
                    except:
                        try:
                            gs = cl.getRoom(msg.to).contacts
                        except:
                            pass
                    tlist = ""
                    for i in gs:
                        tlist = tlist+i.displayName+" "+i.mid+"\n\n"
                    if LINETCRLogged == True:
                        try:
                            ki.sendText(user1,tlist)
                        except:
                            ki.new_post(tlist)
                    else:
                        cl.sendText(msg.to,"Asul ยังไม่ได้ล็อคอิน")
#-----------------------------------------------------------)
            elif msg.text in ["Help2","Key","KEY"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,help2Message)
                else:
                    cl.sendText(msg.to,help2Message)
#----------------------ADMIN COMMAND------------------------------#

            elif ("Kick " in msg.text):
                if msg.from_ in admin:
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

            elif ("Kick1 " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")

            elif ("Kick5 " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki5.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")


                    
            elif msg.text in ["Mention","Tagall","มอง","."]:
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

            elif "Ratakan" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Ratakan","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[ki2,ki3,ki4,ki5]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)

            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")

            elif "Kick: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif msg.text in ["Invite:","ดึง:"]:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "My @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("My @","")
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
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
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
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e

            elif "Copy1 @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy1 @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif "Copy2 @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy2 @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki2.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki2.cloneContactProfile(target)
                                    ki2.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif "Copy3 @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy3 @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki3.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki3.cloneContactProfile(target)
                                    ki3.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif "Copy4 @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy4 @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki4.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki4.cloneContactProfile(target)
                                    ki4.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif "Copy5 @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy5 @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki5.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki5.cloneContactProfile(target)
                                    ki5.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e

            elif msg.text in ["backup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    ki.sendText(msg.to, str (e))

            elif "Bc:ct " in msg.text:
                bctxt = msg.text.replace("Bc:ct ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                
            elif "Bc:grup " in msg.text:
                bctxt = msg.text.replace("Bc:grup ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif msg.text in ["me","Me","คท","กู"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)

#            elif msg.text in ["me","Me"]:
 #               msg.contentType = 13
  #              msg.contentMetadata = {'mid': msg.from_}
   #             cl.sendMessage(msg)
    #            print "SUKSES -- SEND CONTACT"    
            

            elif cms(msg.text,["แอดมิน","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿 ")
#                msg.contentType = 13
 #               msg.contentMetadata = {'mid': admin}
  #              cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
   #             cl.sendMessage(msg)
    #            cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿 ")
            
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["Clear grup"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text in ["Ginfo","เชคกลุ่ม"]:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "ไวรัส01":
	            cl.sendText(msg.to,"หยุดดดดดด....\nขอให้ทุกคนอยู่ในความสงบ\n\n 1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
            
            elif ".music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
            
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])

            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
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
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e

            elif msg.text.lower() == 'blocklist':
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
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
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
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
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
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")

#===============================================                
            elif msg.text in ["Invite on","เชินเปิด"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"🌟เปิดเชิญด้วยคอนแทค🌟")

            elif msg.text in ["Invite off","ปิดเชิน"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = False
                random.choice(KAC).sendText(msg.to,"🌟ปิดเชิญ🌟")
#===============================================                
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif msg.text in ["Mid","ไอดี"]:
                cl.sendText(msg.to, msg.from_)

            elif msg.text in ["Link on","เปิดลิ้ง"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["Link off","ปิดลิ้ง"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close👈")
                    else:
                        cl.sendText(msg.to,"URL close👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl","ลิ้ง"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["list"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki2.getGroup(i).name + " | [ " + str(len (ki2.getGroup(i).members)) + " ]")
                ki2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki3.getGroup(i).name + " | [ " + str(len (ki3.getGroup(i).members)) + " ]")
                ki3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki4.getGroup(i).name + " | [ " + str(len (ki4.getGroup(i).members)) + " ]")
                ki4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[���] %s \n" % (ki5.getGroup(i).name + " | [ " + str(len (ki5.getGroup(i).members)) + " ]")
                ki5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                    
            elif msg.text == "ลิ้ง":
                    ki.sendText(msg.to,"nekopoi.host")
                    ki.sendText(msg.to,"sexvideobokep.com")
                    ki.sendText(msg.to,"memek.com")
                    ki.sendText(msg.to,"pornktube.com")
                    ki.sendText(msg.to,"faketaxi.com")
                    ki.sendText(msg.to,"videojorok.com")
                    ki.sendText(msg.to,"watchmygf.mobi")
                    ki.sendText(msg.to,"xnxx.com")
                    ki.sendText(msg.to,"pornhd.com")
                    ki.sendText(msg.to,"xvideos.com")
                    ki.sendText(msg.to,"vidz7.com")
                    ki.sendText(msg.to,"m.xhamster.com")
                    ki.sendText(msg.to,"xxmovies.pro")
                    ki.sendText(msg.to,"youporn.com")
                    ki.sendText(msg.to,"pornhub.com")
                    ki.sendText(msg.to,"anyporn.com")
                    ki.sendText(msg.to,"hdsexdino.com")
                    ki.sendText(msg.to,"rubyourdick.com")
                    ki.sendText(msg.to,"anybunny.mobi")
                    ki.sendText(msg.to,"cliphunter.com")
                    ki.sendText(msg.to,"sexloving.net")
                    ki.sendText(msg.to,"free.goshow.tv")
                    ki.sendText(msg.to,"eporner.com")
                    ki.sendText(msg.to,"Pornhd.josex.net")
                    ki.sendText(msg.to,"m.hqporner.com")
                    ki.sendText(msg.to,"m.spankbang.com")
                    ki.sendText(msg.to,"m.4tube.com")
                    ki.sendText(msg.to,"brazzers.com")
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif "Speed" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ᴘʀᴏɢʀᴇss...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))    
                ki5.sendText(msg.to, "%sseconds" % (elapsed_time))    
#-----------------------------------------------
            elif "Sp" in msg.text:
                start = time.time()
                cl.sendText(msg.to, "ᴘʀᴏɢʀᴇss...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))    
#-----------------------------------------------        
            
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki5.sendText(msg.to, text)
                profile = ki5.getProfile()

#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif ("Ban " in msg.text):
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
                        cl.sendText(msg.to,"Succes Banned")
                    except:
                        pass

            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                    nk0 = msg.text.replace("Ban:","")
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

            elif "Unban:" in msg.text:                  
                    nk0 = msg.text.replace("Unban:","")
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

            elif msg.text.lower() == 'Banlist':
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "�" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "�" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")



            elif msg.text in ["cb","���้างดำ"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Whitelist","ขาว"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Blacklist","ดำ"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Banlist","เชคดำ"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin:
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
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    cl.sendText(msg.to,"Masih Mauko Sundala")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ada Member")
                        ki2.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Hahaha")
                                ki2.sendText(msg,to,"Fakyu Sundala")

#-----------------------------------------------

#-----------------------------------------------
            elif "Kicker" in msg.text:
                        X = cl.getGroup(msg.to)                    
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        invsend = 0 
                        Ti = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ti)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ti)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ti)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ti)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ti)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(msg.to)
#-----------------------------------------------
            elif msg.text in ["Sayang","Kuy","All join","Minna"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'spcome':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "As1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "As2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "As3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "As4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "As5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["คิกออก","Bye","กุเกลียดมึง","Sayonara"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"ไปก็ได้ บ๊ายบาย "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "As1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "As2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "As3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "As4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "As5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------

            elif msg.text in ["Welcome","wc on","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                wait["wc"] = True
                cl.sendText(msg.to,"ยินดีต้อนรับสู่กลุ่ม " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                
            elif msg.text in ["Welcome","wc off","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                wait["wc"] = False
                cl.sendText(msg.to,"ยินดีต้อนรับสู่กลุ่ม " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )

#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in kimid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
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
                if wait['likeOn'] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
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
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By C-A_Bot😊\n\n☆º°˚˚✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰º°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


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
                nowT = datetime.strftime(now2,"(%H:%M)")
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
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
