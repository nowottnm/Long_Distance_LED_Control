import imaplib
import email
import sys
from email.message import EmailMessage
from smtplib import SMTP_SSL, SMTP_SSL_PORT

account = sys.argv[1]
pw = sys.argv[2]

# connect inbox
imap_server = imaplib.IMAP4_SSL(host='posteo.de')
imap_server.login(account, pw)
imap_server.select() # default inbox
_, message_numbers_raw = imap_server.search(None, 'ALL')
for  message_number in message_numbers_raw[0].split():
	_,msg = imap_server.fetch(message_number, '(RFC822)')
	message = email.message_from_bytes(msg[0][1])
	content = message.get_payload()
	print(content)
	import pdb; pdb.set_trace()
	
from_email = 'christmas2020@posteo.de'
to_email = from_email
email_message = EmailMessage()
email_message.add_header('To', to_email)
email_message.add_header('From', from_email)
body="0.1 0.1 0.1"
email_message.add_header('Subject','rgb')
email_message.add_header('X-Priority', '1')
email_message.set_content('0.1 0.1 0.2')



smtp_server = SMTP_SSL('posteo.de', port = SMTP_SSL_PORT)
smtp_server.set_debuglevel(1)
smtp_server.login(account, pw)
smtp_server.sendmail(from_email, to_email, email_message.as_bytes())
