def init_console():
    try:
        with open("data.txt","r") as file:
            print("Database ready init done!")
    except:
        print("Database not found!, Creadted!")
        with open("data.txt","w",encoding="utf-8") as file:
            nik = input("Masukan NIK :")
            nama = input("Masukan Nama :")
            alamat = input("Alamat :")
            data_str = f"{nik},{nama},{alamat}"
            file.write(data_str)