import random
def suit_jepang():
    pilihan=["G","B","K"]
    skor_kita = 0
    skor_musuh = 0
    while skor_kita<3 and skor_musuh<3:
        pilihan_musuh = random.choice(pilihan)
        pilihan_kita = input("Apa pilihan mu?")
        if pilihan_kita.upper() == pilihan_musuh:
            print("SERI! Musuh juga memilih " + pilihan_musuh)
            print("Skormu saat ini adalah " + str(skor_kita)
                  + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
        elif pilihan_kita.upper()!=pilihan_musuh:
            if pilihan_kita.upper()=="G":
                if pilihan_musuh=="K":
                    print("Kamu menang!")
                    skor_kita+=1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
                elif pilihan_musuh=="B":
                    print("Kamu kalah!")
                    skor_musuh += 1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
            elif pilihan_kita.upper()=="B":
                if pilihan_musuh=="G":
                    print("Kamu menang!")
                    skor_kita += 1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
                elif pilihan_musuh=="K":
                    print("Kamu kalah!")
                    skor_musuh += 1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
            elif pilihan_kita.upper()=="K":
                if pilihan_musuh=="B":
                    print("Kamu menang!")
                    skor_kita+=1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
                elif pilihan_musuh=="G":
                    print("Kamu kalah!")
                    skor_musuh += 1
                    print("Skormu saat ini adalah " + str(skor_kita)
                          + "\nSkor musuh saat ini adalah " + str(skor_musuh)+"\n")
            else:
                print("Ketik \"G\" / \"B\" / \"K\"")
    if skor_musuh==3:
        print("Maaf! Kamu kalah"
              "\n Permainan selesai")
    elif skor_kita==3:
        print("Selamat! Kamu pemenangnya"
              "\n Permainan selesai")