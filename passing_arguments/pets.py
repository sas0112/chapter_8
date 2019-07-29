def describe_pet(animal_type, pet_name="willie"):
    """display information about a pet"""
    print("\nI have a " + animal_type.title() + "!")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + "!")


describe_pet("dog", "betty")
describe_pet("cat", "ketty")
describe_pet("alice", "shepherd")
describe_pet(pet_name="kile", animal_type="snake")
describe_pet("bird", pet_name="betty")
