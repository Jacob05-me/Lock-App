import pyautogui
import time
import json
import ctypes
import PySimpleGUI as sg
import playsound

# abs() ABSOLUTE VALUE

VersionNum = '0.2'
DefaultChekBoxFinLock = False
DefaultChekBoxDayPromt = False
DefaultChekBoxConstTop = True
DefaultChekBoxPresSpce = False  
DefaultChekBoxShowProgs = False
DefaultChekBoxTimeStop = True
X, Y = 960, 540
SetFinLock = False
SetDayPromt = False
SetConstTop = True
PresSpce = False
Days = 0
Hours = 0
Minutes = 0
Seconds = 0

Alarm1 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm1.mp3'
Alarm2 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm2.mp3'
Alarm3 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm3.mp3'
Ringtone1 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone1.mp3'
Ringtone2 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone2.mp3'
Ringtone3 = 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone3.mp3'
AlarmUsed = Alarm1
RingtoneUsed = Ringtone1

data = {}
data['ALARMDICT'] = []
data['ALARMDICT'].append({
    'Alarm1' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm1.mp3',
    'Alarm2' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm2.mp3',
    'Alarm3' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm3.mp3',
    'Alarm4' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm4.mp3',
    'UserAlarm' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Alarm1.mp3',
    'Ringtone1' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone1.mp3',
    'Ringtone2' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone2.mp3',
    'Ringtone3' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone3.mp3',
    'Ringtone4' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone4.mp3',
    'UserRingtone' : 'C:/Users/jacob/OneDrive/Desktop/Sublime Text Build 3211 updated/pyhton/LockAPP/Sounds/Ringtone1.mp3'
    })

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# with open('data.json') as json_file:
#     data = json.load(json_file)
#     for A in data['ALARMDICT']:
#         print('Alarm1: ' + A['Alarm1']), playsound.playsound(A['Alarm1'])
#         print('Alarm2: ' + A['Alarm2']), playsound.playsound(A['Alarm2'])
#         print('Alarm3: ' + A['Alarm3']), playsound.playsound(A['Alarm3'])
#         print('Alarm4: ' + A['Alarm4']), playsound.playsound(A['Alarm4'])
#         print('UserAlarm: ' + A['UserAlarm']), playsound.playsound(A['UserAlarm'])
#         print('Ringtone1: ' + A['Ringtone1']), playsound.playsound(A['Ringtone1'])
#         print('Ringtone2: ' + A['Ringtone2']), playsound.playsound(A['Ringtone2'])
#         print('Ringtone3: ' + A['Ringtone3']), playsound.playsound(A['Ringtone3'])
#         print('Ringtone4: ' + A['Ringtone4']), playsound.playsound(A['Ringtone4'])
#         print('UserRingtone: ' + A['UserRingtone']), playsound.playsound(A['UserRingtone'])

def ProgressPage(Days, Hours, Minutes, Secconds, Time_Hour, Time_Minute):
    # Logic
    if (Time_Hour) != 0:
        Time_Now_H = time.strftime('%H')
        Time_Now_M = time.strftime('%M')
        try:
            Time_Till_H = Hours - Time_Now_H
            Time_Till_M = Minutes - Time_Now_M
            Hours = Time_Till_H
            Minutes = Time_Till_M
        except:
            pyautogui.alert(text='ERROR AT LINE 264 \nINVALAD COMPUTE AT: Sleep', title='COMPUTE ERROR', button='OK')
            print('ERROR AT LINE 39 \nINVALAD COMPUTE AT: Sleep')
            time.sleep(10)
            exit()
        try:
            Hours = int(Hours) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: "Hours"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: "Hours"')
            time.sleep(10)
            exit()
            pass
        try:
            Hours = int(Hours) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 243 \nINVALAD INPUT STRING AT: "Hours"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 18 \nINVALAD INPUT STRING AT: "Hours"')
            time.sleep(10)
            exit()
        try:
            Minutes = int(Minutes) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 250 \nINVALAD INPUT STRING AT: "Minutes"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 25 \nINVALAD INPUT STRING AT: "Minutes"')
            time.sleep(10)
            # exit()
        try:
            Sleep = int(Hours) + int(Minutes)
        except:
            pyautogui.alert(text='ERROR AT LINE 264 \nINVALAD COMPUTE AT: Sleep', title='COMPUTE ERROR', button='OK')
            print('ERROR AT LINE 39 \nINVALAD COMPUTE AT: Sleep')
            time.sleep(10)
            exit()
        try:
            while Sleep != 0:
                Sleep = Sleep - 1
                print(Sleep + 1)
                time.sleep(1)
            # time.sleep(int(Sleep))
        except:
            pyautogui.alert(text='ERROR AT LINE 26 \nERROR AT "SLEEP" WHILE LOOP', title='LOOP ERROR', button='OK')
            print('ERROR AT LINE 26 \nERROR AT SLEEP WHILE LOOP')
            time.sleep(10)
            exit()
    else:
        try:
            Days = int(Days) * 12
        except:
            pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: "Days"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: "Days"')
            time.sleep(10)
            exit()
            pass
        try:
            Days = int(Days) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: "Days"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: "Days"')
            time.sleep(10)
            exit()
            pass
        try:
            Days = int(Days) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: "Days"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: "Days"')
            time.sleep(10)
            exit()
            pass
        try:
            Hours = int(Hours) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: "Hours"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: "Hours"')
            time.sleep(10)
            exit()
            pass
        try:
            Hours = int(Hours) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 243 \nINVALAD INPUT STRING AT: "Hours"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 18 \nINVALAD INPUT STRING AT: "Hours"')
            time.sleep(10)
            exit()
        try:
            Minutes = int(Minutes) * 60
        except:
            pyautogui.alert(text='ERROR AT LINE 250 \nINVALAD INPUT STRING AT: "Minutes"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 25 \nINVALAD INPUT STRING AT: "Minutes"')
            time.sleep(10)
            # exit()
        try:
            Seconds = Seconds
        except:
            pyautogui.alert(text='ERROR AT LINE 257 \nINVALAD INPUT STRING AT: "Seconds"', title='INPUT ERROR', button='OK')
            print('ERROR AT LINE 32 \nINVALAD INPUT STRING AT: "Seconds"')
            time.sleep(10)
            exit()
        try:
            Sleep = int(Hours) + int(Minutes) + int(Seconds)
        except:
            pyautogui.alert(text='ERROR AT LINE 264 \nINVALAD COMPUTE AT: Sleep', title='COMPUTE ERROR', button='OK')
            print('ERROR AT LINE 39 \nINVALAD COMPUTE AT: Sleep')
            time.sleep(10)
            exit()
        try:
            if Sleep == 4255:
                exit()
        except:
            exit()
    try:
        while Sleep != 0:
            Sleep = Sleep - 1
            print(Sleep + 1)
            time.sleep(1)
        # time.sleep(int(Sleep))
    except:
        pyautogui.alert(text='ERROR AT LINE 26 \nERROR AT "SLEEP" WHILE LOOP', title='LOOP ERROR', button='OK')
        print('ERROR AT LINE 26 \nERROR AT SLEEP WHILE LOOP')
        time.sleep(10)
        exit()
    #---------------------------------------------------------------------------------------------------------------
    Progss_Layout = [
            [sg.ProgressBar(Sleep, orientation='h', size=(20, 20), key='progressbar')],
            [sg.Cancel()]
    ]
    Window_Progss = sg.Window('Progress', Progss_Layout, keep_on_top=True, location = (X, Y), finalize=True)
    progress_bar = Window_Progss['progressbar']
    for i in range(Sleep):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = Window_Progss.read(timeout=10)
        if event == 'Cancel'  or event == sg.WIN_CLOSED:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i + 1)

def playsoundss(sound):
    with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
                for A in data['ALARMDICT']:
                    playsound.playsound(A[sound])

