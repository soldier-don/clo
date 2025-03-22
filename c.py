import requests
import random
import string
import uuid
from faker import Faker
import telegram
import asyncio

# Initialize Faker for Indian data
fake = Faker('en_IN')  # Using Indian locale

# Telegram Bot Token and Chat ID (replace with your own)
TELEGRAM_BOT_TOKEN = ""  # Replace with your bot token from BotFather
TELEGRAM_CHAT_ID = ""     # Replace with your chat ID

# Initialize Telegram bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_headers():
    device_id = str(uuid.uuid4())
    user_agents = [
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)} Safari/537.36",
        f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(13, 15)}_{random.randint(1, 5)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)} Safari/537.36",
        f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)} Safari/537.36"
    ]
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": random.choice(user_agents),
        "Referer": "https://unified.cloudways.com/",
        "Origin": "https://unified.cloudways.com",
        "X-Device-Id": device_id
    }
    return headers

def generate_random_data(email, password):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_unique_id = str(uuid.uuid4())
    data = {
        "email": email,
        "first_name": first_name,
        "gdpr_consent": True,
        "last_name": last_name,
        "password": password,
        "persona_tag_id": random.randint(10, 15),
        "promo_code": "",
        "signup_page_template_id": 0,
        "signup_price_id": random.choice(["a", "b", "c"]),
        "user_unique_id": user_unique_id
    }
    return data

async def send_to_telegram(email, password, response_status, response_text):
    message = (
        f"New Account Created (India):\n"
        f"Email: {email}\n"
        f"Password: {password}\n"
        f"Response Status: {response_status}\n"
        f"Response: {response_text}"
    )
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

async def main():
    # Get email and password from user
    print("Bhai, ek legit email daal (jaise Gmail), temp mail se block ho sakta hai!")
    email = input("Apna email ID daal do: ")
    password = input("Ab password daal do: ")
    
    # Generate random headers and data
    headers = generate_random_headers()
    data = generate_random_data(email, password)
    
    # URL for the API
    url = "https://api.cloudways.com/api/v2/guest/signup"
    
    try:
        # Make the POST request
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        # Print the response locally
        print("\nRequest Headers:")
        print(headers)
        print("\nRequest Data:")
        print(data)
        print("\nResponse Status Code:", response.status_code)
        print("Response:", response.text)
        
        # Send to Telegram
        await send_to_telegram(email, password, response.status_code, response.text)
        print("Telegram pe message bhej diya bhai!")
        
    except requests.exceptions.RequestException as e:
        print(f"Error ho gaya bhai: {e}")
        await send_to_telegram(email, password, "Error", str(e))

if __name__ == "__main__":
    asyncio.run(main())