def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
        print(f"Successfully written to {file_path}")

# Example usage:
write_text_file(r'D:\coding\JALA academy\python\11_files\xyz.txt', 'Hello,Ankur writing in this file')
