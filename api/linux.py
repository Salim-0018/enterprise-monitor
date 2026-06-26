import psutil
import platform
import socket
from datetime import datetime

def get_linux_stats():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "kernel": platform.release(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "uptime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        "load_average": list(psutil.getloadavg()),
        "logged_users": len(psutil.users()),
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