def AlarmSelect():
    global X, Y
    layoutAlarmSelect = [
        [sg.Radio('Alarm1', 'AlarmRadio'), sg.Button('Play Alarm1', key='PlayAlarm1')],
        [sg.Radio('Alarm2', 'AlarmRadio'), sg.Button('Play Alarm2', key='PlayAlarm2')],
        [sg.Radio('Alarm3', 'AlarmRadio'), sg.Button('Play Alarm3', key='PlayAlarm3')],
        [sg.Radio('Alarm4', 'AlarmRadio'), sg.Button('Play Alarm4', key='PlayAlarm4')],
    ]
    Window_Alarm_select = sg.Window('Select Alarm', layoutAlarmSelect, keep_on_top=True, location = (X, Y), finalize=True)
    while True:
        # DONT REMOVE!!!!!
        # IT BREAKS
        event, values = Window_Alarm_select.read()
        print(Window_Alarm_select.CurrentLocation())
        if event in (None, 'PlayAlarm1'):
            playsoundss('Alarm1')

def D_H_M_S_SLIDER():
    global DefaultChekBoxFinLock
    global DefaultChekBoxDayPromt
    global DefaultChekBoxConstTop
    global DefaultChekBoxTimeStop
    global X, Y
    global SetConstTop
    global SetDayPromt
    global SetFinLock
    global Days
    global Hours
    global Minutes
    global Seconds

    if DefaultChekBoxTimeStop == True:
        TimeStop_Layout = [
            [sg.Frame('Time Stop',[
                [sg.Text(text='Hours'), sg.Text(text='Minutes')],
                [sg.Spin([i for i in range(0,25)], initial_value=1, tooltip='Lock at Time (Hour) (0 to ignore)', key='Time_Hour'), sg.Text(text='  '), sg.Spin([i for i in range(0, 61)], initial_value=0, tooltip='Lock at Time (Minutes)', key='Time_Minute')]])
                ]
        ]

    if SetDayPromt == True:
        Day_layout = [
            [sg.Frame('Days', [[sg.Slider(range=(0, 364), orientation='h', size=(20, 10), default_value=Days, key='SlideDays')]])]
        ]
    else:
        Day_layout = []

    # Slider_Col_1 = [
    #     Day_layout,
    #     [sg.Frame('Hours', [[sg.Slider(range=(0, 24), orientation='h', size=(20, 10), default_value=Hours, key='SlideHours')]])],
    #     [sg.Frame('Minutes', [[sg.Slider(range=(0, 60), orientation='h', size=(20, 10), default_value=Minutes, key='SlideMinutes')]])],
    #     [sg.Frame('Secconds', [[sg.Slider(range=(0, 60), orientation='h', size=(20, 10), default_value=Seconds, key='SlideSecconds')]])],
    #     [sg.Button('Done', key='DONE_BTN'), sg.Button('Cancel', key='CANCEL_BTN')]
    # ]

    Slider_layout = [
        [sg.T('Set the time until lock:', justification='center', font=("Helvetica", 15))],
        [sg.T('_' * 28)],
        # sg.Column(Slider_Col_1),
        [Day_layout],
        [sg.Frame('Hours', [[sg.Slider(range=(0, 24), orientation='h', size=(20, 10), default_value=Hours, key='SlideHours')]])],
        [sg.Frame('Minutes', [[sg.Slider(range=(0, 60), orientation='h', size=(20, 10), default_value=Minutes, key='SlideMinutes')]])],
        [sg.Frame('Secconds', [[sg.Slider(range=(0, 60), orientation='h', size=(20, 10), default_value=Seconds, key='SlideSecconds')]])],
        [sg.Button('Done', key='DONE_BTN'), sg.Button('Cancel', key='CANCEL_BTN')],
        [TimeStop_Layout]
    ]
    
    Window_Slider = sg.Window('Sliders', Slider_layout, keep_on_top=True, location = (X, Y), finalize=True)

    while True:
        event, values = Window_Slider.read()
        print(Window_Slider.CurrentLocation())

        if event in (Window_Slider, ''):
            pass
        if event == sg.WIN_CLOSED or event == 'Exit':
            exit()
        if event in (Window_Slider, 'DONE_BTN'):
            print('DONE_BTN is Pressed')
            try:
                Days = values['SlideDays']
            except:
                Days = 0
                pass
            try:
                Time_Hour = values['Time_Hour']
                Time_Minute = values['Time_Minute']
            except:
                Time_Hour = 0
                Time_Minute = 0
            Hours = values['SlideHours']
            Minutes = values['SlideMinutes']
            Seconds = values['SlideSecconds']
            print(str(Days) + ', ' + str(Hours) + ', ' + str(Minutes) + ', ' + str(Seconds) + ' | ' + str(Time_Hour) + ':' + str(Time_Minute))
            ProgressPage(Days, Hours, Minutes, Seconds, Time_Hour, Time_Minute)
            break
  
        if event in (None, 'CANCEL_BTN'):	# if user closes window or clicks cancel
            ExitPopup = sg.Window('Exit', [[sg.T('Are you sure you want to exit?')], [sg.Button('Yes', key='YES_BTN'), sg.Button('No', key='NO_BTN')]], keep_on_top=True, finalize=True)
            while True:
                event, values = ExitPopup.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    ExitPopup.close()
                    break
                if event in (ExitPopup, 'YES_BTN'):
                    ExitPopup.close()
                    Window_Slider.close()
                    exit()
                if event in (ExitPopup, 'NO_BTN'):
                    ExitPopup.close()
                    break
    Window_Slider.close()

