def write_to_file():
    with open("my_life.txt", "w") as file:
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
