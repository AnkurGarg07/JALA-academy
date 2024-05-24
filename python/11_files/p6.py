import os

def check_file_permissions(file_path):
    has_read_access = os.access(file_path, os.R_OK)
    has_write_access = os.access(file_path, os.W_OK)
    print(f"Read access: {'Yes' if has_read_access else 'No'}")
    print(f"Write access: {'Yes' if has_write_access else 'No'}")

# Example usage:
check_file_permissions(r'D:\coding\JALA academy\python\11_files\xyz.txt')
