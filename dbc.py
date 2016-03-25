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
    init_deck = list(itertools.chain.from_iterable(init_cards))
    # If the init deck is not supposed to be the same all the time
    # statement of random.shuffle(init_deck) should be add here
    player['deck'] = init_deck
    player['hand'] = []
    player['discard'] = []
    player['active'] = []
    if player['deck'] == init_deck and player['hand'] == [] and\
    player['discard'] == [] and player['active'] == []:
        return 0
    else:
        return 1

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
    if player['health'] == 30 and player['handsize'] == 5 and\
    player['deck'] == None and player['hand'] == None and\
    player['active'] == None and player['discard'] == None and\
    player['money'] == 0 and player['attack'] == 0:
        return 0
    else:
        return 1

# This function is used to initialize central deck
def init_central_deck(central_deck):
    central['name'] = 'central'
    central['activeSize'] = 5
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    central['deck'] = deck
    sup = list(itertools.chain.from_iterable(supplement))
    central['supplement'] = sup
    central['active'] = []
    max = central['activeSize']
    count = 0
    while count < max:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1
    if central['name'] == 'central' and central['activeSize'] == 5 and\
    central['active'] != [] and central['deck'] == deck and\
    central['supplement'] == sup:
        return 0
    else:
        return 1

# This function is used to print all cards in the list
def show_cards(card_list):
    index  = 0
    for card in card_list:
        print "[%s] %s " % (index, card)
        index = index + 1
    if index == len(card_list):
        return 0
    else:
        return 1

# This function, containing many function calls, is used to initialize a new game.
def init_new_game():
    if init_player_info(player_human) or init_player_info(player_computer):
        print "Players fail to initialized"
        return -1
    if init_player_decks(player_human) or init_player_decks(player_computer):
        print "Players' deck fail to initialized"
        return -1
    if init_central_deck(central):
        print "central deck fail to initialized"
        return -1
    show_available_cards()
    return 0

# This is a input checker used to check whether the input value is valid
# check_type:
# 1. Check start game input
# 2. Check opponent selection input
# 3. Check action input
# 4. Check purchase option input
def input_check(input_value, check_type):
    if len(input_value) != 1:
        print "Invalid Input, please input one character at a time!"
        return 1
    else:
        if check_type == 1:
            if input_value not in ['Y', 'y', 'N', 'n']:
                print "Invalid Input, please enter 'Y' or 'N' !"
                return 1
            else:
                return 0
        elif check_type == 2:
            if input_value not in ['A', 'a', 'Q', 'q']:
                print "Invalid Input, please enter 'A' or 'Q' !"
                return 1
            else:
                return 0
        elif check_type == 3:
            if input_value not in ['P', 'p', 'B', 'b', 'A', 'a', 'E', 'e', 'V', 'v'] \
                and input_value.isdigit() is False:
                print "Invalid action, please follow the instruction"
                return 1
            else:
                return 0
        elif check_type == 4:
            if input_value not in ['S', 's', 'E', 'e'] \
                and input_value.isdigit() is False:
                print "Invalid option, please follow the purchase instruction"
                return 1
            else:
                return 0

# This function is used to display action interface
def display_main_information(player1, player2):
    print "Player Health %s" % player1['health']
    print "Computer Health %s" % player2['health']
    print "\nYour Hand:"
    if show_cards(player1['hand']):
        print "fail to load your hand cards"
        return 1
    print "\nYour Active Cards"
    if show_cards(player1['active']):
        print "fail to load your active cards"
        return 1
    print "\nYour money %s \nYour attack %s\n" % (player1['money'], player1['attack'])
    print "Choose Action: (V = View available cards, P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"
    return 0

# This function is used when the purchase of supplement occurs
def purchase_supplement(player):
    if len(central['supplement']) > 0:
        original_discard_length = len(player['discard'])
        if player['money'] >= central['supplement'][0].cost:
            player['money'] = player['money'] - central['supplement'][0].cost
            player['discard'].append(central['supplement'].pop())
            if len(player['discard']) == original_discard_length + 1:
                print "Supplement Bought"
                return 0
            else:
                return 1
        else:
            print "insufficient money to buy"
            return 0
    else:
        print "no supplements left"
        return 0

