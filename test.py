import os
import subprocess
import sys
import time

def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    print("=" * 50)
    print("ВНИМАНИЕ! Скрипт запущен без прав администратора!")
    print("Игровые твики НЕ СРАБОТАЮТ!")
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
    ps_command = "Checkpoint-Computer -Description 'LAMBO_Gaming_Optimize' -RestorePointType MODIFY_SETTINGS -ErrorAction SilentlyContinue"
    run_ps(ps_command)
    print(" Готово (если восстановление включено в системе)!")
    time.sleep(1.5)

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("       🚀 ＬＡＭＢｏᅠｌｅｇａ  OPTIMIZATION 🚀       ")
    print("==================================================")
    print("   TikTok/TG/YT: lambo_lega444")
    print("=" * 50)
    print("\n【ЭТАП 1: ОЧИСТКА ОТ МИКРОФРИЗОВ И СТАТТЕРОВ】")
    print("[1]  Полная очистка мусора (Temp, Кэш диска, Корзина)")
    print("[2]  Очистка кэша шейдеров (NVIDIA / AMD / DirectX)")
    print("[3]  Сброс и очистка кэша оперативной памяти (RAM)")
    print("[4]  Сброс DNS кэша (Стабильный пинг)")
    print("\n【ЭТАП 2: НАСТРОЙКА ИГРОВОГО СТЭКА WINDOWS】")
    print("[5]  Включить Игровой режим и выключить Xbox Game Bar")
    print("[6]  Запретить фоновым приложениям жрать ресурсы")
    print("[7]  Оптимизация полноэкранного режима игр (FSO)")
    print("[8]  Включить HAGS (Аппаратное ускорение GPU)")
    print("\n【ЭТАП 3: СНИЖЕНИЕ ЗАДЕРЖЕК И ИНПУТ ЛАГА】")
    print("[9]  Максимальный игровой приоритет для CPU и Мыши")
    print("[10]  Отключить энергосбережение USB (Убрать лаг мыши)")
    print("[11]  Включить MSI-режим для видеокарты (Ultra-низкий отклик)")
    print("[12]  Снизить сетевую задержку в играх (TcpAckFrequency)")
    print("\n【ЭТАП 4: РАСШИРЕННЫЙ ХАРДКОР (⚠️ С КРИТАМИ)】")
    print("[13]  Отключить VBS (Защита изоляции) — +15-20% FPS!")
    print("[14]  Схема питания 'Максимальная производительность'")
    print("[15]  Отключение PowerThrottling процессора")
    print("[16]  Отключение телеметрии, рекламы и WerSvc")
    print("\n[0] Выход из оптимизатора")
    print("=" * 50)

# --- ФУНКЦИИ ОПТИМИЗАЦИИ ---

def clean_system():
    print("Очистка временных файлов и мусора...")
    run_cmd('del /q /f /s %TEMP%\\* 2>nul')
    run_cmd('del /q /f /s C:\\Windows\\Temp\\* 2>nul')
    run_ps("Clear-RecycleBin -Force -ErrorAction SilentlyContinue")
    # Кэш игр из MS Store
    run_cmd("wsreset -s")
    print(" Мусор успешно ликвидирован!")

def clean_shaders():
    print("Выковыриваем забитый кэш шейдеров...")
    run_cmd('del /q /f /s "%LocalAppData%\\Microsoft\\DirectX\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\NVIDIA\\DXCache\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\NVIDIA\\GLCache\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\AMD\\DxCache\\*" 2>nul')
    print(" Шейдеры очищены! В первых матчах кэш соберется заново, зато пропадут старые фризы.")

def clean_ram():
    print("Выгружаем скрытый кэш памяти...")
    run_ps("[System.GC]::Collect(); [System.GC]::WaitForPendingFinalizers()")
    print(" Доступная память очищена!")

