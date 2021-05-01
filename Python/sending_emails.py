import smtplib
smtp_obj=smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo()
print(smtp_obj.starttls())

import getpass

# app password is ktqriewcgdmoxavb

email=getpass.getpass("Email : ")
password=getpass.getpass("Password: ")
print(smtp_obj.login(email,password))

from_address=email
to_address=email
subject=input('enter your subject: ')
message=input('enter your body message: ')
msg='Subject: '+subject+'\n'+message

smtp_obj.sendmail(from_address,to_address,msg)
smtp_obj.quit()