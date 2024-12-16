# import platform
#
# import psutil
#
#
# cpu_name = platform.processor()
# disc_info = psutil.disk_partitions()
# disc_count = len(disc_info)
# info = psutil.disk_usage('/')

import win32com.client

# for i, disc in enumerate(disc_info):
#     if os.name == 'nt':
#         if 'cdrom' in disc.opts or disc.fstype == '':
#             continue
#     info = psutil.disk_usage(disc.mountpoint)
#     total = info.total // (1024 ** 3)
#     used = info.used // (1024 ** 3)
#     free = info.free // (1024 ** 3)
#     print(f"Диск {i+1}: {disc.device}: Объем: {total} Gb, Занято: {used} Gb, Свободно: {free} Gb")


# processes = [item.name() for item in psutil.process_iter()]
# print(processes)
#
# processes = []
# for process in psutil.process_iter():
#     name = process.name()
#     processes.append({'name': name})
#
# print(processes, "\n")
# print(len(processes))


# processes = psutil.process_iter(["name"])
# for item in processes:
#     print(str(item.name()))


# print(os.name)
#
# print(disc_count)
# print(cpu_name)
# print(disc_info)
# print(info)


# print(disc_info(sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')))

import subprocess

# def list_scheduled_tasks():
#     try:
#
#         result = subprocess.run(
#             ["schtasks", "/Query", "/FO", "LIST", "/V"],
#             capture_output=True,
#             text=True,
#             check=True,
#         )
#
#         tasks_output = result.stdout.split("\n\n")
#         tasks = []
#
#         for task_block in tasks_output:
#             task_info = {}
#             lines = task_block.splitlines()
#             for line in lines:
#                 if ": " in line:
#                     key, value = line.split(": ", 1)
#                     task_info[key.strip()] = value.strip()
#             if task_info:
#                 tasks.append(task_info)
#
#         return tasks
#
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка выполнения команды schtasks: {e}")
#         return []
#
#
# def print_task_info(tasks):
#     for task in tasks:
#         print(f"Имя задачи: {task.get('Task Name', 'N/A')}")
#         print(f"Время последнего выполнения: {task.get('Last Run Time', 'N/A')}")
#         print(f"Статус: {task.get('Status', 'N/A')}")
#         print(f"Следующее выполнение: {task.get('Next Run Time', 'N/A')}")
#         print(f"Активна: {task.get('Enabled', 'N/A')}")
#         print("-" * 50)
#
#
# if __name__ == "__main__":
#     tasks = list_scheduled_tasks()
#     print_task_info(tasks)


# scheduler = win32com.client.Dispatch('Schedule.Service')
# scheduler.Connect()
# tasks = scheduler.GetFolder('\\').GetTasks(0)
# for task in tasks:
#     tsk = task.Name
#     pr = str(task.Path)
#     state = task.State
#     if state == 1:
#         state = "Выполняется"
#     if state == 2:
#         state = "Готова"
#     if state == 3:
#         state = "Приостановлена"
#     last_run = task.LastRunTime
#     next_run = task.NextRunTime
#     enb = task.Enabled
#     if enb:
#         enb = "Включена"
#     if not enb:
#         enb = "Выключена"
#
#     print(f"Название задачи:{tsk}\nМестоположение задачи:{pr}\nСостояние задачи:{state}\nПоследнее время выполнения:"
#           f"{last_run}\n"
#           f"Следующее время выполнения:{next_run}\nСтатус задачи:{enb}\n---\n")


# scheduler = win32com.client.Dispatch('Schedule.Service')
# scheduler.Connect()
# tasks = scheduler.GetFolder('\\').GetTasks(0)
# task_list = ""
# for task in tasks:
#     tsk = task.Name
#     pr = str(task.Path)
#     state = task.State
#     if state == 1:
#         state = "Выполняется"
#     if state == 2:
#         state = "Готова"
#     if state == 3:
#         state = "Приостановлена"
#     last_run = task.LastRunTime
#     next_run = task.NextRunTime
#     enb = task.Enabled
#     if enb:
#         enb = "Включена"
#     if not enb:
#         enb = "Выключена"
#     task_list = f"Название задачи:{tsk}\nМестоположение задачи:{pr}\nСостояние задачи:{state}\nПоследнее время выполнения:" \
#                 f"{last_run}\n" \
#                 f"Следующее время выполнения:{next_run}\nСтатус задачи:{enb}\n---\n"
#     print(task_list)
