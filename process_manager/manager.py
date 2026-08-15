from process_manager.monitor import get_system_usage, get_processes
from process_manager.display import build_process_dashboard, print_manage_menu
from rich.live import Live 

def list_processes(sort, limit):
  with Live(refresh_per_second=2) as live: 
    try:
      while True:
        cpu, memory, disk = get_system_usage()
        process_data = get_processes()

        if sort == "cpu":
          process_data.sort(key=lambda x: x[0],reverse=True)
        else:
          process_data.sort(key=lambda x: x[1],reverse=True)

        dashboard = build_process_dashboard(
          cpu,
          memory,
          disk,
          process_data,
          limit
        )

        live.update(dashboard)
        
    except KeyboardInterrupt:
      print("\nReturning to menu...")

def manage_process(pid):
  try:
    process = psutil.Process(pid)

    while True:
      print_manage_menu(pid)

      option = input("\nChoose an option: ")

      if option == "1":
        confirm = input(f"\nAre you sure you want to terminate {process.name()} ({pid})? [y/n]").lower()

        if confirm == "y":
          process.terminate()
          print_success("Process terminated")
          break 
        elif confirm == "n":
          print_info("Operation cancelled")
        else:
          print_error("Invalid option")
          
      elif option == "2":
        confirm = input(f"\nAre you sure you want to kill {process.name()} ({pid})? [y/n]").lower()

        if confirm == "y":
          process.kill()
          print_success("Process killed")
          break 
        elif confirm == "n":
          print_info("Operation cancelled")
        else:
          print_error("Invalid option")

      elif option == "3":
        process.suspend()
        print_success("Process suspended")
      elif option == "4":
        process.resume()
        print_success("Process resumed")
      elif option == "5":
        print_info("Exiting...")
        break 
      else:
        print_error("Invalid option")

  except psutil.NoSuchProcess:
    print_error(f"Process {pid} does not exist")
  except psutil.AccessDenied:
    print_error(f"Access denied to process {pid}")