"""Print frequency of using symbols in text."""

def frequency_of_symbols():
    """Print frequency of using symbols in text."""
    f = lambda text,letter: 1 if len(text) == 1 and text == letter else  \
                        0 if len(text) == 1 else f(text[0],i)+f(text[1:],i)
    text = input()
    t1 = set(text)
    for i in t1:
        print(f"Частота вхождения символа {i}  равна {f(text,i)}")


if __name__ == "__main__":
    frequency_of_symbols()