from kivy.config import Config

Config.set('graphics','resizable',0)

import requests
import json
import pyttsx3
from geopy.distance import geodesic
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from pycricbuzz import Cricbuzz
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import time
import sqlite3
import re
import getpass
import datetime
import win32api #install using pipwin
import wmi#new
from word2number import w2n#new
from plyer import notification#new
import os
import threading
import sys
import webbrowser
import pyscreenshot as ss
from random import randint
from quotes import Quotes#today
import pyautogui#today
from time import sleep#today

#gui import files
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton,MDRectangleFlatButton,MDRaisedButton
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.floatlayout import FloatLayout
# import gui2

#classes goes here-
class Chattwidget(Widget):
    
    # def wished(self):
        # wish(getpass.getuser())
    
    def BotM(self,str1):
        if str1!="":
            # str1=txt_inp
            nxl_pos=19
            # i=19
            if len(str1)>30:
                while(nxl_pos>=5):
                    if str1[nxl_pos]==' ':
                        # if len(str1)-nxl_pos<20:
                        break
                    else:
                        nxl_pos-=1
                    if nxl_pos==15:
                        nxl_pos=20
                        break
            if(len(str1)>20):
                str2=str1[:nxl_pos] +'\n'+str1[nxl_pos+1:]
            else:
                str2=str1
            bubble=FloatLayout(pos_hint={'x':0,'y':0})
            labl=MDLabel(text=str2)
            newsize=labl.size
            label=MDRaisedButton(text=str2,
                          pos_hint={'left':0.5,'y':0},
                          size_hint_y=None,
                          size_hint_x=None,
                          size=(newsize[0]+10,newsize[1]+10),
                          md_bg_color=(1,1,0,1)
                          
                          )
            bubble.add_widget(label)
            self.ids.flayout.add_widget(bubble)
            # flayout.add_widget(bubble)
            
            # txt_inp.text=""

    def emptee(self,txt_inpt):
        txt_inpt.text=""
        # print(flay)

    def sendM(self,txt_inp0,le):
        str1=txt_inp0

        if str1!="":
            nxl_pos=19
            # i=19
            if len(str1)>30:
                while(nxl_pos>=5):
                    if str1[nxl_pos]==' ':
                        # if len(str1)-nxl_pos<20:
                        break
                    else:
                        nxl_pos-=1
                    if nxl_pos==5:
                        nxl_pos=30
                        break
            if(len(str1)>30):
                str2=str1[:nxl_pos] +'\n'+str1[nxl_pos+1:]
            else:
                str2=str1
            bubble=FloatLayout(pos_hint={'x':1,'y':0})
            labl=MDLabel(text=str2)
            newsize=labl.size
            label=MDRaisedButton(text=str2,
                          pos_hint={'right':1,'y':0},
                          size_hint_y=None,
                          size_hint_x=None,
                          size=(newsize[0]+10,newsize[1]+10),
                          md_bg_color=(1,0,1,1)
                          
                          )
            bubble.add_widget(label)
            self.ids.flayout.add_widget(bubble)
            
            # if type(txt_inp0)!=type(''):
                # txt_inp0.text=""
            if le: 
                # print('call run_asst')
                run_assistant_txt(str1.lower())


    def run_asst(self):
        query=run_assistant()
        self.sendM(query,False)
        # sample.inpt(flayout)


Builder.load_file("helper3.kv")

class ChattApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        self.theme_cls.primary_hue="700"
        # self.theme_cls.theme_style='Dark'
        # print('build')
        # screen=Screen()
        # self.widg_obj=Chattwidget()
        return self.widg_obj

    def create_widg(self,widge1):
        self.widg_obj=widge1

    def assign(self,db):
        self.db=db
        # print('assign')

    def callBotM(self,text):
        self.widg_obj.BotM(text)
        
class SayQuote():
    def gonoobs(self):
        q=Quotes()
        qt=q.random()
        speak('a quote by '+qt[0]+' '+qt[1])
        
class PlaySong():
    def gonoobs(c):
        url='https://music.youtube.com/search?q='+c
        webbrowser.get('chrome').open_new_tab(url)
        
class WikiSearch():
    def gonoobs(query):
        results=wikipedia.summary(query, sentences=2)
        speak(results)

class Screenshot():
    def gonoobs(self):
        img=ss.grab()
        img.save(self.getRandName())
        #file saved with 25 characters long random name in png format
    def getRandName(self):
        name = ''
        for i in range(20):
            name+=chr(65+randint(0,25))
        for i in range(5):
            name+=str(randint(0,9))
        return name+'.png'

