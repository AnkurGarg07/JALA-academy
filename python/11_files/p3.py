def read_file_stream(file_path):
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            print(chunk)

# Example usage:
read_file_stream(r'D:\coding\JALA academy\python\11_files\xyz.txt')
