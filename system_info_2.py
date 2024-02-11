import psutil
from tabulate import tabulate

# Функция для получения информации о загрузке процессов, памяти и слотов
def get_system_info():
    processes = len(list(psutil.process_iter()))
    memory = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    slots = psutil.cpu_count()
    return [
        ("Процессы", processes),
        ("Память (%)", memory),
        ("Swap (%)", swap),
        ("Слоты", slots)
    ]
# Функция для получения информации о диске и сети
def get_disk_and_network_info():
    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total // (1024 ** 3)  # в Гб
    used_disk = disk_usage.used // (1024 ** 3)    # в Гб
    disk_percent = disk_usage.percent

    network_info = []
    for interface, stats in psutil.net_if_stats().items():
        if stats.isup:
            network_info.append(interface)

    return [
        ("Общий объем диска (Гб)", total_disk),
        ("Использовано диска (Гб)", used_disk),
        ("Загрузка диска (%)", disk_percent),
        ("Работающие интерфейсы", ", ".join(network_info))
    ]

# Функция для получения информации о запущенных процессах
def get_running_processes():
    process_info = []
    for process in psutil.process_iter():
        try:
            process_info.append((process.pid, process.name()))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_info

# Функция для отображения информации в виде таблицы
def display_info(info, title):
    print(f"\n{title}\n")
    print(tabulate(info, headers=["Параметр", "Значение"]))

# Основная функция
def main():
    while True:
        print("\nВыбиерите действие:")
        print("1. Информация о системе (процессы, память, слоты)")
        print("2. Информация о диске и сети")
        print("3. Запущенные процессы")
        print("4. Выйти")

        choice = input("Введите номер действия:")

        if choice == "1":
            system_info = get_system_info()
            display_info(system_info, "Информация о системе (процессы, память, слоты)")
        elif choice == "2":
            disk_network_info = get_disk_and_network_info()
            display_info(disk_network_info, "Информация о диске и сети")
        elif choice == "3":
            process_info = get_running_processes()
            display_info(process_info, "Запущенные процессы")
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

# Запуск основной функции
if __name__ == "__main__":
    main()