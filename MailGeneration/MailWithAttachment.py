import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#Set up SMTP port and server
SMTP_Port = 587                      # Standard secure SMTP port
SMTP_Server = "smtp.gmail.com"       # Google SMTP server

#credentials
email_from = 'itsmeamalroy@gmail.com'
# email_to = ['itsmeamalroy@gmail.com']
email_to = ['itsmeamalroy@gmail.com','itsmeamalroy@gmail.com'] #For sending to multiple mails

pswd = "spqeubsoqnfpjjwi" #access this externally when doing main projects as we dont want password out in open

subject = 'Test mail with Attachment'

def send_emails(email_to) :
    for person in email_to:
        body = f"""
        Hi Dude,
            Checkout this attachment.
        
        Best Regards,
        Amal
        """
        msg = MIMEMultipart()  #Create a mimeobject todefine parts of the mail
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        #Attach body of the message
        msg.attach(MIMEText(body,'plain'))

        #Define file to be send
        #filename = 'FirstMail.png'
        filename = '/home/amalr/Desktop/PythonTraining/MailGeneration/FirstMail.png'

        #Open the file as a binary
        attachment = open(filename,'rb')  #r=read,b=binary

        #Encode the attachment using base-64
        attachment_package = MIMEBase('application','octet-stream') #This is what we attach
        attachment_package.set_payload(attachment.read()) #Pass the contents to this new object
        encoders.encode_base64(attachment_package) #Encode
        attachment_package.add_header('Content-Disposition',"attachment;filename= "+filename) #Set header
        msg.attach(attachment_package) #Attach package
        # print(msg) #debug

        #cast to string
        text = msg.as_string() #This is final message

        # print(text) #debug

        #connect with server
        server = smtplib.SMTP(SMTP_Server,SMTP_Port)
        server.starttls()
        server.login(email_from,pswd)
        print('Successfully Connected to server')
        print()

        print(f"Sending mail to {person}")
        server.sendmail(email_from,person,text)
        print("Mail send successfully")

    server.quit()


#Call the function
send_emails(email_to)

