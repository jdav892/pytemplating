PLACEHOLDER = "[name]"
"""reading a name file to have list of names"""
with open(f"path.txt") as name_file:
    names = name_file.readlines()
    """reading the letter to know the letter content"""
with open(f"path.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        """stripping white space from the names to add to directory"""
        stripped_name = name.strip()
        """replacing placeholder value with names that are iterated through"""
        new_letter = letter_content.replace(PLACEHOLDER, name)
        """writing the new letter with the names from the name file"""
        with open(f"path{stripped_name}.txt", mode="w") as finished_file:
            finished_file.write(new_letter)