mkdir speech2text_analysis


cd speech2text_analysis


py -0

py -3.12 -m venv venv

source venv/Scripts/activate

touch main.py install.md requirements.txt


python -m pip install pyaudio numpy matplotlib SpeechRecognition

python.exe -m pip install --upgrade pip

python -m pip list > requirements.txt