from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress

console = Console()

def build_system_usage(cpu, memory, disk):
  progress = Progress()

  progress.add_task(
    "[cyan]CPU[/cyan]",
    total=100,
    completed=cpu
  )

  progress.add_task(
    "[green]RAM[/green]",
    total=100,
    completed=memory
  )

  progress.add_task(
    "[yellow]DISK[/yellow]",
    total=100,
    completed=disk
  )

  return Panel(
    progress,
    title="[bold cyan]System Usage[/bold cyan]",
    border_style="cyan"
  )


def build_process_table(process_data, limit):
  table = Table(
    title="Running Processes",
    header_style="bold cyan"
  )

  table.add_column("PID", width=8, justify="right")
  table.add_column("NAME", width=38, no_wrap=True)
  table.add_column("USER", width=18, no_wrap=True)
  table.add_column("CPU %", width=10, justify="right")
  table.add_column("MEM %", width=10, justify="right")

  for cpu, memory, process in process_data[:limit]:
    try:
      table.add_row(
        str(process.pid),
        process.name(),
        process.username() or "-",
        f"{cpu:.1f}",
        f"{memory:.1f}"
      )
    except Exception:
      continue

  return table

def build_process_dashboard(cpu, memory, disk, process_data, limit):
  system_usage = build_system_usage(cpu, memory, disk)
  process_table = build_process_table(process_data, limit)

  return Group(
    system_usage,
    process_table
  )

def print_process_info(info):
  console.print(
    Panel(
      f"[bold]PID:[/bold] {info['pid']}\n"
      f"[bold]Name:[/bold] {info['name']}\n"
      f"[bold]User:[/bold] {info['username']}\n"
      f"[bold]Status:[/bold] {info['status']}\n"
      f"[bold]Parent PPID:[/bold] {info['ppid']}\n"
      f"[bold]Threads:[/bold] {info['threads']}\n"
      f"[bold]CPU:[/bold] {info['cpu']:.1f}%\n"
      f"[bold]Memory:[/bold] {info['memory']:.1f}%",
      title="[bold cyan]Process Information[/bold cyan]",
      border_style="cyan"
    )
  )

def print_menu():
  console.print(
    Panel(
      "[bold cyan]SYSTEM PROCESS MANAGER[/bold cyan]\n\n"
      "[1] List processes\n"
      "[2] Process information\n"
      "[3] Manage process\n"
      "[4] Exit",
      title="Main Menu",
      border_style="cyan"
    )
  )

def print_manage_menu(process):
  console.print(
    Panel(
      f"[bold]Process:[/bold] {process.name()}\n"
      f"[bold]PID:[/bold] {process.pid}\n\n"
      "[1] Terminate\n"
      "[2] Kill\n"
      "[3] Suspend\n"
      "[4] Resume\n"
      "[5] Back",
      title="[bold cyan]Manage Process[/bold cyan]",
      border_style="red"
    )
  )

def print_success(message):
  console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message):
  console.print(f"[bold red]✗[/bold red] {message}")


def print_info(message):
  console.print(f"[bold yellow]![/bold yellow] {message}")