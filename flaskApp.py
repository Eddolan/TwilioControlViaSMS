"""
Let me know if you need credentials for anything like mongo, heroku or twilio to debug

todo:
2) implement the variable referenced in code as 'unique_id' # be sure to read my notes on uniqueID
3) implement method specified as receive_instructions().parser_call()
    ### This is where all the TWIML code will go
    ### Think about most moducual and simple way to implement TWIML and as many options as possible (female record)
4) Make URLs work
5) Debug
    ### I have not ran the code to debug since the code was much smaller, so there will be bugs
    ### Alot of what I have written is almost pseudocode
"""

## evniornmental varibles
import os
from flask import Flask , request, url_for
import datetime as dt
import smtplib
from MongoConnector import *
from TwilioConnector import *
from InstructionParser import *


debug = False

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask app is up and running'


@app.route('/receive_text', methods=['GET','POST'])
def receiveSMS():
    """
    Should be set as request URL on twilio (post)
    receives an SMS
    1) Checks who its from
        if admin: send to recieve_instructions
        else: forward to you (with number from)
    """
    from_number = request.values.get('From', None)
    instructions = request.values.get('Body')
    if instructions[0] == "+":
        foo = receive_instructions(instructions, callers[from_number])
        foo.parse()


@app.route('/check_schedules_tasks')
def check_scheduled_tasks():
    """
    Checks mongo for scheduled tasks: if so run to parse
    Heroku will run this every 10 mins
    """
    pass

@app.route('/call/<call_id>')
def return_TWIML(call_id):
    """
    returns the TWIML for a call ID from MongoDB
    TWIML must already be hosted and stored in MongoDB (see recieve_instructions().parser_call)
    """
    pass

@app.route('/getrequests')
def return_requests():
    """
    Shows all previous and future calls (FUTURE CALLS SEPERATED)
    """
    pass


if __name__ == '__main__':
    app.run()