# This function is used to play all cards in hands. This is used by computer by default
def play_all_cards(player):
    money = 0
    attack = 0
    if len(player['hand']) > 0:
        for x in range(0, len(player['hand'])):
            card = player['hand'].pop()
            player['active'].append(card)
            money = money + card.get_money()
            attack = attack + card.get_attack()
    return [money,attack]

# This function put all remaining cards in hand and all cards in active area into discarded pile
def discard_cards(player):
    if len(player['hand']) > 0:
        for x in range(0, len(player['hand'])):
            player['discard'].append(player['hand'].pop())
    if len(player['active']) > 0:
        for x in range(0, len(player['active'])):
            player['discard'].append(player['active'].pop())
    if len(player['active']) > 0 or len(player['hand']) > 0:
        return 1
    else:
        return 0

# This function is called to decide whethe the game is finished
def  will_continue():
    if player_human['health'] <= 0:
        print "Computer wins"
        return False
    elif player_computer['health'] <= 0:
        print 'Player One Wins'
        return False
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
        return False
    else:
        return True

def show_available_cards():
    print "Available Cards"
    show_cards(central['active'])
    print "Supplement"
    if len(central['supplement']) > 0:
        print central['supplement'][0]

def human_purchase():
    while player_human['money'] > 0:
        print "Available money: %s" % player_human['money']
        print "Available Cards"
        ind = 0
        for card in central['active']:
            print "[%s] %s" % (ind, card)
            ind = ind + 1
        print "\nChoose a card to buy [0-n], S for supplement, E to end buying"
        purchase_option = raw_input("Choose option: ")
        while input_check(purchase_option, 4):
            print "\nChoose a card to buy [0-n], S for supplement, E to end buying"
            purchase_option = raw_input("Choose option: ")
        if purchase_option == 'S' or purchase_option == 's':
            if purchase_supplement(player_human):
                print "purchase supplement failed"
                return 1
        elif purchase_option == 'E' or purchase_option == 'e':
            return 0
        elif purchase_option.isdigit():
            if int(purchase_option) < len(central['active']):
                original_discard_length = len(player_human['discard'])
                if player_human['money'] >= central['active'][int(purchase_option)].cost:
                    player_human['money'] = player_human['money'] - central['active'][int(purchase_option)].cost
                    player_human['discard'].append(central['active'].pop(int(purchase_option)))
                    if len(central['deck']) > 0:
                        card = central['deck'].pop()
                        central['active'].append(card)
                    else:
                        central['activeSize'] = central['activeSize'] - 1
                    if len(player_human['discard']) == original_discard_length + 1:
                        print "Card bought %s" % card
                    else:
                        print "card purchase failed"
                        return 1
                else:
                    print "Insufficient money to buy\n"
            else:
                print "Invalid index! Please enter a valid index number\n"

def computer_purchase():
    computer_purcase = True
    templist = []
    print "Starting Money %s and computer_purcase %s " % (player_computer['money'], computer_purcase)
    while computer_purcase:
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
                        if templist[intindex][1].get_money() > templist[highestIndex][1].get_money():
                            highestIndex = intindex
            source = templist[highestIndex][0]
            if source in range(0, 5):
                if player_computer['money'] >= central['active'][int(source)].cost:
                    original_discard_length = len(player_computer['discard'])
                    player_computer['money'] = player_computer['money'] - central['active'][int(source)].cost
                    card = central['active'].pop(int(source))
                    player_computer['discard'].append(card)
                    if len(player_computer['discard']) == original_discard_length + 1:
                        print "Card bought %s" % card
                    else:
                        print "card purchase failed"
                        return 1
                    
                    if len(central['deck']) > 0:
                        card = central['deck'].pop()
                        central['active'].append(card)
                    else:
                        central['activeSize'] = central['activeSize'] - 1
                else:
                    print "Error Occurred"
            else:
                purchase_supplement(player_computer)
        else:
            computer_purcase = False
            return 0

# Card list should be consistent and can be modified here
sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], \
           3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)], \
           3 * [Card('Tailor', (0, 4), 3)], 3 * [Card('Crossbowman', (4, 0), 3)], \
           3 * [Card('Merchant', (0, 5), 4)], 4 * [Card('Thug', (2, 0), 1)], \
           4 * [Card('Thief', (1, 1), 1)], 2 * [Card('Catapault', (7, 0), 6)], \
           2 * [Card('Caravan', (1, 5), 5)], 2 * [Card('Assassin', (5, 0), 4)]]
