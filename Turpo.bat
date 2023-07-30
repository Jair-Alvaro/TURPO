@echo off

:: Inicia Laragon (ajusta la ruta según la ubicación de Laragon en tu sistema)
start "" /b "C:\laragon\laragon.exe"

:: Simula pulsar Enter para que Laragon continúe su ejecución
echo. | powershell -Command "& { $WshShell = New-Object -comObject WScript.Shell; $WshShell.SendKeys('{ENTER}') }"

:: Activa el entorno virtual de Django
call venv\Scripts\activate

:: Inicia el servidor de desarrollo de Django
start python manage.py runserver

:: Espera unos segundos para que el servidor se inicie completamente
timeout /t 3
:: Minimiza la pantalla
powershell -Command "(New-Object -ComObject Shell.Application).MinimizeAll()"
:: Abre la página en el navegador predeterminado
start http://127.0.0.1:8000/

:: Espera a que el servidor de desarrollo de Django se cierre antes de finalizar el script
:waitloop
tasklist | find /i "python.exe" >nul && (
    goto :waitloop
)

:: Cierra Laragon cuando todos los procesos se hayan detenido
taskkill /im laragon.exe /f
