PLACEHOLDER = "[name]"
"""Placeholder is simply an example used"""
with open("path") as names_file:
    names = names_file.readlines()
    
with open("path") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name_stripped = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)
        with open(f"path{name_stripped}.text", mode="w") as finished_letter:
            finished_letter.write(new_letter)
    

            