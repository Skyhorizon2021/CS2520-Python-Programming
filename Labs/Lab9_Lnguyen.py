#Name: Loc Nguyen
#Lab 9 
'''Objective: 
A student object should contain at least the following fields: name, id, the current quiz score, and the
highest quiz score. A student is allowed to test tests as many times as he/she wishes. Initially the above
two scores are set to 0. Once a student takes a test (should be 5 multiple choice questions), it will
update the current test score (the score for this quiz), may also updates the highest test score if this test
score is higher than the stored highest score. Your should decide whether additional Objects should be
included, e.g. Test objects, Score objects,
'''
class Student:
    def __init__(self, name, id, score, highscore):
        self.name = name
        self.id = id
        self.score = score
        self.highscore = highscore
        pass