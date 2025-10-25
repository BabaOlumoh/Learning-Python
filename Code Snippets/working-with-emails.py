import smtplib, getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()
smtp_object.starttls()


smtp_object.ehlo()
email = getpass.getpass("Email: ")
password=getpass.getpass("Enter password: ")
smtp_object.login(email,password)

from_address = email
to_address = email
subject = "Testing"
message = "This is a test"
msg = "Subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()