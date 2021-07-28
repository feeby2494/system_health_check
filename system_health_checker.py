#!/usr/bin/env python3

import shutil
import psutil

def get_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return float(format(free, '.2f'))

def get_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage

def free_disk_less_than_20(disk):
	free = get_disk_usage(disk)
	return free > 20

def cpu_usage_less_than_75():
	usage = get_cpu_usage()
	return usage < 75

if not free_disk_less_than_20("/"):
	print(f"ERROR: Disk free space is only: {get_disk_usage('/')} percent!")
elif not cpu_usage_less_than_75():
	print(f"ERROR: CPU usage is: {get_cpu_usage()} percent on core 1!")
else:
	print("Everything is OK!")

