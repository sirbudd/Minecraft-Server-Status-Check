import pickle
from multiprocessing import shared_memory
import logging
from functions import *
from mcstatus import MinecraftServer


config = open_cfg()  
logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config


def CheckServerStatus():
    server = MinecraftServer.lookup(config['server_ip'])
    

if __name__ == '__main__':
    CheckServerStatus()