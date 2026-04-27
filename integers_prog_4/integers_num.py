def process_integers():
    try:
        # Read integers from source file
        with open("integers.txt", "r") as infile:
            numbers = infile.readlines()

        # Convert each line to an integer
        numbers = [int(num.strip()) for num in numbers]

        # Separate processing
        with open("double.txt", "w") as even_file, open("triple.txt", "w") as odd_file:
            for num in numbers:
                if num % 2 == 0:
                    # Square of even numbers
                    even_file.write(str(num ** 2) + "\n")
                else:
                    # Cube of odd numbers
                    odd_file.write(str(num ** 3) + "\n")

        print("Processing complete! Check double.txt and triple.txt.")

    except FileNotFoundError:
        print("Error: integers.txt not found.")
    except ValueError:
        print("Error: integers.txt must contain only integers.")

# Example usage
process_integers()
