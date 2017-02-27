import imaplib
import email
from parsemessage import ParseMessage
from intermap import InterMap
from respond import Respond

#link to mail account
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('YOUR EMAIL', 'YOUR PASSWORD')
mail.list()

while True:
	#open inbox
	mail.select("inbox")

	#take all unread messages
	result, data = mail.search(None, "UNSEEN")

	#if there are undread messages...
	if data != [b'']:

		#parse the first message to string
		ids = data[0]
		id_list = ids.split()
		latest_email_id = id_list[-1]
		result, data = mail.fetch(latest_email_id, "(RFC822)")
		raw_email = data[0][1]
		raw_email = raw_email.decode('utf-8')
		message = email.message_from_string(raw_email)

		#try:
			#get message content
		request = ParseMessage(message)

			#respond to message content
		response = InterMap(message['From'], request)

			#message back
		Respond(message['From'], response)

			#message is marked as read by default
		#except (TypeError, IndexError, Exception):
			#print('Parse Error')
