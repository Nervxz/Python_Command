import os

# Current directory
current_dir = os.getcwd()

# Func ls
def ls():
    global current_dir
    for item in os.listdir(current_dir):
        print(item)

# Func cd
def cd(directory):
    global current_dir
    if directory == "..":
        # Move up one directory
        new_dir = os.path.normpath(os.path.join(current_dir, ".."))
    else:
        # Move into the specified directory
        new_dir = os.path.normpath(os.path.join(current_dir, directory))

    if os.path.isdir(new_dir):
        try:
            os.chdir(new_dir)
            current_dir = new_dir
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Error: {directory} is not a directory.")

# Func pwd
def pwd():
    return os.getcwd()


# Func find 

def find(substring):
    global current_dir
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if substring in file:
                print(os.path.join(root, file))
        for dir in dirs:
            if substring in dir:
                print(os.path.join(root, dir))

'''
 def find(substring):
    global current_dir
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if substring in file:
                print(os.path.join(root, file))
        for dir in dirs:
            if substring in dir:
                print(os.path.join(root, dir))
'''

# Loop to take user input
while True:
    user_input = input(f"{current_dir} $ ")
    if user_input == "ls":
        ls()
    elif user_input.startswith("cd "):
        directory = user_input.split()[1]
        cd(directory)
    elif user_input == "pwd":
        pwd()
    elif user_input.startswith("find "):
        substring = user_input.split()[1]
        found_items = find(substring)
        if found_items:
            for item in found_items:
                print(item)
        else:
            print(f"No files or directories found containing '{substring}'")    
    elif user_input == "exit":
        print("Exiting...")
        break
    else:
        print("Re-enter Command.")