import os

def main():
    print("main program started")

    pid = os.fork()

    if pid < 0:
        print("fork failed!")

    if pid == 0:
        print("this is child process")
        print("child's PID: " + str(os.getpid()))  # Convert to string
    else:
        print("this is parent process")
        print("parent's PID: " + str(os.getpid()))  # Convert to string
        
if __name__ == "__main__":
    main()
