import os
import sys
import stat
import time

file = sys.argv[1]
info = os.stat(file)

permissions = stat.filemode(info.st_mode)

access_time = time.ctime(info.st_atime)

owner = info.st_uid

print("File Name:", file)

print("Owner ID:", owner)

print("Permissions:", permissions)

print("Last Access Time:", access_time)