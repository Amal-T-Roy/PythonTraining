import secrets

def GenerateKey():
    key = secrets.token_hex(16)
    with open("key.txt", "w") as f:
        f.write(key)
    return key


print("****Python****")
Key = GenerateKey()  # Random Key is generated
print(Key)  # Prints the key in the terminal
print("****END OF PYTHON SCRIPT****\n")
