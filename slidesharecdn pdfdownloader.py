# First import wget python module.
import wget
import threading
import time
sayfa_sayısı = input("Pdf sayfalarının sayısı kaç :\t")

def indir(i):
    
    link = f"https://image.slidesharecdn.com/astragmanualfinocroptimizedversion5compatiblesecured-100905133558-phpapp02/95/astra-gmanual-finocroptimizedversion5compatible-secured-{i+1}-1024.jpg?cb=1283694326"
    print(i+1)
    aa= i+1
        

    image_filename = wget.download(link,str(aa)+".jpg")
    print('Image Successfully Downloaded: ', image_filename)

for i in range(0,int(sayfa_sayısı)):
    t1 = threading.Thread(target=indir,args=(i,))
    t1.start()
    time.sleep(0.1)