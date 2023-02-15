import smtplib
import ssl

#Set up SMTP port and server
SMTP_Port = 587                      # Standard secure SMTP port
SMTP_Server = "smtp.gmail.com"       # Google SMTP server

#credentials
email_from = 'itsmeamalroy@gmail.com'
email_to = 'itsmeamalroy@gmail.com'
pswd = "spqeubsoqnfpjjwi" #access this externally when doing main projects as we dont want password out in open



#content
message = "Dear Bro,mail me back!!!"

simple_email_context = ssl.create_default_context()

try:
    print("Connecting to server")
    server = smtplib.SMTP(SMTP_Server,SMTP_Port) #start server
    server.starttls(context = simple_email_context)
    """
    inform the email server that the email client wants to 
    upgrade from an insecure connection to a secure one using TLS or SSL
    TLS = Transport Layer Security
    SSL = Secure sockets Layer
    """
    context = ssl.create_default_context() # returns a new context with secure default settings
    server.login(email_from,pswd) #logins
    print("Connected to server :-)")

    print()
    print(f"sending mail to -{email_to}")
    server.sendmail(email_from,email_to,message)
    print(f"Email succesfully sent to - {email_to}")
     
except Exception as e :
    print(e)
finally :
    server.quit()