import smtplib
import ssl

#Set up SMTP port and server
SMTP_Port = 587                      # Standard secure SMTP port
SMTP_Server = "smtp.gmail.com"       # Google SMTP server

#credentials
email_from = itsmeamalroy@gmail.com
email_to = itsmeamalroy@gmail.com
pswd = "spqeubsoqnfpjjwi" #access this externally when doing main projects as we dont want password out in open



#content
message = "Dear Bro,mail me back!!!"

simple_email_context = ssl.create_default_context()

try:
    print("Connecting to server")
    TIE_server = smtplib.SMTP(SMTP_Server,SMTP_Port)
    TIE_server = starttls(context = simple_email_context)
    TIE_server.login(email_from,pswd)
    print("Connected to server :-)")

    print()
    print(f"sending mail to -{email_to}")
    TIE_server.sendmail(email_from,email_to,message)
    print(f"Email succesfully sent to - {email_to}")
     
except Exception as e :
    print(e)
finally :
    TIE_server.quit()