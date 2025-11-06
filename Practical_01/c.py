import os
import time

def main():
    print("main program started")

    pid = os.fork()

    if pid < 0:
        print("fork failed!")
    elif pid == 0:
        print("this is child process")
        print("child's PID: " + str(os.getpid()))
        time.sleep(2)
        print("child work done")
    else:
        print("Parent's PID: " + str(os.getpid()))
        child_pid,status = os.wait()
        print(f"parent process Child: {child_pid} finished with status {status}")
        print("parent process terminated")

main()