from itertools import groupby


def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in
                groupby(sorted(args, key=lambda i: str(i[0]).capitalize()), key=lambda i: str(i[0]).capitalize()) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "марина", "Петр", "Алина", "Бибочка"))
