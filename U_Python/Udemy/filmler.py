filmler = {
    "Kara Korsanın Laneti":{"Yapım Yılı":1957, "Imbd": 8.2, "Tür": "Korku"},
    "Sineğin İntikamı":{"Yapım Yılı":2957, "Imbd": 7.5, "Tür": "Belgesel"}
}

def filmEkle():
    film_adı= input("Film adı Girin: ")
    global filmler

    if film_adı:
        yapım_yılı=input("Yapım Yılını Girin: ")
        imbd=input("İmbd puanı girin: ")
        film_turu=input("Film Türü Girin: ")

        filmler[film_adı] = {"Yapım Yılı":yapım_yılı, "Imbd": imbd, "Tür": film_turu}
        print("Film başarıyla eklendi...")
    else:
        print("Film İsmi boş Olamaz...")

# filmEkle()
# print(filmler)

def filmsil():
    film_adı= input("Film adı Girin: ")

    if film_adı:
        filmler.pop(film_adı)
        print("Film Başarıyla Silindi...")
    else:
        print("Film İsmi boş Olamaz...")

# filmsil()
# print(filmler)

def filmGetir():
    film_adı= input("Film adı Girin: ")

    if film_adı in filmler.keys():
        film=filmler.get(film_adı)
        yapım_yılı=film.get("Yapım Yılı", "Yapım Yılı Girilmemiş")
        imbd=film.get("Imbd", "Imbd Girilmemiş")
        film_turu=film.get("Tür", "Tür Girilmemiş")        
        
        print(f"Film Adı: {film_adı}, Yapım Yılı: {yapım_yılı}, Imbd: {imbd}, Tür:{film_turu}")
    
    else:
        print("Film Mevcut Değil...")
    input("Devam etmek için bir tuşa basın")

def filmleriListele():
    for film in filmler:
        film_adı= film
        yapım_yılı=filmler[film_adı].get("Yapım Yılı", "Yapım Yılı Girilmemiş")
        imbd= filmler[film_adı].get("Imbd", "Imbd Girilmemiş")
        film_turu= filmler[film_adı].get("Tür", "Tür Girilmemiş")
        print(f"Film Adı: {film_adı}, Yapım Yılı: {yapım_yılı}, Imbd: {imbd}, Tür:{film_turu}")
        print("="*80)
    input("Devam etmek için bir tuşa basın")

#filmGetir()
#filmleriListele()

while True:
    print("""
    [1]- Tüm Filmleri Listele
    [2]- Film Ara
    [3]- Film Ekle
    [4]- Film Sil  
    
    """)
    
    secenek=int(input("Seçiminizi Yapınız:  "))

    if secenek==1:
        filmleriListele()
    elif secenek==2:
        filmGetir()
    elif secenek==3:
        filmEkle()
    elif secenek==4:
        filmsil()
    else:
        break
