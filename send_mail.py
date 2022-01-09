#!/usr/bin/python
import logging
from functions import *
import smtplib

config = open_cfg()
logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config

def send_email():
    """
    Function that connects to a given SMTP (google, in our case) and sends an email
    """

    sender = config['sender_email_address']
    password = config['sender_password']          #account login info for sender & receiver
    receiver = config['receiver_email_address']     
    
    subject = "Minecraft Server Status" #email title
    body = "Server Down"  #email text

    # header
    message = f"""From: MC_Server {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}"""

    server = smtplib.SMTP("smtp.gmail.com", 587)    #connect to google SMTP
    server.starttls()

    try:
        server.login(sender,password)
        server.sendmail(sender, receiver, message)
        logging.info("Email sent")
    except smtplib.SMTPAuthenticationError:
        logging.error("Unable to sign in, check your credentials")