class SetReminder():
    def gonoobs(self):
        title = None
        while(title == None):
            gui_obj.widg_obj.BotM('what do you want to be reminded')
            speak('what do you want to be reminded')
            title=self.input_speech()
        rdt = None
        while(rdt== None):
            gui_obj.widg_obj.BotM('when do you want it to be reminded')
            speak('when do you want it to be reminded')
            rdt=self.input_speech()
        print(rdt)
        rdt = self.extract_date_from_string(rdt)
        kill_process()#database rdata.db in use so need to kill the process
        db = sqlite3.connect('C:\\Users\\shash\\Desktop\\python project\\final\\rdata.db')
        c = db.cursor()
        c.execute('insert into ReminderData(title,datetime) values ( ? , ?)',(title,rdt))
        db.commit()
        gui_obj.widg_obj.BotM('reminder set')
        speak('reminder set')
        thread = threading.Thread(target = start_process,daemon=True)
        thread.start()
        #c.close()
        #db.close()
    def extract_date_from_string(self,text):
        text = text.lower()
        text = self.modify_text(text)
        now = datetime.datetime.now()
        y,m,d,h,mn = now.year,now.month,now.day,now.hour,now.minute #default values
        #setting date
        if 'tommorow' in text:
            now += datetime.timedelta(days = 1)#getting tommorow's date
            y,m,d = now.year , now.month , now.day
        elif 'week' in text or 'weeks' in text:# after 1 week
            tm = re.match('(\d+) week.*').groups()
            if tm == None:#default case
                now += datetime.timedelta(days=7)
            else:
                now+=datetime.timedelta(days = 7*int(tm[0]))
            y,m,d = now.year , now.month , now.day
        else:
            #user has specified date on text or no date specified
            tm= self.getmonthday(text) #toget int month from string
            if tm!=None:
                d,m = tm
        #we got the date now time to get time
        if 'hour' in text or 'hours' in text:
            try:
                tm = re.match('(\d+) hour.*',text).groups()
                #print(tm)
                if tm == None:
                    tm=('1',)#default case
                if 'at' in text:
                    h=int(tm[0])
                else:
                    now += datetime.timedelta(hours = int(tm[0]))
                    y,m,d,h,mn = now.year,now.month,now.day,now.hour,now.minute
            except:
                pass
        if 'minute' in text or 'minutes' in text:
            try:
                tm = re.match('(\d+) minute.*',text).groups()
                #print(tm)
                if 'at' in text:
                    mn = int(tm[0])
                else:
                    now += datetime.timedelta(minutes = int(tm[0]))
                    y,m,d,h,mn = now.year,now.month,now.day,now.hour,now.minute
            except:
                pass

        if 'p.m.' in text or 'a.m.' in text or 'o\'clock' in text:
            tm = re.match('(\d+)\W(\d*) a\.m\..*|(\d+)\W(\d*) p\.m\..*|(\d+)\W(\d*) o\'clock.*',text).groups()
            if tm ==None:
                pass
            if len(tm)==1:
                h=int(tm[0])
                mn=0
            else :
                h,mn = int(tm[0]),int(tm[1])
            if 'a.m.' in text:
                if h>12:
                    h=h%12
            if 'p.m.' in text:
                if h<12:
                    h=12+h
        if 'morning' in text:
            h,mn = 8,0
        elif 'afternoon' in text:
            h,mn = 12,0
        elif 'evening' in text:
            h,mn = 18,0
        elif 'night' in text:
            h,mn = 23,59

        return datetime.datetime(y,m,d,h%24,mn%60)
    def modify_text(self,text):
        '''changes text numbers into digits'''
        words = re.split('\W+',text)
        for i in words:
            try:
                text.replace(i,str(w2n.word_to_num(i)))
            except:
                pass
        return text

    def getmonthday(self,text):
        day =datetime.datetime.now().day
        month=0
        mname=''
        if 'january' in text:
            mname = 'january'
            month = 1
        elif 'february' in text:
            mname = 'february'
            month = 2
        elif 'march' in text:
            mname = 'march'
            month = 3
        elif 'april' in text:
            mname = 'april'
            month = 4
        elif 'may' in text:
            mname = 'may'
            month = 5
        elif 'june' in text:
            mname = 'june'
            month = 6
        elif 'july' in text:
            mname = 'july'
            month = 7
        elif 'august' in text:
            mname = 'august'
            month = 8
        elif 'september' in text:
            mname = 'september'
            month = 9
        elif 'october' in text:
            mname = 'october'
            month = 10
        elif 'november' in text:
            mname = 'november'
            month = 11
        elif 'december' in text:
            mname = 'december'
            month = 12
        if month!=0:
            tm = re.match('(\d+).*'+mname).groups()
            if tm == None:
                return day,month
            else:
                return int(tm[0]),month
        return None

    def input_speech(self):
        try:
            recg=spr.Recognizer()
            with spr.Microphone() as source:
                recg.adjust_for_ambient_noise(source,duration=0.5)
                audio=recg.listen(source)
                query=recg.recognize_google(audio)
                query=query.lower()
                return query
        except:
            gui_obj.widg_obj.BotM('sorry some error occured while listening , please try again')
            speak('sorry some error occured while listening , please try again')
            return None

