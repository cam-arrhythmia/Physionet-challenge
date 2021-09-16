#!/usr/bin/python3
# Example challenge entry

import sys
import scipy.io
import os

training_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'training')

# Read waveform samples (input is in WFDB-MAT format)
mat_data = scipy.io.loadmat(os.path.join(training_dir, 'A00001.mat'))
samples = mat_data['val']

# Your classification algorithm goes here...
if samples[0][0] < 0:
    answer = "N"
else:
    answer = "A"

# Write result to answers.txt
answers_file = open(os.path.join(os.path.dirname(__file__), "answers.txt"), "a")
answers_file.write("%s,%s\n" % ('A00001', answer))
answers_file.close()
