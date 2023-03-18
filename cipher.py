# *********
# credits to VoxelPixel https://github.com/VoxelPixel/
# Made by lucianoscarpaci https://github.com/lucianoscarpaci/
# 3/18/23
import base64

def xor_encrypt():
    msg = input("\nEnter a message to encrypt: ")
    key = input("Enter password: ")

    encrypt_it = ""
    key_itr = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[key_itr])
        encrypt_it += hex(temp)[2:].zfill(2)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0

    msg_bytes = encrypt_it.encode("ascii")
    base64_encode = base64.b64encode(msg_bytes)
    base64_str = base64_encode.decode("ascii")

    print("Encrypted message: {}".format(base64_str))


def xor_decrypt():
    base64_msg = input("\nEnter a message to decrypt: ")
    msg_bytes = base64_msg.encode("ascii")
    base64_decode = base64.b64decode(msg_bytes)
    hex_str = base64_decode.decode("ascii")

    key = input("Enter password: ")

    hex_to_uni = ""
    for i in range(0, len(hex_str), 2):
        hex_to_uni += bytes.fromhex(hex_str[i:i+2]).decode('utf-8')
    
    decrypt_it = ""
    key_itr = 0
    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(key[key_itr])
        decrypt_it += chr(temp)
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0
    print("Decrypted message: {}".format(decrypt_it))


def main():
    
    character = input("\nEnter E for encryption:\nEnter D for decryption:\nEnter Q to quit:\n$:")
    if character == 'E':
        print("\nYou choose to encrypt")
        xor_encrypt()
    elif character == 'D':
        print("\nYou choose to decrypt")
        xor_decrypt()
    elif character == 'Q':
        print("Goodbye...")
        exit(0)
    else:
        print("Invalid character")
    main()
        

if __name__ == "__main__":
    main()