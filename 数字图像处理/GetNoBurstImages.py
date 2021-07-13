# -*- coding = utf-8 -*-
# @Time : 2021/4/11 14:40
# @Author : 水神与月神
# @File : NoBurstImage.py
# @Software : PyCharm
#%%
import os
import mypackage.dip_function as df
import mypackage.dip_class as cf
import datetime

# %%
path_log = r"G:\LearmonthData\日志文件合并\2001-2020合并清洗.xlsx"
path_image = r"G:\LearmonthData\learmonth_pics2\{:0>2d}"
file_name_format = "LM{:0>2d}{:0>2d}{:0>2d}.srs.png"
data = df.read_log(path_log)

for one_date in data:
    start_year = one_date[0].year
    start_month = one_date[0].month
    start_day = one_date[0].day
    start_hour = one_date[0].hour

    if start_hour > 20:
        one_date[0] = one_date[0] + datetime.timedelta(hours=24)
        start_month = one_date[0].month
        start_day = one_date[0].day

    path_image = path_image.format(start_year % 100)
    file_name = file_name_format.format(start_year % 100, start_month, start_day)
    full_path = os.path.join(path_image, file_name)
    try:
        os.remove(full_path)
        print('成功移除')
    except FileNotFoundError:
        pass

# %%

path_read = r"G:\LearmonthData\learmonth_pics2\08"
path_save = r"G:\LearmonthData\New\useful\noburst"
file_names = os.listdir(path_read)

full_path = []

for file_name in file_names:
    full_path.append(os.path.join(path_read, file_name))

for i in full_path:
    cf.ImageSegmentation(i, path_save).size(500)
