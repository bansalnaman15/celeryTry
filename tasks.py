import random,os,string
from celery import Celery
from time import sleep

app = Celery('tasks',broker="redis://139.59.94.114")

@app.task
def task():
    task2()


def task2():
    sleep(5)
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=4))
    os.mkdir(res)

    #celery -A tasks worker --pool=solo --loglevel=INFO