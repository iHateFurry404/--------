from random import randint

def shuffleCard(list):
    result = list[:]
    n = len(result)
    
    for i in range(n):
        randomIndex = randint(i, n - 1)
        result[i], result[randomIndex] = result[randomIndex], result[i]
        
    return result

def returnCard(cards, sumOfCard):
    kindOfCard = ''
    numberOfCard = ''

    if cards[0] == 'S':
        kindOfCard = '스페이드'
    elif cards[0] == 'H':
        kindOfCard = '하트'
    elif cards[0] == 'D':
        kindOfCard = '다이아몬드'
    elif cards[0] == 'C':
        kindOfCard = '클럽'

    checker = 0
    try:
        checker = int(cards[1:])
    except:
        checker = -1
        
    if checker >= 1:
        numberOfCard = cards[1]
        sumOfCard += checker
    elif cards[1] == 'A':
        numberOfCard = '에이스'
        
        if sumOfCard + 11 <= 21:
            sumOfCard += 11
        else:
            sumOfCard += 1
    elif cards[1] == 'J':
        numberOfCard = '잭'
        sumOfCard += 10
    elif cards[1] == 'Q':
        numberOfCard = '퀸'
        sumOfCard += 10
    elif cards[1] == 'K':
        numberOfCard = '킹'
        sumOfCard += 10
        
    return kindOfCard, numberOfCard, sumOfCard
