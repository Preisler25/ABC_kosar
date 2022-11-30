class Hazai:
    def __init__(self, list):
        self.nev = list[0]
        self.pontok = int(list[2])

class Idegen:
    def __init__(self, list):
        self.nev = list[1]
        self.pontok = int(list[3])
    
class Meccs:
    def __init__(self, list):
        self.helyszin = list[4]
        self.ido = list[5]

def ImportFromTXT(filename):
    hazai = []
    idegen = []
    meccs = []
    f = open(filename, "r", encoding="windows-1252").read()
    lines = f.split("\n")
    for i in lines[1:]:
        hazai.append(Hazai(i.split(";")))
        idegen.append(Idegen(i.split(";")))
        meccs.append(Meccs(i.split(";")))
    return hazai, idegen, meccs


def f3(list, name):
    temp = 0
    for i in list:
        if i.nev == name:
            temp += 1
    return temp

def f4(list, list2):
    for i in range(len(list)):
        if list[i].pontok == list2[i].pontok:
            return "igen"
    return "nem"

def f5(list):
    for i in list:
        if "Barcelona" in i.nev:
            return i.nev

def f6(list, list2, list3):
    temp = ""
    for i in range(len(list)):
        if list3[i].ido == "2004-11-21":
            temp += f"\n\t{list[i].nev} - {list2[i].nev} ({list[i].pontok}:{list2[i].pontok})"
    return temp

def f7(list):
    stadiumMap = dict()
    for i in list:
        if i.helyszin not in stadiumMap:
            stadiumMap[i.helyszin] = 0
        stadiumMap[i.helyszin] += 1
    temp = ""
    for i in stadiumMap:
        if stadiumMap[i] > 20:
            temp += f"\n\t{i}: {stadiumMap[i]}"
    return temp


def main():
    hazai_list, idegen_list, meccs_list = ImportFromTXT("eredmenyek.csv")
    print(f"3. feladat: Real Madrid: Hazai: {f3(hazai_list, 'Real Madrid')} Idegen: {f3(idegen_list, 'Real Madrid')}")
    print(f"4. feladat: Volt döntetlen? {f4(hazai_list, idegen_list)}")
    print(f"5. feladat: Barcelona: {f5(hazai_list)}")
    print(f"6. feladat: 2004.11.21-én játszott meccsek: {f6(hazai_list, idegen_list, meccs_list)}")
    print(f"7. feladat: Stadionok: {f7(meccs_list)}")
main()