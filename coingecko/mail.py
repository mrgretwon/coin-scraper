import smtplib

from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

sender = 'coingecko.cmc.bot@gmail.com'
password = 'TNTSucks!'


def send_email(receiver, message):
    email_body = """<html>\n\n""" \
        """<head></head>\n\n""" \
        """<body>\n"""
    msg = MIMEMultipart()
    msg['Subject'] = 'Coingecko new listings'
    msg['From'] = sender
    msg['To'] = receiver
    email_body += message
    email_body += """</body>\n""" \
        """</html>\n"""
    msg.attach(MIMEText(email_body, 'html'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, password)
    session.send_message(msg)
    session.quit()
