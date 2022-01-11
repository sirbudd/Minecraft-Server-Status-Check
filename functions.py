#!/usr/bin/python
import os
import logging
import json
import pymongo
from pymongo import MongoClient
import smtplib 


logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config

#separate file for functions that are used globally

def MongoDB(data):
    """
    Function for connecting to my my MongoDB
    """
    cluster = MongoClient("mongodb+srv://mcpython:mcpython123@cluster0.vqetj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #establising mongodb connection
    db = cluster["minecraft"] #database name from MongoDB
    collection = db["server-logs"]
    collection.insert_one(data)


def open_cfg():
    """
    Function for opening the cfg file.
    Expected input : correct parameters from the cfg.json file
    Expected outpt : data loaded into data variable
    """
    
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        jsonfile = open(os.path.join(__location__, "cfg.json"))
        data = json.load(jsonfile)
    except IOError:
        print("Failed to read JSON Config File")    
    return data



