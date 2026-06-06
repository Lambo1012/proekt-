@echo off
:: Включаем поддержку UTF-8 для корректного вывода всех эмодзи и спецсимволов в меню
chcp 65001 >nul

:: Проверка прав администратора
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run_script
) else (
    goto :get_admin
)

:get_admin
echo [LAMBO_lega] Запрашиваем права администратора для работы оптимизатора...
powershell -Command "Start-Process '%~f0' -Verb RunAs"
exit /b

:run_script
title 🚀 ＬＡＭＢＯ_ＬＥＧＡ ОПТИМИЗАТОР 🚀

:: Переходим в директорию, где лежит этот батник
cd /d "%~dp0"

:: Запуск Python-скрипта (убедитесь, что имя файла совпадает)
powershell -NoProfile -ExecutionPolicy Bypass -Command "python test.py"

:: Предотвращает закрытие окна при возникновении критических ошибок
if %errorLevel% neq 0 (
    echo.
    echo [Ошибка] Произошел сбой при выполнении Python-скрипта.
    pause
)