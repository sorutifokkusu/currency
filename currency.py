import requests
import json

birim = requests.get("https://api.exchangeratesapi.io/latest")
birim = json.loads(birim.text)
birim = birim["rates"]
birimstr = ""
print
print("".center(100,"*"))
print("Kur Hesaplama".center(100,"*"))
print("".center(100,"*"))
print("Kaynak: https://exchangeratesapi.io/".center(100,"*"))
print("".center(100,"*"))

while True:
    islem = input("İşlem seçin:\n1- Döviz hesapla\n2- Kullanılabilir birimler\n3- Çıkış\n\nSeçiminiz: ")
    try:
        if islem == "1":
            x = input("Bozulan döviz türü: ")
            y = input("Alınan döviz türü: ")
            z = input(f"Ne kadar {x} bozdurmak istiyorsunuz: ")
            try:
                if x=="EUR":
                    exchange = requests.get("https://api.exchangeratesapi.io/latest")
                    exchange = json.loads(exchange.text)
                    rates = exchange[f"rates"]
                    x_rate = 1
                    print(f"\nGüncel kur: {x_rate} {x} = {rates[f'{y}']} {y}\n")
                    calculate_x = float(x_rate)
                    calculate_y = float(rates[f"{y}"])
                    calculated_x = calculate_x * float(z)
                    calculated_y = calculate_y * float(z)
                    print(f"Hesaplanan: {calculated_x} {x} = {calculated_y} {y}\n")
                    continue


                else:
                    exchange = requests.get(f"https://api.exchangeratesapi.io/latest?base={x}&symbols={x},{y}")
                    exchange = json.loads(exchange.text)
                    rates = exchange[f"rates"]
                    #print((rates[f"{x} "]), x ," = ", (rates[f"{y}"]))
                    print(f"\nGüncel kur: {rates[f'{x}']} {x} = {rates[f'{y}']} {y}\n")
                    calculate_x = float(rates[f"{x}"])
                    calculate_y = float(rates[f"{y}"])
                    calculated_x = calculate_x * float(z)
                    calculated_y = calculate_y * float(z)
                    print(f"Hesaplanan: {calculated_x} {x} = {calculated_y} {y}\n")
                    continue
            
                
            except:
                print("\nHatalı Giriş\n")


        if islem == "2":
            for key in birim.keys():
                birimstr += (f" '{key}'\n")
            print(f"Kullanılabilir birimler: {birimstr}".center(100,"*"))
        
        if islem == "3":
            break

        else:
            raise Exception
    except:
        print("\nHatalı Giriş\n")
    

