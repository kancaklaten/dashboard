# Simulasi data user dan password
user_data = {
    "admin": "admin",
    "user1": "admin"
}

def login():
    print("=== Halaman Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in user_data and user_data[username] == password:
        print(f"Login berhasil. Selamat datang, {username}!")
    else:
        print("Login gagal. Username atau password salah.")

# Menjalankan program login
login()
