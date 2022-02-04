from datetime import datetime
import pyautogui as pa
import requests
import time
import sys

def AutoAccept():
    i=0
    while True:
        coordinates1=pa.locateCenterOnScreen('lol-accept.png')
        coordinates2=pa.locateCenterOnScreen('cs-accept.png')
        if coordinates1!=None:
            pa.moveTo(coordinates1.x, coordinates1.y)
            pa.click(coordinates1.x, coordinates1.y)
            print('Game Automaticly Accepted')
            return 'League of Legends'

        elif coordinates2!=None:
            pa.moveTo(coordinates2.x, coordinates2.y)
            pa.click(coordinates2.x, coordinates2.y)
            print('Game Automaticly Accepted')
            return 'Counter-Strike Global Offensive'

        elif coordinates1==None and coordinates2==None:
            if i%4==0:
                info='Running - no match |'
            elif i%4==1:
                info='Running - no match /'
            elif i%4==2:
                info='Running - no match -'
            elif i%4==3:
                info='Running - no match \\'

            
            sys.stdout.write('%s\r' % info)
            sys.stdout.flush()
            i += 1
            time.sleep(0.5)   


def Discord_bot_push():
    
    url='<CHANNEL ID>'

    payload = {
        'content' : 'Game has been accepted automatically      '+ f'            game id:  {game_id} '+ '                                                        action id: '+ str(datetime.now())
    }
       
    header = {
        'authorization' : '<BOT DISCORD ACCOUNT AUTHORIZATION ID>'
    }

    r=requests.post(url, data=payload, headers=header)


game_id = AutoAccept()
Discord_bot_push()