import pandas as pd
import re

file = open("laptop_price.csv", "r")

data = {"L_ID": [], "Company": [], "Product": [], "TypeName": [], "Inches": [], "Resolution": [], "CPU": [], "RAM": [], "Memory": [], "GPU": [], "OpSys": [], "Weight": [], "Price_Euros": []}
wrong_lines = []

counter = 1
for line in file:
    d_arr = line.split(",")
    if len(d_arr) != 13:
        print(f"Line {counter} isn't right length:\n{d_arr}")
        wrong_lines.append(counter)
        counter += 1
        continue
    print(d_arr)
    l_id = re.findall("[0-9]+", d_arr[0])
    data["L_ID"].append(int(l_id[0]))
    data["Company"].append(d_arr[1])
    data["Product"].append(d_arr[2].replace('"', ''))
    data["TypeName"].append(d_arr[3])
    try:
        inches = float(d_arr[4])
    except:
        print(f"Inches:    {d_arr[4]}")
        inches = float(input("Inches:    "))
    data["Inches"].append(inches)
    resolution = re.findall("[0-9]+x[0-9]+", d_arr[5])
    print(resolution)
    data["Resolution"].append(resolution[0])
    data["CPU"].append(d_arr[6])

    if "gb" not in d_arr[7].lower():
        print(f"RAM:    {d_arr[7]}")
        ram = int(input("RAM:    "))
    else:
        r1 = re.findall("[0-9]+", d_arr[7])
        ram = int(r1[0])
    data["RAM"].append(ram)
    data["Memory"].append(d_arr[8])
    data["GPU"].append(d_arr[9])
    data["OpSys"].append(d_arr[10])

    if "kg" not in d_arr[11].lower():
        print(f"Weight:    {d_arr[11]}")
        weight = float(input("Weight:    "))
    else:
        w = re.findall("[0-9]+.[0-9]+", d_arr[11])
        if len(w) == 0:
            w1 = re.findall("[0-9]+", d_arr[11])
            if len(w1) == 0:
                print(f"Weight:    {d_arr[11]}")
                weight = float(input("Weight:    "))
            else:
                weight = float(w1[0])
        else:
            weight = float(w[0])
    data["Weight"].append(weight)

    price = re.findall("[0-9]+.[0-9]+", d_arr[12])
    if len(price) == 0:
        print(f"Price:    {d_arr[12]}")
        price = float(input("Price:    "))
        data["Price_Euros"].append(price)
    else:
        data["Price_Euros"].append(float(price[0]))

    print(f"Line {counter} complete!")
    counter += 1


for i in range(len(data["L_ID"])):
    temp = []
    for j in list(data.keys()):
        temp.append(data[j][i])
    print(temp)

if len(wrong_lines) > 0:
    print(f"The following lines couldn't be converted:\n{wrong_lines}")
else:
    print(data["L_ID"][13:16])
    df = pd.DataFrame.from_dict(data)
    df.to_csv("CLEANED_laptop_price.csv", index=False, header=False)