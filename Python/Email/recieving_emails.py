import imaplib
M=imaplib.IMAP4_SSL('imap.gmail.com')

import getpass
email=getpass.getpass("Email: ")
password=getpass.getpass('Password: ')

M.login(email,password)
print(M.list())
print(M.select('inbox'))

typ,data=M.search(None,'SUBJECT "NEW TEST PYTHON"')

print(typ)
emailid=data[0]
result,email_data=M.fetch(emailid,'(RFC822)')
raw_email=email_data[0][1]
raw_email_string=raw_email.decode('utf-8')

import email
email_message=email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type()=='text/plain':
        body=part.get_payload(decode=True)
        print(body)