#!/usr/bin/env python3

import shutil
import psutil

import requests
import socket

# Checking basic Networking Ablitly
def check_localhost():
        localhost = socket.gethostbyname("localhost")
        return localhost == "127.0.0.1"

def check_connectivity():
        request = requests.get("http://www.google.com")
        return request.status_code == int(200)

# Get current percentage of free space on specified disk
def get_disk_freespace(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return float(format(free, '.2f'))

# get CPU usage on the first core
def get_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage

# If freespace percentage less than 20%, return false
def free_disk_less_than_20(disk):
	free = get_disk_freespace(disk)
	return free > 20

# If cpu usage more than 75%, return false
def cpu_usage_less_than_75():
	usage = get_cpu_usage()
	return usage < 75

if not free_disk_less_than_20("/"):
	print(f"ERROR: Disk free space is only: {get_disk_freespace('/')} percent!")
elif not cpu_usage_less_than_75():
	print(f"ERROR: CPU usage is: {get_cpu_usage()} percent on core 1!")
elif not check_localhost():
	print(f"Localhost is set to wrong IP address!")
elif not check_connectivity():
	print(f"Not Connected to internet!")
else:
	print("Everything is OK!")

