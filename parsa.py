#!/usr/bin/python3

import glob
from lib.exercise import Exercise, Answer, Tipology

tipologies = []

for moodle_file in glob.glob('../stefano/db/*.xml'):
    tipology = Tipology(moodle_file)
    for e in tipology.choose_random(3):
        print(e)


exit(0)
with open('res.tex', 'w') as result:
    with open('header.tex', 'r') as f:
        result.write(f.read())
    for n, e in enumerate(exercises):
        result.write(str(e))
    with open('footer.tex', 'r') as f:
        result.write(f.read())



