def check_int_number(x):
    """Проверим правильность ввода с клавиатуры
    числа, является ли оно типом int."""

    def view_bad_number(x):
        """Проверяем что привело к ошибке в 
        преобразовании ввода в int"""
        #Проверка на дробное число
        if x.find('.') != -1 and x.count('.') == 1: 
            print(f"{x} - дробное число.")
            return False
        elif x:
            print(f"{x} - не число.")
            return False
        else:
            print("Вы ничего не ввели.")
            return False

    def number(x):
        try:
            x = int(x)
        except ValueError:
            # Проверяем что привело к ошибке
            return view_bad_number(x)
        except OverflowError:
            print("Число слишком большое.")
            return False
        else:
            return x
    
    return number(x)

def check_float_number(x):
    try:
        x = float(x)
    except ValueError:
        print(f"{x} - не число." if x else "Вы ничего не ввели.")
        return False
    except OverflowError:
        print(f"{x} - число слишком большое.")
        return False
    else:
        return x

def read_file_b(road_to_file):
    try:
        with open(road_to_file, "rb") as f:
            f = f.read()
            return f
    except PermissionError:
        print("Недостаточно прав для работы с файлом.")
        return False
    except FileNotFoundError:
        print("Неверный путь к файлу или такого файла не существует.")
        return False

def write_file_b(road_to_file, text):
    try:
        with open(road_to_file, "wb") as f:
            f.write(text)
    except PermissionError:
        print("Недостаточно прав для работы с файлом.")
        return False
    except FileNotFoundError:
        print("Неверный путь к файлу или такого файла не существует.")
        return False
    else:
        return True