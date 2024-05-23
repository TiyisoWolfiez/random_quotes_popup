import requests
import tkinter as tk
from tkinter import messagebox
import schedule
import time
import random

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return data['content'], data['author']
    except requests.RequestException as e:
        return "Could not fetch quote", str(e)

def show_quote():
    quote, author = get_random_quote()
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Random Quote", f"{quote}\n\n- {author}")
    root.destroy()

def job():
    show_quote()

def random_interval_job():
    interval = random.randint(5, 10)  # Random interval between 5 to 10 minutes
    schedule.every(interval).minutes.do(job)

random_interval_job()

while True:
    schedule.run_pending()
    time.sleep(1)
