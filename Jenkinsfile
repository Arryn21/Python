@echo off

REM Checkout
git clone https://github.com/Arryn21/Python.git .

REM Setup Environment
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM Run Tests
call venv\Scripts\activate.bat
pytest --html=report.html

REM Archive the test report
copy report.html <desired_location>

REM Check result
IF %ERRORLEVEL% EQU 0 (
    echo Build and tests were successful!
) ELSE (
    echo Build or tests failed!
)

pause