class OpenSoftware():
    '''opens any software'''
    def find_file_in_all_drives(self,file_name):
        #create a regular expression for the file
        rex = re.compile(file_name+'[a-zA-Z0-9 ]*'+'\.exe')
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
            b=self.find_file( drive, rex )
            if b:
                return True
    def find_file(self,root_folder, rex):
        for root,dirs,files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print(str(f))
                    print(root+'\\'+str(f))
                    os.system('\"'+os.path.join(root, f)+'\"')
                    #print(os.path.join(root, f))
                    return True# if you want to find only ones
    def gonoobs(self,sfname):
        if 'command' in sfname or 'prompt' in sfname:
            sfname = 'cmd'
        try:
            os.startfile('\"'+sfname+'\"')
        except:
            if not self.find_file_in_all_drives(sfname):
                print('file not found')

class LiveScores():
    def __init__(self):
        self.c=Cricbuzz()
        self.all_matches = self.c.matches()
    def gonoobs(self):
        print('---LIVE SCORES---')
        count=0
        for match in reversed(self.all_matches):
            try:
                batting_data=self.c.livescore(match['id'])['batting']
                bowling_data=self.c.livescore(match['id'])['bowling']
                '''
                print(batting_data)
                print(batting_data['team'],':',batting_data['score'][0]['runs'],'/',batting_data['score'][0]['wickets'],'Overs:',batting_data['score'][0]['overs'])
                print('versus ',bowling_data['team'])
                print('status:',self.c.matchinfo(match['id'])['status'])
                count+=1
                #print(self.c.scorecard(match['id']))
                '''
                count+=1
                innings='second' if batting_data['score'][0]['inning_num']=='2' else 'first'
                assistant.say('match '+batting_data['team']+' versus '+bowling_data['team'])
                assistant.say(innings+' innings '+batting_data['team']+' is batting with score '+batting_data['score'][0]['runs']+' at '+batting_data['score'][0]['wickets'])
                gui_obj.widg_obj.BotM('in '+batting_data['score'][0]['overs']+' overs')
                speak('in '+batting_data['score'][0]['overs']+' overs')                

            except:
                pass
        if count==0:
            gui_obj.widg_obj.BotM('NO LIVE MATCHES NOW')
            speak('NO LIVE MATCHES NOW')

class Temperature():
    def __init__(self):
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        self.__api_key = '1d0e999398d111f7c2c2b0a0852fb4d8'

    def gonoobs(self,city):
        try:
            response = requests.get(self.__base_url+city+"&appid="+self.__api_key)
            temperature = response.json()['main']['temp']
            temperature=round(temperature-273.15,2)
            text='the current temperature in '+city +' is '+str(temperature)+ ' degrees celcius'
            gui_obj.widg_obj.BotM(text)
            speak(text)
        except:
            gui_obj.widg_obj.BotM('Sorry can not find temprature now , make sure you are connected to the internet')
            speak('Sorry can not find temprature now , make sure you are connected to the internet')

class WeatherReport():
    '''Uses openweathermap api to get current weather status
    of any city across the world'''
    def __init__(self):
        self.__base_url = "http://api.openweathermap.org/data/2.5/weather?q="
        self.__api_key = '1d0e999398d111f7c2c2b0a0852fb4d8'
    def gonoobs(self,city):
        try:
            response = requests.get(self.__base_url+city+"&appid="+self.__api_key)
            data= response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            temperature=round(temperature-273.15,2)
            txt1='the current temperature in '+city +' is '+str(temperature)+ ' degrees celcius'
            txt2='and the current weather is ' + str(report[0]['description'])
            gui_obj.widg_obj.BotM(txt1+txt2)
            speak(txt1+txt2)
        except:
            gui_obj.widg_obj.BotM('Sorry can not find weather details now ')
            speak('Sorry can not find weather details now ')
            

