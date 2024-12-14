import threading
import time

def function1(sec):
    print(f"sleepin for:{sec}")
    time.sleep(sec)

function1(3)
function1(2)
function1(3)