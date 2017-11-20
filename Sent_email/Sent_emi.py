import smtplib
from email.mime.text import MIMEText
from find_ChangchunToKunming.Spider_tiket import load_massage


url = 'https://sjipiao.fliggy.com/flight_search_result.htm?_input_charset=utf-8&spm=181.7091613.a1z67.1001&searchBy=1280&tripType=0&depCityName=%E9%95%BF%E6%98%A5&depCity=&depDate=2018-01-13&arrCityName=%E6%98%86%E6%98%8E&arrCity=KMG&arrDate='


_user = "541573560@qq.com"
_pwd  = "rlapjidinhdnbegc"
_to_list   = ["541573560@qq.com"]

qqq = load_massage(url)

msg = MIMEText(qqq)
msg["Subject"] = u"机票信息"
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
