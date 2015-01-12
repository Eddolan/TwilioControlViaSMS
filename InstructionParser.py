
class parse_instructions:
    """
    Class to handle instructions.
    """

    def __init__(self, instructions):
        self.instructions = instructions
        if not debug: self.log_in_mongo()



    def log_in_mongo(self):
        """
        # dt.datetime should not be string
        """
        MongoDatabase.InstructionLog.insert({
            "time"              :       dt.datetime.now(),
            "sent_from"         :       self.admin,
            "instructions"      :       self.instructions
        })

    def parse(self):
        """
        ########
         +:-   <<<<<<<<<< DON'T USE THESE IN MESSAGE
        ########
        First: test for time requests (delimted by  #16:00):
            takes message without timing and saves it to timed request ####
        Parses for:
            1) number deliminated by +
            2) message delimiated by :
            3) options deliminated by -
        option default to -t which is a text:
        other option is:
            -c (call)
                f (female)
                ? (record)
        """

        foo = self.instructions.split("+")[1:]
        foo[-1] = foo[-1].split(" ")[0]
        numbers = foo[0]


        foo = self.instructions.split(":")[1]
        foo = foo.split("-")[0]
        message = foo


        foo = self.instructions.split("-")[1]
        options = foo

        if 'c' in options:       self.parser_call(numbers, message, 'f' in options, '?' in options)
        else:                    self.parser_text(numbers, message)


    def parser_call(self, number, message, female_bool, record_bool):
        """
        UNFINISHED
        Helper method for parser
        This method will:
            1) generate the twliml String
            2) Store it into MongoDB['Instructions'] using unique_id as '_id' in mongo
                        #### I have not figured out a great way to generate and pass a unique_id
                        #### unique_id will also be a part of the URL needed to retrieve TWIMK
                        #### unknown if this means unique_id cant have ' ' (space character) in it
            3) place the call as so:
                    unique_id = 'randomholder'
                    foo = twilio_instanc
                    foo.call(number, 'baseurl/call/unique_id')
                        ### 'baseurl/call/unique_id direct' generates the url that calls app.return_twiml()
                        ### app.return_twiml() returns TWIML from mongo

        """
        unique_id = 'randomholder'
        foo = twilio_instance()
        foo.call(number, 'baseurl/call/unique_id')

    def parser_text(self, number,  message):
        """
        Helper method for parser
        """
        foo = twilio_instance()
        foo.sms(number, message)
