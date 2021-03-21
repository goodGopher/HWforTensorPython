"""Removing duplicate elements in list.

Functions:
    list_reading(my_list):
        Allows to read list from keyboard.
    remove_copies(m_list):
        Removing duplicate elements in list.
    main():
        Organize entering and clearing of list.

"""

import checks

def remove_copies(m_list):
    """Removing duplicate elements in list."""
    rand_list = list(set(m_list))
    m_list.reverse()
    for i in rand_list:
        while m_list.count(i) > 1:
            m_list.remove(i)
    m_list.reverse()


def main():
    """Organize entering and clearing of list."""
    print("Введите список через Enter:")
    main_list = []
    checks.list_reading(main_list)
    remove_copies(main_list)
    print(f"обработанный список {main_list}")


if __name__ == "__main__":
    main()
