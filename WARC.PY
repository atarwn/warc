import time
import importlib
import os
LoopShell = True
ShellName = 'WARC'
ShellVersion = '0.03'

def loader():
    try:
        with open("LOADER.txt") as loader:
            lines = loader.read().split('\n')
            for line in lines:
                if line != 'ignore':
                    print(f'[ COM ] {line}')
                    kernelExecuteLoader(line)
                else:
                    break
    except Exception as ex:
        print(f'[ ERROR ] Ошибка выполнения LOADER.txt\n{ex}')

    print(f"[{ShellName} {ShellVersion}] (с) atarwn, 2024\nНачните работу написав help")

def help():
    print("Системные команды:")
    for key in corecoms.keys():
        print(f"- {key}")
    print("Остальные команды:")
    for key in coms.keys():
        print(f"- {key}")

class Imp:
    def import_module(module_name, path):
        """
        Импортирует модуль по имени и пути к файлу.

        Args:
            module_name: Имя модуля (например, "deepseek").
            path: Путь к файлу Python (например, "deepseek.py").

        Returns:
            Модуль или None, если модуль не найден.
        """
        spec = importlib.util.spec_from_file_location(module_name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def imp(*ctx):
        if ctx != ():
            ctx = ' '.join(ctx)
            module_path = f"pkgs/{ctx}/{ctx}.py"
            module = imp.import_module(ctx, module_path)
            coms[ctx] = getattr(module, f"{ctx}")
            comshelp[ctx] = getattr(module, f"{ctx}_help")  # Доступ к функции program
            # print(coms[ctx], comshelp[ctx])
            print(f"Модуль {ctx} успешно установлен")
        else:
            files = os.listdir('pkgs')
            for file in files:
                #if file.endswith(".py"):
                print(file)
imp = Imp

class System:
    current_path = os.getcwd()
    def dir():
        print(f"Текущий каталог: {system.current_path}")
        for entry in os.listdir(os.getcwd()):
            if os.path.isdir(entry):
                print(f'[D] {entry}')
            elif os.path.isfile(entry):
                print(f'[F] {entry}')
            else:
                print(f'[?] {entry}')
    def cd(path):
        try:
            new_directory = path
            if os.path.exists(new_directory) and os.path.isdir(new_directory):
                system.current_path = new_directory
            else:
                print("Неверный путь к каталогу.")
        except IndexError:
            print("Неверный формат команды.")
    def mkdir(path):
        try:
            os.mkdir(os.path.join(system.current_path, path))
        except FileExistsError:
            print("Папка с таким именем уже существует.")
    def rm(path):
        if os.path.isfile(path):
            try:
                os.remove(os.path.join(system.current_path, path))
            except FileNotFoundError:
                print("Файл не найден.")
        elif os.path.isdir(path):
            try:
                os.rmdir(os.path.join(system.current_path, path))
            except FileNotFoundError:
                print("Папка не найдена.")
        else:
            print('Не найдено')

    def shutdown(*ctx):
        def s_now():
            print('Выключаем wiSHpy...')
            global LoopShell
            LoopShell = False
            return 0
        def s_timer():
            print('wiSH будет выключен через 60 секунд')
            time.sleep(60)
            print('Выключаем wiSHpy...')
            global LoopShell
            LoopShell = False
            return 0
        if ctx == None:
            print('shutdown: -n -t')
            print('-n: Завершить работу сейчас')
            print('-t: Завершить работу через 60 секунд')
        elif ('-n' in ctx) and ('-t' in ctx):
            print(f"Введены не совместимые аргументы: {' '.join(ctx)}")
        elif '-n' in ctx:
            s_now()
        elif '-t' in ctx:
            s_timer()
system = System


def var():
    print(str(coms))

corecoms = {
    'help': help,
    'imp': imp.imp,
    'shutdown': system.shutdown,
    'dir': system.dir,
    'cd': system.cd,
    'mkdir': system.mkdir,
    'rm': system.rm,
}
coms = {}
comshelp = {}

def commandListener(user_input):
    context = user_input.split(' ')
    com = context[0]
    params = context[1:]
    if com in corecoms:
        try:
            corecoms[com](*params)
            return 0
        except Exception as ex:
            print(f"Произошла ошибка при выполнении {com}:\n{ex}")
            return 1
    elif com in coms:
        try:
            coms[com](*params)
            return 0
        except Exception as ex:
            print(f"Произошла ошибка при выполнении {com}:\n{ex}")
            return 1
    else:
        print('Неизвестная команда!')
        return 1
def kernelExecuteLoader(input):
    context = input.split(' ')
    com = context[0]
    params = context[1:]
    if com in corecoms:
        try:
            corecoms[com](*params)
            return 0
        except Exception as ex:
            print(f"[ ERROR ] Произошла ошибка в {com}:\n{ex}")
            return 1
    elif com in coms:
        try:
            coms[com](*params)
            return 0
        except Exception as ex:
            print(f"[ ERROR ] Произошла ошибка в {com}:\n{ex}")
            return 1
    else:
        print('[ ERROR ] Неизвестная команда')
        return 1
    
loader()
while LoopShell:
    user_input = input(f"{system.current_path} ~? ")
    commandListener(user_input)
