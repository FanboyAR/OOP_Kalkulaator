#Kalkulaator
class cal():
    # Salvestame kaks arvu objekti sisse
    def __init__(self,a,b):
        self.a = a
        self.b = b
# Defineerime klassid
    #Liitmine
    def liitmine(self):
        return self.a + self.b
    #Lahutamine
    def lahutamine(self):
        return self.a - self.b
    #Korrutamine
    def korrutamine(self):
        return self.a * self.b
    #Jagamine
    def jagamine(self):
        return self.a / self.b
    #Jääk
    def jaak(self):
        return self.a % self.b
    #Astendamine
    def astendamine(self):
        return self.a ** self.b
    #Absoluut väärtus
    def absoluut(self):
        return abs(self.a)
    #Kahe arvu keskmine
    def keskmine(self):
        return (self.a + self.b) / 2
# Küsime kasutaja sisendit
a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))
# Kalkulaator
kalk = cal(a,b)
#Programm töötab kuni kasutaja teeb valiku
while True:
    #Menüü
    def menu():
        x = ('1. Liitmine \n2. Lahutamine \n3. Korrutamine \n4. Jagamine \n5. Jäägi leidmine \n6. Astendamine \n7. Absoluut \n8. Keskmine ')
        print(x)
    #Näitab menüüd
    menu ()
    #Küsib kasutaja valikut, millist operatsiooni teha
    valik = int(input("Sisesta üks valikutest: "))
    #Kontrollib valikut ja kuvab vastuse
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.astendamine())
        break
    elif valik == 7:
        print("Vastus: ",kalk.absoluut())
        break
    elif valik == 8:
        print("Vastus: ",kalk.keskmine())
        break
    elif valik == 0:
        print("Sisesta uuesti üks valikutest")
        break
