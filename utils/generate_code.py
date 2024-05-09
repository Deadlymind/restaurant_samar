import random
import string

def generate_code(length=8):
    characters = string.ascii_uppercase + string.digits  # alphabets and numbers
    code = ''.join(random.choice(characters) for _ in range(length))
    return code
