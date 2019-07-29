def make_shirt(message="l love python", size="l"):
    """this function tell us to make a shirt"""
    message = str(message)
    size = str(size)
    print("\nmaking shirt that is the size of " + size.upper() +
          " with the message: "
          "\n" + message)


make_shirt("al is well!", "l")
make_shirt(size="m", message="victory")
make_shirt()
