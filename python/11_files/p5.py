def read_file_at_index(file_path, index):
    with open(file_path, 'rb') as file:
        file.seek(index)
        content = file.read()
        print(content)

# Example usage:
read_file_at_index(r'D:\coding\JALA academy\python\11_files\xyz.txt', 15)
