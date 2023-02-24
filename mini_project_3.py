import time
import os

def print_time(h, m, s):
    (hh,mm,ss) = (str(h), str(m), str(s))
    hh = ("0" + hh) * (len(hh) == 1) + hh * (len(hh) == 2)
    mm = ("0" + mm) * (len(mm) == 1) + mm * (len(mm) == 2)
    ss = ("0" + ss) * (len(ss) == 1) + ss * (len(ss) == 2)
    print(f"{hh}: {mm}: {ss}")  #    print(f"{hh}: {mm}: {ss}", end = "\r")

def timer(second):
    while second != 0:
        
        houer = second // 3600
        minute = (second - houer * 3600) // 60
        s = second - houer * 3600 - minute * 60
        print_time(houer, minute, s)
        time.sleep(1)
        second -= 1
        
    os.system("clear||cls")
    print("Time is up!", end = "\r\a")

def timer_start(start):
    while start:

        os.system("clear||cls")
        t = input("Enter time: ")
        os.system("clear||cls")
        (h, m, s) = (int(elem.strip()) for elem in t.split(":"))
        all_seconds = h * 60 * 60 + m * 60 + s
        timer(all_seconds)
        start = input("Continue?(Y/n)").lower() in ["y", "yes"]

    os.system("clear||cls")

start = True

timer_start(start)

