"""Simulate traffic light

Functions:
    menu():
        Show user's actions.
    traffic_light():
        Simulate traffic light 

"""

def menu():
    """Show user's actions."""
    print("Введите цевет светофора:желтый, зеленый или красный.\nДля выхода введите: выход.\n ")
    print("Введите цвет:")


def traffic_light():
    """Simulate traffic light."""
    print("СВЕТОФОР")
    menu()
    response = input()
    while response != "выход":
        print("Ваше действие:")
        if response == "желтый":
            print("ждите другого сигнала")
        elif response == "зеленый":
            print("Вперед!")
        elif response == "красный":
            print("Стой!")
        else:
            print("Введите одно из предложенных значений в следующий раз.")
        print("\n")
        menu()
        response = input()


if __name__ == "__main__":
    traffic_light()