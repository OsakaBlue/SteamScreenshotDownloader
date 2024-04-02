@echo off

echo Starting URL_from_html.py
python scripts\URL_from_html.py
echo First link list created - urls.txt.

echo Waiting...

echo Starting getURLfromURL.py
python scripts\getURLfromURL.py
echo Second link list created - URLS.

echo Waiting...

echo Starting SaveIMGs.py
python scripts\SaveIMGs.py

echo Screenshots saved in Screenshots folder

echo Removing temporary files...
del /q /s scripts\temp\*.*

pause
