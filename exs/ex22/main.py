print("-=-" *20)
print("analizador de triângulos")
print("-=-" *20)
r1 = float(input("primeiro seguimento: "))
r2 = float(input("segundo seguimento: "))
r3 = float(input("terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("estes seguimentos podem formar triângulos")
else:
    print("estes seguimentos não podem formar triângulos")