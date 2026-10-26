import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Membaca daftar 10.000 password
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]

    # Jika use_salts bernilai True, baca juga daftar salt dari known-salts.txt
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f]

        for password in passwords:
            for salt in salts:
                # 1. Coba prepend salt (salt ditaruh di depan password)
                prepended = hashlib.sha1((salt + password).encode("utf-8")).hexdigest()
                if prepended == hash:
                    return password

                # 2. Coba append salt (salt ditaruh di belakang password)
                appended = hashlib.sha1((password + salt).encode("utf-8")).hexdigest()
                if appended == hash:
                    return password
    else:
        # Jika use_salts bernilai False, langsung hash password tanpa salt
        for password in passwords:
            hashed_pw = hashlib.sha1(password.encode("utf-8")).hexdigest()
            if hashed_pw == hash:
                return password

    # Jika tidak ada yang cocok setelah seluruh daftar diperiksa
    return "PASSWORD NOT IN DATABASE"