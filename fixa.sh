#!/bin/bash

MIDICOMP="/usr/local/bin/midicomp"

mkdir -p temp_files result_dir

${MIDICOMP} "the line trummor.mid" > temp_files/temp_1.asc
python3 try_fix_drum_midi_file.py temp_files/temp_1.asc > temp_files/temp_2.asc
${MIDICOMP} -c result_dir/the_line_trummor.mid < temp_files/temp_2.asc

echo "Trying to play the resulting MIDI file."
timidity result_dir/the_line_trummor.mid

