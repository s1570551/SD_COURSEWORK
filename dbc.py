import itertools, random

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1, clan=None):
        self.name = name
        self.cost = cost
        self.values = values
        self.clan = clan
    def __str__(self):
        return 'Name %s costing %s with attack %s and money %s' %\
                            (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
        return self.values[1]

# This function is used to initialize player deck.
def init_player_decks(player):
    init_cards = [8 * [Card('Serf', (0, 1), 0)], 2 * [Card('Squire', (1, 0), 0)]]
    pod = list(itertools.chain.from_iterable(init_cards))
    player['deck'] = pod
    player['hand'] = []
    player['discard'] = []
    player['active'] = []

# This function is used to drae cards from deck to hand.
def draw_cards(player):
    for x in range(0, player['handsize']):
        if len(player['deck']) == 0:
            random.shuffle(player['discard'])
            player['deck'] = player['discard']
            player['discard'] = []
        card = player['deck'].pop()
        player['hand'].append(card)

# This function is used to initialize player information
def init_player_info(player):
    player['health'] = 30
    player['handsize'] = 5
    player['deck'] = None
    player['hand'] = None
    player['active'] = None
    player['discard'] = None
    player['money'] = 0
    player['attack'] = 0

# This function is used to initialize central deck
def init_central_deck(central_deck):
    central['name'] = 'central'
    central['activeSize'] = 5
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

# This function is used to print all cards in the list
def show_cards(card_list):
    index  = 0
    for card in card_list:
        print "[%s] %s " % (index, card)
        index = index + 1

# This function, containing many function calls, is used to initialize a new game.
def init_new_game():
    init_player_info(player_human)
    init_player_info(player_computer)
    init_player_decks(player_human)
    init_player_decks(player_computer)
    init_central_deck(central)
    print "Available Cards"
    show_cards(central['active'])
    print "Supplement"
    print central['supplement'][0]

# This is a input checker used to check whether the input value is valid
# check_type:
# 1. Check start game input
# 2. Check opponent selection input
# 3. Check action input
def input_check(input_value, check_type):
    if len(input_value) != 1:
        print "Invalid Input, please input one character at a time!\n"
        return 1
    else:
        if check_type == 1:
            if input_value not in ['Y', 'y', 'N', 'n']:
                print "Invalid Input, please enter 'Y' or 'N' !\n"
                return 1
            else:
                return 0
        elif check_type == 2:
            if input_value not in ['A', 'a', 'Q', 'q']:
                print "Invalid Input, please enter 'A' or 'Q' !\n"
                return 1
            else:
                return 0
        elif check_type == 3:
            if input_value not in ['P', 'p', 'B', 'b', 'A', 'a', 'E', 'e'] \
                and input_value.isdigit() == False:
                print "Invalid action, please follow the instruction\n"
                return 1
            else:
                return 0

# This function is used to display action interface
def display_main_information(player1, player2):
    print "Player Health %s" % player1['health']
    print "Computer Health %s" % player2['health']
    print "\nYour Hand:"
    show_cards(player1['hand'])
    print "\nYour Active Cards"
    show_cards(player1['active'])
    print "\nYour money %s \nYour attack %s\n" % (player1['money'], player1['attack'])
    print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)\n"


# Card list should be constant and can be modified here
sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], \
           3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)], \
           3 * [Card('Tailor', (0, 4), 3)], 3 * [Card('Crossbowman', (4, 0), 3)], \
           3 * [Card('Merchant', (0, 5), 4)], 4 * [Card('Thug', (2, 0), 1)], \
           4 * [Card('Thief', (1, 1), 1)], 2 * [Card('Catapault', (7, 0), 6)], \
           2 * [Card('Caravan', (1, 5), 5)], 2 * [Card('Assassin', (5, 0), 4)]]
supplement = 10 * [Card('Levy', (1, 2), 2)]

