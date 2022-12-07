#from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication

#Form, Window = uic.loadUiType("window.ui")

#app = QApplication([])
#window = Window()
#form = Form()
#form.setupUi(window)
#window.show()
#app.exec()


#читаем названия всех файлов в дириктории C:/Users/89015/OneDrive/Документы/EVE/logs/Marketlogs, если файлов больше 1-го выдаст ошибку
import os
path = ('D:/Питон илья/test/')
dirs = os.listdir( path )
#print(dirs)

#перевод названия файла как списка в текст
Str = "".join(dirs)

#присваеваем переменной полного пути к файлу
dirsis='D:/Питон илья/test/'+ Str

#печать полного пути к файлу
#print(dirsis)
print(Str)

#открываем фаил для чтения
file=open(dirsis)
    
#создаем пустой список
jita_buy = []
jita_sell = []


#создаем строку из каждой строчки
lines=file.readlines()
for x0 in lines:
#    print(x0)
    sot = x0.split(',')
#    print(sot)
    solar_system = sot[-3]
    if not (solar_system == "30000142"): #30000142 = Jita 30000144 = Perimeter 30002187 = Amarr
        continue
    price = sot[0]
#    print(price)
    is_sell_order = sot[7]
    if is_sell_order == "False":
        jita_sell.append(price)
#        print(jita_sell)
    else:
        jita_buy.append(price)
#        print(jita_buy)

z11=float(jita_sell[0]) # минимальная стоимость товара в маркете по sell ордерам
print(z11)
z22=float(jita_buy[0]) # максимальная стоимость товара в маркете по buy ордерам
print(z22)

Brokers_fee=0.0104
Sales_tax=0.036

buy=z22*(1+Brokers_fee) # полная цена покупки товара
sell=z11*(1-Brokers_fee-Sales_tax) # полная цена за продажу товара
margin=(sell-buy)/sell*100
profit=(sell-buy)/1000
print("Маржа=",int(round(margin,0)),"%")
print("Прибыль=",int(round(profit,0)),"k isk")
print("Прибыль от 1000 шт.=",int(round(profit*1000,0)),"k isk")

#удаляем списки
del jita_buy
del jita_sell

#закрываем фаил
file.close()
#удаляем фаил из дириктории C:/Users/89015/OneDrive/Документы/EVE/logs/Marketlogs
os.remove(dirsis)
