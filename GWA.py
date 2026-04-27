def find_top_student(filename):
    highest_gwa = None
    top_student = ""

    # Open and read the file
    with open(filename, "r") as file:
        for line in file:
            # Each line should look like: Name GWA
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # skip malformed lines

            name, gwa_str = parts
            try:
                gwa = float(gwa_str)
            except ValueError:
                continue  # skip if GWA is not a number

            # Compare to find highest
            if highest_gwa is None or gwa < highest_gwa:
                highest_gwa = gwa
                top_student = name

    # Output result
    if top_student:
        print(f"Top student: {top_student} with GWA {highest_gwa}")
    else:
        print("No valid student data found.")

# Example usage
find_top_student("student_grades.txt")
