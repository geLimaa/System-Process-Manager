import argparse
import os
import time
from process_manager.monitor import (get_system_usage, get_processes)
from process_manager.process import get_process_info
from process_manager.display import (print_system_usage, print_processes, print_process_info)

def list_processes(sort, limit):
  while True:
    os.system("clear")

    cpu, memory, disk = get_system_usage()
    process_data = get_processes()

    if sort == "cpu":
      process_data.sort(key=lambda x: x[0],reverse=True)
    else:
      process_data.sort(key=lambda x: x[1],reverse=True)

    print_system_usage(cpu, memory, disk)
    print_processes(process_data, limit)
    time.sleep(2)

def main():
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
    help="Sorting key"
  )

  parser.add_argument(
    "--limit",
    type=int,
    default=20,
    help="Number of processes to show"
  )

  parser.add_argument(
    "--info",
    type=int,
    metavar="PID",
    help="Show information about a process"
  )

  args = parser.parse_args()

  if args.list:
    list_processes(args.sort, args.limit)

  elif args.info is not None:
    info = get_process_info(args.info)

    if info is None:
      print(f"Process {args.info} does not exist.")

    elif info == "access_denied":
      print(f"Access denied to process {args.info}.")

    else:
      print_process_info(info)

if __name__ == "__main__":
    main()