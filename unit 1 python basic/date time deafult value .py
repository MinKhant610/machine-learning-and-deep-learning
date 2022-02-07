from datetime import datetime

def fun(msg,*,dt=datetime.utcnow()):
    print (f'{dt}{msg}')
fun ('text message1',dt = '2020-06-01 00:01:11 0123456 ')
fun ('text message2')

#if date is not show current date to write this

def x (mes,*,dat=None):
    if not dat :
        dat = datetime.utcnow()
        print (f'{dat}{mes}')
x ('message 1')