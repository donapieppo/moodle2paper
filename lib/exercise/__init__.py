import random
from bs4 import BeautifulSoup

def clean_text(txt):
    return(txt.replace('\(', '$')
              .replace('\)', '$')
              .replace('<p>', '')
              .replace('</p>', '')
              .replace('&egrave;', '\`e'))

def parse_exercises(file_name):
    with open(file_name, 'r') as f:
        soup = BeautifulSoup(f.read(), 'xml')

    exercises = []
    for q in soup.find_all('question'):
        if q.attrs['type'] != 'multichoice':
            continue
        qtext = q.select('questiontext text')[0].get_text()
        if not qtext:
            continue

        exercise = Exercise()
        exercise.set_question(qtext)

        for i, answer in enumerate(q.find_all('answer')):
            a = Answer(answer.get_text().strip(), answer.attrs['fraction'] == '100')
            exercise.add_answer(a)

        exercises.append(exercise)
    return(exercises)

class Answer:
    def __init__(self, text, correct):
        self.text = clean_text(text)
        self.correct = correct

    def __str__(self):
        mark = "*" if self.correct else ""
        return(f"{mark} {self.text}")

class Tipology:
    def __init__(self, filename):
        self.filename = filename
        self.exercises = parse_exercises(filename)

    def num(self):
        len(self.exercises)

    def choose_random(self, n):
        if (len(self.exercises) < n):
            n = len(self.exercises)

        return(random.sample(self.exercises, n))

class Exercise:
    def __init__(self):
        self.answers = []

    def set_question(self, question):
        self.question = clean_text(question)

    def add_answer(self, answer):
        self.answers.append(answer)

    def __str__(self):
        opt = ['a', 'b', 'c', 'd']
        res = f'{self.question}\n \\newline \n'
        for i, a in enumerate(self.answers):
            res = res + '\\fbox{' + opt[i] + '}' + str(a) + '\n'
        return(res)
