import smtplib
from email.mime.text import MIMEText
from crontab import CronTab
from find_ChangchunToKunming.Spider_tiket import parser_html


_user = "541573560@qq.com"
_pwd  = "xhdlmgojfcwzbfeh"
_to_list   = ["541573560@qq.com","1150995508@qq.com","1848918059@qq.com"]

qqq = parser_html()

msg = MIMEText(str(qqq))
msg["Subject"] = "don't panic"
msg["From"]    = _user

def sent_email():
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        for _to in _to_list:
            msg["to"] = _to
            s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print ("Success!")
    except :
        print ("Falied!QAQ")

if __name__ =='__main__':
    sent_email()