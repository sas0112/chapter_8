def get_formatted_name(first_name, middle_name, last_name):
    """this function gives you the neated formattd name"""
    if middle_name:
        full_name = first_name.title() + " " + last_name.title()
    else:
        full_name = first_name.title() + " " + last_name.title()
    return full_name


musician = get_formatted_name("jimi", "hendrix")
print(musician)
