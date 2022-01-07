import pickle
from multiprocessing import shared_memory
import logging
from functions import *
from mcstatus import MinecraftServer
import socket

config = open_cfg()  
logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config


def CheckServerStatus():
    try:
        server = MinecraftServer.lookup(config['server_ip'])
        query = server.query()
        status = server.status()
        print(status.latency)
    except socket.timeout:
        print("Socket timed out")
        print("Maybe check your server's IP?")


    # print(f"Server version : {query.software.version}")
    # print(f"Server MOTD : {status.description}")
    # print(f"Players : {query.players.names}")
    logging.info(f"Server version : {query.software.version}")
    logging.info(f"Server MOTD : {status.description}")
    logging.info(f"Players : {query.players.names}")
    logging.info(f"==============")

if __name__ == '__main__':
    CheckServerStatus()