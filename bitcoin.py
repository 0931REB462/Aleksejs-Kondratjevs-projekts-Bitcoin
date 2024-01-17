import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Nodrošināt pareizo URL
api_url = "https://api.livecoinwatch.com/coins/single"
api_key = "487741b3-7b2e-45b9-8a43-b5d08a8a5924" #lai dabūt bezmaksas api kodu ir jāreģistējas (https://www.livecoinwatch.com/tools/api#try)
email_sender = 'aaaaaa@edu.rtu.lv' # šeit ievadam e pasta adresi (tikai microsoft adresi, jo citādi ir jāmaina smtplib.SMTP)
email_receiver = 'aaaaaa@edu.rtu.lv'
email_password = 'aaaaa' #ievadam epasta adreses paroli

# Funkcija, lai iegūtu BTC datus
def get_btc_data():
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        "currency": "USD",
        "code": "BTC",
        "meta": True
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json()

previous_data = None

# Funkcija, lai pārbaudītu datus un paziņotu
def check_data_and_notify():
    global previous_data
    current_data = get_btc_data()
    current_rate = current_data.get("rate")

    # Pārbaudīt izmaiņas cenā par 0.50 centiem
    if previous_data is None:
        previous_data = current_rate
    elif abs(current_rate - previous_data) >= 0.50:
        current_name = current_data.get("name")
        send_email(current_name, current_rate)
        previous_data = current_rate

# Funkcija, lai nosūtītu e-pastu
def send_email(name, rate):
    message = MIMEMultipart()
    message['From'] = email_sender
    message['To'] = email_receiver
    message['Subject'] = 'BTC Rate Update'

    body = f"Name: {name}\nRate: {rate}"
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    try:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, message.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

# Iestatīt grafiku, lai pārbaudītu datus ik pēc 10 sekundēm
schedule.every(10).seconds.do(check_data_and_notify)

# Sākt bezgalīgu ciklu
while True:
    schedule.run_pending()
    time.sleep(1)

