#!/usr/bin/python
import logging
from mcstatus import MinecraftServer
import socket
from functions import *

config = open_cfg()

logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config

def CheckServerStatus():
    status_report = 0 #variable for "boolean"
    try:
        server = MinecraftServer.lookup(config['server_ip'])                       #checking the desired server
        query = server.query()                                                     #query = for detailed information on the server
        status = server.status()                                                   #status = for not so detailted information on the server
        logging.info(f"Latency : {status.latency}")
        logging.info(f"Server version : {query.software.version}")
        logging.info(f"Server MOTD : {status.description}")
        logging.info(f"Players : {query.players.names}")
        
        status_report = 1                                                          # 1 = server UP/ 0 = server DOWN
        logging.info(f"Status report : {status_report}")
        logging.info(f"=======================")
    except socket.timeout:
        logging.error("Socket timed out")
        status_report = 0
        logging.info(f"Status report : {status_report}")
        logging.info(f"=======================")
    return status_report


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


if __name__ == '__main__':
    CheckServerStatus()
    flag = CheckServerStatus()
    print(f"flag = {flag}")
    if flag == 0:
        send_email()
        print("email sent!")