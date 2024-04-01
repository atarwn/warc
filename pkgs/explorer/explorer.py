import shutil
import os
def explorer():
    import os

def list_files(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)

def main():
    current_directory = os.getcwd()
    while True:
        print(f"Current Directory: {current_directory}")
        print("1. List files")
        print("2. Change directory")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_files(current_directory)
        elif choice == '2':
            new_directory = input("Enter the directory path: ")
            if os.path.exists(new_directory) and os.path.isdir(new_directory):
                current_directory = new_directory
            else:
                print("Invalid directory path.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()