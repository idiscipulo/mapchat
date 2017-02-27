import email
from email.mime.text import MIMEText
import smtplib

def ParseMessage(message):
	#check carrier
	if str(message['From']).find('att') != -1 :
		for part in message.walk():
			#get message content
			if part.get_content_type() == 'text/html':
				num = 20
				printString = ""
				content = part.get_payload().split()
				while content[num] != "</td>":
					#concat the contents into one string
					printString = printString + content[num]
					num = num + 1
				return(printString)		
	elif str(message['From']).find('vtext') != -1:
		for part in message.walk():
			num = 0;
			printString = ""
			content = part.get_payload().split()
			for i in range(0, len(content)):
				printString = printString + content[i]
			return(printString)
