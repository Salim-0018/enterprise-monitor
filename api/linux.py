import psutil
import platform
import socket
from datetime import datetime

def   get_linux_stats():
      cpu = psutil.cpu_percent(interval=1)
      memory = psutil.virtual_memory().percent
      disk = psutil.disk_usage("/").percent


      if  cpu > 80 or memory > 80 or disk > 80:

           health = "Critical"

      elif  cpu >= 50 or memory >= 50 or disk >= 50:

          health = "Warning"
      else:

          health = "Healthy"


      return {
          "health": health,
          "hostname": socket.gethostname(),
          "os": platform.system(),
          "os_version": platform.version(),
          "kernel": platform.release(),
          "cpu_usage": cpu,
          "memory_usage": memory,
          "disk_usage": disk,
          "uptime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
          "load_average": list(psutil.getloadavg()),
          "logged_users": len(psutil.users()),
          "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }

