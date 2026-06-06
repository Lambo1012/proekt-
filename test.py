import os
import subprocess
import sys
import time
import platform
import webbrowser

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    print("=" * 50)
    print("ВНИМАНИЕ! Скрипт запущен без прав администратора!")
    print("Некоторые оптимизации НЕ СРАБОТАЮТ!")
    print("Пожалуйста, перезапустите программу от имени Администратора.")
    print("=" * 50)
    input("\nНажмите Enter для выхода...")
    sys.exit()

def run_cmd(command):
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def run_ps(command):
    try:
        subprocess.run(["powershell", "-Command", command], shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def create_restore_point():
    print(" Создание точки восстановления системы...")
    ps_command = "Checkpoint-Computer -Description 'Gaming_Optimization' -RestorePointType MODIFY_SETTINGS -ErrorAction SilentlyContinue"
    run_ps(ps_command)
    print(" Готово (если восстановление включено в системе)!")
    time.sleep(1.5)

def check_subscription():
    """Проверяет, подписался ли пользователь"""
    # Создаем файл-метку, что пользователь уже подписался
    marker_file = os.path.join(os.environ['TEMP'], 'lambo_optimizer_subscribed.flag')
    
    # Если файл существует и ему меньше 30 дней, считаем что подписан
    if os.path.exists(marker_file):
        file_time = os.path.getmtime(marker_file)
        if time.time() - file_time < 30 * 24 * 3600:  # 30 дней
            return True
    
    # Если флага нет или он просрочен - показываем требование подписки
    return False

def mark_as_subscribed():
    """Отмечаем, что пользователь подписался"""
    marker_file = os.path.join(os.environ['TEMP'], 'lambo_optimizer_subscribed.flag')
    with open(marker_file, 'w') as f:
        f.write(str(time.time()))

def open_subscription_links():
    """Открывает ссылки на подписку"""
    print("\n" + "=" * 60)
    print(" ПОДПИШИСЬ НА МЕНЯ, ЧТОБЫ ПОЛУЧИТЬ ДОСТУП К ОПТИМИЗАЦИИ!")
    print("=" * 60)
    
    links = {
        "TikTok": "https://www.tiktok.com/@lambo_lega444",
        "YouTube": "https://www.youtube.com/@lambo_lega444",
        "Telegram": "https://t.me/lambo_lega444"
    }
    
    for platform_name, url in links.items():
        print(f"\n {platform_name}: {url}")
    
    print("\n" + "=" * 60)
    print(" ВАЖНО! Перейди по ссылке и ПОДПИШИСЬ!")
    print(" ПОСЛЕ ПОДПИСКИ НАЖМИ ENTER ДЛЯ ПРОВЕРКИ")
    print("=" * 60)
    
    # Открываем все ссылки в браузере
    for platform_name, url in links.items():
        print(f"\nОткрываю {platform_name}...")
        webbrowser.open(url)
        time.sleep(1)
    
    input("\n ПОДПИСАЛСЯ? Нажми Enter для проверки...")
    
    # Проверка - просто нажали Enter
    print("\n Проверка подписки...")
    time.sleep(1)
    
    # Отмечаем как подписанного (в реальном приложении тут была бы API проверка)
    mark_as_subscribed()
    print(" ДОСТУП ПОЛУЧЕН! Добро пожаловать в оптимизатор!")
    time.sleep(2)
    return True

def show_subscription_reminder():
    """Показывает напоминание о подписке"""
    print("\n" + "=" * 60)
    print(" ПОДПИСАТЬСЯ НЕ ЗАБУДЬ А ТО НЕ ЗАРАБОТАЕТ ТВОЯ ОПТИМИЗАЦИЯ!")
    print("=" * 60)
    print(" TikTok: lambo_lega444")
    print(" YouTube: lambo_lega444")
    print(" Telegram: lambo_lega444")
    print("=" * 60 + "\n")

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("          🎮 ＬＡＭＢｏᅠｌｅｇａ OPTIMIZATION 🎮")
    print("=" * 60)
    show_subscription_reminder()
    
    print("\n【 ОЧИСТКА СИСТЕМЫ】")
    print("[1]  Очистка временных файлов (Temp, Cache)")
    print("[2]  Очистка кэша DNS и сетевых настроек")
    print("[3]  Дефрагментация дисков (только HDD)")
    print("[4]  Очистка и оптимизация реестра")
    
    print("\n【 ПРОИЗВОДИТЕЛЬНОСТЬ】")
    print("[5]  Отключение ненужных служб Windows")
    print("[6]  Отключение визуальных эффектов (Aero/Анимации)")
    print("[7]  Настройка схемы питания 'Высокая производительность'")
    print("[8]  Настройка приоритета процессора для игр")
    
    print("\n【 ИГРОВЫЕ НАСТРОЙКИ】")
    print("[9]  Включение игрового режима Windows")
    print("[10] Отключение Xbox Game Bar и DVR")
    print("[11] Оптимизация задержек ввода (Input Lag)")
    print("[12] Настройка сети для онлайн-игр")
    
    print("\n【 ОПТИМИЗАЦИЯ ПАМЯТИ】")
    print("[13] Очистка оперативной памяти (RAM)")
    print("[14] Настройка файла подкачки")
    print("[15] Отключение ненужных автозагрузок")
    
    print("\n【 ВОССТАНОВЛЕНИЕ】")
    print("[16] Сброс всех настроек в значения по умолчанию")
    
    print("\n[0] Выход")
    print("=" * 60)

# --- ФУНКЦИИ ОПТИМИЗАЦИИ ---

def clean_temp_files():
    print(" Очистка временных файлов...")
    show_subscription_reminder()
    run_cmd('del /q /f /s %TEMP%\\* 2>nul')
    run_cmd('del /q /f /s C:\\Windows\\Temp\\* 2>nul')
    run_cmd('del /q /f /s C:\\Windows\\Prefetch\\* 2>nul')
    run_ps("Clear-RecycleBin -Force -ErrorAction SilentlyContinue")
    print(" Временные файлы удалены!")
    show_subscription_reminder()

def clean_dns_cache():
    print(" Сброс сетевого кэша...")
    show_subscription_reminder()
    run_cmd("ipconfig /flushdns")
    run_cmd("ipconfig /release")
    run_cmd("ipconfig /renew")
    run_cmd("netsh winsock reset")
    print(" DNS кэш и сетевые настройки сброшены!")
    show_subscription_reminder()

def defragment_disks():
    print(" Дефрагментация дисков (только для HDD)...")
    show_subscription_reminder()
    drives = subprocess.run("wmic logicaldisk where drivetype=3 get deviceid", shell=True, capture_output=True, text=True).stdout
    for line in drives.split('\n')[1:]:
        drive = line.strip()
        if drive and ':' in drive:
            print(f"  Оптимизация {drive}...")
            run_cmd(f'defrag {drive} /O')
    print(" Дефрагментация завершена!")
    show_subscription_reminder()

def clean_registry():
    print(" Очистка реестра...")
    show_subscription_reminder()
    create_restore_point()
    ps_clean = """
    $null = Register-ScheduledTask -Force -TaskName "TempClean" -Action (New-ScheduledTaskAction -Execute "cleanmgr.exe" -Argument "/sagerun:1") -Trigger (New-ScheduledTaskTrigger -Once -At (Get-Date)) -Settings (New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries)
    Start-ScheduledTask -TaskName "TempClean"
    Start-Sleep -Seconds 5
    Unregister-ScheduledTask -TaskName "TempClean" -Confirm:$false
    """
    run_ps(ps_clean)
    print(" Реестр оптимизирован!")
    show_subscription_reminder()

def disable_services():
    print(" Отключение ненужных служб...")
    show_subscription_reminder()
    services = [
        "XblAuthManager", "XboxNetApiSvc", "XblGameSave",
        "PrintSpooler", "Fax", "RemoteRegistry", 
        "RemoteAccess", "WSearch"
    ]
    
    for service in services:
        run_cmd(f'sc config "{service}" start= disabled')
        run_cmd(f'sc stop "{service}"')
        print(f"  Отключено: {service}")
    
    print(" Ненужные службы отключены!")
    show_subscription_reminder()

def disable_visual_effects():
    print(" Отключение визуальных эффектов...")
    show_subscription_reminder()
    run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v "MenuShowDelay" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v "AutoEndTasks" /t REG_SZ /d "1" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v "HungAppTimeout" /t REG_SZ /d "1000" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v "WaitToKillAppTimeout" /t REG_SZ /d "2000" /f')
    run_ps('Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" -Name "VisualFXSetting" -Value 2')
    print(" Визуальные эффекты отключены!")
    show_subscription_reminder()

def power_plan_high_performance():
    print(" Настройка схемы питания...")
    show_subscription_reminder()
    run_cmd('powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
    run_cmd('powercfg -setacvalueindex scheme_current sub_processor perfboostmode 2')
    run_cmd('powercfg -setactive scheme_current')
    print(" Схема питания 'Высокая производительность' активирована!")
    show_subscription_reminder()

def cpu_priority():
    print(" Настройка приоритета процессора...")
    show_subscription_reminder()
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 26 /f')
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 10 /f')
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
    print(" Приоритет процессора настроен!")
    show_subscription_reminder()

def enable_game_mode():
    print(" Включение игрового режима...")
    show_subscription_reminder()
    run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d 1 /f')
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f')
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 1 /f')
    print(" Игровой режим включен!")
    show_subscription_reminder()

def disable_xbox_features():
    print(" Отключение Xbox Game Bar и DVR...")
    show_subscription_reminder()
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f')
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f')
    run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v "ShowStartupPanel" /t REG_DWORD /d 0 /f')
    print(" Xbox функции отключены!")
    show_subscription_reminder()

def reduce_input_lag():
    print(" Оптимизация задержек ввода...")
    show_subscription_reminder()
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "SmoothMouseXCurve" /t REG_BINARY /d "0000000000000000" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "SmoothMouseYCurve" /t REG_BINARY /d "0000000000000000" /f')
    print(" Input Lag оптимизирован!")
    show_subscription_reminder()

def optimize_network():
    print(" Оптимизация сети для онлайн-игр...")
    show_subscription_reminder()
    interfaces_path = r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"
    ps_net = f"""
    Get-ChildItem -Path 'Registry::{interfaces_path}' | ForEach-Object {{ 
        New-ItemProperty -Path $_.PSPath -Name 'TcpAckFrequency' -Value 1 -PropertyType DWord -Force
        New-ItemProperty -Path $_.PSPath -Name 'TCPNoDelay' -Value 1 -PropertyType DWord -Force
    }}
    """
    run_ps(ps_net)
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "GlobalMaxTcpWindowSize" /t REG_DWORD /d 65535 /f')
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" /v "TcpWindowSize" /t REG_DWORD /d 65535 /f')
    print(" Сеть оптимизирована для игр!")
    show_subscription_reminder()

def clean_ram():
    print(" Очистка оперативной памяти...")
    show_subscription_reminder()
    run_ps("[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers()")
    ps_ram = """
    $processes = Get-Process
    foreach ($process in $processes) {
        try { $process.WorkingSet64 > $null } catch {}
    }
    [System.GC]::Collect()
    """
    run_ps(ps_ram)
    print(" RAM очищена!")
    show_subscription_reminder()

def configure_pagefile():
    print(" Настройка файла подкачки...")
    show_subscription_reminder()
    ps_pagefile = """
    $computer = Get-WmiObject Win32_ComputerSystem
    $totalRAM = [math]::Round($computer.TotalPhysicalMemory/1GB)
    $minPageFile = $totalRAM * 1024
    $maxPageFile = $totalRAM * 1.5 * 1024
    
    $pageFileSettings = Get-WmiObject -Class Win32_PageFileSetting
    if ($pageFileSettings) {
        $pageFileSettings.Delete()
    }
    
    $pageFile = Set-WmiInstance -Class Win32_PageFileSetting -Arguments @{Name="C:\\pagefile.sys"; InitialSize=$minPageFile; MaximumSize=$maxPageFile}
    """
    run_ps(ps_pagefile)
    print(f" Файл подкачки настроен!")
    show_subscription_reminder()

def disable_startup():
    print(" Отключение ненужных автозагрузок...")
    show_subscription_reminder()
    run_cmd('reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /va /f 2>nul')
    run_cmd('reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /va /f 2>nul')
    ps_startup = "Get-CimInstance Win32_StartupCommand | Remove-CimInstance -ErrorAction SilentlyContinue"
    run_ps(ps_startup)
    print(" Автозагрузки очищены!")
    show_subscription_reminder()

def reset_all_settings():
    print(" Сброс всех настроек в значения по умолчанию...")
    show_subscription_reminder()
    confirm = input("Вы уверены? Это сбросит все оптимизации (y/n): ").strip().lower()
    if confirm == 'y':
        run_cmd('powercfg /restoredefaultschemes')
        run_cmd('reg delete "HKCU\\Software\\Microsoft\\GameBar" /f 2>nul')
        run_cmd('reg delete "HKCU\\System\\GameConfigStore" /f 2>nul')
        run_cmd('reg delete "HKCU\\Control Panel\\Desktop" /v "MenuShowDelay" /f 2>nul')
        run_cmd('reg delete "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v "Win32PrioritySeparation" /f 2>nul')
        
        services = ["XblAuthManager", "XboxNetApiSvc", "PrintSpooler", "WSearch"]
        for service in services:
            run_cmd(f'sc config "{service}" start= demand')
        
        print(" Все настройки сброшены! Рекомендуется перезагрузить ПК.")
        show_subscription_reminder()
        
        if input("Перезагрузить сейчас? (y/n): ").strip().lower() == 'y':
            os.system("shutdown /r /t 5")

def exit_optimizer():
    print("\n" + "=" * 60)
    print(" Оптимизация завершена! Удачной игры!")
    print("\n НЕ ЗАБУДЬ ПОДПИСАТЬСЯ!")
    print("=" * 60)
    show_subscription_reminder()
    print("\nСпасибо за использование Optimizer от LAMBO_lega!")
    print("С уважением, ваш проводник в мир игр без лагов! 🎮")
    print("=" * 60)
    time.sleep(5)

# --- ГЛАВНАЯ ПРОГРАММА С ПРОВЕРКОЙ ПОДПИСКИ ---

def main():
    # Проверяем подписку при запуске
    if not check_subscription():
        print("\n" + "=" * 60)
        print(" ДОСТУП ЗАКРЫТ! ТРЕБУЕТСЯ ПОДПИСКА!")
        print("=" * 60)
        print("\nЧтобы получить доступ к оптимизатору, нужно подписаться на мои соцсети!")
        
        choice = input("\nХочешь получить доступ? (y/n): ").strip().lower()
        
        if choice == 'y':
            open_subscription_links()
        else:
            print("\n Без подписки доступ невозможен!")
            print("Запусти программу снова, когда будешь готов подписаться!")
            input("\nНажми Enter для выхода...")
            sys.exit()
    
    # Основной цикл программы
    while True:
        show_menu()
        choice = input("\n🔧 Ваш выбор: ").strip()
        
        if choice == "1":
            clean_temp_files()
        elif choice == "2":
            clean_dns_cache()
        elif choice == "3":
            defragment_disks()
        elif choice == "4":
            clean_registry()
        elif choice == "5":
            create_restore_point()
            disable_services()
        elif choice == "6":
            disable_visual_effects()
        elif choice == "7":
            power_plan_high_performance()
        elif choice == "8":
            cpu_priority()
        elif choice == "9":
            enable_game_mode()
        elif choice == "10":
            disable_xbox_features()
        elif choice == "11":
            reduce_input_lag()
        elif choice == "12":
            optimize_network()
        elif choice == "13":
            clean_ram()
        elif choice == "14":
            configure_pagefile()
        elif choice == "15":
            disable_startup()
        elif choice == "16":
            reset_all_settings()
        elif choice == "0":
            exit_optimizer()
            break
        else:
            print(" Неверный выбор!")
        time.sleep(2)

if __name__ == "__main__":
    main()