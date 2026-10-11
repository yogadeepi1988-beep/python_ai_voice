import threading
import sys 
import time
import pyaudio
import numpy as mp
import wave
import matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData

stop_event = threading.Event()

def wait_for_enter():
    input(f"\n Press Enter To Stop Recording..............\n")
    stop_event.set()

def spinner():
    chars = '|/-\\|/-\\'
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r Recording.............{chars[1 % 4]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print("\r RECORDING COMPLETE !          ")

def record_audio():