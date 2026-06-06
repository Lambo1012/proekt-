@echo off
:: Включаем поддержку UTF-8, чтобы текст и соцсети не превращались в иероглифы
chcp 65001 >nul

:: Проверка прав администратора
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :run_script
) else (
    goto :get_admin
)

:get_admin
echo Запрашиваем права администратора для LAMBo_lega ОПТИМИЗАТОР...
powershell -Command "Start-Process '%~f0' -Verb RunAs"
exit /b

:run_script
title LAMBo_lega ОПТИМИЗАТОР
:: Переходим в папку, где находится сам батник
cd /d "%~dp0"

:: Запускаем Python внутри безопасного окружения PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command "python test.py"
pause