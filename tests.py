

def main():
    values = get_values()
    unknown = int(input("Сколько неправильных?: "))
    #target = float(input("Сумма: "))
    target = 451643567
    slack = 10
    print(values)
    combos = find_combo([], unknown, 1, values, target, slack)
    print()
    for i in combos:
        print(i)


def get_values():
    values = []
    path = "C:\\Users\\User\\Desktop\\АГВ Проекты\\Поиск ошибок в БД\\numbers.txt"
    with open(path, "r") as file:
        for row in file.readlines():
            row = row.strip('\n').replace(",", ".")
            values.append(float(row))
    return values


def find_combo(indices: list, limit: int, cut_depth: int, values: list, trgt: float, slack):
    combo = []
    for i in values:
        index = values.index(i)
        if index in indices:
            continue
        if cut_depth == limit:
            indices.append(index)
            #print(indices)
            #print("in")
            s = sum(values) - sum([values[i] for i in indices])
            #print(s)
            if s < trgt + slack and s > trgt - slack:
                combo.append(indices.copy())
                print(indices, "got it------------------------------")
            indices.remove(index)
        else:
            indices.append(index)
            #print(indices, "skip")
            combo.append(find_combo(indices, limit, cut_depth + 1, values, trgt, slack))
            indices.remove(index)
    return combo


main()
