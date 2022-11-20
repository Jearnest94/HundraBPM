import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import librosa
import librosa.display
import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np


def main():
    Tk().withdraw()
    path = tkinter.filedialog.askopenfilename()
    print("Selected file: " + path)
    y, sr = librosa.load(path, sr=None)
    print("Sample Rate: " + str(librosa.get_samplerate(path)))
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    print(tempo)

    bpm = round(tempo[0])
    print(f'{bpm}bpm')
    filename_output_noprefix = (path[path.rfind(r'/'):])
    filename_output_noprefix = filename_output_noprefix[1:]
    old_name = f'{filename_output_noprefix}'
    new_name = f'{bpm} {filename_output_noprefix}'
    print(f"old name: {old_name}")
    print(f"new name: {new_name}")
    os.rename(old_name, new_name)

    """
    D = np.abs(librosa.stft(y))
    times = librosa.times_like(D)
    
    fig, ax = plt.subplots(nrows=2, sharex=True)
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                             y_axis='log', x_axis='time', ax=ax[0], sr=sr)
    ax[0].set(title='Power spectrogram')
    ax[0].label_outer()
    """


if __name__ == '__main__':
    main()
