file_path = input("Enter the full file name: ")

file_content = ""
t = True

while t== True:
    try:
        with open(file_path, 'r') as file:
            for line in file:
                file_content+=line
        print(file_content)
        t = False

    except ValueError as VE:
        print(VE)
        file_path = input("Enter the correct file name: ")
    except FileNotFoundError as e:
        print(e)
        file_path = input("Enter the correct file name: ")


user_input = input("do you want to write some data in some file: (yes or no): ")
if (user_input == "yes"):
    user_input = input("do you want to write data in the same file: (yes or no): ")
    if (user_input == "yes"):
        content = input("input the data that you want to write in file: ")
        with open(file_path, 'a') as file:
            file.write(content)
        print("data is stored and file closed")
    else:
        input_file_path = input("enter the file name that you want to create: ")
        content = input("input the data that you want to write in file: ")
        with open(input_file_path, 'a') as file:
            file.write(content)
        print("data is stored and file is closed")
else:
    print("session is closed, thank you:))))")