class UpcomingMatches():
    def __init__(self):
        self.c=Cricbuzz()
        try:
            self.all_matches = self.c.matches()
        except :
            self.all_matches=None
    def gonoobs(self):
        if self.all_matches == None:

            gui_obj.widg_obj.BotM('Cannot find match details now')
            speak('Cannot find match details now')
            return
        matches_available=False
        for match in self.all_matches:
            if 'Starts' in match['status']:
                matches_available = True
                assistant.say('match '+match['team1']['name']+'vs'+match['team2']['name'])
                assistant.say(match['status'])
                assistant.runAndWait()
        if not matches_available:
            gui_obj.widg_obj.BotM('No matches in nearby future')
            speak('No matches in nearby future')

class DistanceFinder():
    def __init__(self):
        self.geolocator = Nominatim(user_agent="p_finder")
    def gonoobs(self,loc1,loc2):
        try:
            l1 = self.geolocator.geocode(loc1)
            l2 = self.geolocator.geocode(loc2)
            start_point=(float(l1.longitude),float(l1.latitude))
            end_point=(float(l2.longitude),float(l2.latitude))
            d=round(geodesic(start_point,end_point).kilometers,2)
            #d2=round(great_circle(start_point,end_point).kilometers,2)
            gui_obj.widg_obj.BotM('approximate distance between '+loc1+' and '+loc2+' is '+str(d)+' kilometers')
            speak('approximate distance between '+loc1+' and '+loc2+' is '+str(d)+' kilometers')
        except:
            gui_obj.widg_obj.BotM('cannot find distance make sure you are connected to the internet')
            speak('cannot find distance make sure you are connected to the internet')

class News():
    def __init__(self):
        self.__apikey='e91abf1c8a1147b4813b9dbbd87fb0bc'
        self.url='https://newsapi.org/v2/top-headlines?country=in&apiKey='+self.__apikey
        self.total_count=1

    def gonoobs(self):
        try:
            response = requests.get(self.url)
            newscollection = json.loads(response.text)
            count=0
            # gui_obj.widg_obj.BotM('Top new headlines are as follows')
            # speak('Top  new headlines are as follows')
            for news in newscollection['articles']:
                if count==self.total_count:
                    break
                speak(str(news['title']))
                gui_obj.widg_obj.BotM(str(news['title']))
                count+=1
        except:
            gui_obj.widg_obj.BotM('sorry cannot load news at this time')
            speak('sorry cannot load news at this time')

class Whatsapp():

    chrome_path="C:\\Users\\vnp\\AppData\\Local\\Programs\\Opera\\launcher.exe"
    webbrowser.register('opera',None,webbrowser.BackgroundBrowser(chrome_path))

    
    def input_speech(self):
        try:
            recg=spr.Recognizer()
            with spr.Microphone() as source:
                recg.adjust_for_ambient_noise(source,duration=0.5)
                audio=recg.listen(source)
                query=recg.recognize_google(audio)
                query=query.lower()
                return query
        except:
            speak('sorry some error occured while listening , please try again')
            return None
    
    def gonoobs(self):
        contact = None
        while(contact == None):
            speak('whom do you want to send the message? ')
            contact=self.input_speech()
        message = None
        while(message== None):
            speak('Please input message')
            message=self.input_speech()
        
        self.whatsapp(contact,message)
        
        
    
    def speak(self,text):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        newVoiceRate = 150
        engine.setProperty('rate',newVoiceRate)
        engine.say(text)
        engine.runAndWait()

    def whatsapp(self):
        url='https://web.whatsapp.com'
        self.speak('opening whatsapp.....please scan the q.r. code from your smartphone if not already logged in')
        webbrowser.get('chrome').open_new_tab(url)
        sleep(0.5)
        while pyautogui.locateOnScreen('search_dark1.png')==None and pyautogui.locateOnScreen('search_light.png')==None: 
            continue
        
        sleep(2)
        pyautogui.hotkey('tab')
        sleep(2)
        pyautogui.typewrite(self.contact)
        sleep(3)
        pyautogui.hotkey('down')
        sleep(1)
       
        if pyautogui.locateOnScreen('chats.png')!=None and pyautogui.locateOnScreen('chats_light.png')!=None:
            pyautogui.hotkey('alt', 'tab', interval=0.15)
            #print('Chat/Contact not found. Please try again.')
            self.speak('Contact not found. Please try again.')
            pyautogui.hotkey('ctrl', 'f4', interval=0.15) 
            pyautogui.hotkey('alt', 'tab', interval=0.15)
        else:
            pyautogui.hotkey('enter')
            sleep(2)
            pyautogui.typewrite(self.message)
            sleep(1)
            pyautogui.hotkey('enter')
            self.speak('Message sent!')
            pyautogui.hotkey('ctrl', 'f4', interval=0.15) 
            pyautogui.hotkey('alt', 'tab', interval=0.15)
            
