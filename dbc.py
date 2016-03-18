import itertools, random

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1, clan=None):
        self.name = name
        self.cost = cost
        self.values = values
        self.clan = clan
    def __str__(self):
                return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
            return self.values[1]

def init_decks(player):
    init_cards = [8 * [Card('Serf', (0, 1), 0)], 2 * [Card('Squire', (1, 0), 0)]]
    pod = list(itertools.chain.from_iterable(init_cards))
    player['deck'] = pod
    player['hand'] = []
    player['discard'] = []
    player['active'] = []

def draw_cards(player):
    for x in range(0, player['handsize']):
        if (len(player['deck']) == 0):
            random.shuffle(player['discard'])
            player['deck'] = player['discard']
            player['discard'] = []
        card = player['deck'].pop()
        player['hand'].append(card)


if __name__ == '__main__':
    player_human = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None}
    player_computer = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}
    central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], 3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)],3 * [Card('Tailor', (0, 4), 3)],3 * [Card('Crossbowman', (4, 0), 3)],3 * [Card('Merchant', (0, 5), 4)],4 * [Card('Thug', (2, 0), 1)],4 * [Card('Thief', (1, 1), 1)],2 * [Card('Catapault', (7, 0), 6)], 2 * [Card('Caravan', (1, 5), 5)],2 * [Card('Assassin', (5, 0), 4)]]

    init_decks(player_human)
    init_decks(player_computer)


    supplement = 10 * [Card('Levy', (1, 2), 2)]
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    central['deck'] = deck
    central['supplement'] = supplement
    central['active'] = []

    max = central['activeSize']
    count = 0
    while count < max:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1

    draw_cards(player_human)
    draw_cards(player_computer)


    print "Available Cards"
    for card in central['active']:
        print card

    print "Supplement"
    if len(central['supplement']) > 0:
        print central['supplement'][0]



    pG = raw_input('Do you want to play a game?:')
    continue_game = (pG=='Y')
    oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent")
    aggressive = (oT=='A')
    while continue_game:
        money = 0
        attack = 0
        while True:

            print "\nPlayer Health %s" % player_human['health']
            print "Computer Health %s" % player_computer['health']

            print "\nYour Hand"
            index = 0
            for card in player_human['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1
            print "\nYour Values"
            print "Money %s, Attack %s" % (money, attack)
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"

            act = raw_input("Enter Action: ")
            print act
            if act == 'P':
                if(len(player_human['hand'])>0):
                    for x in range(0, len(player_human['hand'])):
                        card = player_human['hand'].pop()
                        player_human['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()

                print "\nYour Hand"
                index = 0
                for card in player_human['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1

                print "\nYour Active Cards"
                for card in player_human['active']:
                    print card
                print "\nYour Values"
                print "Money %s, Attack %s" % (money, attack)
            if act.isdigit():
                if( int(act) < len(player_human['hand'])):
                    player_human['active'].append(player_human['hand'].pop(int(act)))
                    for card in player_human['active']:
                        money = money + card.get_money()
                        attack = attack + card.get_attack()
                print "\nYour Hand"
                index = 0
                for card in player_human['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1

                print "\nYour Active Cards"
                for card in player_human['active']:
                    print card
                print "\nYour Values"
                print "Money %s, Attack %s" % (money, attack)
            if (act == 'B'):

                notending = True
                while money > 0:
                    print "Available Cards"
                    ind = 0
                    for card in central['active']:
                        print "[%s] %s" % (ind,card)
                        ind = ind + 1
                    print "Choose a card to buy [0-n], S for supplement, E to end buying"
                    bv = raw_input("Choose option: ")
                    if bv == 'S':
                        if len(central['supplement']) > 0:
                            if money >= central['supplement'][0].cost:
                                money = money - central['supplement'][0].cost
                                player_human['discard'].append(central['supplement'].pop())
                                print "Supplement Bought"
                            else:
                                print "insufficient money to buy"
                        else:
                            print "no supplements left"
                    elif bv == 'E':
                        notending = False
                        break;
                    elif bv.isdigit():
                        if int(bv) < len(central['active']):
                             if money >= central['active'][int(bv)].cost:
                                money = money - central['active'][int(bv)].cost
                                player_human['discard'].append(central['active'].pop(int(bv)))
                                if( len(central['deck']) > 0):
                                    card = central['deck'].pop()
                                    central['active'].append(card)
                                else:
                                    central['activeSize'] = central['activeSize'] - 1
                                print "Card bought"
                             else:
                                print "insufficient money to buy"
                        else:
                             print "enter a valid index number"
                    else:
                        print "Enter a valid option"


            if act == 'A':
                player_computer['health'] = player_computer['health'] - attack
                attack = 0
            if act == 'E':
                if (len(player_human['hand']) >0 ):
                    for x in range(0, len(player_human['hand'])):
                        player_human['discard'].append(player_human['hand'].pop())


                if (len(player_human['active']) >0 ):
                    for x in range(0, len(player_human['active'])):
                        player_human['discard'].append(player_human['active'].pop())
                for x in range(0, player_human['handsize']):
                    if len(player_human['deck']) == 0:
                        random.shuffle(player_human['discard'])
                        player_human['deck'] = player_human['discard']
                        player_human['discard'] = []
                    card = player_human['deck'].pop()
                    player_human['hand'].append(card)
                break

        print "Available Cards"
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]

        print "\nPlayer Health %s" % player_human['health']
        print "Computer Health %s" % player_computer['health']

        money = 0
        attack = 0
        for x in range(0, len(player_computer['hand'])):
                        card = player_computer['hand'].pop()
                        player_computer['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()

        print " Computer player values attack %s, money %s" % (attack, money)
        print " Computer attacking with strength %s" % attack
        player_human['health'] = player_human['health'] - attack
        attack = 0
        print "\nPlayer Health %s" % player_human['health']
        print "Computer Health %s" % player_computer['health']
        print " Computer player values attack %s, money %s" % (attack, money)
        print "Computer buying"
        if money > 0:
            cb = True
            templist = []
            print "Starting Money %s and cb %s " % (money, cb)
            while cb:
                templist = []
                if len(central['supplement']) > 0:
                    if central['supplement'][0].cost <= money:
                        templist.append(("S", central['supplement'][0]))
                for intindex in range (0, central['activeSize']):
                    if central['active'][intindex].cost <= money:
                        templist.append((intindex, central['active'][intindex]))
                if len(templist) >0:
                    highestIndex = 0
                    for intindex in range(0,len(templist)):
                        if templist[intindex][1].cost > templist[highestIndex][1].cost:
                            highestIndex = intindex
                        if templist[intindex][1].cost == templist[highestIndex][1].cost:
                            if aggressive:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack():
                                    highestIndex = intindex
                            else:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money():
                                    highestIndex = intindex
                    source = templist[highestIndex][0]
                    if source in range(0,5):
                        if money >= central['active'][int(source)].cost:
                            money = money - central['active'][int(source)].cost
                            card = central['active'].pop(int(source))
                            print "Card bought %s" % card
                            player_computer['discard'].append(card)
                            if( len(central['deck']) > 0):
                                card = central['deck'].pop()
                                central['active'].append(card)
                            else:
                                central['activeSize'] = central['activeSize'] - 1
                        else:
                            print "Error Occurred"
                    else:
                        if money >= central['supplement'][0].cost:
                            money = money - central['supplement'][0].cost
                            card = central['supplement'].pop()
                            player_computer['discard'].append(card)
                            print "Supplement Bought %s" % card
                        else:
                            print "Error Occurred"
                else:
                    cb = False
                if money == 0:
                    cb = False
        else:
            print "No Money to buy anything"

        if (len(player_computer['hand']) >0 ):
            for x in range(0, len(player_computer['hand'])):
                player_computer['discard'].append(player_computer['hand'].pop())
        if (len(player_computer['active']) >0 ):
            for x in range(0, len(player_computer['active'])):
                player_computer['discard'].append(player_computer['active'].pop())
        for x in range(0, player_computer['handsize']):
                    if len(player_computer['deck']) == 0:
                        random.shuffle(player_computer['discard'])
                        player_computer['deck'] = player_computer['discard']
                        player_computer['discard'] = []
                    card = player_computer['deck'].pop()
                    player_computer['hand'].append(card)
        print "Computer turn ending"


        print "Available Cards"
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]

        print "\nPlayer Health %s" % player_human['health']
        print "Computer Health %s" % player_computer['health']

        if player_human['health'] <= 0:
            continue_game = False
            print "Computer wins"
        elif player_computer['health'] <= 0:
            continue_game = False
            print 'Player One Wins'
        elif central['activeSize'] == 0:
            print "No more cards available"
            if player_human['health'] > player_computer['health']:
                print "Player One Wins on Health"
            elif player_computer['health'] > player_human['health']:
                print "Computer Wins"
            else:
                pHT = 0
                player_computerT = 0
                if pHT > player_computerT:
                    print "Player One Wins on Card Strength"
                elif player_computerT > pHT:
                    print "Computer Wins on Card Strength"
                else:
                    print "Draw"
            continue_game = False
        if not continue_game:
            pG = raw_input("\nDo you want to play another game?:")
            continue_game = (pG=='Y')
            if continue_game:
                oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent")
                aggressive = (oT=='A')
                player_human = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None,
                             'handsize': 5,
                             'discard': None}
                player_computer = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                            'discard': None}
                central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
                sdc = [
                                4 * [Card('Archer', (3, 0), 2)],
                                4 * [Card('Baker', (0, 3), 2)],
                                3 * [Card('Swordsman', (4, 0), 3)],
                                2 * [Card('Knight', (6, 0), 5)],
                                3 * [Card('Tailor', (0, 4), 3)],
                                3 * [Card('Crossbowman', (4, 0), 3)],
                                3 * [Card('Merchant', (0, 5), 4)],
                                4 * [Card('Thug', (2, 0), 1)],
                                4 * [Card('Thief', (1, 1), 1)],
                                2 * [Card('Catapault', (7, 0), 6)],
                                2 * [Card('Caravan', (1, 5), 5)],
                                2 * [Card('Assassin', (5, 0), 4)]
                            ]
                playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                                 2 * [Card('Squire', (1, 0), 0)]
                            ]
                pod = list(itertools.chain.from_iterable(playeronedeck))
                player_human['deck'] = pod
                player_human['hand'] = []
                player_human['discard'] = []
                player_human['active'] = []
                playertwodeck = [
                            8 * [Card('Serf', (0, 1), 0)],
                            2 * [Card('Squire', (1, 0), 0)]
                ]
                ptd = list(itertools.chain.from_iterable(playertwodeck))
                player_computer['deck'] = ptd
                player_computer['hand'] = []
                player_computer['discard'] = []
                player_computer['active'] = []

                supplement = 10 * [Card('Levy', (1, 2), 2)]
                deck = list(itertools.chain.from_iterable(sdc))
                random.shuffle(deck)
                central['deck'] = deck
                central['supplement'] = supplement
                central['active'] = []

                for x in range(0, central['activeSize']):
                    card = central['deck'].pop()
                    central['active'].append(card)

                draw_cards(player_human)

                draw_cards(player_computer)


                print "Available Cards"
                max = central['activeSize']
                count = 0
                while count < max:
                    print central['active'][count]
                    count = count + 1

                print "Supplement"
                if len(central['supplement']) > 0:
                    print central['supplement'][0]
    exit()
