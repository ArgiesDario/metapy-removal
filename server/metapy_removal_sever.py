from flask import Flask, render_template
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import time

def scheduled_func():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

#Scheduler execution
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_func, trigger="interval", seconds=3)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()