import imaplib
import email
import sys

# connect inbox
imap_server = imaplib.IMAP4_SSL(host='posteo.de')
imap_server.login(sys.argv[1], sys.argv[2])
imap_server.select() # default inbox
_, message_numbers_raw = imap_server.search(None, 'ALL')
for  message_number in message_numbers_raw[0].split():
	_,msg = imap_server.fetch(message_number, '(RFC822)')
	import pdb; pdb.set_trace()s
	message = email.message_from_bytes(msg[0][1])
	content = message.get_payload
	print(content)
	import pdb; pdb.set_trace()
