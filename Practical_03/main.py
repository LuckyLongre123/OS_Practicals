try:
  import psutil
  mem = psutil.virtual_memory()
  print("Total Memory: " + mem.total / (1024**3):.2f + "GB")
  print("Available Memory: " + mem.available / (1024**3):.2f + "GB")
  print("Used Memory: " + mem.used / (1024**3):.2f + "GB")
  print("Free Memory: " + mem.free / (1024**3):.2f + "GB")
  print("Memory Usage: " + mem.percent}%")
  
except ImportError:
    print("Install psutil: pip install psutil")
