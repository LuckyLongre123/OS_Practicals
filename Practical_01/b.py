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
        print("Child doing child work")
        for i in range(3):
            print("child work: " + str(i))
    else:
        my_pid = os.getpid()
        print("Parent's PID: " + str(my_pid))
        print("parent doing parent work")
        for i in range(3):
            print("parent work: " + str(i))
        os.wait()
