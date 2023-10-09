def validation_number(number):
    if len(str(number)) == 11 or len(str(number)) == 12:
        if str(number)[0:2] == '08' or str(number)[0:2] == '62':
            return True
        else:
            return False
def check_pulsa(have_pulsa, need_pulsa):
    if have_pulsa >= need_pulsa:
        return True
    else:
        return False
def pulsa(angka):
    if angka == 1:
        print("Silahkan masukkan nomor tujuan Transfer Pulsa:\n (contoh: 08xxxx atau 628xxxx)")
        nomor = str(input())
        
        if validation_number(nomor) == False:
            print("nomor yang kamu masukan invalid silahkan menggunakan format: 08xxxx atau 628xxxx")
            exit()
        print("Silahkan masukkan jumlah pulsa yang akan\nditransfer : (min 5000, max 1jt & tanpa. (titik)\natau, (koma))")
        nominal = int(input())
        if nominal < 5000:
            print("Jumlah pulsa yang Anda masukkan kurang dari Rp5000")
            exit()

        print(f"Hati2 penipuan. Anda akan Transfer\nPulsa {nominal} ke {nomor}?\n(Biaya 1850 & 1 Poin undian TP\niPhone14)\n1.Ya\n0.Home")
        confirm = int(input())
        if confirm == 1:
            if check_pulsa(10000, nominal) == False:
                print("Maaf, pulsa Anda tidak mencukupi untuk melakukan transfer pulsa.")
                exit()
            print("Terima kasih permintaan Anda sedang diproses.")
        elif confirm == 0:
            main()
        else:
            print("Maaf, input Anda salah. Silahkan coba lagi.")
            exit()

    elif angka == 2:
        print("Silahkan masukkan nomor tujuan Minta Pulsa:")
        print("(contoh: 08xxxx atau 628xxxx)")
        a2 = str(input())
        if a2[0:2] == "08" or a2[0:3] == "628" :
            print("Silahkan masukkan jumlah pulsa yang akan\ndiminta : (min 5000, max 1jt & tanpa. (titik) atau , (koma))")
            a21 = int(input())
            if a21 <= 5000 or a21 >= 1000000:
                print ("anda akan meminta pulsa", str(a21),"ke nomor", str(a2), "? (biaya 100)")
                print("1.Ya")
                print("2.Tidak")
                print("0.Home")
                a22 = int(input())
                if a22 == 1:
                    print ("Terima kasih permintaan Anda sedang diproses")
                    print ("*iklan* apakah mau mengambil penawaran iklan ?")
                    print("1.Iya")
                    print("2.Tidak")
                    a221 = int(input())
                    if a221 == 1:
                        print("*menu iklan")
                    elif a221 == 2:
                        print(" ")
                        exit
                elif a22 == 2:
                    exit
            else:
                print("Maaf nominal yang Anda masukan tidak sesuai.")
                exit
        else:
            print("Nomor yang anda masukkan tidak valid")
            exit
    
    elif angka == 3:
        print("Silahkan masukkan nomor tujuan yang anda Auto Transfer Pulsa:")
        a3 = int(input())
    elif angka == 4:
        print("Silahkan masukkan nomor tujuan yg akan")
        print("dihapus dari list Auto Transfer Pulsa:")
        a4 = int(input())
    elif angka == 5:
        print("Terima kasih permintaan Anda sedang diproses.")
        print("Sampaikan pd JIWA BERSEDIH! Lagu viral")
        print("dr Ghea Indrawari di LangitMusik Midium")
        print("Rp4400/3hr. Mau?")
        print("1.Ya")
        print("2.Tidak")
        a5 = int(input())
        if a5 == 1:
            print("Terima kasih permintaan Anda sedang di proses")
        else:
            print("Terima kasih.")
    else:
        print("Jumlah kupon Anda adalah : 0 Kupon")

def main():
    print("Mau Samsung Fold 4 dr Aldi Taher?")
    print("Hub di *500*352#")
    print("1.Transfer Pulsa")
    print("2.Minta Pulsa")
    print("3.Auto TP")
    print("4.Delete Auto TP")
    print("5.List Auto TP")
    print("6.Cek Kupon Undian TP")

    angka =int (input("Masukan menu: "))
    pulsa(angka)
if __name__ == "__main__":
    main()