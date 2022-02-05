from random import random


import random

def getAnimalString():
    with open("animals.txt","r") as animalsFile:
        animalsText = animalsFile.readlines()
        randomAnimal = animalsText[random.randint(0,len(animalsText) - 1)]
        if randomAnimal[0].lower() in ['a','e','i','o','u',"x"]:
            return "n " + randomAnimal[:-1]
        else:
            return " " + randomAnimal[:-1]

def getAdjective():
    with open("adjectives.txt","r") as adjectivesFile:
        adjectivesText = adjectivesFile.readlines()
        return adjectivesText[random.randint(0,len(adjectivesText) - 1)][:-1]

def getFruit():
    with open("fruits.txt","r") as fruitsile:
        fruitsText = fruitsFile.readlines()
        return fruitsText[random.randint(0,len(fruitsText) - 1)][:-1]

questionFormats = {
    0 : 'Whose aesthetic screams "{adj}" the most?',
    1 : 'Whose energy could best be described as "{adj}"?',
    2 : 'Could [name] ever be {adj}?',
    3 : 'Whose spirit animal is most likely a{animal}?',
    4 : 'Could a{animal} be domesticated if [name] tried hard enough?',
    5 : 'Describe a{animal} in one word.',
    6 : 'Would [name] own a{animal} as a pet?',
    7 : 'Does ?'
    8 : '
}


with open("TestQuestions.txt","w") as testQsFile:
    for i in range(15):
        randomInteger = random.randint(0,6)
        if randomInteger <= 2:
            testQsFile.writelines(questionFormats[randomInteger].format(adj = getAdjective())+ "\n")
        elif randomInteger <= 6:
            testQsFile.writelines(questionFormats[randomInteger].format(animal = getAnimalString())+ "\n")
