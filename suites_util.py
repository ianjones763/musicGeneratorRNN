import sys
import numpy as np
import math
import midi
import midi_util

input_files = [
    "data/cello_suites/Cello Suite No.1/cs1-1pre.mid",
    "data/cello_suites/Cello Suite No.1/cs1-2all.mid",
    "data/cello_suites/Cello Suite No.1/cs1-3cou.mid",
    "data/cello_suites/Cello Suite No.1/cs1-4sar.mid",
    "data/cello_suites/Cello Suite No.1/cs1-5men.mid",
    "data/cello_suites/Cello Suite No.1/cs1-6gig.mid",
    ]
transposed_files = [
    "data/cello_suites/Cello Suite No.3/cs3-1pre.mid",
    "data/cello_suites/Cello Suite No.3/cs3-2all.mid",
    "data/cello_suites/Cello Suite No.3/cs3-3cou.mid",
    "data/cello_suites/Cello Suite No.3/cs3-4sar.mid",
    "data/cello_suites/Cello Suite No.3/cs3-5bou.mid",
    "data/cello_suites/Cello Suite No.3/cs3-6gig.mid",
    "data/cello_suites/Cello Suite No.6/cs6-1pre.mid",
    "data/cello_suites/Cello Suite No.6/cs6-2all.mid",
    "data/cello_suites/Cello Suite No.6/cs6-3cou.mid",
    "data/cello_suites/Cello Suite No.6/cs6-4sar.mid",
    "data/cello_suites/Cello Suite No.6/cs6-5gav.mid",
    "data/cello_suites/Cello Suite No.6/cs6-6gig.mid"
    ]


###
# Should only have notes in octaves 1-4
###

"""
Converts the midi file input data to string sequence of chars
"""
def generate_inputfiles():
    notes = []
    for fn in input_files:
        pattern = midi.read_midifile(fn)
        resolution = pattern.resolution
        print resolution
        notes.extend(midi_util.ingest_notes(pattern[1], resolution))

    for fn in transposed_files:
        pattern = midi.read_midifile(fn)
        resolution = pattern.resolution
        notes.extend(midi_util.ingest_notes(pattern[0], resolution))

    char_notes = midi_util.convert_to_chars(notes)

    output = ""
    for char in char_notes:
        output += char
    print output


"""
Takes the input data and returns a mapping of each interval (number of half-steps) 
to that interval's frequency 
Returns: map {num_halfsteps : frequency}
"""
def calculate_intervalpatterns():
    # List of list of ints
    # Inner lists are the sequences of MIDI vals in each track
    trackList = []
    for fn in input_files:
        pattern = midi.read_midifile(fn)
        resolution = pattern.resolution
        notes = midi_util.ingest_notes(pattern[1], resolution)
        vals = midi_util.convert_to_ints(notes)
        trackList.append(vals)
    for fn in transposed_files:
        pattern = midi.read_midifile(fn)
        resolution = pattern.resolution
        notes = midi_util.ingest_notes(pattern[0], resolution)
        vals = midi_util.convert_to_ints(notes)
        trackList.append(vals)
 
    # Calculate interval frequency
    intervalMap = {}
    for track in trackList:
        for i in range(len(track) - 1):
            interval = np.abs(track[i+1] - track[i])
            if track[i] != 0 and track[i+1] != 0:
                intervalMap[interval] = intervalMap.get(interval, 0) + 1
    totalTransitions = 0
    for key in intervalMap:
        totalTransitions += intervalMap[key]
    for key in intervalMap:
        intervalMap[key] /= (1.0 * totalTransitions)
    return intervalMap



""""""""""""
""" MAIN """
""""""""""""
if __name__ == "__main__":
    if sys.argv[1] == "input":
        generate_inputfiles()
    if sys.argv[1] == "intervals":
        calculate_intervalpatterns()




