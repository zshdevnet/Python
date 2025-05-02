try:
    with open("notes.txt", "r") as file:
        lines = file.readlines()
        if not lines:  # Empty file
            print("No notes yet.")
        else:
            for line in lines:
                print(line.strip())  # strip() removes newline characters
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print("Something went wrong:", e)
