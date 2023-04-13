import sqlite3

con = sqlite3.connect("spotify.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS spotify(isim TEXT, sarkici TEXT, sirket TEXT, sure INT)")
    con.commit()

tablo_olustur()

def veri_ekle():
    cursor.execute("INSERT INTO spotify VALUES('Gel Düşümdeki Sevgili', 'Ahmet Kaya', 'Kayagam', 3)")
    con.commit()

#veri_ekle()

def veri_ekle2():
    isim = input("Şarkı ismi: ")
    sarkici = input("Sanatçı: ")
    sirket = input("Yapımcı: ")
    sure = int(input("Süre(dk): "))
    cursor.execute("INSERT INTO spotify VALUES(?,?,?,?)", (isim, sarkici, sirket, sure))
    con.commit()

#veri_ekle2()

def güncelle(eski_sarkici,yeni_sarkici):
    cursor.execute("Update spotify set sarkici= ? where sarkici = ? ",(yeni_sarkici,eski_sarkici))
    con.commit()
#güncelle("Abdal","Ahmet Aslan")

def sil(isim):
    cursor.execute("Delete from spotify isim = ?",(isim,))
    con.commit()
#sil("Gel")

def topla():
    pass
    cursor.execute("Select sure from spotify")
    toplam += cursor.fetchall()
    print(toplam)
#topla()

con.close()