def ebob(sayı1,sayı2):
    liste1 = []
    liste2 = []
    liste3 = []
    for i in range(1,sayı1+1):
        if sayı1%i == 0:
            liste1.append(i)
    for x in range(1,b+1):
        if b%x == 0:
            liste2.append(x)

    for i in liste1:
        for x in liste2:
            if i == x:
                liste3.append(i)
    print(liste3[-1])

while True:
    a = input("İlk Sayı:")
    b = input("İkinci Sayı:")
    if a == "q" or b == "q":
        break
    else:
        a = int(a)
        b = int(b)
        ebob(a,b)