class Instagram():
    
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

    def input_speech(self):
        try:
            recg=spr.Recognizer()
            with spr.Microphone() as source:
                recg.adjust_for_ambient_noise(source,duration=0.5)
                audio=recg.listen(source)
                query=recg.recognize_google(audio)
                query=query.lower()
                return query
        except:
            speak('sorry some error occured while listening , please try again')
            return None
    
    def gonoobs(self):
        contact = None
        while(contact == None):
            speak('whom do you want to send the message? ')
            contact=self.input_speech()
        message = None
        while(message== None):
            speak('Please input message')
            message=self.input_speech()
        
        self.instagram(contact,message)

    def speak(self,text):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        newVoiceRate = 150
        engine.setProperty('rate',newVoiceRate)
        engine.say(text)
        engine.runAndWait()
        
    def instagram(self):
        url='https://www.instagram.com/direct/inbox/'
        self.speak('opening Instagram.....please login with your credentials if not already logged in. The program will wait for you to log in.')
        webbrowser.get('chrome').open_new_tab(url)
        sleep(0.5)
       
       
        while pyautogui.locateOnScreen('msg_button.png')==None:
            continue
       
        sleep(3)

        loc=pyautogui.locateOnScreen('msg_button.png')
        pyautogui.click(loc, button='left')
        sleep(2)
        
        pyautogui.typewrite(self.contact)
        sleep(3)
        pyautogui.hotkey('tab')
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.moveTo(pyautogui.locateOnScreen('Capture.png'))
        pyautogui.move(0, 14)
        pyautogui.click()
        sleep(2)    
        pyautogui.typewrite(self.message)
        sleep(1)
        pyautogui.hotkey('enter')
        #print('Message Sent!')
        self.speak('Message sent!')
        pyautogui.hotkey('ctrl', 'f4', interval=0.15) 
        pyautogui.hotkey('alt', 'tab', interval=0.15)
    
class Facebook():
    
    
    chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

    def input_speech(self):
        try:
            recg=spr.Recognizer()
            with spr.Microphone() as source:
                recg.adjust_for_ambient_noise(source,duration=0.5)
                audio=recg.listen(source)
                query=recg.recognize_google(audio)
                query=query.lower()
                return query
        except:
            speak('sorry some error occured while listening , please try again')
            return None
    
    def gonoobs(self):
        contact = None
        while(contact == None):
            speak('whom do you want to send the message? ')
            contact=self.input_speech()
        message = None
        while(message== None):
            speak('Please input message')
            message=self.input_speech()
        
        self.facebook(contact,message)
      

    def speak(self,text):
        
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        newVoiceRate = 150
        engine.setProperty('rate',newVoiceRate)
        engine.say(text)
        engine.runAndWait()

    def facebook(self):
        url='https://www.facebook.com/messages'
        self.speak('opening Facebook.....please login with your credentials if not already logged in. The program will wait for you to log in.')
        webbrowser.get('chrome').open_new_tab(url)
        sleep(0.5)
        while pyautogui.locateOnScreen('facebook_dark.png')==None and pyautogui.locateOnScreen('facebook_light.png')==None: 
            continue
        sleep(1)

        loc=pyautogui.locateOnScreen('fbsearch_dark.png') or pyautogui.locateOnScreen('fbsearch_light.png')
        pyautogui.click(loc, button='left')
        sleep(2)
        pyautogui.typewrite(self.contact)
        sleep(3)
        '''
        loc2=pyautogui.locateOnScreen('contacts_light.png') or pyautogui.locateOnScreen('contacts_dark.png')
        if(loc2== None):
            print('Contact not found. Please try again.')
            self.speak('Contact not found. Please try again!')
            pyautogui.hotkey('alt', 'tab', interval=0.15)
        else:
            pyautogui.hotkey('down')
            sleep(1)
            pyautogui.hotkey('enter')
            sleep(1)
            loc3=pyautogui.locateOnScreen('message_light.png') or pyautogui.locateOnScreen('message_dark.png')
            pyautogui.click(loc3, button='left')
            sleep(1)
            pyautogui.typewrite(message)
            sleep(1)
            pyautogui.hotkey('enter')
        
        '''
        pyautogui.hotkey('down')
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(1)
        loc3=pyautogui.locateOnScreen('message_light.png') or pyautogui.locateOnScreen('message_dark.png')
        pyautogui.click(loc3, button='left')
        sleep(1)
        pyautogui.typewrite(self.message)
        sleep(1)
        pyautogui.hotkey('enter')
        #print('Message Sent!')
        self.speak('Message sent!')
        pyautogui.hotkey('ctrl', 'f4', interval=0.15) 
        pyautogui.hotkey('alt', 'tab', interval=0.15)