def FinLockChek():
    global X, Y
    if SetFinLock == True:
        print('Verify')
        layout_Verify = [
            [sg.T('Are you sure you want to lock?')],
            [sg.Button('Yes', key='YesVeriBtn'), sg.Button('No', key='NoVeriBtn')]
        ]
        window_Verify = sg.Window('Verify', layout_Verify, keep_on_top=True, location = (X, Y), finalize=True)
        while True:
            event, values = window_Verify.read()
            print(event, values)
            if event in (None, 'Cancel'):	# if user closes window or clicks cancel
                exit()
            if event == sg.WIN_CLOSED or event == 'Exit':
                exit()
            if event in (None, 'YesVeriBtn'):
                window_Verify.close()
                ctypes.windll.user32.LockWorkStation()
            if event in (None, 'NoVeriBtn'):
               break
                
        pass
    elif SetFinLock != True:
        ctypes.windll.user32.LockWorkStation() 
        pass

def PresSpceChek():
    global PresSpce
    if PresSpce == True:
        print('PRESS SPACE')
        pyautogui.press('Space')
    if PresSpce != True:
        pass

def Settings():
    global DefaultChekBoxFinLock
    global DefaultChekBoxDayPromt
    global DefaultChekBoxConstTop
    global DefaultChekBoxPresSpce
    global DefaultChekBoxShowProgs
    global DefaultChekBoxTimeStop
    global X, Y
    global SetConstTop
    global SetDayPromt
    global SetFinLock
    global Days
    global Hours
    global Minutes
    global Seconds
    global PresSpce

    Tab_General = [
        [sg.T('Always prompt on top:', tooltip='when prompts are displayed it will/will not be locked on top'), sg.Checkbox('', default=DefaultChekBoxConstTop, tooltip='When prompts are displayed it will/will not be locked on top', key='SetConstTop')],
        [sg.T('Do Final Lock Prompt:', tooltip='Prompts if you want to lock at end of the allotted time'), sg.Checkbox('', default=DefaultChekBoxFinLock, tooltip='Prompts if you want to lock at end of the allotted time', key='SetFinLock')],
        [sg.T('Ask for days:', tooltip='Prompts the "Days" until lock (like Hours, Minutes, and Secconds)'), sg.Checkbox('', default=DefaultChekBoxDayPromt, tooltip='Prompts the "Days" until lock (like Hours, Minutes, and Secconds)', key='SetDayPromt')],
        [sg.T('Press space bar once locked:', tooltip='When locked it will press the spce button to pause/play selected window'), sg.Checkbox('', default=DefaultChekBoxPresSpce, tooltip='When locked it will press the spce button to pause/play selected window', key='SetPresSpce')],
        [sg.T('Show a progress bar until lock:', tooltip='Will show the time untill the lock as a progress bar and in secconds'), sg.Checkbox('', default=DefaultChekBoxShowProgs, tooltip='Will show the time untill the lock as a progress bar and in secconds', key='SetShowProgs')],
        [sg.T('Time option avalible:', tooltip='Will allow the option to end at certin times.'), sg.Checkbox('', default=DefaultChekBoxTimeStop, tooltip='Will allow the option to end at certin times.', key='TimedStop')]
    ]
    Tab_About = [
        [sg.T('AutoLock Version ' + VersionNum)]
    ]
    Tab_Sounds = [
        [sg.Radio('Use your selected alarm', 'SoundRadio', default=True, size=(22,1), tooltip='MP3 files only', key='UseUserAlarmRadio')],
        [sg.Text('Alarm:', size=(11, 1), auto_size_text=False, justification='right', tooltip='MP3 files only'), sg.InputText('File Destination', tooltip='MP3 files only'), sg.FolderBrowse(tooltip='MP3 files only')],
        [sg.Radio('Use your selected ringtone', 'SoundRadio', default=False, size=(22,1), tooltip='MP3 files only', key='UseUserRingtoneRadio')],
        [sg.Text('Ringtone:', size=(11, 1), auto_size_text=False, justification='right', tooltip='MP3 files only'), sg.InputText('File Destination', tooltip='MP3 files only', key='UserRingtoneInput'), sg.FolderBrowse(tooltip='MP3 files only', key='UserRingtoneBrouse')],
        [sg.Radio('Use preset alarms', 'SoundRadio', default=True, size=(22,1), key='UseAplicationAlarmRadio'), sg.Button('Select Alarm', key='SelectAlarmBtn')],
        [sg.Radio('Use preset ringtones', 'SoundRadio', default=False, size=(22,1), key='UseAplicationRingtoneRadio'), sg.Button('Select Ringtone', key='SelectRingtoneBtn')]
    ]
    layout_Settings = [  
        [sg.Text('Settings', font=("Helvetica", 20))],
        [sg.TabGroup([[sg.Tab('General', Tab_General, key='TabGeneral'), sg.Tab('About', Tab_About, key='Tab_About'), sg.Tab('Sounds', Tab_Sounds, key='Tab_Sounds')]], key='TabOpen')],
        [sg.Text('_' * 67)],
        [sg.Button('Ok'), sg.Button('Apply'), sg.Button('Cancel')]
    ]

    # Create the Window
    window_Settings = sg.Window('Settings', layout_Settings, keep_on_top=True, location = (X, Y), finalize=True)    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window_Settings.read()
        print(event, values)
        print(window_Settings.CurrentLocation())

        if event in (None, 'Cancel'):	# if user closes window or clicks cancel
            exit()
        if values['TimedStop'] == True:
            DefaultChekBoxTimeStop = True
            print('TimedStop is True')
        if values['SetFinLock'] == True:
            SetFinLock = True
            DefaultChekBoxFinLock = True
            print('SetFinLock is True')
        if values['SetDayPromt'] == True:
            SetDayPromt = True
            DefaultChekBoxDayPromt = True
            print('SetDayPromt is True')
        if values['SetConstTop'] == True:
            SetConstTop = True
            DefaultChekBoxConstTop = True
            print('SetConstTop is True')
        if values['SetPresSpce'] == True:
            PresSpce = True
            DefaultChekBoxPresSpce = True
            print('SetPresSpce is True')
        if values['SetShowProgs'] == True:
            DefaultChekBoxShowProgs = True
            print('SetShowProgs is True')
        if values['SetFinLock'] == False:
            DefaultChekBoxFinLock = False
            print('SetFinLock is False')
        if values['SetDayPromt'] == False:
            DefaultChekBoxDayPromt = False
            print('SetDayPromt is False')
        if values['SetConstTop'] == False:
            DefaultChekBoxConstTop = False
            print('SetConstTop is False')
        if values['SetPresSpce'] == False:
            PresSpce = False
            DefaultChekBoxPresSpce = False
            print('SetPresSpce is False')
        if values['TimedStop'] == False:
            DefaultChekBoxTimeStop = False
            print('TimedStop is False')
        if values['SetShowProgs'] == False:
            DefaultChekBoxShowProgs = False
            print('SetShowProgs is False')
        if event in (None, 'Ok'):
            Reload = False
            print('You entered Ok')
            break
        if event in (None, 'settings'):
            print('You entered Settings')
        if event in (None, 'SelectAlarmBtn'):
            print('SelectAlarmBtn pressed')
            AlarmSelect()
        if event in (None, 'SelectRingtoneBtn'):
            print('SelectRingtoneBtn pressed')
            # RingtoneSelect()
        if event == sg.WIN_CLOSED or event == 'Exit':
            exit()
        if event in (None, 'Apply'):
            print('Reload Pg')
            Reload = True
            break
    if Reload == True:
        X, Y = window_Settings.CurrentLocation()
        print('Position:' + str(X) + ' | ' + str(Y))
        window_Settings.close()
        Settings()
    elif Reload == False:
        window_Settings.close()
        D_H_M_S_SLIDER()
        pass

