import requests
from datetime import datetime
import os

# گرفتن اطلاعات از Secrets
TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# تاریخ شروع
start_date = datetime(2025, 10, 11)

# تاریخ امروز (UTC)
today = datetime.utcnow()

# اختلاف روز
delta = today - start_date
days_passed = delta.days

# ساخت پیام
if days_passed >= 0:
    message = f"{days_passed} روزگی روتیشنمون مبارک🎉 "
else:
    message = f"{abs(days_passed)} days left until October 11, 2025."

# ارسال پیام به تلگرام
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(url, data=data)
