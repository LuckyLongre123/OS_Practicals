import stat
import time
import pwd
import os

filename = "./example.txt"

try:
    file_stat = os.stat(filename)

    print(f"File: {filename}")
    print(f"Size: {file_stat.st_size} bytes")
    print(f"Inode: {file_stat.st_ino}")

    try:
        owner = pwd.getpwuid(file_stat.st_uid).pw_name
        print(f"Owner: {owner} (UID: {file_stat.st_uid})")
    except KeyError:
        print(f"Owner UID: {file_stat.st_uid}")

    mode = file_stat.st_mode
    perms = stat.filemode(mode)
    print(f"Permissions: {perms}")
    print(f"Octal Permissions: {oct(stat.S_IMODE(mode))}")

    print(f"Last Access Time: {time.ctime(file_stat.st_atime)}")
    print(f"Last Modification Time: {time.ctime(file_stat.st_mtime)}")
    print(f"Last Status Change Time: {time.ctime(file_stat.st_ctime)}")

except FileNotFoundError:
    print(f"Error: File {filename} not found")
except Exception as e:
    print(f"Error: {e}")