# -*- coding = utf-8 -*-
# @Time : 2020/11/29 21:09
# @Author : 水神与月神
# @File : ReadFile2.py
# @Software : PyCharm


# 24 401*2
# 40 501*4

# %%
import os
import numpy as np
import cv2 as cv


# %%
# 这个函数用来按字节读取数据，num为读取的字节的个数，bytestream是打开的文件

def read_uint_num(bytestream, num):
    dt = np.dtype(np.uint8)  # 读取字节
    return np.frombuffer(bytestream.read(num), dtype=dt)


# %%
# 这个函数用来生成文件


def my_read(fileName):
    array = []
    with open(fileName, "rb") as f:
        while True:
            discard24uint8 = read_uint_num(f, 40)
            needed = read_uint_num(f, 2004)
            if len(needed) == 0:
                break
            needed = needed[::-1]
            array.append(needed)

    array = np.concatenate(array, axis=0)
    dt = np.dtype(np.uint8)
    ndarray = np.array(array, dtype=dt)
    try:
        ndarray = ndarray.reshape(-1, 2004)
    except ValueError as e:
        print("图片转换失败！")

    ndarray = np.transpose(ndarray)
    ndarray = ndarray.astype(np.uint8)
    return ndarray


def save(name_read, save_path_root, path_save, name_save):
    path_names = os.listdir(save_path_root)
    if path_save in path_names:
        pass
    else:
        os.makedirs(os.path.join(save_path_root, path_save))

    out = my_read(name_read)
    lf = os.path.join(os.path.join(save_path_root, path_save), name_save)
    cv.imwrite(lf + ".png", out)


if __name__ == '__main__':
    read_path = r'C:/Users/dell/Desktop/SPEC000101'
    save_path = r'C:/Users/dell/Desktop/'
    save(read_path, save_path, '001', 'SPEC000101')





    # read_path_root = "G:/learmonth原始数据/"
    # save_path_root = "G:/learmonth_pics/"
    #
    # path_names = os.listdir(read_path_root)
    #
    # for path_name in path_names:
    #     # 将path_name变成完整的路径的名字
    #     path_name_read = os.path.join(read_path_root, path_name)
    #
    #     file_names = os.listdir(path_name_read)
    #     for file_name in file_names:
    #         if file_name[0] == "L":
    #             full_name_read = os.path.join(path_name_read, file_name)  # 完整的路径和名称
    #             save(full_name_read, save_path_root,path_name, file_name)
    #             print(file_name + ".png" + "保存成功")


