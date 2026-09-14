def average(scores: list) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def get_result(results: dict, name: str) -> str:
    try:
        scores = results[name]
    except KeyError:
        return "A tanuló nem található!"

    avg = average(scores)
    result = grade(avg)
    return f"{name}: {avg:.2f} -> {result}"


def print_all_results(results: dict) -> None:
    for name in results:
        print(get_result(results, name))


def count_passed(results: dict) -> int:
    passed = 0
    for scores in results.values():
        if grade(average(scores)) != "F":
            passed += 1
    return passed


def best_student(results: dict) -> tuple:
    best_name = ""
    best_avg = -1

    for name, scores in results.items():
        avg = average(scores)
        if avg > best_avg:
            best_name = name
            best_avg = avg

    return best_name, best_avg


def main() -> None:
    results = {
        "Anna": [85, 92, 78],
        "Béla": [55, 61, 58],
        "Csilla": [95, 88, 91],
        "Dávid": [40, 52, 45],
        "Erika": [72, 75, 80],
    }

    print_all_results(results)
    print(f"Ebből átment: {count_passed(results)} fő")

    name, avg = best_student(results)
    print(f"Legjobb eredmény: {name} ({avg:.2f})")

    while True:
        nev = input(
            "Írja be a diák nevét, akinek szeretné látni az átlagát, vagy írja be az exit parancsot a kilépéshez\n--> "
        )

        if nev == "exit":
            print("A program bezárul!")
            break

        print(get_result(results, nev))


if __name__ == "__main__":
    main()
