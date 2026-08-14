import os
import argparse
import psutil
import time

def list_processes():
  while True:
    os.system("clear")
    print("Listing Processes...")

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
        memory = ps.memory_percent()
        process_data.append((cpu, memory, ps))
      except(psutil.NoSuchProcess, psutil.AccessDenied):
        continue 
    
    if args.sort == "cpu":
      process_data.sort(key=lambda x: x[0], reverse=True)
    else:
      process_data.sort(key=lambda x: x[1], reverse=True)

    print(f"CPU: {cpu_total}%\nRAM: {ram_memory}%\nDISK: {disk}%\n")
    print(f"{'PID':<8}{'NAME':<38}{'USER':<18}{'CPU[%]':<12}{'MEM[%]':<10}")

    for cpu, memory, ps in process_data[:args.limit]:
      try:
        print(f"{ps.pid:<8}"
              f"{ps.name():<38}"
              f"{ps.username():<18}"
              f"{cpu:<12}"
              f"{memory:<10}")
      except(psutil.NoSuchProcess, psutil.AccessDenied):
        continue 

    time.sleep(2)

def process_info(pid):
  try:
    ps = psutil.Process(pid)

    ps.cpu_percent()
    time.sleep(2)
    cpu = ps.cpu_percent()

    print(f"PID: {pid}\n"
          f"Name: {ps.name()}\n"
          f"User: {ps.username()}\n"
          f"Status: {ps.status()}\n"
          f"Parent PPID: {ps.ppid()}\n"
          f"Threads: {ps.num_threads()}\n"
          f"CPU: {cpu}\n"
          f"Memory: {ps.memory_percent()}\n"
    )

  except psutil.NoSuchProcess:
    print(f"Process with PID {pid} does not exist.")

  except psutil.AccessDenied:
    print(f"Access denied to process {pid}.")

parser = argparse.ArgumentParser(
  description="System Process Manager"
)

parser.add_argument(
  "--list",
  action="store_true",
  help="List running processes"
)

parser.add_argument(
  "--sort",
  choices=["cpu", "memory"],
  default="cpu",
  help="Sorting key to the processes"
)

parser.add_argument(
  "--limit",
  type=int,
  default=20,
  help="Number of processes to be shown"
)

parser.add_argument(
  "--info",
  type=int,
  metavar="PID",
  help="Show information about a process"
)

args = parser.parse_args()
if args.list:
  list_processes()

if args.info is not None:
  process_info(args.info)