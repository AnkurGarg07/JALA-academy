def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

read_text_file(r'D:\coding\JALA academy\python\11_files\xyz.txt')
