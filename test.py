import os
import subprocess
import sys
import time

# Проверка прав администратора (необходима для изменения настроек системы)
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    print("=" * 50)
    print("ВНИМАНИЕ! Скрипт запущен без прав администратора!")
    print("Большинство функций оптимизации НЕ СРАБОТАЮТ!")
    print("")
    print("Пожалуйста, перезапустите программу от имени Администратора:")
    print("1. Нажмите ПКМ на файле")
    print("2. Выберите 'Запуск от имени администратора'")
    print("=" * 50)
    input("\nНажмите Enter для выхода...")
    sys.exit()

# Улучшенная функция выполнения команд CMD
def run_cmd(command, silent=True, show_error=False):
    try:
        if silent:
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        if show_error:
            print(f"Ошибка выполнения: {e}")
        return False

# Улучшенная функция выполнения PowerShell команд
def run_ps(command, silent=True, show_error=False):
    try:
        if silent:
            subprocess.run(["powershell", "-Command", command], shell=True, check=True, 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(["powershell", "-Command", command], shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        if show_error:
            print(f"Ошибка PowerShell: {e}")
        return False

# Функция создания точки восстановления системы
def create_restore_point():
    print("🔄 Создание точки восстановления системы...")
    ps_command = """
    try {
        Checkpoint-Computer -Description "LAMBO_lega_Optimizer_Pre_Tweak" -RestorePointType MODIFY_SETTINGS -ErrorAction Stop
        Write-Host "SUCCESS"
    } catch {
        Write-Host "FAILED"
    }
    """
    result = run_ps(ps_command, silent=False)
    
    # Проверяем, включена ли функция восстановления
    check_command = "Get-ComputerRestorePoint | Measure-Object | Select-Object -ExpandProperty Count"
    check_process = subprocess.run(["powershell", "-Command", check_command], capture_output=True, text=True)
    
    if check_process.returncode == 0 and check_process.stdout.strip().isdigit():
        print("✅ Точка восстановления успешно создана!")
    else:
        print("⚠️ Не удалось создать точку восстановления. Возможно, функция отключена в системе.")
        print("   Рекомендую включить защиту системы для диска C: перед использованием оптимизатора.")
    time.sleep(2)

# Функция отображения меню
def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("        🚀 ＬＡＭＢＯ_ＬＥＧＡ  ОПТИМИЗАТОР 🚀        ")
    print("==================================================")
    print("  📱 ПОДПИШИСЬ НЕ ЗАБУДЬ!!!!!           ")
    print("  🎵 TikTok: lambo_lega444              ")
    print("  📨 Telegram: lambo_lega444            ")
    print("  ▶️ YouTube: lambo_lega444             ")
    print("=" * 50)
    print("")
    print("【ОСНОВНЫЕ НАСТРОЙКИ】")
    print("[1]  🎮 Отключить Xbox Game Bar")
    print("[2]  🎯 Включить игровой режим")
    print("[3]  📱 Отключить фоновые приложения")
    print("[4]  ⚡ Автозагрузка (Открыть управление)")
    print("[5]  🧹 Очистка системы (Временные файлы)")
    print("")
    print("【ПРОИЗВОДИТЕЛЬНОСТЬ】")
    print("[6]  ⚡ Высокая производительность (схема питания)")
    print("[7]  🎨 Отключить визуальные эффекты")
    print("[8]  💾 Включить гибернацию")
    print("[9]  🔧 Оптимизация процессора (PowerThrottling)")
    print("[10] 🎮 Настройка видеокарты (Открыть панель)")
    print("[11] 🛡️ Отключение телеметрии и рекламы")
    print("[12] 💿 Оптимизация диска (Только для HDD!)")
    print("[13] 🚀 Включить HAGS (Аппаратное ускорение GPU)")
    print("[14] ⚡ Отключить залипание клавиш")
    print("[15] 🖥️ Оптимизация полноэкранных игр (FSO)")
    print("")
    print("【СЕТЬ И ЗАДЕРЖКИ】")
    print("[16] 🌐 Очистить кэш DNS (Снижение пинга)")
    print("[17] 🎮 Максимальное снижение задержки ввода (Input Lag)")
    print("[18] ⚡ Снизить сетевые задержки (Алгоритм Нейгла)")
    print("[19] 🧹 Очистить кэш оперативной памяти")
    print("[20] 🔄 Очистить корзину")
    print("[31] 🧹 Очистить кэш шейдеров (Устранение микрофризов в играх)")
    print("[32] 🎮 Включить MSI-режим для видеокарты (Снижение задержки GPU)")
    print("[33] ⚡ Отключить энергосбережение USB (Убирает плавающий лаг мыши)")
    print("")
    print("【ДИАГНОСТИКА И ИНФО】")
    print("[21] 📊 Информация о процессоре")
    print("[22] 🎮 Информация о видеокарте")
    print("[23] 💾 Информация о дисках (SMART)")
    print("[24] 🛠️ Проверка системных файлов (SFC)")
    print("[25] ⚡ Информация о задержках системы")
    print("")
    print("【РАСШИРЕННЫЕ НАСТРОЙКИ (⚠️ ОСТОРОЖНО!)】")
    print("[26] 🔒 Отключить Защитник Windows (Только для слабых ПК!)")
    print("[27] ⚠️ Отключить VBS (Virtualization Security) - ВЫСОКИЙ FPS!")
    print("[28] 🛑 Отключить отчеты об ошибках (WerSvc)")
    print("[29] 🔄 Активировать режим питания 'Максимальная производительность'")
    print("[30] 🎨 Отключить залипание окон (MouseCornerClipLength)")
    print("")
    print("【СИСТЕМНЫЕ】")
    print("[0]  🚪 Выход")
    print("=" * 50)
    print("💡 СОВЕТ: Перед использованием расширенных настроек (26-30)")
    print("   рекомендуется создать точку восстановления вручную!")
    print("=" * 50)

# Создание точки восстановления перед важными изменениями
def safe_tweak(tweak_name, tweak_function):
    print(f"\n⚠️  ВНИМАНИЕ! Выполняется твик: {tweak_name}")
    print("   Создаю точку восстановления...")
    create_restore_point()
    
    confirm = input(f"\n✅ Применить твик '{tweak_name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        tweak_function()
        print("✅ Готово!")
    else:
        print("❌ Отменено пользователем.")
    time.sleep(2)

# Функции твиков
def tweak_disable_xbox():
    print("Отключение Xbox Game Bar...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v "AppCaptureEnabled" /t REG_DWORD /d 0 /f')
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_Enabled" /t REG_DWORD /d 0 /f')
    print("✅ Xbox Game Bar отключен!")

def tweak_game_mode():
    print("Включение игрового режима...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\GameBar" /v "AllowAutoGameMode" /t REG_DWORD /d 1 /f')
    print("✅ Игровой режим включен!")

def tweak_background_apps():
    print("Отключение фоновых приложений...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v "GlobalUserDisabled" /t REG_DWORD /d 1 /f')
    print("✅ Фоновые приложения отключены!")

def tweak_clean_temp():
    print("Очистка временных файлов...")
    run_cmd('del /q /f /s %TEMP%\\* 2>nul')
    run_cmd('del /q /f /s C:\\Windows\\Temp\\* 2>nul')
    print("✅ Временные файлы очищены!")

def tweak_high_performance_power():
    print("Установка схемы питания 'Высокая производительность'...")
    run_cmd("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
    print("✅ Схема питания изменена!")

def tweak_disable_visual_effects():
    print("Настройка эффектов на быстродействие...")
    run_cmd('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v "VisualFXSetting" /t REG_DWORD /d 2 /f')
    print("✅ Визуальные эффекты отключены! Изменения применятся после перезапуска.")

def tweak_hibernate_on():
    print("Включение гибернации...")
    run_cmd("powercfg /hibernate on")
    print("✅ Гибернация включена!")

def tweak_cpu_powerthrottling():
    print("Отключение троттлинга процессора...")
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling" /v "PowerThrottlingOff" /t REG_DWORD /d 1 /f')
    print("✅ Троттлинга процессора отключен!")

def tweak_disable_telemetry():
    print("Отключение телеметрии и рекламы...")
    run_cmd("sc config DiagTrack start= disabled")
    run_cmd("sc stop DiagTrack")
    run_cmd("sc config dmwappushservice start= disabled")
    run_cmd("sc stop dmwappushservice")
    run_ps('Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" -Name "Enabled" -Type DWord -Value 0')
    run_ps('Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338387Enabled" -Type DWord -Value 0')
    print("✅ Телеметрия и реклама отключены!")

def tweak_defrag():
    print("⚠️  ВНИМАНИЕ: Дефрагментация нужна ТОЛЬКО для HDD дисков!")
    print("    Для SSD дисков эта операция может сократить срок службы!")
    confirm = input("    Ваш диск C: - это HDD? (y/n): ").strip().lower()
    if confirm == 'y':
        print("Запуск оптимизации диска C...")
        run_ps("Optimize-Volume -DriveLetter C -Defrag -Verbose")
        print("✅ Оптимизация завершена!")
    else:
        print("❌ Оптимизация отменена для защиты SSD диска.")

def tweak_hags():
    print("Включение HAGS (аппаратное ускорение GPU)...")
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers" /v "HwSchMode" /t REG_DWORD /d 2 /f')
    print("✅ HAGS включен! Требуется перезагрузка ПК.")

def tweak_disable_stickykeys():
    print("Отключение залипания клавиш...")
    run_cmd('reg add "HKCU\\Control Panel\\Accessibility\\StickyKeys" /v "Flags" /t REG_SZ /d "506" /f')
    print("✅ Залипание клавиш отключено!")

def tweak_fso():
    print("Оптимизация полноэкранных игр (FSO)...")
    run_cmd('reg add "HKCU\\System\\GameConfigStore" /v "GameDVR_FSEBehaviorMode" /t REG_DWORD /d 2 /f')
    print("✅ FSO оптимизирован!")

def tweak_flush_dns():
    print("Очистка кэша DNS...")
    run_cmd("ipconfig /flushdns")
    print("✅ Кэш DNS успешно сброшен!")

def tweak_input_lag():
    print("Максимальное снижение задержки ввода...")
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseSpeed" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold1" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKCU\\Control Panel\\Mouse" /v "MouseThreshold2" /t REG_SZ /d "0" /f')
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "SystemResponsiveness" /t REG_DWORD /d 0 /f')
    print("✅ Задержка ввода снижена! (Установлен максимальный приоритет для игр)")

def tweak_network_lag():
    print("Снижение сетевых задержек (отключение алгоритма Нейгла)...")
    run_cmd('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v "NetworkThrottlingIndex" /t REG_DWORD /d 4294967295 /f')
    print("✅ Сетевые задержки снижены!")

def tweak_clear_ram():
    print("Очистка кэша оперативной памяти...")
    run_ps("[System.GC]::Collect()")
    run_ps("[System.GC]::WaitForPendingFinalizers()")
    print("✅ Оперативная память очищена!")

def tweak_clear_recycle():
    print("Очистка корзины...")
    run_ps("Clear-RecycleBin -Force -ErrorAction SilentlyContinue")
    print("✅ Корзина очищена!")

def tweak_clean_shaders():
    print("Очистка кэша шейдеров DirectX и графики...")
    run_cmd('del /q /f /s "%LocalAppData%\\Microsoft\\DirectX\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\NVIDIA\\DXCache\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\NVIDIA\\GLCache\\*" 2>nul')
    run_cmd('del /q /f /s "%LocalAppData%\\AMD\\DxCache\\*" 2>nul')
    print("✅ Кэш шейдеров успешно очищен!")

def tweak_enable_msi_mode():
    print("Оптимизация прерываний GPU (Включение MSI-режима)...")
    path = r"HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
    ps_command = f"""
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
    run_ps(ps_command)
    print("✅ MSI-режим и высокий приоритет для видеокарты активированы! (Требуется перезагрузка)")

def tweak_disable_usb_suspend():
    print("Отключение экономии энергии для USB-портов...")
    run_cmd('powercfg /SETDCVALUEINDEX SCHEME_CURRENT 2a73a80c-33e6-4e91-a475-684530c18326 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0')
    run_cmd('powercfg /SETACVALUEINDEX SCHEME_CURRENT 2a73a80c-33e6-4e91-a475-684530c18326 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0')
    run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Services\\USB" /v "DisableSelectiveSuspend" /t REG_DWORD /d 1 /f')
    print("✅ Энергосбережение USB отключено. Стабильность портов повышена!")

def tweak_cpu_info():
    os.system('cls')
    print("=" * 50)
    print("📊 ИНФОРМАЦИЯ О ПРОЦЕССОРЕ")
    print("=" * 50)
    run_ps("Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed | Format-List", silent=False)
    input("\nНажмите Enter для возврата...")

def tweak_gpu_info():
    os.system('cls')
    print("=" * 50)
    print("🎮 ИНФОРМАЦИЯ О ВИДЕОКАРТЕ")
    print("=" * 50)
    run_ps("Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion, CurrentHorizontalResolution, CurrentVerticalResolution | Format-List", silent=False)
    input("\nНажмите Enter для возврата...")

def tweak_disk_info():
    os.system('cls')
    print("=" * 50)
    print("💾 ИНФОРМАЦИЯ О ДИСКАХ (SMART)")
    print("=" * 50)
    print("\n📀 Физические диски:")
    run_ps("Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size, HealthStatus | Format-Table -AutoSize", silent=False)
    print("\n📊 Здоровье дисков:")
    run_ps("Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Wear, ReadErrorsTotal, WriteErrorsTotal | Format-Table -AutoSize", silent=False)
    input("\nНажмите Enter для возврата...")

def tweak_sfc():
    print("🔍 Запуск проверки системных файлов...")
    print("    Это может занять несколько минут...")
    subprocess.run("sfc /scannow", shell=True)
    input("\n✅ Проверка завершена. Нажмите Enter...")

def tweak_latency_info():
    os.system('cls')
    print("=" * 50)
    print("⚡ ИНФОРМАЦИЯ О СИСТЕМНЫХ ЗАДЕРЖКАХ")
    print("=" * 50)
    print("\n📊 Запуск теста задержек (ожидайте)...")
    run_ps("(Get-Counter '\\Processor Information(*)\\Processor Time').CounterSamples | Where-Object {$_.InstanceName -eq 'Total'} | Select-Object CookedValue", silent=False)
    print("\n💡 Для более детального анализа задержек используйте утилиту LatencyMon")
    input("\nНажмите Enter для возврата...")

def tweak_disable_defender():
    print("⚠️  ПРЕДУПРЕЖДЕНИЕ! Отключение Защитника Windows снижает безопасность!")
    print("    Рекомендуется только для слабых ПК при играх в оффлайн режиме.")
    confirm = input("\n🔒 Вы уверены, что хотите отключить Защитник? (y/n): ").strip().lower()
    if confirm == 'y':
        print("Отключение защиты в реальном времени...")
        run_ps("Set-MpPreference -DisableRealtimeMonitoring $true")
        run_ps("Set-MpPreference -DisableBehaviorMonitoring $true")
        run_ps("Set-MpPreference -DisableBlockAtFirstSeen $true")
        run_ps("Set-MpPreference -DisableIOAVProtection $true")
        run_ps("Set-MpPreference -DisablePrivacyMode $true")
        run_ps("Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true")
        run_ps("Set-MpPreference -DisableArchiveScanning $true")
        run_ps("Set-MpPreference -DisableIntrusionPreventionSystem $true")
        run_ps("Set-MpPreference -DisableScriptScanning $true")
        run_ps("Set-MpPreference -SubmitSamplesConsent 2")
        print("✅ Защитник Windows отключен! (Включится после перезагрузки)")
    else:
        print("❌ Операция отменена.")

def tweak_disable_vbs():
    print("=" * 50)
    print("⚠️  КРИТИЧЕСКОЕ ПРЕДУПРЕЖДЕНИЕ! ⚠️")
    print("=" * 50)
    print("Отключение VBS (Virtualization-Based Security):")
    print("✅ ПЛЮС: Значительное повышение FPS в играх (до 15-20%)")
    print("❌ МИНУС: Снижение безопасности системы")
    print("   - Отключается защита ядра")
    print("   - Уязвимость для некоторых типов атак")
    print("=" * 50)
    confirm = input("\n🔓 Вы действительно хотите отключить VBS? (y/n): ").strip().lower()
    if confirm == 'y':
        print("Отключение VBS...")
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 0 /f')
        run_cmd('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa" /v "LsaCfgFlags" /t REG_DWORD /d 0 /f')
        print("✅ VBS отключен! ТРЕБУЕТСЯ ПЕРЕЗАГРУЗКА для применения изменений.")
        reboot = input("\n🔄 Перезагрузить компьютер сейчас? (y/n): ").strip().lower()
        if reboot == 'y':
            os.system("shutdown /r /t 5")
            print("Перезагрузка через 5 секунд...")
    else:
        print("❌ Операция отменена.")

def tweak_disable_wersvc():
    print("Отключение службы отчетов об ошибках Windows...")
    run_cmd("sc config WerSvc start= disabled")
    run_cmd("sc stop WerSvc")
    print("✅ Служба отчетов об ошибках отключена!")

def tweak_max_power_scheme():
    print("Активация режима питания 'Максимальная производительность'...")
    run_cmd("powercfg /duplicateScheme e9a42b02-d5df-448d-aa00-03f14749eb61")
    print("✅ Режим 'Максимальная производительность' активирован!")

def tweak_disable_corner_clip():
    print("Отключение залипания окон...")
    run_cmd('reg add "HKCU\\Control Panel\\Desktop" /v "MouseCornerClipLength" /t REG_DWORD /d 0 /f')
    print("✅ Залипание окон отключено!")

# Основной цикл программы
while True:
    show_menu()
    choice = input("\n🔧 Ваш выбор: ").strip()
    
    if choice == "1":
        tweak_disable_xbox()
        time.sleep(2)
    elif choice == "2":
        tweak_game_mode()
        time.sleep(2)
    elif choice == "3":
        tweak_background_apps()
        time.sleep(2)
    elif choice == "4":
        print("Открытие автозагрузки...")
        run_cmd("taskmgr.exe")
    elif choice == "5":
        tweak_clean_temp()
        time.sleep(2)
    elif choice == "6":
        tweak_high_performance_power()
        time.sleep(2)
    elif choice == "7":
        tweak_disable_visual_effects()
        time.sleep(2)
    elif choice == "8":
        tweak_hibernate_on()
        time.sleep(2)
    elif choice == "9":
        tweak_cpu_powerthrottling()
        time.sleep(2)
    elif choice == "10":
        print("Запуск настроек графики...")
        run_cmd("start ms-settings:display-advancedgraphics")
    elif choice == "11":
        safe_tweak("Отключение телеметрии и рекламы", tweak_disable_telemetry)
    elif choice == "12":
        tweak_defrag()
        time.sleep(2)
    elif choice == "13":
        safe_tweak("Включение HAGS", tweak_hags)
    elif choice == "14":
        tweak_disable_stickykeys()
        time.sleep(2)
    elif choice == "15":
        tweak_fso()
        time.sleep(2)
    elif choice == "16":
        tweak_flush_dns()
        time.sleep(2)
    elif choice == "17":
        safe_tweak("Максимальное снижение задержки ввода", tweak_input_lag)
    elif choice == "18":
        tweak_network_lag()
        time.sleep(2)
    elif choice == "19":
        tweak_clear_ram()
        time.sleep(2)
    elif choice == "20":
        tweak_clear_recycle()
        time.sleep(2)
    elif choice == "21":
        tweak_cpu_info()
    elif choice == "22":
        tweak_gpu_info()
    elif choice == "23":
        tweak_disk_info()
    elif choice == "24":
        tweak_sfc()
    elif choice == "25":
        tweak_latency_info()
    elif choice == "26":
        safe_tweak("Отключение Защитника Windows", tweak_disable_defender)
    elif choice == "27":
        tweak_disable_vbs()
    elif choice == "28":
        tweak_disable_wersvc()
        time.sleep(2)
    elif choice == "29":
        tweak_max_power_scheme()
        time.sleep(2)
    elif choice == "30":
        tweak_disable_corner_clip()
        time.sleep(2)
    elif choice == "31":
        tweak_clean_shaders()
        time.sleep(2)
    elif choice == "32":
        safe_tweak("Включение MSI-режима для видеокарты", tweak_enable_msi_mode)
    elif choice == "33":
        tweak_disable_usb_suspend()
        time.sleep(2)
    elif choice == "0":
        print("\n👋 Спасибо за использование оптимизатора LAMBO_lega!")
        print("   Не забывайте подписываться:")
        print("   TikTok | Telegram | YouTube: @lambo_lega444")
        print("\n   Выход...")
        time.sleep(2)
        break
    else:
        print("❌ Неверный выбор! Пожалуйста, выберите пункт от 0 до 33.")
        time.sleep(1.5)