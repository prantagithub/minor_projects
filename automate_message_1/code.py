AUTH_KEY="iqzp56DvLeUF142StnwCojsVJlAcPOkmQbKBxIyR9hXg3rYud0QiSDIJlwyYnbfR1r7hUXOLF3sj0N2t"
#----------------------------------------------------------------------------------------------------------------------------------------------
import time
import os
import requests
import ntplib
from datetime import datetime
def send():

	global AUTH_KEY
	url="https://www.fast2sms.com/dev/bulkV2"
	numbers=["6009907163"]
	payload="sender_id=TXTIND&message_text=Hi,this%20is%20cool&language=english&route=v3&flash=0&&numbers="
	for a in numbers:
		payload+=a

	headers={
		'authorization': AUTH_KEY,
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control':"no-cache",
	}
	response=requests.request("POST",url,data=payload,headers=headers)

if __name__=="__main__":
	now=datetime.now()
	curtime=now.strftime("%H:%M:%S")
	send()
	if curtime=="22:00:00":
		send()

