import time
import pyttsx3
import datetime
import sqlite3
from plyer import notification


def check_reminder():
    date_time_now = datetime.datetime.now()
    c.execute('select datetime from ReminderData')
    #print(c.fetchall())
    all_reminder_dates = c.fetchall()
    if all_reminder_dates==None:
        return
    for str_reminder_date in all_reminder_dates:
        #reminder_date=eval(reminder_date[0])
        reminder_date = datetime.datetime.strptime(str_reminder_date[0],'%Y-%m-%d %H:%M:%S')
        if (date_time_now >= reminder_date):
            c.execute('select * from ReminderData where datetime = \''+str_reminder_date[0]+'\'')
            reminders = c.fetchall()
            for reminder in reminders:
                remind(reminder)
            #Deleting the reminder
            c.execute('delete from ReminderData where datetime = ?',(str_reminder_date[0],))
            db.commit()




    #remind(c.fetchall())

def remind(reminder):
    title = reminder[0]
    notification.notify(
        title='GoNoobs Virtual Assistant',
        message='Your reminder for '+title,
        app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
        timeout=30,  # seconds
    )
    assistant.say('your reminder for '+ title )

    assistant.runAndWait()

if __name__=='__main__':
    assistant = pyttsx3.init()
    db = sqlite3.connect('rdata.db')
    c = db.cursor()
    while True:
        check_reminder()
        time.sleep(1)
