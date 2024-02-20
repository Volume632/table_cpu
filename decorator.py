import os
import psutil

def write_to_file(system_tes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(system_tes, 'w') as file:
                for process in result:
                    file.write(f"Name: {process['name']}\n")
                    file.write(f"PID: {process['pid']}\n")
                    file.write(f"CPU: {process['cpu']}\n")
                    file.write(f"Memory: {process['memory']}\n")
                    file.write(f"UserName: {process['username']}\n")
            return result
        return wrapper
    return decorator

@write_to_file('processes_info.txt')
def get_processes_info():
    processes_info = []
    for process in psutil.process_iter():
        try:
            process_info = {
                'name': process.name(),
                'pid': process.pid,
                'cpu': process.cpu_percent(interval=None),
                'memory': process.memory_percent(),
                'username': process.username(),
            }
            processes_info.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes_info

if __name__ == "__main__":
    get_processes_info()