import random
import string
import hashlib

def load_dictionary(filename):
    with open(filename, 'r', encoding='iso-8859-1') as file:
        dictionary = [line.strip() for line in file]
    return dictionary

def generate_password(dictionary):
    choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    if choice == 1:
        password = random.choice(dictionary) + random.choice(string.digits) + random.choice(string.ascii_letters)
    elif choice == 2:     
        password = random.choice(string.digits) + random.choice(string.ascii_letters) + random.choice(dictionary)
    elif choice == 3:
        password = ''.join(reversed(random.choice(dictionary))) + random.choice(string.digits) + random.choice(string.ascii_letters)
    elif choice == 4:     
        password = random.choice(string.digits) + random.choice(string.ascii_letters) + ''.join(reversed(random.choice(dictionary)))
    elif choice == 5:
        password = random.choice(dictionary) + random.choice(string.digits)
    elif choice == 6:     
        password = random.choice(string.digits) + random.choice(dictionary)
    elif choice == 7:
        password = ''.join(reversed(random.choice(dictionary))) + random.choice(string.digits)
    elif choice == 8:     
        password = random.choice(string.digits) + ''.join(reversed(random.choice(dictionary)))
    password = password.strip()
    return password

def hash_password(password):
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    return sha256

# Ejemplo de uso
dictionary_file = 'rockyou.txt'  # Reemplaza con la ruta a tu archivo de diccionario
dictionary = load_dictionary(dictionary_file)
num_datasets = 5
num_passwords_per_dataset = 100

for dataset_num in range(1, num_datasets + 1):
    clear_passwords = []
    hashed_passwords = []

    for _ in range(num_passwords_per_dataset):
        password = generate_password(dictionary)
        clear_passwords.append(password)
        hashed_password = hash_password(password)
        hashed_passwords.append(hashed_password)

    # Crear un archivo para almacenar contraseñas en claro
    with open(f'clear_passwords_dataset_{dataset_num}_SHA256.txt', 'w') as clear_file:
        clear_file.write('\n'.join(clear_passwords))

    # Crear un archivo para almacenar contraseñas hasheadas
    with open(f'hashed_passwords_dataset_{dataset_num}_SHA256.txt', 'w') as hashed_file:
        hashed_file.write('\n'.join(hashed_passwords))
