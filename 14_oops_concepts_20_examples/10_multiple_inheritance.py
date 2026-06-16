# Topic: OOP Concepts
# Example: 10 multiple inheritance

class Developer:
    def code(self):
        print('Writing code')

class Trainer:
    def train(self):
        print('Delivering training')

class TechTrainer(Developer, Trainer):
    pass

person = TechTrainer()
person.code()
person.train()
