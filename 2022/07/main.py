#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines
def cd(line: str, curdir):
    if line == '$ ls':
        return curdir
    cd_path = line[5:]
    new_path = '/'
    if cd_path == '..':
        new_path = '/'.join(curdir.split('/')[:-2])
    elif cd_path != '/':
        new_path = curdir + cd_path

    if not new_path.endswith('/'):
        new_path += '/'
    return new_path

def add_ls(files: list, folders: list, line: str, curdir: str):
    size_or_type, file = line.split()
    if size_or_type == 'dir':
        folders.append(curdir + file + '/')
        return
    files.append((curdir + file, size_or_type))


def main():
    lines = read_file()
    curdir = "/"
    files = []
    folders = ["/"]
    response = 0
    for l in lines:
        if l.startswith('$'):
            curdir = cd(l, curdir)
        else:
            add_ls(files, folders, l, curdir)
    for fd in folders:
        size = 0
        for file_name, file_size in files:
            if file_name.startswith(fd):
                size += int(file_size)
        if size <= 100000:
            response += size

    print("Start 1: ", response)
    root_size = 0
    for file_name, file_size in files:
        if file_name.startswith('/'):
            root_size += int(file_size)
    available_space = 70000000 - root_size
    size_to_delete = 30000000 - available_space
    folder_to_delete = ('/', root_size)
    for fd in folders:
        size = 0
        for file_name, file_size in files:
            if file_name.startswith(fd):
                size += int(file_size)
        if size < folder_to_delete[1] and size >= size_to_delete :
            folder_to_delete = (fd, size)

    print("Start 2: ", folder_to_delete)

main()
