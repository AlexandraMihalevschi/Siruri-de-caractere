litere = list(input("Dati un sir de caractere: "))
print(litere)
litere1 = []
for i in range(len(litere)):
    if (ord(litere[i]) != 90) and (ord(litere[i]) != 32):
        a = int(ord(litere[i]))
        b = a + 1
        litere1.append(chr(b))
print(litere1)

for i in range(len(litere)):
    if ord(litere[i]) == 90:
        litere[i] = chr(65)
print(litere)

for i in range(len(litere)):
    if ord(litere[i]) == 32:
        litere[i] = chr(45)
print(litere)