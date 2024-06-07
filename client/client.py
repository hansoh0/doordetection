#! /usr/bin/env python3

import gpiozero
import datetime
import subprocess
import requests

pin40 = gpiozero.InputDevice(40)

def doorcheck():
    was_open = False
    while True:
        is_open = pin40.value == 1 
        if is_open and not was_open:
            writelog()
            send_status()
            was_open = True 
        elif not is_open:
            was_open = False

def writelog():
    todayinfo = datetime.datetime.now() + datetime.timedelta(hours=4)
    date = todayinfo.strftime("%Y-%m-%d")
    time = todayinfo.strftime("%H:%M:%S")
    dooropened = f"DOOR OPENED: {date} {time}\n"
    
    with open("doorlog.txt", "a+") as doorlog:
        doorlog.write(dooropened)
        check_header(doorlog, date, time)

def check_header(doorlog, date, time):
    header = f"LOG START {date} {time}\n"
    doorlog.seek(0)
    doorlogtext = doorlog.read()
    if header not in doorlogtext:
        try:
            remotebackup()
            doorlog.write(header)
        except Exception as e:
            doorlog.write(f"DOORLOG HEADER ERROR: {e}\n")

def send_status():
    url = "http://192.168.xxx.xxx:1312/catch" 
    payload = {
        "status": "OPEN",
        "timestamp": datetime.datetime.now().isoformat()
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send status: {e}")

def remotebackup():
    subprocess.run(["scp", "doorlog.txt", "host@server:PATH"])

def main():
    doorcheck()

if __name__ == "__main__":
    main()
