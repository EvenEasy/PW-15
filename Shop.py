percent = {
    '1' : 10,
    '2' : 5,
    '3' : 7,
    '4' : 10
}
price = int(input("Введіть ціну товару : \n"))
for week, perc in percent.items():
    print(f'{week} тиждень  +[{perc}%] - {round(float(price * (1 + (perc * 0.01))), 3)} $')