@echo off
:: Кодировка UTF-8, чтобы корректно отображался русский текст
chcp 65001 > nul

:: Проверка прав администратора
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo ============================================================
    echo Запрос прав администратора...
    echo ============================================================
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Переход в директорию, где находится сам батник
cd /d "%~dp0"

:: Проверка, установлен ли Python в системе
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ОШИБКА] Python не найден в системе!
    echo Пожалуйста, установите Python и поставьте галочку "Add Python to PATH".
    pause
    exit /b
)

:: Проверка наличия самого скрипта
if not exist "optimizer.py" (
    echo [ОШИБКА] Файл optimizer.py не найден в текущей папке!
    echo Убедитесь, что батник и скрипт находятся в одном месте.
    pause
    exit /b
)

:: Запуск Python-скрипта
echo Запуск оптимизатора...
python optimizer.py

pause