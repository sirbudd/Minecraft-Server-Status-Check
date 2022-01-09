#!/usr/bin/python
from multiprocessing import shared_memory
import os
import logging
import json

logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config

#separate file for functions that are used globally

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



