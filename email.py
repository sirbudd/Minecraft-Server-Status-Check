import pickle
from multiprocessing import shared_memory
import smtplib
import logging
from functions import *

logging.basicConfig(filename='logs.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s') #logging file config
config = open_cfg()

def send_email():
    """
    Function that connects to a given SMTP (google, in our case) and sends an email
    Expected input : data from old_data.pickle
    Expected output : succesfull email sent
    """
    try:
        with open('old_data.pickle', 'rb') as file:   #opening the old Temp & Humidity data
            old_weather = pickle.load(file)
    except:
        logging.error("Pickled data couldn't be deserialized")

    sender = config['sender_email_address']
    password = config['sender_password']          #account login info for sender & receiver
    receiver = config['receiver_email_address']     
    
    subject = "Weather App Warning - High Delta" #email title
    body = "Attention! Temperature or Humidity delta too big! New Temp & Humidity : " ,old_weather['old_temperature'],old_weather['old_humidity']  #email text

    # header
    message = f"""From: Weather {sender}
    To: {receiver}
    Subject: {subject}\n
    {body}"""

    server = smtplib.SMTP("smtp.gmail.com", 587)    #connect to google SMTP
    server.starttls()

    try:
        server.login(sender,password)
        server.sendmail(sender, receiver, message)
    except smtplib.SMTPAuthenticationError:
        logging.error("Unable to sign in, check your credentials")