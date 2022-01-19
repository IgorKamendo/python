import json


class Model:
    title = "1"
    text = "2"
    autor = "3"

    def save(self):
        d = {}
        attr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
        attr.remove("save")
        for i in attr:
            d[i] = eval("self." + i)
        with open("file.json", "w") as f:
            json.dump(d, f)
        return print(d)


test = Model()
test.title = "Питон"
test.text = "Задача"
test.autor = "Игорь"
test.save()
