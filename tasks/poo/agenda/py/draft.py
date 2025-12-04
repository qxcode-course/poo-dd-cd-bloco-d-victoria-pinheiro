class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def getId(self) -> str:
        return self.id
    
    def getNumber(self) -> str:
        return self.number

    def isValid(self) -> bool:
        return self.__number

    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"
    
class Contact:
    def __init__(self, favorited: bool, name: str):
        self.favorited: bool = False
        self.name: str = name
        self.fone = list[Fone] = []

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: fone invalido")
        
    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: indice invalido")

    def toogleFavorited(slef):
        self.__favorited = not self.__favorited
        
    def isFavorited(self) -> bool: 
        return self.__favorited

    def getFones(self) -> list:
        return self.fone

    def getFavorited(self) -> bool:
        return self.favorited

    def getName(self) -> str:
        return self.name
    
    def setName(self, name: str) -> str:
        self.__name = name 

    def __str__(self) -> str:
        fav = "@" if self.__favorited else "-"
        fones_str = ",". join(str(fone) for fone in self.__fones)
        return f"{fav} {self.__name} {{fones_str}}"   
         
class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []
        
    def __findPosByName(self)


def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            fones: list[list[str]] = []
            for fone_str in args[2]:
                id, number = fone_str.split(":")
                fones.append([id, number])
            agenda.addContact(name, fones)

main()
