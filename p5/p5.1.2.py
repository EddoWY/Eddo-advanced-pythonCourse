
# import winsound doesn't work
from pydub.generators import Sine
import simpleaudio as sa

# Dictionary of notes and their frequencies
freqs = {
    "la": 220,
    "si": 247,
    "do": 261,
    "re": 293,
    "mi": 329,
    "fa": 349,
    "sol": 392,
}

# String of notes and their durations
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

# Split the string by hyphens to create a list of notes with their durations
note_list = notes.split('-')

# Loop to play the notes
for note in note_list:
    # Split each note-duration pair by the comma
    note_name, duration = note.split(',')

    # Get the frequency of the note from the dictionary
    frequency = freqs[note_name]

    # Convert the duration to an integer (in milliseconds)
    duration = int(duration)

    # Generate the sound for the note
    sine_wave = Sine(frequency).to_audio_segment(duration=duration)

    # Play the note using simpleaudio
    play_obj = sa.play_buffer(
        sine_wave.raw_data,
        num_channels=1,
        bytes_per_sample=2,
        sample_rate=sine_wave.frame_rate
    )

    # Wait for the note to finish playing
    play_obj.wait_done()