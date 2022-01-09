from multiprocessing import shared_memory
import smtplib
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
    

    jsonfile =  open("cfg.json", "r")
    data = json.load(jsonfile)

    print("Failed to read JSON Config File")    
    return data


