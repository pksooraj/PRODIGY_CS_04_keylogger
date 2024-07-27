from cryptography.fernet import Fernet

# Define the files
log_file = "encrypted_key_log.txt"
key_file = "key.key"
decrypted_log_file = "decrypted_key_log.txt"

# Load the encryption key
with open(key_file, "rb") as kf:
    key = kf.read()

cipher_suite = Fernet(key)

# Function to decrypt the log file
def decrypt_log_file():
    with open(log_file, "rb") as lf, open(decrypted_log_file, "wb") as dlf:
        for line in lf:
            decrypted_data = cipher_suite.decrypt(line.strip())
            dlf.write(decrypted_data + b'\n')

# Decrypt the log file
decrypt_log_file()
