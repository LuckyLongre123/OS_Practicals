try:
    import psutil
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024**3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
    print(f"Free Memory: {mem.free / (1024**3):.2f} GB")
    print(f"Memory Usage: {mem.percent}%")
except ImportError:
    print("Install psutil: pip install psutil")