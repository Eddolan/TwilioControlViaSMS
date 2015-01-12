
import os
from twilio.rest import TwilioRestClient
import twilio.twiml
from MongoConnector import *
import datetime as dt

class twilio_connector:
    """
    Class to handle twilio
    Should be initiated each time you want to make a call or text
    """

    def __init__(self, sentBy):
        ACCOUNT_SID          = os.environ["TWILIO_SID"]
        AUTH_TOKEN           = os.environ["AUTH_TOKEN"]
        self.client          = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
        self.from_number     = os.environ["FROM_NUMBER"]
        self.sentBy          = sentBy
        self.MongoCollection = "TwilioLogs"

    def call(self, number, message_url):
        """
        calls number and directs at message_URL
        """
        call = self.client.calls.create(
                                                url     = message_url,
                                                to      = number,
                                                from_   = self.from_number
                                        )
        self.log_In_Mongo(number, message_url, call.sid, "call")

    def sms(self, number, SMStext):
        """
        Sends an SMS with the given text to the number
        """
        message = self.client.messages.create(
                                                body    = SMStext,
                                                to      = number,
                                                from_   = self.from_number
                                            )
        self.log_In_Mongo(number, SMStext, message.sid, "text")

    def log_In_Mongo(self, number, content, twilioID, callOrText):
        """
        Logs the twilio request data into a MongoDB collection.
        Relies on MongoConnector.py
        """
        logged_data = {
            "insert_time"       : dt.datetime.now(),#this is the time the text was logged, not time it was sent
            "to"                : number,
            "from"              : self.from_number,
            "content"           : content,
            "twilioID"          : twilioID,
            "Type"              : callOrText,
            "sentBy"            : self.sentBy
        }
        MongoConnection = MongoConnector()
        MongoConnection.insertIntoMongo(self.MongoCollection, logged_data)

    def get_Mongo_Logs(self, params = {}):
        """
        Returns MongoDB enteries that match criteria outlines in params. 
        Defaults to returning all. 
        The return value is an interator of the objects in the collection.
        The collection is defined in the the class initialization.
        """
        return MongoConnector().pullFromMongo(self.MongoCollection, params)

