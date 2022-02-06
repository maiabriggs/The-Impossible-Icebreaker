from random import random

import random

questionFormats = {
    0 : 'Whose aesthetic screams "{adj}" the most?4',
    1 : 'Whose energy could best be described as "{adj}"?4',
    2 : 'Could [name] ever be {adj}?2',
    3 : 'Whose spirit animal is most likely a{animal}?4',
    4 : 'Could a{animal} be domesticated if [name] tried hard enough?2',
    5 : 'Describe a{animal} in one word.W',
    6 : 'Would [name] own a{animal} as a pet?2',
    7 : '{fruit} is evil.2',
    8 : '{fruit} is legendary.2'
}

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
    with open("fruits.txt","r") as fruitsFile:
        fruitsText = fruitsFile.readlines()
        return fruitsText[random.randint(0,len(fruitsText) - 1)][:-1]

def getQuestion():
    randomKey = random.randint(0,8)
    questionFormat = questionFormats[randomKey]
    if randomKey <= 2:
        questionFormat.format(adj = getAdjective())
    elif randomKey <= 6:
        questionFormat.format(animal = getAnimalString())
    elif randomKey <= 8:
        questionFormat.format(fruit = getFruit())
    return questionFormat


