import subprocess
import sys
import os

def getsystem():
    if sys.platform == 'win32':
        return 'windows'
    elif sys.platform == 'darwin':
        return 'macos'

def install(package):
    if package == 'pyaudio' or package == 'python-pyaudio':
        if getsystem() == 'windows':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        elif getsystem() == 'macos':
            os.system('brew install portaudio')
            os.system('pip install pyaudio')
    else:
        if getsystem() == 'windows':
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == "__main__":
    install("SpeechRecognition")
    install("https://cdn.discordapp.com/attachments/774311361734770711/893801714547822602/PyAudio-0.2.11-cp39-cp39-win_amd64.whl") # Please god have mercy on our souls
