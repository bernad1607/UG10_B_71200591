#soal 2
#Test Case 1: Jika kedua indikator menunjukan sinyal jual
#RSI : 100
#MACD : deatg-cross

print ("Masukkan besar RSI :100")
print ("Masukan kondisi MACD :death-cross")
print ("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")

#Test Case 2: Jika kedua indikator menunjukann sinyal Beli
#RSI : 25
#MACD : golden-cross

print ("masukan besaran RSI :25")
print ("Masukan kondisi MACD :golden-cross")
print ("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya beli")

#Test Case 3: jika indikator RSI menunjukan sinyal jual, sedangkan indikator MACD menunjukan sinyal beli
#RSI : 100
#MACD : golden-cross

print ("Masukan besaran RSI : 100")
print ("Masukan kondisi MACD : golden cross")
print ("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")

#Test Case 4: jika indikator RSI menunjukan sinyal Beli, sedangkan indikator MACD menunjukan sinyal jual
#RSI : 20
#MACD : death-cross

print ("masukan besaran RSI :20")
print ("masukan kondisi MACD : death-cross")
print ("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD smpai Golden-cross")

#Test Case 5: jika indikator RSI tidak menunjukan sinyal Beli maupun sinyal jual, tetapi MACD menunjukan sinyal beli
#RSI : 55
#MACD : golden-cross

print ("masukan besaran RSI : 55")
print ("Masukan kondisi MACD : golden-cross")
print ("RSI berada di area 30 - 70, bukan saatnya membeli maupun menjual")
