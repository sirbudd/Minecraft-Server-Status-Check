#import pickle
from multiprocessing import shared_memory
import logging
from functions import *
from mcstatus import MinecraftServer
import socket


logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config
config = open_cfg()

def CheckServerStatus():
    status_report = 0 #variable for "boolean"
    try:
        server = MinecraftServer.lookup(config['server_ip'])                       #checking the desired server
        query = server.query()                                                     #query = for detailed information on the server
        status = server.status()                                                   #status = for not so detailted information on the server
        logging.info(status.latency)
        logging.info(f"Server version : {query.software.version}")
        logging.info(f"Server MOTD : {status.description}")
        logging.info(f"Players : {query.players.names}")
        logging.info(f"=======================")
        
        status_report = 1                                                          # 1 = server UP/ 0 = server DOWN
        print(status_report)
    except socket.timeout:
        logging.error("Socket timed out")
        print("Yey,error")
        status_report = 0

    return status_report


if __name__ == '__main__':
    CheckServerStatus()