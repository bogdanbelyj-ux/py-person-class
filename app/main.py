class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for pers in people:
        result.append(Person(pers["name"], pers["age"]))

    for pers in people:
        inst = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            inst.wife = Person.people[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            inst.husband = Person.people[pers["husband"]]

    return result
