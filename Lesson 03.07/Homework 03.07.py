#Task 1

number=int(input("Введите номер квартиры:"))
if 0<number<=144:
    podj = number//36+ bool(number % 36)
    nip = number - 36 * (podj - 1)#number in podjezd
    floor=nip//4 + bool(0<nip%4)
    nof=nip-(floor-1)*4#number on floor
    print(f"Эта квартира находиться в {podj} подъезде, на {floor} этаже и это {nof} квартира на этаже")
else:
    print("Введен неверный номер квартиры.")

#Task 2

year=int(input("Введите год:"))
if not year%4 and year%100 or not year%400:
    print(f"{year} это высокосный год")
else:
    print(f"{year} это не высокосный год")

#Task 3

a,b,c=int(input("Введите длину стороны А:")),int(input("Введите длину стороны B:")),int(input("Введите длину стороны C:"))
res="Такой треугольник не может существовать"
if a+b>c:
    if b+c>a:
        res=f"Возможность существования такого треугольника: {b<a+c}"
print(res)