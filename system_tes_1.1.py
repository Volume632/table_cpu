import psutil
from tabulate import tabulate

def get_processes_info():
    processes_info = []
    for process in psutil.process_iter(['name', 'pid', 'cpu_percent', 'username']):
        try:
            process_info = [
                process.info['name'],
                process.info['pid'],
                process.info['cpu_percent'],
                process.info['username']
            ]
            processes_info.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes_info

def get_system_info():
    # Загрузка процессора и памяти
    cpu_load = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    # Информация о диске
    disk_info = psutil.disk_partitions()
    
    # Информация о сети
    network_interfaces = psutil.net_if_addrs()
    
    return cpu_load, memory_usage, disk_info, network_interfaces

def main():
    processes_info = get_processes_info()
    system_info = get_system_info()
    
    headers_processes = ["Name", "PID", "CPU%", "UserName"]
    print("Processes:")
    print(tabulate(processes_info, headers=headers_processes))
    
    cpu_load, memory_usage, disk_info, network_interfaces = system_info
    
    print("\nSystem Info:")
    print(f"CPU Load: {cpu_load}%")
    print(f"Memory Usage: {memory_usage}%")
    
    print("\nDisk Info:")
    print(tabulate(disk_info, headers=["Drive", "Mountpoint", "Type", "Options"]))
    
    print("\nNetwork Interfaces:")
    for interface, addresses in network_interfaces.items():
        print(f"Interface: {interface}")
        for address in addresses:
            print(f"  {address.family.name}: {address.address}")
        
if __name__ == "__main__":
    main()