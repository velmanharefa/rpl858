def pulsa(angka):
    if angka == 1:
        print("Silahkan masukkan nomor tujuan Transfer Pulsa:")
        print("(contoh: 08xxxx atau 628xxxx)")
        a1 = int(input())
        print("Silahkan masukkan jumlah pulsa yang akan")
        print("ditransfer : (min 5000, max 1jt & tanpa. (titik)")
        print("atau, (koma))")
        b1 = int(input())
    elif angka == 2:
        print("Silahkan masukkan nomor tujuan Minta Pulsa:")
        print("(contoh: 08xxxx atau 628xxxx)")
        a2 = str(input())
        if a2[0:2] == "08" or a2[0:3] == "628" :
            print("Silahkan masukkan jumlah pulsa yang akan\ndiminta : (min 5000, max 1jt & tanpa. (titik) atau , (koma))")
            a21 = int(input())
            if a21 >= 5000 and a21 <= 1000000:
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