def lock():
    global DefaultChekBoxFinLock
    global DefaultChekBoxDayPromt
    global DefaultChekBoxConstTop
    global X, Y
    global SetConstTop
    global SetDayPromt
    global SetFinLock
    global Days
    global Hours
    global Minutes
    global Seconds

    # Sleep = 7200  2 hours
    # Enter settings.
    Settings()
    # ------------------------------
    # try:
    #     Hours = int(Hours) * 60
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 235 \nINVALAD INPUT STRING AT: Hours', title='INPUT ERROR', button='OK')
    #     print('ERROR AT LINE 10 \nINVALAD INPUT STRING AT: Hours')
    #     time.sleep(10)
    #     exit()
    #     pass
    # try:
    #     Hours = int(Hours) * 60
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 243 \nINVALAD INPUT STRING AT: Hours', title='INPUT ERROR', button='OK')
    #     print('ERROR AT LINE 18 \nINVALAD INPUT STRING AT: Hours')
    #     time.sleep(10)
    #     exit()
    # try:
    #     Minutes = int(Minutes) * 60
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 250 \nINVALAD INPUT STRING AT: Minutes', title='INPUT ERROR', button='OK')
    #     print('ERROR AT LINE 25 \nINVALAD INPUT STRING AT: Minutes')
    #     time.sleep(10)
    #     # exit()
    # try:
    #     Seconds = Seconds
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 257 \nINVALAD INPUT STRING AT: Seconds', title='INPUT ERROR', button='OK')
    #     print('ERROR AT LINE 32 \nINVALAD INPUT STRING AT: Seconds')
    #     time.sleep(10)
    #     exit()
    # try:
    #     Sleep = int(Hours) + int(Minutes) + int(Seconds)
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 264 \nINVALAD COMPUTE AT: Sleep', title='COMPUTE ERROR', button='OK')
    #     print('ERROR AT LINE 39 \nINVALAD COMPUTE AT: Sleep')
    #     time.sleep(10)
    #     exit()
    # try:
    #     if Sleep == 4255:
    #         exit()
    # except:
    #     exit()
    # try:

    #     while Sleep != 0:
    #         Sleep = Sleep - 1
    #         print(Sleep + 1)
    #         time.sleep(1)
    #     # time.sleep(int(Sleep))
    # except:
    #     pyautogui.alert(text='ERROR AT LINE 26 \nERROR AT "SLEEP" WHILE LOOP', title='LOOP ERROR', button='OK')
    #     print('ERROR AT LINE 26 \nERROR AT SLEEP WHILE LOOP')
    #     time.sleep(10)
    #     exit()
    # Loading_bar.loading_text_bar(10, W, '#', 'Locking your PC', 1, 10, 'F', 'T')
    print('Done')
    # conferm = pyautogui.confirm(text='Do you want to lock?', title='Lock or Naw', buttons=['Yes', 'No'])

    PresSpceChek()
    FinLockChek() 
    



if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )  
    lock()