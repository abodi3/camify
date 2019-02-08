import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def notify(obj): #notifiy by email
    emailFrom = "group@gmail.com"

    emailTo = "members@gmail.com"

    file = obj #Takes the string passed when called and places it in file

    msg = MIMEMultipart()

    msg["From"] = emailFrom
    msg["To"] = emailTo
    msg["Subject"] = "Pir Detects Motion"
    msg.preamble = "Attachment Sent"

    ctype, encoding = mimetypes.guess_type(file)

    if ctype is None or encoding is not None:


        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text": 

        fp = open(file)
        attachment = MIMEText(fp.read(), _subtype = subtype)
        fp.close()
    
    elif maintype == "image":

        fp = open(file, "rb")
        attachment = MIMEImage(fp.read(), _subtype = subtype)
        fp.close()

    else:
        fp = open(file, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)

    attachment.add_header("Content-Disposition", "attachment", filename = file)
    msg.attach(attachment)




    server = smtplib.SMTP('smtp.gmail.com', 587) #server object with google
    server.starttls()
    server.login(emailFrom, "Group_007")
    server.sendmail(emailFrom, emailTo, msg.as_string())
    server.quit()









