import platform
try:
    with open('/proc/version','r') as f:
        print("kernal version :"+f.read())
    print("CPU informations")
    with open('/proc/cpuinfo', 'r') as f:
        for line in f:
                if 'model name' in line or 'cpu cores' in line or 'processor' in line:
                    print(line.strip())
except FileNotFoundError:
        print("Running on non-Linux system. Using alternative method:")
        print("System: " + platform.system())
        print("Release: " + platform.release())
        print("Processor: " + platform.processor())
