from typing import Literal
from pythonping import *
import os
import threading
def whole_program():
    threading.Timer(30.0, whole_program).start()
    ip = "8.8.8.8"
    ping_count = 4
    def counter():
        count = 0
        while True:    
            if ping(ip, verbose=False, timeout=0.8, count=ping_count, df=True).success(1):
                count += 1
                print(count)
            else: break
            if count == 5:
                break
        return count

    counter()
whole_program()