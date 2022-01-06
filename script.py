import pickle
from multiprocessing import shared_memory
import smtplib
import logging
import warnings
from functions import *
from mcstatus import MinecraftServer

warnings.filterwarnings("ignore")
logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config

server = MinecraftServer.lookup("157.90.221.188:6055")
status = server.status()
print(f"The server has {status.players.online} players and replied in {status.latency} ms")


config = open_cfg()  #open our config file
# query = server.query()
# print(f"The server has the following players online: {', '.join(query.players.names)}")
