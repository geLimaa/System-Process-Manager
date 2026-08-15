# System Process Manager

A terminal-based system process manager built with Python, `psutil` and `Rich`.

The project allows you to monitor system resources, inspect running processes, and manage them directly from the terminal.

## Features

- Monitor CPU, RAM and disk usage
- List running processes
- Sort processes by CPU or memory usage
- Limit the number of displayed processes
- View detailed information about a process
- Terminate processes
- Kill processes
- Suspend processes
- Resume processes
- Interactive terminal interface using Rich

## Requirements

- Python 3.10+
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/System-Process-Manager.git
cd System-Process-Manager
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python3 main.py
```

The program provides an interactive menu where you can:

1. List processes
2. View process information
3. Manage a process
4. Exit

Some process management operations may require appropriate permissions.

## Project Structure

```text
System-Process-Manager/
├── main.py
├── process_manager/
│   ├── cli.py
│   ├── display.py
│   ├── manager.py
│   ├── monitor.py
│   └── process.py
├── requirements.txt
└── README.md
```

## Dependencies

- [psutil](https://github.com/giampaolo/psutil) — System and process monitoring
- [Rich](https://github.com/Textualize/rich) — Terminal formatting and UI

## Technologies

- Python
- psutil
- Rich

## License

This project is for educational and portfolio purposes.