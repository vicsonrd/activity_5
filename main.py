def separate_numbers():
    try:
        # Open the input file and read all numbers
       with open("number.txt", "r") as infile:   # ❌ should be "numbers.txt"
        numbers = infile.readlines()
        
        # Convert each line to an integer
        numbers = [int(num.strip()) for num in numbers]

        # Separate even and odd numbers
        evens = [num for num in numbers if num % 2 == 0]
        odds = [num for num in numbers if num % 2 != 0]

        # Write even numbers to even.txt
        with open("even.txt", "w") as even_file:
            for num in evens:
                even_file.write(str(num) + "\n")

        # Write odd numbers to odd.txt
        with open("odd.txt", "w") as odd_file:
            for num in odds:
                odd_file.write(str(num) + "\n")

        print("Separation complete! Check even.txt and odd.txt.")

    except FileNotFoundError:
        print("Error: numbers.txt not found.")
    except ValueError:
        print("Error: numbers.txt must contain only integers.")

# Run the function
separate_numbers()