if __name__ == '__main__':

    # Declare dictionaries
    player_human = {'name':'player human'}
    player_computer = {'name':'player computer'}
    central = {}

    init_new_game()
    pG = raw_input('Do you want to play a game?\nY = Yes , N = No: ')
    while input_check(pG, 1):
        pG = raw_input('Do you want to play a game?\nY = Yes , N = No: ')
    play_game = (pG == 'Y' or pG == 'y')
    while play_game:
        draw_cards(player_human)
        draw_cards(player_computer)
        oT = raw_input("What kind of opponent do you want?\nA = Aggressive opponent, Q = acquisative opponent:")
        while (input_check(oT, 2)):
            oT = raw_input("What kind of opponent do you want?\nA = Aggressive opponent, Q = acquisative opponent:")
        aggressive = (oT == 'A' or oT == 'a')
        continue_game = True
        print "\n\n==============================================\n\n"
        print "Game starts!!!\n"

        while continue_game:
            money = player_human['money']
            attack = player_human['attack']
            while True:

                display_main_information(player_human, player_computer)

                act = raw_input("Enter Action: ")
                while input_check(act, 3):
                    print "Choose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)\n"
                    act = raw_input("Enter Action: ")
                if act == 'P' or act == 'p':
                    if(len(player_human['hand']) > 0):
                        for x in range(0, len(player_human['hand'])):
                            card = player_human['hand'].pop()
                            player_human['active'].append(card)
                            player_human['money'] = player_human['money'] + card.get_money()
                            player_human['attack'] = player_human['attack'] + card.get_attack()

                if act.isdigit():
                    if(int(act) < len(player_human['hand'])):
                        out_card = player_human['hand'].pop(int(act))
                        player_human['active'].append(out_card)
                        player_human['money'] = player_human['money'] + out_card.get_money()
                        player_human['attack'] = player_human['attack'] + out_card.get_attack()

                if act == 'B' or act == 'b':
                    notending = True
                    while player_human['money'] > 0:
                        print "Available Cards"
                        ind = 0
                        for card in central['active']:
                            print "[%s] %s" % (ind, card)
                            ind = ind + 1
                        print "Choose a card to buy [0-n], S for supplement, E to end buying"
                        bv = raw_input("Choose option: ")
                        if bv == 'S' or bv == 's':
                            if len(central['supplement']) > 0:
                                if player_human['money'] >= central['supplement'][0].cost:
                                    player_human['money'] = player_human['money'] - central['supplement'][0].cost
                                    player_human['discard'].append(central['supplement'].pop())
                                    print "Supplement Bought"
                                else:
                                    print "insufficient money to buy"
                            else:
                                print "no supplements left"
                        elif bv == 'E' or bv == 'e':
                            notending = False
                            break
                        elif bv.isdigit():
                            if int(bv) < len(central['active']):
                                if player_human['money'] >= central['active'][int(bv)].cost:
                                    player_human['money'] = player_human['money'] - central['active'][int(bv)].cost
                                    player_human['discard'].append(central['active'].pop(int(bv)))
                                    if len(central['deck']) > 0:
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


                if act == 'A' or act == 'a':
                    player_computer['health'] = player_computer['health'] - player_human['attack']
                    player_human['attack'] = 0
                if act == 'E'  or act == 'e':
                    player_human['money'] = 0
                    player_human['attack'] = 0
                    if (len(player_human['hand']) >0 ):
                        for x in range(0, len(player_human['hand'])):
                            player_human['discard'].append(player_human['hand'].pop())


                    if (len(player_human['active']) > 0 ):
                        for x in range(0, len(player_human['active'])):
                            player_human['discard'].append(player_human['active'].pop())

                    draw_cards(player_human)
                    print "\n*****Computer's turn started*****\n"
                    break

            print "Available Cards"
            for card in central['active']:
                print card

            print "Supplement"
            if len(central['supplement']) > 0:
                print central['supplement'][0]

            print "\nPlayer Health %s" % player_human['health']
            print "Computer Health %s" % player_computer['health']

            money = player_computer['money']
            attack = player_computer['attack']
            for x in range(0, len(player_computer['hand'])):
                card = player_computer['hand'].pop()
                player_computer['active'].append(card)
                player_computer['money'] = player_computer['money'] + card.get_money()
                player_computer['attack'] = player_computer['attack'] + card.get_attack()

            print " Computer player values money %s, attack %s" % (player_computer['money'], player_computer['attack'])
            print " Computer attacking with strength %s" % player_computer['attack']
            player_human['health'] = player_human['health'] - player_computer['attack']
            attack = 0
            print "\nPlayer Health %s" % player_human['health']
            print "Computer Health %s" % player_computer['health']
            print " Computer player values money %s, attack %s" % (player_computer['money'], player_computer['attack'])
            print "Computer buying"
            if player_computer['money'] > 0:
                cb = True
                templist = []
                print "Starting Money %s and cb %s " % (player_computer['money'], cb)
                while cb:
                    templist = []
                    if len(central['supplement']) > 0:
                        if central['supplement'][0].cost <= player_computer['money']:
                            templist.append(("S", central['supplement'][0]))
                    for intindex in range(0, central['activeSize']):
                        if central['active'][intindex].cost <= player_computer['money']:
                            templist.append((intindex, central['active'][intindex]))
                    if len(templist) > 0:
                        highestIndex = 0
                        for intindex in range(0, len(templist)):
                            if templist[intindex][1].cost > templist[highestIndex][1].cost:
                                highestIndex = intindex
                            if templist[intindex][1].cost == templist[highestIndex][1].cost:
                                if aggressive:
                                    if templist[intindex][1].get_attack() > templist[highestIndex][1].get_attack():
                                        highestIndex = intindex
                                else:
                                    if templist[intindex][1].get_attack() > templist[highestIndex][1].get_money():
                                        highestIndex = intindex
                        source = templist[highestIndex][0]
                        if source in range(0, 5):
                            if player_computer['money'] >= central['active'][int(source)].cost:
                                player_computer['money'] = player_computer['money'] - central['active'][int(source)].cost
                                card = central['active'].pop(int(source))
                                print "Card bought %s" % card
                                player_computer['discard'].append(card)
                                if len(central['deck']) > 0:
                                    card = central['deck'].pop()
                                    central['active'].append(card)
                                else:
                                    central['activeSize'] = central['activeSize'] - 1
                            else:
                                print "Error Occurred"
                        else:
                            if player_computer['money'] >= central['supplement'][0].cost:
                                player_computer['money'] = player_computer['money'] - central['supplement'][0].cost
                                card = central['supplement'].pop()
                                player_computer['discard'].append(card)
                                print "Supplement Bought %s" % card
                            else:
                                print "Error Occurred"
                    else:
                        cb = False
                    if player_computer['money'] == 0:
                        cb = False
            else:
                print "No Money to buy anything"

            if len(player_computer['hand']) > 0:
                for x in range(0, len(player_computer['hand'])):
                    player_computer['discard'].append(player_computer['hand'].pop())
            if len(player_computer['active']) > 0:
                for x in range(0, len(player_computer['active'])):
                    player_computer['discard'].append(player_computer['active'].pop())
            player_computer['attack'] = 0
            player_computer['money'] = 0
            draw_cards(player_computer)
            print "\n*****Computer's turn finished*****"
            print "\n\n==============================================\n\n"

            print "Available Cards"
            for card in central['active']:
                print card

            print "Supplement"
            if len(central['supplement']) > 0:
                print central['supplement'][0]
                print "\n"

            #print "\nPlayer Health %s" % player_human['health']
            #print "Computer Health %s" % player_computer['health']

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
        print "\n\n==============================================\n\n"
        init_new_game()
        pG = raw_input("\nDo you want to play another game?:")
        while input_check(pG,1):
            pG = raw_input('Do you want to play a game?:')
        play_game = (pG == 'Y' or pG == 'y')

    exit()
