def formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()


# this is an infinite loop!

while True:
    print("\nPlease tell me your name:")
    print("enter 'quit' if you want to quit")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("last name: ")
    if l_name == 'quit':
        break
    name = formatted_name(f_name, l_name)
    print("\nHello " + name + "!")

print("This program ends")
