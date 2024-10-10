import random
import string
import hashlib

def generate_password(length, complexity):
    if complexity == 'lower':
        characters = string.ascii_lowercase
    elif complexity == 'upper':
        characters = string.ascii_uppercase
    elif complexity == 'numeric':
        characters = string.digits
    elif complexity == 'alphanumeric':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        pass
    
    return ''.join(random.choice(characters) for _ in range(length))

def generate_password_list(complexity, length, num_passwords):
    password_list = set()
    while len(password_list) < num_passwords:
        password = generate_password(length, complexity)
        md5_password = hashlib.md5(password.encode()).hexdigest()
        password_list.add((password, md5_password))
    return list(password_list)


num_passwords_per_length = 100
complexities = ['lower', 'upper', 'numeric', 'alphanumeric']
password_lengths = [3, 4, 5, 6, 7]

for complexity in complexities:
    for length in password_lengths:
        clear_file_name = f'{complexity}_len{length}_clear_MD5.txt'
        hash_file_name = f'{complexity}_len{length}_hashes_MD5.txt'
        
        with open(clear_file_name, 'w') as clear_file, open(hash_file_name, 'w') as hash_file:
            password_list = generate_password_list(complexity, length, num_passwords_per_length)
            for password, password_hash in password_list:
                clear_file.write(password + '\n')
                hash_file.write(password_hash + '\n')