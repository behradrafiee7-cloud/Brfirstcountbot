import requests
from datetime import datetime
import os

# گرفتن اطلاعات از Secrets
TOKEN = 8403566708:AAEJ8xuIQ2tzYFQne8TbpiEieu8j1eHudzU"]
CHAT_ID = os.environ["72569952"]

# تاریخ شروع
start_date = datetime(2025, 10, 11)

# تاریخ امروز (UTC)
today = datetime.utcnow()

# اختلاف روز
delta = today - start_date
days_passed = delta.days

# ساخت پیام
if days_passed >= 0:
    message = f"{days_passed} days have passed since October 11, 2025."
else:
    message = f"{abs(days_passed)} days left until October 11, 2025."

# ارسال پیام به تلگرام
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": 72569952,
    "text": message
}

requests.post(url, data=data)
