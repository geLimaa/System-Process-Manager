import psutil
import time
import os

while True:
  os.system("clear")

  cpu_total = psutil.cpu_percent()
  ram_memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent

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
      process_data.append((cpu, ps))
    except(psutil.NoSuchProcess, psutil.AccessDenied):
      continue 
  process_data.sort(key=lambda x: x[0], reverse=True)

  print(f"CPU: {cpu_total}%\nRAM: {ram_memory}%\nDISK: {disk}%\n")
  print(f"{'PID':<8}{'NAME':<38}{'USER':<18}{'CPU[%]':<12}{'MEM[%]':<10}")

  for cpu, ps in process_data[:20]:
    try:
      print(f"{ps.pid:<8}"
            f"{ps.name():<38}"
            f"{ps.username():<18}"
            f"{cpu:<12}"
            f"{ps.memory_percent():<10}")
    except(psutil.NoSuchProcess, psutil.AccessDenied):
      continue 

  time.sleep(2)