#!/usr/bin/python
import logging
from mcstatus import MinecraftServer
import socket
from functions import *
from send_mail import *

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


if __name__ == '__main__':
    CheckServerStatus()
    flag = CheckServerStatus()
    print(f"flag = {flag}")
    if flag == 0:
        send_email()
        print("email sent!")