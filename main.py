class Swordsman:

    def __init__(self, n, h, l, s):
        self.name = n
        self.health = h
        self.live = l
        self.status = s
        print("Появился новый мечник с именем: ", self.name)

    def eating(self, count):
        print(f"{self.name} кушает количество жизней увеличенно")
        self.health += count
        if self.health >= 80:
            print(f"{self.name} наелся. Количество жизней увеличилось.")
            self.live += 1
            self.health = 40

    def training(self, count):
        print(f"{self.name} тренеруется")
        self.status += count

    def fighting(self, count):
        print(f"{self.name} начал драку с противником у которого {count} жизней")
        p1 = input("Выберете атаку (Удар мечём, Вихрь из мечей, Три меча, Моментальный меч: ")
        while count > 0:
            if p1 == "Удар мечём":
                count -= (5 + self.status)
                print("Атака прошла -", 5 + self.status)
            elif p1 == "Вихрь из мечей":
                count -= (10 + self.status)
                print("Атака прошла -", 10 + self.status)
            elif p1 == "Три меча":
                count -= (30 + self.status)
                print("Атака прошла -", 30 + self.status)
            elif p1 == "Моментальный меч":
                count -= (20 + self.status)
                print("Атака прошла -", 20 + self.status)
            else:
                print("Такой атаки нет!")

            if count <= 0:
                print("Зоро победил!")
            p1 = input("Выберете атаку (Удар мечём, Вихрь из мечей, Три меча, Моментальный меч: ")


    def info(self):
        print(f"Здоровье: {self.health}")
        print(f"Жизней: {self.live}")
        print(f"Имя: {self.name}")
        print(f"Статус меча: {self.status}")

Zoro = Swordsman("Зоро", 40, 3, 10)


