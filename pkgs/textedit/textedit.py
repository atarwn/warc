import os
def textedit():
    def edit_file(path):
        with open(path, 'r') as file:
            lines = file.readlines()
        
        print("r - Прочитать файл | w - Записать изменения | {i} - Изменить строку под указанным номером")
        while True:
            command = input()
            if command[0] == 'r':
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
            elif command[0].isdigit():
                new_line = input("Введите новое содержимое: ")
                lines[int(command) - 1] = new_line + '\n'
            elif command[0] == 'w':
                with open(path, 'w') as file:
                    file.writelines(lines)
            else:
                print('Неизвестная команда')

        with open(path, 'w') as file:
            file.writelines(lines)

    print("1. Начать работу")
    print("2. Помощь")
    choice = input("Введите число: ")

    if choice == "2":
        print("""
    Программа предоставляет следующие возможности:
    - Чтение файла при помощи команды `r`,
    - Запись изменений в файл при помощи команды `w`,
    - Изменение строк по числовым номерам.

    Для начала выберите файл, введя его имя. Для завершения работы нажмите сочетание клавиш 'Ctrl + C'. Если вам необходимо создать файл, убедитесь, что программа запущена из нужного каталога. Удачи в работе!
    """)
    else:
        print("Если вы не читали помощь, пожалуйста прочтите")

    path = input("Введите название файла: ")
    if os.path.isfile(path):
        edit_file(path)
    else:
        f = open(path, 'w')
        f.close()
        edit_file(path)
