class StringVar:
    def __init__(self, text):
        self.text = text

    def set(self, text):
        self.text = text
        return self.text

    def get(self):
        return self.text


t = StringVar(input("Введите текст: "))
print(t.get())
print(t.set("Привет"))
