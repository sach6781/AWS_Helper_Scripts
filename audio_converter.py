import wave
import sys
from pydub import AudioSegment


def wave_to_raw(filename, out_filename):
    sound = AudioSegment.from_wav(filename)  # can do same for mp3 and other formats
    raw = sound._data  # returns byte string
    binary_file = open(out_filename, "wb")
    binary_file.write(raw)


def raw_to_wav(filename, out_filename):
    inp_f = open(filename, "rb")
    data = inp_f.read()
    out_f = wave.open(out_filename, "wb")
    out_f.setnchannels(1)
    out_f.setsampwidth(2)  # number of bytes
    out_f.setframerate(44100)
    out_f.writeframesraw(data)


# wave_to_raw('C:\\Users\\xxxx\\Downloads\\4.wav', 'C:\\Users\\xxxx\\Downloads\\test.wav')
if __name__ == "__main__":
    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n < 4:
        print("\npass correct args  1(wav to raw)/2(raw to ewav) <inutp> <output>")
        exit(0)

    test = int(sys.argv[1])
    filename = sys.argv[2]
    out_filename = sys.argv[3]
    if test == 1:
        wave_to_raw(filename, out_filename)
    if test == 2:
        raw_to_wav(filename, out_filename)
