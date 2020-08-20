import os
import smtplib
import pandas as pd

email = os.environ.get('EM_NAME')
passw  = os.environ.get('EM_PASS')

data=  pd.read_csv('webinar.csv')
data.head()
'''with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email,passw)
    subject = "Grab Dinner this weekend"
    body = 'How about tdinner at  pm this saturday'

    msg  = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email,email,msg)'''
    


