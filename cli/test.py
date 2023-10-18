class Test:
    def __init__(self):
        self.name = ""
        self.you = ""
        self.me = ""

    def __str__(self):
        return (
            f"{self.name}",
            f"{self.you}"
        )


test = Test()
print(test)