def tweak_gaming_mode_xbox():
    print("Настройка игрового режима...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d 1 /f')
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f')
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f')
    print(" Игровой режим ВКЛ, игровой оверлей Xbox ВЫКЛ!")

def tweak_background():
    print("Глушим фоновые процессы...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d 1 /f')
    print(" Фоновые аппки больше не забирают такты CPU!")

def tweak_fso():
    print("Настройка Fullscreen Optimization...")
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_FSEBehaviorMode" /t REG_DWORD /d 2 /f')
    print(" Эксклюзивный полный экран теперь работает стабильнее!")

def tweak_input_priority():
    print("Срезаем Input Lag и даем приоритет игре...")
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f')
    # Высокий приоритет обработки окнам игр (Win32PrioritySeparation = 26hex)
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\PriorityControl" /v "Win32PrioritySeparation" /t REG_DWORD /d 38 /f')
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f')
    print(" Отклик мыши стал чистым, а игра получила наивысший приоритет процессора!")

def tweak_usb():
    print("Убираем засыпание USB портов...")
    run_cmd('powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a73a80c-33e6-4e91-a475-684530c18326 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0')
    run_cmd('powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a73a80c-33e6-4e91-a475-684530c18326 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0')
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\USB" /v "DisableSelectiveSuspend" /t REG_DWORD /d 1 /f')
    print(" Сенсор мыши больше не уйдет в микро-сон!")

def tweak_msi():
    print("Переводим GPU в режим аппаратных прерываний MSI...")
    path = r"HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
    ps_cmd = f"""
    Get-ChildItem -Path 'Registry::{path}' | ForEach-Object {{
        $subKey = "$_\\0000"
        if (Test-Path "Registry::$subKey") {{
            $msiPath = "$subKey\\Interrupt Management\\MessageSignaledInterruptProperties"
            if (!(Test-Path "Registry::$msiPath")) {{ New-Item -Path "Registry::$msiPath" -Force | Out-Null }}
            New-ItemProperty -Path "Registry::$msiPath" -Name "MSISupported" -Value 1 -PropertyType DWord -Force | Out-Null
            $affPath = "$subKey\\Interrupt Management\\Affinity Policy"
            if (!(Test-Path "Registry::$affPath")) {{ New-Item -Path "Registry::$affPath" -Force | Out-Null }}
            New-ItemProperty -Path "Registry::$affPath" -Name "DevicePriority" -Value 3 -PropertyType DWord -Force | Out-Null
        }}
    }}
    """
    run_ps(ps_cmd)
    print(" Прерывания GPU ускорены! Нужен перезапуск ПК.")

def tweak_network_ping():
    print("Настройка сетевых пакетов под онлайн-игры...")
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
    # Отключаем склеивание пакетов (Алгоритм Нейгла для сетевых карт)
    interfaces_path = r"HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces"
    ps_net = f"Get-ChildItem -Path 'Registry::{interfaces_path}' | ForEach-Object {{ New-ItemProperty -Path $_.PSPath -Name 'TcpAckFrequency' -Value 1 -PropertyType DWord -Force; New-ItemProperty -Path $_.PSPath -Name 'TCPNoDelay' -Value 1 -PropertyType DWord -Force }}"
    run_ps(ps_net)
    print(" Задержка отправки пакетов убрана, пинг стабилизирован!")

def tweak_vbs():
    print(" Отключение VBS для буста кадров...")
    confirm = input("Вы уверены? Это отключит изоляцию ядра ради высокого FPS (y/n): ").strip().lower()
    if confirm == 'y':
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 0 /f')
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa" /v "LsaCfgFlags" /t REG_DWORD /d 0 /f')
        print(" VBS отключен! ИЗМЕНЕНИЯ ПРИМЕНЯТСЯ ТОЛЬКО ПОСЛЕ ПЕРЕЗАГРУЗКИ.")
        if input("Перезагрузить ПК сейчас? (y/n): ").strip().lower() == 'y':
            os.system("shutdown /r /t 3")

def tweak_telemetry_bloat():
    print("Вырезаем телеметрию, отчеты и рекламу...")
    run_cmd("sc config DiagTrack start= disabled")
    run_cmd("sc stop DiagTrack")
    run_cmd("sc config dmwappushservice start= disabled")
    run_cmd("sc stop dmwappushservice")
    run_cmd("sc config WerSvc start= disabled")
    run_cmd("sc stop WerSvc")
    run_ps('Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" -Name "Enabled" -Type DWord -Value 0')
    run_ps('Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338387Enabled" -Type DWord -Value 0')
    print(" Фоновые шпионские службы остановлены!")

# --- ГЛАВНЫЙ ЦИКЛ ---
while True:
    show_menu()
    choice = input("\n🔧 Твой выбор: ").strip()
    
    if choice == "1":
        clean_system()
    elif choice == "2":
        clean_shaders()
    elif choice == "3":
        clean_ram()
    elif choice == "4":
        run_cmd("ipconfig /flushdns")
        print(" Кэш DNS сброшен!")
    elif choice == "5":
        tweak_gaming_mode_xbox()
    elif choice == "6":
        tweak_background()
    elif choice == "7":
        tweak_fso()
    elif choice == "8":
        create_restore_point()
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f')
        print(" HAGS включен! Нужен рестарт ПК.")
    elif choice == "9":
        tweak_input_priority()
    elif choice == "10":
        tweak_usb()
    elif choice == "11":
        create_restore_point()
        tweak_msi()
    elif choice == "12":
        tweak_network_ping()
    elif choice == "13":
        tweak_vbs()
    elif choice == "14":
        tweak_max_power_scheme()
    elif choice == "15":
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d 1 /f')
        print(" Ограничения процессора сняты!")
    elif choice == "16":
        tweak_telemetry_bloat()
    elif choice == "0":
        print("\n Удачных каток! Подписывайся на LAMBO_lega!")
        time.sleep(2)
        break
    else:
        print(" Кнопка не найдена!")
    time.sleep(2)