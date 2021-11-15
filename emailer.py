import smtplib
import constants as const

class Email: 
    def __init__(self, body, username, password):
        self.body = body
        self.username = username
        self.password = password
    def __enter__(self):
        print ('Enter')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
         print('Exit')

    def sendEmail(self):
        sent_from = self.username
        to = [self.username]
        subject = 'Instagram Bot Report'
        body = self.body

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(self.username, self.password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print('Email sent succesfully!')
        except Exception as ex:
            print('Something went wrong...', ex)

