"""
**🚨🚨🚨 AVISO 🚨🚨🚨**
- ISSO É UM EXEMPLO DIDÁTICO

- Não use isso em produção mano, por favor mano
- Eu não usei números seguros, precisaria de primos muito maiores como  2^127 - 1
- Não usei proteção contra ataque de força bruta
- Não tentei garantir autenticidade
- Usei apenas um XOR, que não lá um algoritmo de criptografia, teria que ser algo como AES
"""



small_prime_G = 5
big_prime_P = 23

alice_private_key = 123
bob_private_key = 321

alice_public_key = (small_prime_G ** alice_private_key) % big_prime_P
bob_public_key = (small_prime_G ** bob_private_key) % big_prime_P

print("Alice's public key:", alice_public_key)
print("Bob's public key:", bob_public_key)

alice_shared_key = (bob_public_key ** alice_private_key) % big_prime_P
bob_shared_key = (alice_public_key ** bob_private_key) % big_prime_P

print("Alice's shared key:", alice_shared_key)
print("Bob's shared key:", bob_shared_key)

assert alice_shared_key == bob_shared_key, "Shared keys should be equal"

print("##########################")
print("Alice sends a message")
message = "Hello, Bob!"
encrypted_message = ""

print(f"{'Decrypted Char':^15} | {'Char (Bytes)':^15} | {'Shared Key (Bytes)':^20} | {'Char XOR Shared Key (Bytes)':^30} | {'Encrypted Char':^15}")
for i in range(len(message)):
    encrypted_char = chr(ord(message[i]) ^ alice_shared_key)  # XOR operation
    encrypted_message += encrypted_char
    print(f"{message[i]:^15} | {ord(message[i]):^15} | {alice_shared_key:^20} | {ord(encrypted_char):^30} | {encrypted_char:^15}")

encrypted_message_bytes = [ord(char) for char in encrypted_message]
print("Encrypted message:", encrypted_message)
print("Encrypted message (Bytes):", encrypted_message_bytes)

print("##########################")
print("Bob receives the message")
received_message = encrypted_message
decrypted_message = ""

print(f"{'Encrypted Char':^15} | {'Char (Bytes)':^15} | {'Shared Key (Bytes)':^20} | {'Char XOR Shared Key (Bytes)':^30} | {'Decrypted Char':^15}")
for i in range(len(received_message)):
    decrypted_char = chr(ord(received_message[i]) ^ bob_shared_key)  # XOR operation
    decrypted_message += decrypted_char
    print(f"{received_message[i]:^15} | {ord(received_message[i]):^15} | {bob_shared_key:^20} | {ord(decrypted_char):^30} | {decrypted_char:^15}")

decrypted_message_bytes = [ord(char) for char in decrypted_message]
print("Decrypted message:", decrypted_message)
print("Decrypted message (Bytes):", decrypted_message_bytes)


