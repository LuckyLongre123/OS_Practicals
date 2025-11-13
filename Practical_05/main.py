import os
import sys

src = sys.argv[1]
dest = sys.argv[2]

fd1 = os.open(src, os.O_RDONLY)
fd2 = os.open(dest, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

while True:
    data = os.read(fd1, 1024)
    if not data:
        break
    os.write(fd2, data)

os.close(fd1)
os.close(fd2)
print("File copied successfully.")