supplement = [10 * [Card('Levy', (1, 2), 2)]]
init_cards = [8 * [Card('Serf', (0, 1), 0)], 2 * [Card('Squire', (1, 0), 0)]]

if __name__ == '__main__':

    # Declare dictionaries
    player_human = {'name':'player human'}
    player_computer = {'name':'player computer'}
    central = {}

    if init_new_game() == -1:
        exit(-1)
    pG = raw_input('\nDo you want to play a game?\nY = Yes , N = No: ')
    while input_check(pG, 1):
        pG = raw_input('\nDo you want to play a game?\nY = Yes , N = No: ')
    play_game = (pG == 'Y' or pG == 'y')
    while play_game:
        draw_cards(player_human)
        draw_cards(player_computer)
        opponent_type = raw_input("\nWhat kind of opponent do you want?\nA = Aggressive opponent, Q = acquisative opponent:")
        while input_check(opponent_type, 2):
            opponent_type = raw_input("\nWhat kind of opponent do you want?\nA = Aggressive opponent, Q = acquisative opponent:")
        aggressive = (opponent_type == 'A' or opponent_type == 'a')
        continue_game = True
        print "\n\n==============================================\n\n"
        print "Game starts!!!\n"
        show_available_cards()

        while continue_game:

            while True:

                if display_main_information(player_human, player_computer):
                    print "Error occurs when displaying cards"
                    exit(-1)

                act = raw_input("Enter Action: ")
                while input_check(act, 3):
                    print "\nChoose Action: (V = View available cards, P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"
                    act = raw_input("Enter Action: ")
                if act == 'V' or act == 'v':
                    show_available_cards()

                if act == 'P' or act == 'p':
                    result = play_all_cards(player_human)
                    player_human['money'] = player_human['money'] + int(result[0])
                    player_human['attack'] = player_human['attack'] + int(result[1])

                if act.isdigit():
                    if int(act) < len(player_human['hand']):
                        out_card = player_human['hand'].pop(int(act))
                        player_human['active'].append(out_card)
                        player_human['money'] = player_human['money'] + out_card.get_money()
                        player_human['attack'] = player_human['attack'] + out_card.get_attack()
                    else:
                        print "Invalid index! Please enter a valid index number\n"

                if act == 'B' or act == 'b':
                    if human_purchase():
                        exit(-1)

                if act == 'A' or act == 'a':
                    player_computer['health'] = player_computer['health'] - player_human['attack']
                    player_human['attack'] = 0
                    print "\nPlayer Health %s" % player_human['health']
                    print "Computer Health %s" % player_computer['health']
                    continue_game = will_continue()
                    if(continue_game is False):
                        break

                if act == 'E'  or act == 'e':
                    player_human['money'] = 0
                    player_human['attack'] = 0
                    if discard_cards(player_human):
                        print "discard process error"
                        exit(-1)
                    draw_cards(player_human)
                    print "\n*****Computer's turn started*****\n"
                    break

            if(continue_game is False):
                break

            show_available_cards()

            print "\nPlayer Health %s" % player_human['health']
            print "Computer Health %s" % player_computer['health']

            result = play_all_cards(player_computer)
            player_computer['money'] = player_computer['money'] + int(result[0])
            player_computer['attack'] = player_computer['attack'] + int(result[1])

            print " Computer player values money %s, attack %s" % (player_computer['money'], player_computer['attack'])
            print " Computer attacking with strength %s" % player_computer['attack']
            player_human['health'] = player_human['health'] - player_computer['attack']


            print "\nPlayer Health %s" % player_human['health']
            print "Computer Health %s" % player_computer['health']
            continue_game = will_continue()
            if(continue_game is False):
                break

            print " Computer player values money %s, attack %s" % (player_computer['money'], player_computer['attack'])

            if player_computer['money'] > 0:
                print "Computer buying"
                if computer_purchase():
                    print "computer purchase failed"
                    exit(-1)

            else:
                print "No Money to buy anything"
            player_computer['attack'] = 0
            player_computer['money'] = 0
            if discard_cards(player_computer):
                print "discard process error"
                exit(-1)
            draw_cards(player_computer)
            print "\n*****Computer's turn finished*****"

        print "\n\n==============================================\n\n"
        init_new_game()
        pG = raw_input("\nDo you want to play another game?:")
        while input_check(pG, 1):
            pG = raw_input('Do you want to play a game?:')
        play_game = (pG == 'Y' or pG == 'y')

    exit()
