# 将src内的所有.cpp文件合并为lua.cpp；将include内的所有.hpp文件合并为lua.hpp

from pathlib import Path

INC_DIR = "./include"
SRC_DIR = "./src"

# 递归获取指定目录下所有文件的路径
def get_allfile_path(dir_path, filter="*"):
    return [ str(item) for item in Path(dir_path).rglob(filter) if item.is_file() ]

    
            