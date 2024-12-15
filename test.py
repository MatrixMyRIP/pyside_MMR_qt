import platform
import os
from sched import scheduler

import partition
import psutil
from pip._internal.utils import subprocess
from psutil._common import bytes2human

cpu_name = platform.processor()
disc_info = psutil.disk_partitions()
disc_count = len(disc_info)
info = psutil.disk_usage('/')

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
