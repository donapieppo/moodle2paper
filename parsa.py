#!/usr/bin/python3

import glob
from lib.exercise import Exercise, Answer, Tipology

tipologies = []
total = ""

for moodle_file in glob.glob('test/*.xml'):
    tipology = Tipology(moodle_file)
    for e in tipology.choose_random(3):
        total = total + str(e)

with open('result/res.tex', 'w') as result:
    with open('tex/header.tex', 'r') as f:
        result.write(f.read())
    result.write(total)
    with open('tex/footer.tex', 'r') as f:
        result.write(f.read())



