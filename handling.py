def read_file():
    while True:
        try:
            # Ask user for filename
            filename = input("Please enter the name of the file you want to read: ")
            
            # Try to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile contents:")
                print("--------------")
                print(content)
                return content
                
        except FileNotFoundError:
            print(f"\nError: The file '{filename}' does not exist.")
            print("Please try again with a valid filename.")
            
        except PermissionError:
            print(f"\nError: You don't have permission to read the file '{filename}'.")
            print("Please check the file permissions and try again.")
            
        except IOError as e:
            print(f"\nError: Could not read the file '{filename}'.")
            print(f"System error: {str(e)}")
            print("Please try again with a different file.")
            
        except Exception as e:
            print(f"\nAn unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    read_file()
