import smtplib

def Respond(snd, text):
	#send reply
	mc = 'YOUR EMAIL'

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	server.login(mc, 'YOUR PASSWORD')

	print(text)

	try:
		server.sendmail(mc, snd, text)
	except (TypeError, IndexError, Exception):
		server.sendmail(mc, snd, 'I am sorry, there seems to be an issue processing your request. Enter \"List\" to view available functions.')
