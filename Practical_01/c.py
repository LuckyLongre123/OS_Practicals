import os
import time

print("main program started")

pid = os.fork()

if pid < 0:
    print("fork failed!")
else:
    if pid == 0:
        print("this is child process")
        my_pid = os.getpid()

        print("child's PID: " + str(my_pid))
        time.sleep(2)

        print("child work done")
    else:
        my_pid = os.getpid()
        print("Parent's PID: " + str(my_pid))

        child_pid = os.wait()
        print("parent process Child: " + str(child_pid[0]) + " finished with status " + str(child_pid[1]))
        
        print("parent process terminated")
