import smtplib
from email.mime.text import MIMEText
import requests
from tryy import *


class Currency:
    @current_time
    @do_while
    def get_from_privat(self, mail=True):
        url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
        responce = requests.request("GET", url)
        JsonData = responce.json()
        Lines = []
        for index in range(len(JsonData)):
            symbol = JsonData[index]['ccy']
            curr_buy = JsonData[index]['buy']
            curr_sale = JsonData[index]['sale']
            for i in ['покупки', 'продажи']:
                if i == 'покупки':
                    param = curr_buy
                else:
                    param = curr_sale

                result_message = 'Курс' + i + '{0} {1}'.format(symbol, param) + '\n'
                Lines.append(result_message)
            message_log = ''.join(Lines)
        if mail:
            self.send_mail('kashin.i.i@i.ua', message_log)
        return message_log

    def send_mail(self, to_who, message):
        you = to_who
        login = 'kashin.i.i@ukr.net'
        passw = '14ENASEL'
        url = 'smpt.ukr.net'
        msg = MIMEText(message)
        msg['Subject'] = 'currency now'
        msg['From'] = login
        msg['To'] = 'kashin.i.i@i.ua'
        server = smtplib.SMTP_SSL(url, 465)
        server.login(login, passw)
        server.sendmail(login, you, msg.as_string())
        return server.close()


if __name__ == '__main__':
    exchange = Currency()
    print(exchange.get_from_privat(mail=False))
