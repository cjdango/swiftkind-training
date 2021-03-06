def get_dog_name(name):
    """
    Returns the dog's name with a smile.
    """
    dog_name = name
    dog_name += ':)'
    return dog_name


def get_dog_age(dog_age):
    """
    Returns the dog's age minus 1.
    """
    dog_age -= 1
    return dog_age


def get_dog_toy_count(dog_toy_count):
    """
    Returns the dog's toy count mutiplied by 4.
    """
    dog_toy_count *= 4
    return dog_toy_count


def get_dog_friends_count(dog_friends_count):
    """
    Returns the dog's friends count divided by 2.
    """
    dog_friends_count /= 2
    return dog_friends_count


def get_dog_treats_count(dog_treats_count):
    """
    Returns the remaining dog's treats  count.
    """
    dog_treats_count %= 5
    return dog_treats_count


def get_dog_sibling_count(dog_sibling_count):
    """
    Returns the dog's sibling count^2.
    """
    dog_sibling_count **= 2
    return dog_sibling_count


def get_dog_son_count(dog_son_count):
    """
    Returns the dog's son count floor divide by 3.
    """
    dog_son_count //= 3
    return dog_son_count
