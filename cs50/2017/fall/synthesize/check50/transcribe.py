import array
import math
import wave

import argparse
import numpy

def main():
    parser = argparse.ArgumentParser(prog="transcribe")
    parser.add_argument("wav", metavar="WAV", help="WAV file to be transcribed")
    args = parser.parse_args()

    with wave.open(args.wav) as wav:
        transcribe(wav.readframes(-1), wav.getframerate())

# Rounds a number (toward 0) to the nearest multiple of `base`
def floor_to(x, base=1):
    return base * (x // base)


def transcribe(frames, frame_rate):
    # The beat size is frame_rate / 4 but we are dealing with bytes, not shorts.
    beat_size = frame_rate // 2;
    note_delim = b"\x00\x00" * 5

    start = 0
    while start < len(frames):

        # Find first non zero value. If it is more than beat_size samples away, we have a rest
        try:
            length = floor_to(next(i for i, x in enumerate(frames[start:]) if x), beat_size)
        except StopIteration:
            length = len(frames[start:])
        print(" " * (length // beat_size), end="")

        # Skip over the rest if there was one
        start += length

        # Get all the data until the next note delimiter.
        # Just to make sure we don't get thrown off by the decay, add beat_size/2 to the
        # index of the match and round down to the nearest beat_size
        length = floor_to(frames[start:].find(note_delim) + beat_size // 2, beat_size)

        if length:
            print(get_frequency(frames[start:start + length], frame_rate)
                  + "+" * (length // beat_size - 1),
                  end="")

        start += length

    # Print newline.
    print()


NOTES = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
def get_frequency(bytes, frame_rate):
    # Parse bytes into 16-bit signed ints.
    samples = array.array("h", bytes)

    # Find distance between points at which the sin curve crosses 0.
    zeros = numpy.diff(numpy.where(numpy.diff(numpy.sign(samples)))[0])

    # Find period of wave in samples average distance between 0s (sin crosses 0 2 times during its period)
    sample_period = 2 * numpy.mean(zeros[zeros > 10])

    # Calculate wave frequency in Hz. Honestly not completely sure why the / 2 is necessary, but it is.
    freq = frame_rate / sample_period / 2

    # Get number of semitones from A440.
    semitones = round(12 * math.log2(freq / 440))

    # Account for octave switch occuring at C, not A
    octave_offset = 5 + (semitones % 12 > 2)
    return NOTES[semitones % 12] + str(semitones // 12 + octave_offset)


if __name__ == "__main__":
    main()
