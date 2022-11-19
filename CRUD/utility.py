import random
import string

def random_string(panjang:int) -> str:
    string_random = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return string_random