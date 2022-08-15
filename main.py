from tkinter import *
import  random

def basla():
    global sayi
    sayi = random.randint(1,50)
    etiket1.destroy() #etiket1 kaybolsun
    baslaButton.destroy() #naslabutton kaybolsun
    global etiket2 #etiket oluşturdum
    etiket2 = Label(font="Helvetica 12 bold")
    etiket2.pack(pady=15) #etiket2 pencereye yerleştirildi. nesneler ile arasında 15 birimlik boşluk olsun
    global giris
    giris = Entry() #sayı buraya girilecek
    giris.pack(pady=15)
    dugme = Button(text="Tahmin et/Guess", command=tahmin_et)
    dugme.pack(pady=15)

def tahmin_et():
    tahmin = int(giris.get()) #giris den gelen ifade inte çevirilip tahmine aktarılır
    giris.delete(0,END) #ARDINDAN GİRİLEN SAYI SİLİNSİN

    if tahmin == sayi:
        etiket2.config(text="Bildiniz./you know")
    elif tahmin > sayi:
        etiket2.config(text="aşagı/down")
    elif tahmin < sayi:
        etiket2.config(text="yukarı/above")




pencere = Tk() #pencere oluşturdum
pencere.geometry("600x400") #penceremin boyutunu ayarladım
pencere.title("Sayı Tahmin Oyunu/number guessing game")

etiket1= Label(text="""1 - 50 arasında sayı tuttum.Haydi tahmin et \n I scored between 1-50, guess what""",font="Helvetica 12 bold")
etiket1.place(relx=0.1, rely=0.3) #etiketi1 i bu x y konumuna göre yerleştir

baslaButton=Button(text="Başla/Start", width=10, command=basla)#basla fonksiyonu çağrılır
baslaButton.place(relx=0.4, rely=0.6)
mainloop() #anadöngüyü ayarladım
