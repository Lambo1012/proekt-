@echo off
chcp 65001 >nul

:: Проверка прав администратора
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run_script
) else (
    goto :get_admin
)

:get_admin
echo Запрашиваем права администратора...
powershell -Command "Start-Process '%~f0' -Verb RunAs"
exit /b

:run_script
title LAMBo_lega ОПТИМИЗАТОР
:: Переходим в папку, где лежит сам батник
cd /d "%~dp0"

:: Запуск Python-скрипта внутри сессии PowerShell с правами админа
powershell -NoProfile -ExecutionPolicy Bypass -Command "python test.py"
pause