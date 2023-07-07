import time
from plyer import notification

#Uyarilar kac saatte bir yapılsın
while True  :
    pSureAralik=input("Uyarilar kac saat aralıkla yapılsın?")
    if (pSureAralik.isnumeric())==True:
        pSureAralik=int(pSureAralik)*60
        break


if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Su İçme Vakti",
            message ="Sağlıklı Yaşam İçin Su İçin!.",
            timeout= (10)
        time.sleep(pSureAralik)
