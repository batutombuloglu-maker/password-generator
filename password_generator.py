import random
import string

def generate_password():
    print("--- SECURE PASSWORD GENERATOR V1.0 ---")
    
    # Asking user for password length / Kullanıcıdan şifre uzunluğunu isteme
    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("Error: Please enter a valid number!")
        return

    # Defining character set / Karakter seti
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generating the password / Şifre oluşturma
    password = ""
    for i in range(length):
        password += random.choice(characters)
        
    print("\n---------------------------------")
    print(f"Generated Secure Password: {password}")
    print("---------------------------------")

# Run the program / Programı çalıştır
if __name__ == "__main__":
    generate_password()
