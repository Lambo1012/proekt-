import os
import subprocess
import sys

# Проверка прав администратора (необходима для изменения настроек системы)
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    print("Внимание: Скрипт запущен без прав администратора. Многие функции не сработают!")
    print("Пожалуйста, перезапустите командную строку/терминал от имени Администратора.")
    input("\nНажмите Enter для выхода...")
    sys.exit()

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====================================")
    print("         ＬＡＭＢｏᅠｌｅｇａ  ОПТИМИЗАТОР        ")
    print("=====================================")
    print("[1] Отключить Xbox Game Bar")
    print("[2] Включить игровой режим")
    print("[3] Отключить фоновые приложения")
    print("[4] Автозагрузка (Открыть управление)")
    print("[5] Очистка системы (Временные файлы)")
    print("[6] Высокая производительность")
    print("[7] Максимальное быстродействие")
    print("[8] Включить гибернацию")
    print("[9] Информация о процессоре")
    print("[10] Информация о видеокарте")
    print("[11] Оптимизация процессора")
    print("[12] Настройка видеокарты (Открыть панель)")
    print("[13] Оптимизация служб (Телеметрия)")
    print("[14] Оптимизация диска (Defrag)")
    print("[15] Уменьшение задержки системы")
    print("[16] Ускорение запуска Windows")
    print("[17] Включить HAGS")
    print("[18] Сброс системы (SFC Scannow)")
    print("[0] Выход")
    print("-------------------------------------")

def run_cmd(command):
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def run_ps(command):
    try:
        subprocess.run(["powershell", "-Command", command], shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

while True:
    show_menu()
    choice = input("Выбор: ").strip()

    if choice == "1":
        print("Отключение Xbox Game Bar...")
        run_cmd('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f')
        run_cmd('reg add "HKCU\System\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")
        
    elif choice == "2":
        print("Включение игрового режима...")
        run_cmd('reg add "HKCU\Software\Microsoft\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d 1 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "3":
        print("Отключение фоновых приложений...")
        run_cmd('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d 1 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "4":
        print("Открытие диспетчера задач...")
        run_cmd("taskmgr.exe")

    elif choice == "5":
        print("Очистка временных файлов...")
        run_cmd("del /q /f /s %TEMP%\*")
        run_cmd("del /q /f /s C:\Windows\Temp\*")
        print("Очистка завершена!")
        os.system("timeout /t 2 >nul")

    elif choice == "6":
        print("Установка схемы питания 'Высокая производительность'...")
        run_cmd("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "7":
        print("Настройка эффектов на быстродействие...")
        run_cmd('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects" /v "VisualFXSetting" /t REG_DWORD /d 2 /f')
        print("Готово! Изменения применятся после перезапуска.")
        os.system("timeout /t 3 >nul")

    elif choice == "8":
        print("Включение гибернации...")
        run_cmd("powercfg /hibernate on")
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "9":
        os.system('cls')
        print("--- Информация о процессоре ---")
        run_ps("Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores | Format-List")
        input("Нажмите Enter для возврата...")

    elif choice == "10":
        os.system('cls')
        print("--- Информация о видеокарте ---")
        run_ps("Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion | Format-List")
        input("Нажмите Enter для возврата...")

    elif choice == "11":
        print("Оптимизация работы ядер процессора...")
        run_cmd('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Power\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d 1 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "12":
        print("Запуск настроек графики...")
        run_cmd("start ms-settings:display-advancedgraphics")

    elif choice == "13":
        print("Отключение телеметрии...")
        run_cmd("sc config DiagTrack start= disabled")
        run_cmd("sc stop DiagTrack")
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "14":
        print("Запуск оптимизации диска C...")
        run_ps("Optimize-Volume -DriveLetter C -Defrag -Verbose")
        os.system("timeout /t 3 >nul")

    elif choice == "15":
        print("Снижение сетевых задержек...")
        run_cmd('reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "16":
        print("Оптимизация времени запуска...")
        run_cmd('reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters" /v "EnablePrefetcher" /t REG_DWORD /d 3 /f')
        print("Готово!")
        os.system("timeout /t 2 >nul")

    elif choice == "17":
        print("Включение HAGS...")
        run_cmd('reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f')
        print("Готово! Требуется перезагрузка ПК.")
        os.system("timeout /t 3 >nul")

    elif choice == "18":
        print("Запуск проверки системных файлов...")
        subprocess.run("sfc /scannow", shell=True)
        input("Проверка завершена. Нажмите Enter...")

    elif choice == "0":
        print("Выход...")
        break
    else:
        print("Неверный выбор!")
        os.system("timeout /t 1 >nul")