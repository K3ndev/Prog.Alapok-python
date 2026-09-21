loans = [
    ("Alice", "Python", 12),
    ("Bob", "Algorithms", 5),
    ("Alice", "Databases", 18),
    ("Charlie", "Python", 3),
    ("Bob", "Python", 21),
    ("Alice", "Algorithms", 7),
    ("Charlie", "Databases", 14),
]


def overdue_books(loans: list):
    temp = []

    for row in loans:
        if row[2] > 14:
            temp.append(row)

    return temp


def user_statistics(loans: list):
    temp = {}

    for row in loans:
        name = row[0]
        days = row[2]

        if name not in temp:
            temp[name] = {
                "books": 0,
                "total_days": 0,
                "average_days": 0
            }

        temp[name]["books"] += 1
        temp[name]["total_days"] += days

    for name in temp:
        temp[name]["average_days"] = round(
            temp[name]["total_days"] / temp[name]["books"], 2
        )

    return temp


print(user_statistics(loans))
