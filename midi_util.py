import midi


# Only store 8 octaves (don't even need to store that many) #
midi_to_note = {
    24:"C0", 25:"C#0", 26:"D0", 27:"D#0", 28:"E0", 29:"F0", 30:"F#0", 31:"G0", 32:"G#0", 33:"A0", 34:"A#0", 35:"B0",
    36:"C1", 37:"C#1", 38:"D1", 39:"D#1", 40:"E1", 41:"F1", 42:"F#1", 43:"G1", 44:"G#1", 45:"A1", 46:"A#1", 47:"B1",
    48:"C2", 49:"C#2", 50:"D2", 51:"D#2", 52:"E2", 53:"F2", 54:"F#2", 55:"G2", 56:"G#2", 57:"A2", 58:"A#2", 59:"B2",
    60:"C3", 61:"C#3", 62:"D3", 63:"D#3", 64:"E3", 65:"F3", 66:"F#3", 67:"G3", 68:"G#3", 69:"A3", 70:"A#3", 71:"B3",
    72:"C4", 73:"C#4", 74:"D4", 75:"D#4", 76:"E4", 77:"F4", 78:"F#4", 79:"G4", 80:"G#4", 81:"A4", 82:"A#4", 83:"B4",
    84:"C5", 85:"C#5", 86:"D5", 87:"D#5", 88:"E5", 89:"F5", 90:"F#5", 91:"G5", 92:"G#5", 93:"A5", 94:"A#5", 95:"B5",
    96:"C6", 97:"C#6", 98:"D6", 99:"D#6", 100:"E6", 101:"F6", 102:"F#6", 103:"G6", 104:"G#6", 105:"A6", 106:"A#6", 107:"B6",
    108:"C7", 109:"C#7", 110:"D7", 111:"D#7", 112:"E7", 113:"F7", 114:"F#7", 115:"G7", 116:"G#7", 117:"A7", 118:"A#7", 119:"B7"
    }

# Only worry about octaves 1-4, since that is range for cello suites melody (check this)
note_to_char = {
    "C1": "q", "C#1": "w", "D1": "e", "D#1": "r", "E1": "t", "F1": "y", "F#1": "u", "G1": "i", "G#1": "o", "A1": "p", "A#1": "a", "B1": "s",
    "C2": "d", "C#2": "f", "D2": "g", "D#2": "h", "E2": "j", "F2": "k", "F#2": "l", "G2": "z", "G#2": "x", "A2": "c", "A#2": "v", "B2": "b",
    "C3": "Q", "C#3": "W", "D3": "E", "D#3": "R", "E3": "T", "F3": "Y", "F#3": "U", "G3": "I", "G#3": "O", "A3": "P", "A#3": "A", "B3": "S",
    "C4": "D", "C#4": "F", "D4": "G", "D#4": "H", "E4": "J", "F4": "K", "F#4": "L", "G4": "Z", "G#4": "X", "A4": "C", "A#4": "V", "B4": "B",
    "OFF": "N"
    }

# Dict to convert char back to note after getting output
char_to_note = {
    "q": "C1", "w": "C#1", "e": "D1", "r": "D#1", "t": "E1", "y": "F1", "u": "F#1", "i": "G1", "o": "G#1", "p": "A1", "a": "A#1", "s": "B1",
    "d": "C2", "f": "C#2", "g": "D2", "h": "D#2", "j": "E2", "k": "F2", "l": "F#2", "z": "G2", "x": "G#2", "c": "A2", "v": "A#2", "b": "B2",
    "Q": "C3", "W": "C#3", "E": "D3", "R": "D#3", "T": "E3", "Y": "F3", "U": "F#3", "I": "G3", "O": "G#3", "P": "A3", "A": "A#3", "S": "B3",
    "D": "C4", "F": "C#4", "G": "D4", "H": "D#4", "J": "E4", "K": "F4", "L": "F#4", "Z": "G4", "X": "G#4", "C": "A4", "V": "A#4", "B": "B4",
    "N": "OFF"
    }

