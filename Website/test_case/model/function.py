import os
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml

from Website.test_case.model.fixture import filepath


def inser_img(driver, filename):
    imgfilepath = filepath()+'/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(imgfilepath)



def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(lists[-1])
    file = os.path.join(report_dir, lists[-1])
    return file


def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()
    yamlfile = filepath() + '/Setting/' + 'email.yaml'
    file = open(yamlfile, encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)

    smtpserver = data['smtpserver']

    user = data['user']
    password = data['password']

    sender = data['sender']
    receives = data['receives']

    subject = data['subject']

    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receives
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    text_msg = MIMEText('查看自动化测试请下载附件', 'plain', 'utf-8')
    msg.attach(text_msg)
    file_msg = MIMEApplication(mail_content)
    file_msg.add_header('content-disposition', 'attchment', filename='自动化测试报告.html')

    msg.attach(file_msg)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email....")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end")


if __name__ == '__main__':
    send_mail()
