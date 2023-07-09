from random import randrange
from time import sleep
from blackjackModule import shuffleCard

def printLeftMoney(playerLeftMoney, defaultPlayerMoney):
    if playerLeftMoney < defaultPlayerMoney:
        print(f'현재 남은 돈 : \033[31m{playerLeftMoney}\033[0m')
    else:
        if playerLeftMoney == defaultPlayerMoney:
            print(f'현재 남은 돈 : \033[32m{playerLeftMoney}\033[0m')
        elif playerLeftMoney > defaultPlayerMoney:
            if playerLeftMoney > 1000:
                print(f'현재 남은 돈 : \033[96m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 900:
                print(f'현재 남은 돈 : \033[95m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 700:
                print(f'현재 남은 돈 : \033[94m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 600:
                print(f'현재 남은 돈 : \033[92m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 500:
                print(f'현재 남은 돈 : \033[36m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 400:
                print(f'현재 남은 돈 : \033[35m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 300:
                print(f'현재 남은 돈 : \033[34m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 200:
                print(f'현재 남은 돈 : \033[92m{playerLeftMoney}\033[0m')
            elif playerLeftMoney > 150:
                print(f'현재 남은 돈 : \033[33m{playerLeftMoney}\033[0m')


spade = ['SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK']
heart = ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK']
diamond = ['DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK']
club = ['CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK']

cardArr = ['에이스', 2, 3, 4, 5, 6, 7, 8, 9, '잭', '퀸', '킹']

cards = shuffleCard((spade + heart + diamond + club) * 2)

playerCards = []
computerCards = []

playerLeftMoney = 100

repeat = 1
repeatRequest = input('몇판 하시겠습니까? ')

while repeatRequest is None:
    print('아무것도 입력하수는 없습니다!')
    repeatRequest = input('몇판 하시겠습니까? ')

try:
    repeatRequest = int(repeatRequest)
except:
    repeatRequest = None

while repeatRequest is None:
    print('숫자로 입력해주세요!')
    repeatRequest = input('몇판 하시겠습니까? ')
    try:
        repeatRequest = int(repeatRequest)
    except:
        repeatRequest = None
while repeatRequest < 1:
    print('적어도 1판은 해야합니다!')
    repeatRequest = input('몇판 하시겠습니까? ')
    try:
        repeatRequest = int(repeatRequest)
    except:
        repeatRequest = None

while repeat <= repeatRequest:
    repeat += 1
    canInsurance = False
    if len(cards) <= 9:
        print('적어도 게임을 진행하려면 카드가 10개 필요합니다!')
        resetCardDeck = input('다시 덱을 초기화 할까요? (예/아니오) ')
        while resetCardDeck is None:
            print('아무것도 입력할수는 없습니다!')
            resetCardDeck = input('다시 덱을 초기화 할까요? (예/아니오) ')
        while resetCardDeck != '예' and resetCardDeck != '아니오':
            print(f'{resetCardDeck}이(가) 아닌 (예/아니오)를 입력해주세요!')
            resetCardDeck = input('다시 덱을 초기화 할까요? (예/아니오) ')
        if resetCardDeck == '예':
            cards = spade + heart + diamond + club
            print('덱을 초기화 했습니다.')
        else:
            print('알겠습니다. 게임을 종료하겠습니다.')
            break

    shuffleCard(cards)

    playerCards = []
    computerCards = []
    defaultPlayerMoney = 100
    playerBet = input('얼마나 거시겠습니까? ')

    sumOfCard = 0
    sumOfComputerCard = 0

    while playerBet is None:
        print('아무것도 입력할수는 없습니다!')
        playerBet = input('얼마나 거시겠습니까? ')
    try:
        playerBet = int(playerBet)
    except:
        playerBet = None
    """
    while playerBet > defaultPlayerMoney:
        print(f'기본 지급 금액인 {defaultPlayerMoney}보다 더 높게 걸 수 없습니다!')
        playerBet = int(input('얼마나 거시겠습니까? '))
        try:
            playerBet = int(playerBet)
        except:
            playerBet = None
    """
    while int(playerBet) < 1:
        while playerBet == None:
            print('아무것도 입력할수는 없습니다!')
            playerBet = input('얼마나 거시겠습니까? ')
        try:
            playerBet = int(playerBet)
        except:
            playerBet = None
        print(f'적어도 1이상은 걸어야 합니다!')
        playerBet = input('얼마나 거시겠습니까? ')
        try:
            playerBet = int(playerBet)
        except:
            playerBet = None
    while int(playerBet) > 200:
        while playerBet is None:
            print('아무것도 입력할수는 없습니다!')
            playerBet = input('얼마나 거시겠습니까? ')
        try:
            playerBet = int(playerBet)
        except:
            playerBet = None
        print(f'200 이상으로는 걸수 없습니다!')
        playerBet = input('얼마나 거시겠습니까? ')
        try:
            playerBet = int(playerBet)
        except:
            playerBet = None
    playerLeftMoney -= playerBet
    printLeftMoney(playerLeftMoney, defaultPlayerMoney)

    for _ in range(2):
        a = cards[randrange(0, len(cards))]
        computerCards.append(a)
        cards.remove(a)

    print('딜러의 카드는 ', end='')

    for i in computerCards:
        kindOfComputerCard = ''
        numberOfComputerCard = ''

        if i[0] == 'S':
            # kindOfComputerCard = '스페이드'
            kindOfComputerCard = '♠'
        elif i[0] == 'H':
            # kindOfComputerCard = '하트'
            kindOfComputerCard = '♥'
        elif i[0] == 'D':
            # kindOfComputerCard = '다이아몬드'
            kindOfComputerCard = '♦'
        elif i[0] == 'C':
            # kindOfComputerCard = '클럽'
            kindOfComputerCard = '♣'

        checker = 0
        try:
            checker = int(i[1:])
        except:
            checker = -1

        if checker >= 1:
            numberOfComputerCard = i[1]
            sumOfComputerCard += checker
        elif i[1] == 'A':
            numberOfComputerCard = '에이스'

            if sumOfComputerCard <= 10:
                sumOfComputerCard += 11
            else:
                sumOfComputerCard += 1
        elif i[1] == 'J':
            numberOfComputerCard = '잭'
            sumOfComputerCard += 10
        elif i[1] == 'Q':
            numberOfComputerCard = '퀸'
            sumOfComputerCard += 10
        elif i[1] == 'K':
            numberOfComputerCard = '킹'
            sumOfComputerCard += 10

        if kindOfComputerCard == '스페이드' and numberOfComputerCard == '에이스':
            canInsurance = True

        if not i == computerCards[1]:
            print(f'첫 번째 딜러의 카드는 {kindOfComputerCard} {numberOfComputerCard}, 딜러의 카드의 합은 {sumOfComputerCard}입니다.')

    playerBlackJack = False
    playerBust = False
    computerBust = False
    computerBlackJack = False

    for _ in range(2):
        a = cards[randrange(0, len(cards))]
        playerCards.append(a)
        cards.remove(a)

    print('당신의 카드는 ', end='')

    sumOfCard = 0

    for i in playerCards:
        kindOfCard = ''
        numberOfCard = ''

        if i[0] == 'S':
            # kindOfCard = '스페이드'
            kindOfCard = '♠'
        elif i[0] == 'H':
            # kindOfCard = '하트'
            kindOfCard = '♥'
        elif i[0] == 'D':
            # kindOfCard = '다이아몬드'
            kindOfCard = '♦'
        elif i[0] == 'C':
            # kindOfCard = '클럽'
            kindOfCard = '♣'

        checker = 0
        try:
            checker = int(i[1:])
        except:
            checker = -1

        if checker >= 1:
            numberOfCard = i[1]
            sumOfCard += checker
        elif i[1] == 'A':
            numberOfCard = '에이스'

            if sumOfCard + 11 <= 21:
                sumOfCard += 11
            else:
                sumOfCard += 1
        elif i[1] == 'J':
            numberOfCard = '잭'
            sumOfCard += 10
        elif i[1] == 'Q':
            numberOfCard = '퀸'
            sumOfCard += 10
        elif i[1] == 'K':
            numberOfCard = '킹'
            sumOfCard += 10

        if i == playerCards[1]:
            print(f'{kindOfCard} {numberOfCard}으로(로) 당신의 카드의 합은 {sumOfCard}입니다.')
        else:
            print(f'{kindOfCard} {numberOfCard}, ', end='')
    doSurrender = False
    doInsurance = False
    doEvenMoney = False
    if sumOfCard == 21:
        print(f'\033[32m블랙잭\033[0m! 딜러의 카드를 기다리십시오!')
        playerBlackJack = True
    else:
        surrender = input('서렌더 하시겠습니까? (예, 아니오) ')
        while surrender != '예' and surrender != '아니오':
            print(f'{surrender}이(가) 아닌 (예/아니오)를 입력해주세요!')
            surrender = input('서렌더 하시겠습니까? (예, 아니오) ')
        if surrender == '예':
            print('서렌더 하셨습니다. 배팅금의 절반을 반올림한 값을 돌려드리겠습니다.')
            playerLeftMoney += round(playerBet / 2)
            doSurrender = True
            printLeftMoney(playerLeftMoney, defaultPlayerMoney)
            continue
        if canInsurance and playerBlackJack:
            evenMoney = input('이븐 머니를 하시겠습니까? (예, 아니오) ')
            while evenMoney != '예' and evenMoney != '아니오':
                print(f'{evenMoney}이(가) 아닌 (예/아니오)를 입력해주세요!')
                evenMoney = input('이븐 머니를 하시겠습니까? (예, 아니오) ')
            if evenMoney == '예':
                print('이븐 머니를 하셨습니다. 돈은 돌려주고 게임은 플레이어측의 우승으로 진행하겠습니다.')
                playerLeftMoney += playerBet
                doEvenMoney = True
                printLeftMoney(playerLeftMoney, defaultPlayerMoney)
                continue
        elif canInsurance:
            insurance = input('인슈어런스를 하시겠습니까? (예, 아니오) ')
            while insurance != '예' and insurance != '아니오':
                print(f'{insurance}이(가) 아닌 (예/아니오)를 입력해주세요!')
                insurance = input('인슈어런스를 하시겠습니까? (예, 아니오) ')
            if insurance == '예':
                print('인슈어런스를 하셨습니다. 건 돈의 절반을 반올림 한 값을 보험금으로 지불합니다! 이제 딜러의 카드를 기다립시오!')
                insuranceMoney = round(playerBet / 2)
                playerLeftMoney -= insuranceMoney
                printLeftMoney(playerLeftMoney, defaultPlayerMoney)
                doInsurance = True
        decide = input('어떻게 하실겁니까? (히트, 더블 다운, 스탠드(혹은 스테이)) ')
        while decide == None:
            print('아무것도 입력할수는 없습니다!')
            decide = input('어떻게 하실겁니까? (히트, 더블 다운, 스탠드(혹은 스테이)) ')
        while decide != '히트' and decide != '더블 다운' and decide != '스탠드' and decide != '스테이':
            print(f'{decide}은(는) 선택할 수 없습니다!')
            decide = input('어떻게 하실겁니까? (히트, 더블 다운, 스탠드(혹은 스테이)) ')
        if decide == '스탠드' or decide == '스테이':
            pass
        elif decide == '더블 다운':

            a = cards[randrange(0, len(cards))]
            playerCards.append(a)
            cards.remove(a)

            kindOfCard = ''
            numberOfCard = ''

            if i[0] == 'S':
                # kindOfCard = '스페이드'
                kindOfCard = '♠'
            elif i[0] == 'H':
                # kindOfCard = '하트'
                kindOfCard = '♥'
            elif i[0] == 'D':
                # kindOfCard = '다이아몬드'
                kindOfCard = '♦'
            elif i[0] == 'C':
                # kindOfCard = '클럽'
                kindOfCard = '♣'

            checker = 0
            try:
                checker = int(a[1:])
            except:
                checker = -1

            if checker > -1:
                numberOfCard = a[1]
                sumOfCard += checker
            elif a[1] == 'A':
                numberOfCard = '에이스'

                if sumOfCard + 11 <= 21:
                    sumOfCard += 11
                else:
                    sumOfCard += 1
            elif a[1] == 'J':
                numberOfCard = '잭'
                sumOfCard += 10
            elif a[1] == 'Q':
                numberOfCard = '퀸'
                sumOfCard += 10
            elif a[1] == 'K':
                numberOfCard = '킹'
                sumOfCard += 10
            if playerBet * 2 > 200:
                print(f'더블 다운을 당신이 걸었던 돈이 \033[34m{playerBet}\033[0m에서 \033[91m{playerBet * 2}\033[0m이 되었습니다!')
            elif playerBet * 2 > 300:
                print(f'더블 다운을 당신이 걸었던 돈이 \033[34m{playerBet}\033[0m에서 \033[31m{playerBet * 2}\033[0m이 되었습니다!')
            else:
                print(f'당신이 걸었던 돈이 \033[34m{playerBet}\033[0m에서 \033[36m{playerBet * 2}\033[0m이 되었습니다!')
            print(f'더블 다운을해 {kindOfCard} {numberOfCard}이(가) 나왔습니다. 당신의 카드의 합은 {sumOfCard}이 됩니다.')
            playerBet *= 2
            playerLeftMoney -= playerBet // 2
            printLeftMoney(playerLeftMoney, defaultPlayerMoney)

            if sumOfCard > 21:
                print(f'\033[31m버스트! 당신의 카드의 합인 {sumOfCard}이(가) 21을 초과했습니다!\033[0m')
                playerBust = True
            elif sumOfCard == 21:
                print(f'\033[32m21\033[0m! 이제 딜러의 카드를 기다리십시오!')
        elif decide == '히트':
            hitDecide = '예'
            while hitDecide == '예':
                a = cards[randrange(0, len(cards))]
                playerCards.append(a)
                cards.remove(a)

                kindOfCard = ''
                numberOfCard = ''

                if i[0] == 'S':
                    # kindOfCard = '스페이드'
                    kindOfCard = '♠'
                elif i[0] == 'H':
                    # kindOfCard = '하트'
                    kindOfCard = '♥'
                elif i[0] == 'D':
                    # kindOfCard = '다이아몬드'
                    kindOfCard = '♦'
                elif i[0] == 'C':
                    # kindOfCard = '클럽'
                    kindOfCard = '♣'

                checker = 0
                try:
                    checker = int(a[1:])
                except:
                    checker = -1

                if checker > -1:
                    numberOfCard = a[1]
                    sumOfCard += checker
                elif a[1] == 'A':
                    numberOfCard = '에이스'

                    if sumOfCard + 11 <= 21:
                        sumOfCard += 11
                    else:
                        sumOfCard += 1
                elif a[1] == 'J':
                    numberOfCard = '잭'
                    sumOfCard += 10
                elif a[1] == 'Q':
                    numberOfCard = '퀸'
                    sumOfCard += 10
                elif a[1] == 'K':
                    numberOfCard = '킹'
                    sumOfCard += 10

                print(f'히트를해 {kindOfCard} {numberOfCard}이(가) 나왔습니다. 당신의 카드의 합은 {sumOfCard}이 됩니다.')
                if sumOfCard > 21:
                    print(f'\033[31m버스트! 당신의 카드의 합인 {sumOfCard}이(가) 21을 초과했습니다!\033[0m')
                    playerBust = True
                    break
                elif sumOfCard == 21:
                    print(f'\033[32m21\033[0m! 이제 딜러의 카드를 기다리십시오!')
                    break
                else:
                    hitDecide = input('더 하시겠습니까? (예/아니오) ')
                    while hitDecide == None:
                        print('아무것도 입력할수는 없습니다!')
                        hitDecide = input('더 하시겠습니까? (예/아니오) ')
                    while hitDecide != '예' and hitDecide != '아니오':
                        print(f'{hitDecide}이(가) 아닌 (예/아니오)를 입력해주세요!')
                        hitDecide = input('더 하시겠습니까? (예/아니오) ')

    print(f'딜러의 나머지 카드는 {kindOfComputerCard} {numberOfComputerCard}으로(로), 합은 {sumOfComputerCard}입니다.')
    if sumOfComputerCard == 21:
        print(f'\033[31m딜러의 블랙잭\033[0m!')
        computerBlackJack = True
    else:
        # 16 이하면 무조건 히트, 17 이상이면 무조건 스탠드
        while sumOfComputerCard <= 16:
            a = cards[randrange(0, len(cards))]
            computerCards.append(a)
            cards.remove(a)

            kindOfComputerCard = ''
            numberOfComputerCard = ''

            if i[0] == 'S':
                # kindOfComputerCard = '스페이드'
                kindOfComputerCard = '♠'
            elif i[0] == 'H':
                # kindOfComputerCard = '하트'
                kindOfComputerCard = '♥'
            elif i[0] == 'D':
                # kindOfComputerCard = '다이아몬드'
                kindOfComputerCard = '♦'
            elif i[0] == 'C':
                # kindOfComputerCard = '클럽'
                kindOfComputerCard = '♣'

            checker = 0
            try:
                checker = int(a[1:])
            except:
                checker = -1

            if checker > -1:
                numberOfComputerCard = a[1]
                sumOfComputerCard += checker
            elif a[1] == 'A':
                numberOfComputerCard = '에이스'

                if sumOfComputerCard + 11 <= 21:
                    sumOfComputerCard += 11
                else:
                    sumOfComputerCard += 1
            elif a[1] == 'J':
                numberOfComputerCard = '잭'
                sumOfComputerCard += 10
            elif a[1] == 'Q':
                numberOfComputerCard = '퀸'
                sumOfComputerCard += 10
            elif a[1] == 'K':
                numberOfComputerCard = '킹'
                sumOfComputerCard += 10

            print(f'딜러가 히트를해 {kindOfComputerCard} {numberOfComputerCard}이(가) 나왔습니다. 딜러의 카드의 합은 {sumOfComputerCard}입니다.')
            if sumOfComputerCard > 21:
                print('\033[32m딜러의 버스트\033[0m!')
                computerBust = True
                break
            elif sumOfComputerCard == 21:
                print('\033[31m딜러의 21\033[0m!')
            sleep(2)
    if doSurrender:
        print('서렌더 하셨습니다, 돌려받는것은 없습니다!')
    elif doInsurance:
        if computerBlackJack:
            print('\333[32m딜러는 블랙잭이었습니다\033[0m! 보험금의 \033[36m2배\033[0m를 드리겠습니다!')
            playerLeftMoney += insuranceMoney * 2
        else:
            print('안타깝게도 \033[31m딜러는 블랙잭이 아니었습니다\033[0m. 돌려받는 돈은 없습니다...')
    elif doEvenMoney:
        print('이븐 머니를 하셨으므로 게임은 그대로 진행됩니다.')
    elif playerBlackJack and computerBlackJack:
        print('플레이어와 딜러의 블랙잭, 걸었던 돈을 돌려드립니다.')
        playerLeftMoney += playerBet
        printLeftMoney(playerLeftMoney, defaultPlayerMoney)
    elif not playerBlackJack and computerBlackJack:
        print('\033[31딜러의 블랙잭\033[0m으로 돌려받는 돈은 없습니다...')
    elif playerBlackJack and not computerBlackJack:
        print('\033[32m플레이어의 블랙잭\033[0m! 걸었던 돈의 \033[34m2.5배\033[0m를 반올림 한 돈을 돌려드리겠습니다!')
        playerLeftMoney += round(playerBet * 2.5)
        printLeftMoney(playerLeftMoney, defaultPlayerMoney)
    elif computerBust and playerBust:
        print('\033[31m플레이어와 딜러 양측의 버스트\033[0m! 돌려받는 돈은 없습니다...')
    elif computerBust and not playerBust:
        print('\033[32m플레이어의 승리\033[0m! 걸었던 돈의 \033[36m2배\033[0m를 돌려드리겠습니다!')
        playerLeftMoney += playerBet * 2
        printLeftMoney(playerLeftMoney, defaultPlayerMoney)
    elif not computerBust and playerBust:
        print('\033[31m플레이어의 버스트\033[0m로 돌려받는 돈은 없습니다...')
    elif sumOfCard > sumOfComputerCard:
        print('\033[32m플레이어의 승리\033[0m! 걸었던 돈의 \033[36m2배\033[0m를 돌려드리겠습니다!')
        playerLeftMoney += playerBet * 2
        printLeftMoney(playerLeftMoney, defaultPlayerMoney)
    elif sumOfCard < sumOfComputerCard:
        print('\033[31m딜러의 승리\033[0m로 돌려받는 돈은 없습니다...')
    elif sumOfCard == sumOfComputerCard:
        print('\033[33m플레이어, 딜러의 무승부(푸시)\033[0m로 걸었던 돈을 돌려드립니다.')
        playerLeftMoney += playerBet
        printLeftMoney(playerLeftMoney, defaultPlayerMoney)
    else:
        print('?')
        break
