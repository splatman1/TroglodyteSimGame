class Person:
    def __init__(self):
        pass

    def talk_to_person(self, question, name):
        message = f"A Wild {name} Appeared!\n" \
                  f"Would you like to talk to them(yes/no)"
        if input(message) == "y":
            input(question)

