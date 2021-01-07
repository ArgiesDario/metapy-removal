from flask import Flask, render_template, request, redirect
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
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        print (task_content)
        return redirect('/')
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run()