import os

print("main program started")

pid = os.fork()

if pid < 0:
    print("fork failed!")
else:
    if pid == 0:
        print("this is child process")
        my_pid = os.getpid()
        print("child's PID: " + str(my_pid))
    else:
        print("this is parent process")
        my_pid = os.getpid()
        print("parent's PID: " + str(my_pid))
