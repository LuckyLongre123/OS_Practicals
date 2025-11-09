import os
print("main program started")

pid = os.fork()

if pid < 0:
    print("fork failed!")

if pid == 0:
    print("this is child process")
    print("child's PID: " + str(os.getpid()))
else:
    print("this is parent process")
    print("parent's PID: " + str(os.getpid()))
