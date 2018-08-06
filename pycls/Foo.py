class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


class game_wom:
    def __init__(self, name, sex, age, fa):
        self.name = name
        self.sex = sex
        self.age = age
        self.fa = fa

    def grassland(self):
        self.fa = self.fa - 200

    def pracetice(self):
        self.fa = self.fa + 200

    def incest(self):
        self.fa = self.fa - 500

    def detail(self):
        print('name:%s,    sex:%s,      age:%s,      fa:%s   ' %
              (self.name, self.sex, self.age, self.fa))
