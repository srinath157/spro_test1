class Human:
    def __init__(self):
        self.name = 'Guido'
        self.head = self.createHead()

    def createHead(self):
        return Human.Head(self)

    class Head:
        def __init__(self, human):
            self.human = human

        def talk(self):
            return 'talking...', self.human.name

