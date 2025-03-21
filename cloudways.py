import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from telegram import Bot

# Hardcoded Bot Credentials
BOT_TOKEN = "7379441276:AAHRk9qZGBl1rIoZhAiUcCH9ZPqjmbGpIbk"
ADMIN_ID = 5759284972  # Replace with your Telegram ID

bot = Bot(token=BOT_TOKEN)

def send_message(chat_id, text):
    """Send a message via Telegram bot."""
    bot.send_message(chat_id=chat_id, text=text)

def run_selenium(email, password, chat_id):
    """Automates Cloudways account creation with anti-detection techniques."""
    ua = UserAgent()

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={ua.random}")  # Random User-Agent
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://platform.cloudways.com/signup")
        time.sleep(random.uniform(2, 5))  # Random delay

        # Human-like movements
        pyautogui.moveTo(random.randint(300, 600), random.randint(200, 500), duration=random.uniform(0.5, 2.5))

        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "name").send_keys("Automation User")
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Get Started')]").click()

        time.sleep(random.uniform(5, 10))  # Wait for confirmation

        message = f"✅ **Cloudways Account Created!**\n📧 Email: {email}\n🔑 Password: {password}"
        send_message(chat_id, message)
        send_message(chat_id, "🎉 **Account Created Successfully!**")

        print("✅ Account details sent to Telegram!")

    except Exception as e:
        send_message(chat_id, f"❌ Error: {str(e)}")

    finally:
        driver.quit()