import os
import psutil
from tabulate import tabulate

def write_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                file.write(result)
            return result
        return wrapper
    return decorator

@write_to_file('processes_info.txt')
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
    headers = ["Name", "PID", "CPU%", "Memory%", "UserName",]
    print(tabulate(processes_info, headers=headers))

if __name__ == "__main__":
    main()