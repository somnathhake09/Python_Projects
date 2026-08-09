"""
एकतर्फी प्रेम (One-Side Love) - Original Marathi Song
Prints original lyrics and generates offline TTS audio + soft beat backing.
"""

import pyttsx3
import numpy as np
import wave
import struct

# ---------------- 1. ORIGINAL LYRICS ----------------
lyrics = """
नजरेत तुझ्या शोधतो मी
माझ्यासाठी एक जागा
पण तू मात्र नकळत जाशी
घेऊन माझ्या मनीचा ठसा

बोलायचं होतं खूप काही
शब्द ओठांवर अडखळले
तुझ्या येण्या-जाण्याने रोज
माझे दिवस उजळले

तू नाही म्हणालीस कधी
पण हो पण म्हणाली नाहीस
एकटाच चालतो या वाटेवर
तरी तुझ्या आठवणीत हरवतो मी रोज नव्याने

कदाचित हे प्रेम अपुरं राहील
कदाचित तू कधी कळणार नाहीस
पण जोवर श्वास आहे माझा
तुझ्यावरचं प्रेम कमी होणार नाही
"""

print("=" * 45)
print(" गीत: एकतर्फी प्रेम ".center(45, "="))
print("=" * 45)
print(lyrics)
print("=" * 45)

# ---------------- 2. TEXT-TO-SPEECH (offline, Marathi voice) ----------------
engine = pyttsx3.init()
for voice in engine.getProperty("voices"):
    if "mr" in voice.id.lower() or "marathi" in voice.name.lower():
        engine.setProperty("voice", voice.id)
        break

engine.setProperty("rate", 120)   # slower, emotional pace
voice_file = "/home/claude/love_voice.wav"

# NOTE: espeak/pyttsx3 silently fails to write very long text in one go,
# so we split into stanzas, synthesize each separately, then stitch together.
stanzas = [s.strip() for s in lyrics.strip().split("\n\n") if s.strip()]
stanza_files = []
for idx, stanza in enumerate(stanzas):
    fpath = f"/home/claude/stanza_{idx}.wav"
    engine.save_to_file(stanza, fpath)
    engine.runAndWait()
    stanza_files.append(fpath)

from pydub import AudioSegment
combined = AudioSegment.silent(duration=300)
pause = AudioSegment.silent(duration=700)
for fpath in stanza_files:
    combined += AudioSegment.from_wav(fpath) + pause
combined.export(voice_file, format="wav")
print(f"आवाज तयार झाला: {voice_file}")

# ---------------- 3. SOFT MELODIC BACKING (gentle pad tone, not a hard beat) ----------------
def generate_pad(duration_sec, sample_rate=22050):
    """Soft ambient pad using layered sine waves (emotional background)."""
    t = np.linspace(0, duration_sec, int(duration_sec * sample_rate), False)
    freqs = [196.0, 246.94, 293.66]  # G3, B3, D4 - soft minor-ish chord
    pad = sum(np.sin(2 * np.pi * f * t) for f in freqs) / len(freqs)
    # slow volume swell/fade envelope repeating every ~4s
    envelope = 0.15 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 4 - np.pi / 2))
    return pad * envelope, sample_rate

import wave as wv
with wv.open(voice_file, "rb") as vf:
    voice_duration = vf.getnframes() / vf.getframerate()

pad_track, sr = generate_pad(voice_duration + 1)

with wave.open("/home/claude/pad.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sr)
    for sample in pad_track:
        f.writeframes(struct.pack("<h", int(sample * 32000)))

print("पार्श्वसंगीत (soft pad) तयार झालं: pad.wav")

# ---------------- 4. MIX VOICE + PAD ----------------
try:
    from pydub import AudioSegment
    voice = AudioSegment.from_wav(voice_file)
    pad = AudioSegment.from_wav("/home/claude/pad.wav")
    pad = pad[:len(voice)] - 8
    final = voice.overlay(pad)
    final.export("/mnt/user-data/outputs/oneside_love_song.wav", format="wav")
    print("अंतिम गाणं सेव्ह झालं: oneside_love_song.wav")
except Exception as e:
    import shutil
    shutil.copy(voice_file, "/mnt/user-data/outputs/oneside_love_song.wav")
    print(f"(टीप: mix करता आलं नाही - {e}) फक्त आवाज सेव्ह केला.")