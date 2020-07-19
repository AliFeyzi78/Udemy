kelimeler={

    "get": ["almak","edinmek","olmak","elde etmek"],
    "break": ["mola", "ara", "kırılmak", "fren"],
    "winner": ["kazanan", "galip", "birinci"] 




}

def kelimeleriListele():
    for no, kelime in enumerate(kelimeler,1):
        print(f"{no}.{kelime}")

kelimeleriListele()
#print(list(enumerate(kelimeler,1)))