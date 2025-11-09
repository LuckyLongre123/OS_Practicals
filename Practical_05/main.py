import os

try:
    src_fd = os.open(source, os.O_RDONLY)
    dest_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

    os.sendfile(dest_fd, src_fd, 0, os.path.getsize(source))

    os.close(src_fd)
    os.close(dest_fd)

    print("File copied successfully from", source, "to", destination)

except FileNotFoundError:
    print("Error: Source file", source, "not found")
except Exception as e:
    print("Error:", e)
