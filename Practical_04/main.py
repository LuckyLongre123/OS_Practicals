import stat
import time
import pwd
    
try:
  file_stat = os.stat(filename)
        
  print("File: " + filename)
  print("Size: " + file_stat.st_size + " bytes")
  print("Inode: " + file_stat.st_ino)
        
  try:
    owner = pwd.getpwuid(file_stat.st_uid).pw_name
    print("Owner: " + owner + " (UID: " + file_stat.st_uid + ")")
  except:
    print("Owner UID: " + file_stat.st_uid)
        
    mode = file_stat.st_mode
    perms = stat.filemode(mode)
    print("Permissions: " + perms)
    print("Octal Permissions: " + oct(stat.S_IMODE(mode)))
        
    print("Last Access Time: " + time.ctime(file_stat.st_atime))
    print("Last Modification Time: " + time.ctime(file_stat.st_mtime))
    print("Last Status Change Time: " + time.ctime(file_stat.st_ctime))
        
  except FileNotFoundError:
    print("Error: File " + filename +  "not found")
    except Exception as e:
        print("Error: " + e)
