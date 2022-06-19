import time
import requests
import webbrowser
import sys as n
import random
import webbrowser
import threading

#=======
rhaby2 = int(4)#عدد الحرف ليوزر اذا تريد سوي خماسي خلي رقم 5
#========
rhaby = int(1)
ruksI='IdMN1w9spls'
rg = 'A'
#@DIBIBl
ruks_ = '\033[1;36m'
ruks__ = '\033[1;36m'
jruks = '\033[1;37m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'

N =55
R =('━'*1)
print(f"""{BGreen}{R}

.______       __    __   __  ___      _______.
|   _  \     |  |  |  | |  |/  /     /       |
|  |_)  |    |  |  |  | |  '  /     |   (----`
|      /     |  |  |  | |    <       \   \    
|  |\  \----.|  `--'  | |  .  \  .----)   |   
| _| `._____| \______/  |__|\__\ |_______/    
                                              
{R}
""")
rukS = ("5378572084:AAHlmVF7r4qppRHnDcUc1C7pWk9u3EWiMyE")
Ruks = -1001739884932
print(R)
def ruks():
	global N
	global rukS
	global Ruks
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(2)))
		    email =  str("".join(random.choice(tuks1)for i in range(1)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] Available'+BGreen+f' [{user}]') 
		        	RUKS3= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=━━━━━━━━━━━━\n✥. 𖣨.user : @{user} \n━━━━━━━━━━━━ '
		        	req = ruKs.post(RUKS3)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] Unavailable'+BRed+f'-[{user}]')
	except:
		print(' 𝐓𝐞𝐥𝐞 :@vvvvvnm9 ☆ @vvvvvnm9')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
	
	
	
	
	