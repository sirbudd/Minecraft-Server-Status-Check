#!/usr/bin/python
import os
import logging
import json
import pymongo
from pymongo import MongoClient
import smtplib 

#separate file for functions that are used globally

logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config


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
config = open_cfg()


def MongoDB(data):
    """
    Function for connecting to my my MongoDB
    """
    cluster = MongoClient("mongodb+srv://mcpython:mcpython123@cluster0.vqetj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #establising mongodb connection
    db = cluster["minecraft"] #database name from MongoDB
    collection = db["server-logs"]
    collection.insert_one(data)


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