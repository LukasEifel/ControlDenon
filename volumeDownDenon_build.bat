@echo off
:: get name from filename without path and ext
set name=%~n0
echo ========= %name% =========

:: cut away the suffix "_build"
set name=%name:~0,-6%
set pypath=C:\Users\lukas\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts
set buildpath=%temp%

if not exist %name%.pyw (
    echo ERROR: "%name%.pyw" does not exist here!
    pause
    exit /b
)

%pypath%\pyinstaller.exe --onefile -y %~dp0%name%.pyw --distpath=%~dp0 --workpath=%buildpath% --specpath=%buildpath%