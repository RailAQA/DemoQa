import os

path = "/Users/ann/Dowlnloads/test_file.txt"
def create_new_file():
    try:
        with open(path, "w") as file:
            s = "авто тесты\nэто круто"
            file.write(s)
            print(file.name)
    finally:
        if os.path.exists(path):
            os.remove(path)
create_new_file()