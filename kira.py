from selenium import webdriver
import time
from bs4 import BeautifulSoup
import tkinter as tk





glsstt="https://www.google.com/search?q=tarih+saat&rlz=1C1GCEU_trTR1027TR1027&oq=tarih+saat&aqs=chrome..69i57j0i271l3.5332j0j7&sourceid=chrome&ie=UTF-8"
# start web browser
browser=webdriver.Chrome()

# get source code
browser.get(glsstt)
html = browser.page_source

time.sleep(2)
soup = BeautifulSoup(html, 'html.parser')
timediv =soup.find("div", {"class": "vk_gy vk_sh card-section sL6Rbf"}) 
times= timediv.find("div", {"class": "vk_gy vk_sh"})
time= times.find("span", {"class": "KfQeJ"}).text
k=-1
saklama=[]
mes=len(time)
for i in range(0,5): 
   if time[i] == ' ':
      
      sak1=i
      for j in range(i+1,mes-1):
         k=k+1
         
         if time[j] == ' ':
               sak2=j
               break
             
        
         
         
             
              
        
           
           
            
      break


day=time[sak1+1:sak2]
days=day.lower()
print(days)
ay = ["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]


for t in range(0,len(ay)):
   if days == ay[t]:
      sak3=t #ay
print(sak3)
gun=time[0:2]
gun1=int(gun)#gün

yil=time[sak2+1:len(time)]
yil1=int(yil) #yil

browser.close()

arayuz=tk.Tk()
arayuz.title("kiralama")
arayuz.geometry("300x300")

kullanıcı= tk.Label(text="KİRALAMA GÜNÜ")
kullanıcı.place(x=10,y=10)
t= tk.StringVar()
kullanıcı_g= tk.Entry(textvariable=t)
kullanıcı_g.place(x=100,y=10)

kullanıcı= tk.Label(text="KİRALAMA AYI")
kullanıcı.place(x=10,y=35)
p= tk.StringVar()
kullanıcı_g= tk.Entry(textvariable=p)
kullanıcı_g.place(x=100,y=35)

kullanıcı= tk.Label(text="KİRALAMA YILI")
kullanıcı.place(x=10,y=70)
o= tk.StringVar()
kullanıcı_g= tk.Entry(textvariable=o)
kullanıcı_g.place(x=100,y=70)
d_y= tk.Label(font= "verdana 10 bold")
d_y.place(x=100,y=150)

def kirala_komut():
   
   g = t.get()
   a =p.get()
   y =o.get()
   
   g= int(g)
   a= int(a)
   y= int(y)


  
   
   if y == yil1:
   
    if a == (sak3+1):
       if g <= gun1:
          print("kiralama olusturulamadi")
          d_y.config(text="KİRALANAMADI")
       else : 
          print("kiralama olusturuldu")
          d_y.config(text="KİRALANDI")
    
    if a > (sak3+1):
         print("kiralama olusturuldu")
         d_y.config(text="KİRALANDI")
 
    if a < (sak3+1):
         print("kiralama olusturulamadi")
         d_y.config(text="KİRALANAMADI")
 
 
 
  
  
    
   if y > yil1:
    print("kiralama olusturuldu")
    d_y.config(text="KİRALANDI")
 
      
   if y < yil1:
   
     print("kiralama olusturulamadi")
     d_y.config(text="KİRALANAMADI")






kirala= tk.Button(text="KİRALA",command=kirala_komut)
kirala.place(x=100,y=200)



arayuz.mainloop()












     








 



    



# close web browser