# Dict to convert note to midi value
note_to_midi = {
    "C0":24, "C#0":25, "D0":26, "D#0":27, "E0":28, "F0":29, "F#0":30, "G0":31, "G#0":32, "A0":33, "A#0":34, "B0":35,
    "C1":36, "C#1":37, "D1":38, "D#1":39, "E1":40, "F1":41, "F#1":42, "G1":43, "G#1":44, "A1":45, "A#1":46, "B1":47,
    "C2":48, "C#2":49, "D2":50, "D#2":51, "E2":52, "F2":53, "F#2":54, "G2":55, "G#2":56, "A2":57, "A#2":58, "B2":59,
    "C3":60, "C#3":61, "D3":62, "D#3":63, "E3":64, "F3":65, "F#3":66, "G3":67, "G#3":68, "A3":69, "A#3":70, "B3":71,
    "C4":72, "C#4":73, "D4":74, "D#4":75, "E4":76, "F4":77, "F#4":78, "G4":79, "G#4":80, "A4":81, "A#4":82, "B4":83,
    "C5":84, "C#5":85, "D5":86, "D#5":87, "E5":88, "F5":89, "F#5":90, "G5":91, "G#5":92, "A5":93, "A#5":94, "B5":95,
    "C6":96, "C#6":97, "D6":98, "D#6":99, "E6":100, "F6":101, "F#6":102, "G6":103, "G#6":104, "A6":105, "A#6":106, "B6":107,
    "C7":108, "C#7":109, "D7":110, "D#7":111, "E7":112, "F7":113, "F#7":114, "G7":115, "G#7":116, "A7":117, "A#7":118, "B7":119,
    "OFF":0
    }


""""""""""""""""""""""""""""""""""""""""""
"     """" READ IN MIDI DATA AND """"    "
"        "" RETURN NOTE SEQUENCE ""      "
""""""""""""""""""""""""""""""""""""""""""
def ingest_notes(track, resolution):
    smallest_increment = resolution / 4         # keep track of 1/16th note increments
    notes = []
    noteStruck = False
 
    # Iterate through events in track, storing sequence of notes #
    for msg in track:
        #print msg
        # Detect end of track, continue
        if isinstance(msg, midi.EndOfTrackEvent):
            #print "End of Track Event"
            continue

        # msg.tick is duration of note/rest
        duration = msg.tick
        # Represent longer note/rest as multiple articuations of that note/rest
        numArticulations = duration / smallest_increment
            

        ## Note is on, (velocity == 0 implies note is off) ##
        if isinstance(msg, midi.NoteOnEvent) and msg.get_velocity() != 0:
            noteInProgress = True
            for i in range(numArticulations):
               notes.append("OFF")

        ## Note ended or is off, (velocity == 0 implies note is off) ##
        elif isinstance(msg, midi.NoteOffEvent) or \
             (isinstance(msg, midi.NoteOnEvent) and msg.get_velocity() == 0):
            
            # Note ended
            if noteInProgress: 
                for i in range(numArticulations):
                    notes.append(midi_to_note[msg.get_pitch()])
                noteInProgress = False
            # Note off
            else:
                notes.append("OFF")
    return notes


""""""""""""""""""""""""""""""""""""""""""
"   """" READ IN SEQUENCE OF INTS """"   "
"         "" OUTPUT MIDI FILE ""         "
""""""""""""""""""""""""""""""""""""""""""
def notes_to_midi(midi_vals, fn):
    # Instantiate a MIDI Pattern (contains a list of tracks)
    pattern = midi.Pattern()
    pattern.resolution = 480
    # Instantiate a MIDI Track (contains a list of MIDI events)
    track = midi.Track()
    # Append the track to the pattern
    pattern.append(track)
    
    for val in midi_vals:
        vel = 0 if val == 0 else 100
        # Instantiate a MIDI note on event, append it to the track
        on = midi.NoteOnEvent(tick=0, velocity=vel, pitch=val)
        track.append(on)
            
        # Instantiate a MIDI note off event, append it to the track (1/16th note = 480/16 = 30 ticks)
        off = midi.NoteOffEvent(tick=120, pitch=val)
        track.append(off)

    # Add the end of track event, append it to the track
    eot = midi.EndOfTrackEvent(tick=0)
    track.append(eot)
    # Print out the pattern
    print pattern
    # Save the pattern to disk
    midi.write_midifile(fn, pattern)





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""  Given input array of notes, returns array of chars for input to RNN  """""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def convert_to_chars(notes):
    chars = []
    for note in notes:
        chars.append(note_to_char[note])
    return chars


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""     Given output array of chars from RNN, returns array of notes      """""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def convert_to_notes(chars):
    notes = []
    for char in chars:
        notes.append(char_to_note[char])
    return notes

def convert_to_ints(notes):
    ints = []
    for note in notes:
        ints.append(note_to_midi[note])
    return ints



