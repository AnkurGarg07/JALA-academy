def read_file_random_access(file_path, position, size):
    with open(file_path, 'rb') as file:
        file.seek(position)
        content = file.read(size)
        print(content)


read_file_random_access(r'D:\coding\JALA academy\python\11_files\xyz.txt', 10, 20)
