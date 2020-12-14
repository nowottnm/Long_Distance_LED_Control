from abc import ABC, abstractmethod
import imaplib
import email
import sys
from email.message import EmailMessage
from smtplib import SMTP_SSL, SMTP_SSL_PORT


class MessageInterface(ABC):
    """ template for rgb_update, rgb info pull inteface """

    @abstractmethod
    def send_message(self):
        """ send message to other particpants of parser """
        pass

    @abstractmethod
    def receive_message(self):
        """ send message to other particpants of parser """
        pass


class EmailInterface(MessageInterface):
    """ connects to email and reads last email for input """
    def __init__(self, host, account, password):
        self.host = host
        self.acc = account
        self.pw = password

    def receive_message(self):
        # connect inbox
        imap_server = imaplib.IMAP4_SSL(host=self.host)
        imap_server.login(self.acc, self.pw)
        imap_server.select() # default inbox
        _,message_numbers_raw = imap_server.search(None, 'ALL')
        message_number = message_numbers_raw[0].split()[-1]
        _, msg = imap_server.fetch(message_number, '(RFC822)')
        message = email.message_from_bytes(msg[0][1])
        content = message.get_payload()
        print(content)
        out = []
        try:
            out = [bool(i) for i in content.split()]
        except:
            pass
        if len(out) == 3:
            return(out)
        else:
            return False

    def send_message(self, r, g, b):
        """ send message to other particpants of parser """
        from_email = self.account
        to_email = from_email
        email_message = EmailMessage()
        email_message.add_header('To', to_email)
        email_message.add_header('From', from_email)
        body = f"{r} {g} {b}"
        email_message.add_header('Subject','rgb')
        email_message.add_header('X-Priority', '1')
        email_message.set_content(body)
        smtp_server = SMTP_SSL(self.host, port = SMTP_SSL_PORT)
        smtp_server.set_debuglevel(1)
        smtp_server.login(self.acc, self.pw)
        smtp_server.sendmail(from_email, to_email, email_message.as_bytes())
