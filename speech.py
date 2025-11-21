# speech.py
import sounddevice as sd
import soundfile as sf
import tempfile
import os
import time
import speech_recognition as sr

def record_audio(duration=5, samplerate=44100, channels=1):
    """
    Record `duration` seconds from the default microphone and save to a temp WAV file.
    Returns the temp file path.
    """
    print(f"Recording for {duration} seconds...")
    data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
    sd.wait()
    fd, path = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    sf.write(path, data, samplerate)
    print("Saved audio to:", path)
    return path

def transcribe_wav(wav_path):
    """
    Use SpeechRecognition + Google Web Speech API to transcribe the WAV file.
    (No API key required for this quick method; it's free for small usage.)
    """
    r = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return ""

def get_voice_input(duration=5):
    wav = record_audio(duration=duration)
    text = transcribe_wav(wav)
    try:
        os.remove(wav)
    except Exception:
        pass
    return text

# Quick test (uncomment to test directly)
if __name__ == "__main__":
    print(get_voice_input(4))
