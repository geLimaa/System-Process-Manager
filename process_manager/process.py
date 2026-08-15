import psutil
import time
from process_manager.display import print_error, print_info, print_success

def get_process_info(pid):
  try:
    process = psutil.Process(pid)

    process.cpu_percent()
    time.sleep(2)

    return {
      "pid": process.pid,
      "name": process.name(),
      "username": process.username(),
      "status": process.status(),
      "ppid": process.ppid(),
      "threads": process.num_threads(),
      "cpu": process.cpu_percent(),
      "memory": process.memory_percent()
    }

  except psutil.NoSuchProcess:
    return None

  except psutil.AccessDenied:
    return "access_denied"

