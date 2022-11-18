import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
            
    print("SELAMAT DATANG DI DATABASE KEPENDUDUKAN")
    print("---------------------------------------")
    CRUD.init_console()
       
    while (True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
                
        print("SELAMAT DATANG DI DATABASE KEPENDUDUKAN")
        print("---------------------------------------")

        print(f"1. Read Data NIK")
        print(f"2. Create Data NIK")
        print(f"3. Update Data NIK")
        print(f"4. Delete Data NIK\n")
        
        user_option = input("Silahkan Pilih menu di atas :")
        
        print("---------------------------------------")
        
        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")
            case _:
                print("Pilihan opsi hanya 1,2,3,4 !")
        print("---------------------------------------")
        is_done = input("Apakah akan selesai (y/n)?")
        
        if is_done == 'y' or is_done == "Y":
            break
            
print("Program Done.")            
        

        