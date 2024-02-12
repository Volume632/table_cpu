import psutil
from tabulate import tabulate

def get_processes_info():
    processes_info = []
    for process in psutil.process_iter():
        try:
            process_info = [
                process.name(),
                process.pid,
                process.cpu_percent(interval=None),
                process.memory_percent(),
                process.username(),
            ]
            processes_info.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes_info

def main():
    processes_info = get_processes_info()
    headers = ["Name", "PID", "CPU%", "Memory%", "UserName", "VMemory"]
    print(tabulate(processes_info, headers=headers))

if __name__ == "__main__":
    main()