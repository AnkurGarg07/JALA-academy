try:
    import os

    
    with open(r"D:\coding\JALA_ academy\python\11_files\xyz.txt", "w") as file:
        pass
except IOError as e:
    print(f"IOError: {e}")
