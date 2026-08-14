import psutil
import time

def get_system_usage():
  cpu = psutil.cpu_percent()
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent

  return cpu, memory, disk 

def get_processes():
  processes = list(psutil.process_iter([
    'pid',
    'name',
    'username',
    'cpu_percent',
    'memory_percent'
  ]))

  for ps in processes:
    ps.cpu_percent()

  time.sleep(2)

  process_data = []

  for ps in processes:
    try:
      cpu = ps.cpu_percent()
      memory = ps.memory_percent()

      process_data.append((cpu, memory, ps))
    
    except(psutil.NoSuchProcess, psutil.AccessDenied):
      continue
  
  return process_data
    