def speak(text):
    # gui_obj.widg_obj.BotM(text)
    assistant.say(text)
    assistant.runAndWait()
    

def wish(master):
    hour=int(datetime.datetime.now().hour)

    if hour>4 and hour <12:
        #print('Good Morning!'+master)
        gui_obj.widg_obj.BotM('Good Morning!'+master)
        speak('Good Morning!'+master)
    elif hour>=12 and hour<18:
        gui_obj.widg_obj.BotM('Good Afternoon!'+master)
        speak('Good Afternoon!'+master)
    else:
        gui_obj.widg_obj.BotM('Good Evening!'+master)
        speak('Good Evening!'+master)
    gui_obj.widg_obj.BotM('How may I help you?')
    speak('How may I help you?')

def isProcessRunning():
    f = wmi.WMI()
    for process in f.Win32_Process():
        if 'pythonw' in process.Name.lower():
            return True
    return False

def start_process():
    if not isProcessRunning():
        os.system('pythonw \"C:\\Users\\shash\\Desktop\\python project\\final\\runme.pyw\"')

def kill_process():
    os.system('taskkill /F /IM pythonw.exe /T')

def run_assistant():

    # a.run()
    # c = db.cursor()
    #input
    speak('i am listening')
    #query=input('command: ')#command,Object,attributecount
    query=''#default
    try:
        recg=spr.Recognizer()
        with spr.Microphone() as source:
            recg.adjust_for_ambient_noise(source,duration=0.2)
            audio=recg.listen(source)
            query=recg.recognize_google(audio)
            query=query.lower()
        #print('\''+query+'\'')
    except:
        gui_obj.widg_obj.BotM('sorry some error occured while listening , please try again')
        speak('sorry some error occured while listening , please try again')
        return
    run_assistant_txt(query)
    return query

def run_assistant_txt(query):
    c = db.cursor()
    c.execute('select * from commandtofunction where \''+query+'\' like command;')
    try:
        cmd,o,cnt=c.fetchone()
    except:
        gui_obj.widg_obj.BotM('please try again')
        speak('please try again')
        return
    o=eval(o)
    cmd=cmd.replace('%','(.*)')
    try:
        attributes=list(re.match(cmd,query).groups())
    except:
        gui_obj.widg_obj.BotM('sorry cannot find command')
        speak('sorry cannot find command')
        return
    #print(cnt,len(attributes))
    if cnt==0:
        o.gonoobs()
        return
    if cnt==len(attributes):
        exec='o.gonoobs(\''+attributes[0]+'\''
        for i in range(1,len(attributes)):
            exec=exec+',\''+attributes[i]+'\''
        exec+=')'
        eval(exec)
    else:
        gui_obj.widg_obj.BotM('sorry cannot find command')
        speak('sorry cannot find command')


gui_obj=ChattApp()
# gui_obj.create_widg()
widge_obj=Chattwidget()
gui_obj.create_widg(widge_obj)

if __name__ == '__main__':
    assistant=pyttsx3.init()
    endprocess = False
    #start_process()
    #if start_process() is directly called then program has to wait until it finishes
    #execution which will take infinite time
    thread = threading.Thread(target = start_process,daemon=True)
    thread.start()
    try:
        db = sqlite3.connect('data.db')
        gui_obj.assign(db)
        # wish(getpass.getuser())
        gui_obj.run()
        # print(dir(MDGridLayout))
        # run_assistant()
    except Exception as e:
        gui_obj.widg_obj.BotM('an error occured')
        speak('an error occured')
        print(e)
