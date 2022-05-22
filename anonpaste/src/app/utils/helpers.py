from datetime import datetime
from random import choice
from string import ascii_letters



def get_current_time():
   now = datetime.now()
   current_time = now.strftime("%D %H:%M:%S")
   return str(current_time)


def gen_id():
    id=''
    for i in range(12):
        id+=choice(ascii_letters)
    return id 