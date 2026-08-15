from process_manager.manager import list_processes
from process_manager.display import manage_process
from process_manager.process import get_process_info
from process_manager.display import print_menu, print_process_info, build_process_dashboard
from process_manager.display import print_error, print_info, print_success

def menu():
  while True:
    print_menu()
    option = input("\nChoose an option: ")

    if option == "1":
      sort = input("Sort by [CPU/Memory]: ").lower()

      if(sort not in ["cpu", "memory"]):
        print("Invalid sorting option")
        continue 
      try:
        limit = int(input("Number of processes: "))
      except ValueError:
        print_error("Invalid number")
        continue
      
      list_processes(sort, limit)

    elif option == "2":
      try:
        pid = int(input("PID: "))
      except ValueError:
        print_error("Invalid PID")
        continue

      info = get_process_info(pid)
      if info is None:
        print_error(f"Process {pid} does not exist")
      elif info == "access_denied":
        print_error(f"Acess denied to process {pid}")
      else:
        print_process_info(info)

    elif option == "3":
      try:
        pid = int(input("PID: "))
      except ValueError:
        print_error("Invalid PID")
        continue 

      manage_process(pid)

    elif option == "4":
      print_info("Exiting...")
      break

    else:
      print_error("Invalid option")