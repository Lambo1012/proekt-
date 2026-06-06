@echo off
:: Принудительно включаем UTF-8 для правильного отображения текста и эмодзи
chcp 65001 >nul

:: Проверка на права администратора
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run_script
) else (
    goto :get_admin
)

:get_admin
echo [LAMBO OPTIMIZATION] Запрашиваем права суперпользователя для настройки системы...
powershell -Command "Start-Process '%~f0' -Verb RunAs"
exit /b

:run_script
title 🚀 ＬＡＭＢＯ_ＬＥＧＡ  ＯＰＴＩＭＩＺＡＴＩＯＮ 🚀

:: Переходим в ту папку, где лежит сам батник и скрипт
cd /d "%~dp0"

:: Запуск твоего Python-скрипта.
:: ВАЖНО: Если твой файл называется НЕ "test.py", замени "test.py" ниже на свое имя!
powershell -NoProfile -ExecutionPolicy Bypass -Command "python test.py"

:: Если скрипт завершится с ошибкой или Python не установлен, консоль не закроется сразу
if %errorLevel% neq 0 (
    echo.
    echo [Ошибка] Скрипт завершил работу некорректно.
    echo Проверь, правильно ли указано имя .py файла внутри батника.
    pause
)