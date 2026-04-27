def write_to_file():
    with open(r"C:\Users\vicson pogi\Desktop\New folder (2)\my_life.txt", "a") as file:
        while True:
            line = input("Enter line: ")
            file.write(line + "\n")

            choice = input("Are there more lines y/n? ").strip().lower()
            if choice != "y":
                break

    
    with open("my_life.txt", "r") as file:
        print("\nContents of my_life.txt:")
        print(file.read())

write_to_file()
