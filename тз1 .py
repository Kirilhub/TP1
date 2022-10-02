class Bace:

    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

class Contacts:

    def __init__(self):
        self.bd = [[],[],[],[],[],[]]

    def __add__(self, other):
        self.bd[0].append(len(self.bd[0])+1)
        fio = c.name.split(" ")
        while len(fio)<3:
            fio.append(None)
        self.bd[1].append(fio[0])
        self.bd[2].append(fio[1])
        self.bd[3].append(fio[2])
        if c.phone != '':
            self.bd[4].append(c.phone)
        else:
            self.bd[4].append(None)
        if c.mail != '':
            self.bd[5].append(c.mail)
        else:
            self.bd[5].append(None)

    def Contact(self, id):
        ans = "ID - " + str(self.bd[0][id])+"\n"
        if self.bd[1][id] != None:
            ans += "ФИО: " + self.bd[1][id]
        if self.bd[2][id] != None:
            ans += " " + self.bd[2][id]
        if self.bd[3][id] != None:
            ans += " " + self.bd[3][id]
        if self.bd[4][id] != None:
            ans += "\n " + "Номер телефона: " + self.bd[4][id]
        else:
            ans += "\n " + "Номер телефона: " + "-"
        if self.bd[5][id] != None:
            ans += "\n " + "Почтовый адрес: " + self.bd[5][id] +"\n"
        else:
            ans += "\n " + "Почтовый адрес: " + "-" +"\n"
        return ans

    def phone(self, phone):
        if self.bd[4].__contains__(phone):
            id = self.bd[4].index(phone)
            print(self.Contact(id))
        else:
            print("Ничего не найдено. ")

    def mail(self, mail):
        if self.bd[5].__contains__(mail):
            id = self.bd[5].index(mail)
            print(self.Contact(id))
        else:
            print("Ничего не найдено. ")

    def search(self, fio):
        ids =[]

        if fio[0] != None:

            for i in range(len(self.bd[1])):

                if fio[0] == self.bd[1][i]:
                    ids.append(self.bd[0][i] - 1)
        if fio[1] != None:

            if fio[0]!= None:

                for id in ids:

                    if fio[1]!=self.bd[2][id]:
                        ids.remove(id)
            else:

                for i in range(len(self.bd[2])):

                    if fio[1]==self.bd[2][i]:
                        ids.append(self.bd[0][i]-1)
        if fio[2] != None:

            if fio[0] != None or fio[1] != None:

                for id in ids:

                    if fio[2]!=self.bd[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.bd[3])):

                    if fio[2]==self.bd[2][i]:

                        ids.append(self.bd[0][i]-1)
        if len(ids)==0:
            print("Ничего не найдено. ")

        else:
            for id in ids:
                print(self.Contact(id))

    def change(self, id, c):
        id -= 1
        fio = c.name.split(" ")

        while len(fio) < 3:
            fio.append(None)
        self.bd[1][id] = fio[0]
        self.bd[2][id] = fio[1]
        self.bd[3][id] = fio[2]

        if len(c.phone) > 0:
            self.bd[4][id] = c.phone

        else:
            self.bd[4][id] = None

        if len(c.mail) > 0:
            self.bd[5][id] = c.mail

        else:
            self.bd[5][id] = None

    def printAll(self):
        for i in range(len(self.bd[0])):
            print(self.Contact(i))

def Commands():
    print("Список доступных команд: ")
    print("1 - Показать все контакты", "2 - Найти по ФИО", "3 - Найти по телефону", "4 - Найти по почте", 
          "5 - Изменение контакта", "6 - остановить программу", sep="\n")

print("Введите название файла ")
fileName = input()
file = open(fileName, encoding='utf-8')
base = Contacts()

for stroka in file:
    arr = stroka.split(",")
    c = Bace(arr[0], arr[1].replace(" ", ""), arr[2].replace(" ", "").replace("\n", ""))
    base.__add__(c)

print("База сформирована.")
Commands()
com = int(input())

while com != "akdna@@@kdn":
    if com == 1:
        base.printAll()

    elif com == 4:

        fio = []
        print("Введите фамилию")
        f = input()

        if f == '':
            fio.append(None)

        else:
            fio.append(f)
        print("Введите имя")
        i = input()

        if i == '':
            fio.append(None)

        else:
            fio.append(i)
        print("Введите отчество")
        o = input()

        if o == '':
            fio.append(None)

        else:
            fio.append(o)
        base.search(fio)

    elif com == 3:
        print("Введите телефон ")
        phone = input()
        base.phoneSearch(phone)

    elif com == 4:
        print("Введите Почтовый адрес")
        mail = input()
        base.mailSearch(mail)
    
    elif com == 5:
        print("Введите id контакта, чтобы изменить его", "(Впишите в две разные строки)", sep="\n")
        id = int(input())
        q = input().split(",")
        c = Contacts(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        base.change(id, c)

    elif com == 6:
        "программа закрыта"
        break

    Commands()
    com = int(input())