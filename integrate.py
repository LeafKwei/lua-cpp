# 将src内的所有.cpp文件合并为lua.cpp；将include内的所有.hpp文件合并为lua.hpp

import re
from pathlib import Path

INC_DIR = "./include"
SRC_DIR = "./src"

# 递归获取指定目录下所有文件的路径
def get_allfile_path(dir_path, filter="*"):
    return [ str(item) for item in Path(dir_path).rglob(filter) if item.is_file() ]

# 删除列表中符合正则表达式的文本行
def trim_on_pattern(lines, pattern, direction):
    start = 0
    end = len(lines)
    step = 1

    # 根据遍历顺序调整初始值(asc正序，dec逆序)
    if direction == "dec":
        start = end - 1
        end = -1
        step = -1

    for idx in range(start, end, step):
        if re.search(pattern, lines[idx]):
            del lines[idx]
            break

# 收集头文件依赖关系
def save_dependencies(lines, header_include_std, header_include_usr):
    pass

# 1.读取文件，删除用于保证头文件唯一性的XXX_HPP宏和对应的条件编译指令
# 2.将处理后的文件另存为备份，等待后续合并
# 3.统计头文件内的依赖关系
def preprocess_file(header, header_include_std, header_include_usr):
    path = Path(header).resolve()
    parent = path.parent
    basename = path.name
    lines = []
    
    with open(header, "r", encoding="utf-8") as rstream:
        lines = rstream.readlines()

    # 裁剪语句
    trim_on_pattern(lines, "#ifndef", "asc")
    trim_on_pattern(lines, "#define", "asc")
    trim_on_pattern(lines, "#endif", "dec")

    # 收集头文件依赖关系
    save_dependencies(lines, header_include_std, header_include_usr)

    # 另存为
    with open(f"{parent}\\{basename}.htmp", "w", encoding="utf-8") as wstream:
        wstream.writelines(lines)

# 合并头文件
def integrate_headers():
    headers = get_allfile_path("./include", "*.hpp")
    header_includes_std = []
    header_includes_usr = []

    for header in headers:
        preprocess_file(header, header_includes_std, header_includes_usr)
        

# 合并源文件
def integrate_sources():
    headers = get_allfile_path("./include", "*.cpp")
    header_includes_std = []
    header_includes_usr = []



# main
integrate_headers()
integrate_sources()