class wordList():
    def __init__(self):
        with open('words.txt') as word_file:
            self.w = list(word_file.read().split())
        self.limitByLen(5)
    def limitByLen(self, num):
        self.w = [word for word in self.w if len(word) == num]
    def out(self):
        if len(self.w) > 2000:
            print(len(self.w))
        else:
            print(self.w)

    def has(self, *args):
        for arg in args:
            self.w = [word for word in self.w if arg in list(word)]
    def notHas(self, *args):
        for arg in args:
            self.w = [word for word in self.w if not arg in list(word)]

    def green(self,char,pos):
        self.w = [word for word in self.w if word[pos] == char]

    def orange(self, char, pos):
        self.w = [word for word in self.w if not word[pos] == char]
        self.has(char)