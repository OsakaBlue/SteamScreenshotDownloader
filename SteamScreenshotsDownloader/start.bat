@echo off
echo Creating and activating virtual environment...
python -m venv .venv
call .venv\Scripts\activate

echo Installing required libraries...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Starting the download process...
python download.py

echo Execution completed. Exiting...
deactivate
