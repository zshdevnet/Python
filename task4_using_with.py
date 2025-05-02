user_name = input("Your name, please: ")
personal_note = input("Write here your personal note: ")
try:
    with open("notes.txt", 'a') as file:
        file.write(f"\n[{user_name}]: {personal_note}")
    print("Note saved successfully.")
except Exception as e:
    print("Something went wrong:", e)
