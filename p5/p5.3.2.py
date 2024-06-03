class MusicNotes:
    def __init__(self):
        self.notes = [
            [55, 110, 220, 440, 880],  # La
            [61.74, 123.48, 246.96, 493.92, 987.84],  # Si
            [65.41, 130.82, 261.64, 523.28, 1046.56],  # Do
            [73.42, 146.84, 293.68, 587.36, 1174.72],  # Re
            [82.41, 164.82, 329.64, 659.28, 1318.56],  # Mi
            [87.31, 174.62, 349.24, 698.48, 1396.96],  # Fa
            [98, 196, 392, 784, 1568]  # Sol
        ]
        self.octave = 0
        self.note_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.octave >= len(self.notes[0]):
            raise StopIteration

        current_freq = self.notes[self.note_index][self.octave]

        # Move to the next note
        self.note_index += 1
        if self.note_index >= len(self.notes):
            self.note_index = 0
            self.octave += 1

        return current_freq


# Example usage
notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)