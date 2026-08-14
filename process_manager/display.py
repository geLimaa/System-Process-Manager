import psutil

def print_system_usage(cpu, memory, disk):
  print(
    f"CPU: {cpu}%\n"
    f"RAM: {memory}%\n"
    f"DISK: {disk}%\n"
  )

def print_processes(process_data, limit):
  print(
    f"{'PID':<8}"
    f"{'NAME':<38}"
    f"{'USER':<18}"
    f"{'CPU[%]':<12}"
    f"{'MEM[%]':<10}"
  )

  for cpu, memory, process in process_data[:limit]:
    try:
      print(
        f"{process.pid:<8}"
        f"{process.name():<38}"
        f"{process.username():<18}"
        f"{cpu:<12}"
        f"{memory:<10}"
      )

    except (psutil.NoSuchProcess, psutil.AccessDenied):
      continue

def print_process_info(info):
  print(
      f"PID: {info['pid']}\n"
      f"Name: {info['name']}\n"
      f"User: {info['username']}\n"
      f"Status: {info['status']}\n"
      f"Parent PPID: {info['ppid']}\n"
      f"Threads: {info['threads']}\n"
      f"CPU: {info['cpu']}\n"
      f"Memory: {info['memory']}\n"
  )