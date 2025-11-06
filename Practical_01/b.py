import os

def main():
    print("main program started")

    pid = os.fork()

    if pid < 0:
        print("fork failed!")
    elif pid == 0:
        print("this is child process")
        print("child's PID: " + str(os.getpid()))
        print("Child doing child work")
        for i in range(3):
            print(f"child work:  {i}")
    else:
        print("Parent's PID: " + str(os.getpid()))
        print("parent doing parent work")
        for i in range(3):
            print(f"parent work:  {i}")
        os.wait()

main()