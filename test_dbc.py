import unittest
import dbc


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

class DBCTestCase(unittest.TestCase):


    def test_init_player_info(self):
        self.assertEquals(dbc.init_player_info(player_human), 0,
                          msg="Fail to initialize user")

    def test_init_player_decks(self):
        dbc.init_player_info(player_human)
        self.assertEquals(dbc.init_player_decks(player_human), 0,
                          msg="Fail to initialize user's deck")
        self.assertEquals(player_human['hand'], [],
                          msg="The user's hand deck is not empty")
        self.assertEquals(len(player_human['deck']), 10,
                          msg="The user's hand deck length is incorrect")

    def test_init_central_deck(self):
        self.assertEquals(dbc.init_central_deck(test_central), 0,
                          msg="Fail to initialize central deck")
        self.assertEquals(len(test_central['deck']), 31,
                          msg="The central deck length is incorrect %s" % len(test_central['deck']))

    def test_show_cards(self):
        self.assertEquals(dbc.show_cards(supplement), 0,
                          msg="Error occurs in show card function")

    def test_init_new_game(self):
        self.assertEquals(dbc.init_new_game(player_human, player_computer, test_central), 0,
                          msg="Fail to initialize new game")

    def test_input_check(self):
        self.assertEquals(dbc.input_check('y',1), 0,
                          msg="Check input type 1 failed")
        self.assertEquals(dbc.input_check(';',1), 1,
                          msg="Check input type 1 failed")
        self.assertEquals(dbc.input_check('q',2), 0,
                          msg="Check input type 2 failed")
        self.assertEquals(dbc.input_check('Y',2), 1,
                          msg="Check input type 2 failed")
        self.assertEquals(dbc.input_check('3',3), 0,
                          msg="Check input type 3 failed")
        self.assertEquals(dbc.input_check('Y',3), 1,
                          msg="Check input type 3 failed")
        self.assertEquals(dbc.input_check('E',4), 0,
                          msg="Check input type 3 failed")
        self.assertEquals(dbc.input_check('p',4), 1,
                          msg="Check input type 3 failed")

    def test_purchase_supplement(self):
        dbc.init_player_info(player_human)
        dbc.init_central_deck(test_central)

        self.assertEquals(dbc.purchase_supplement(player_human,test_central), 0,
                          msg = "User purchase supplement failed")

    def test_play_all_cards(self):
        dbc.init_new_game(player_human, player_computer, test_central)
        dbc.draw_cards(player_human)
        result = dbc.play_all_cards(player_human)
        self.assertEquals(result, [3, 2],
                          msg="Error occurs in playing all cards %s" %result)

    def test_discard_cards(self):
        dbc.init_new_game(player_human, player_computer, test_central)
        dbc.draw_cards(player_human)
        result = dbc.discard_cards(player_human)
        self.assertEquals(result, 0,
                          msg="Error occurs in discarding cards %s" %result)

    def test_will_continue(self):
        dbc.init_new_game(player_human, player_computer, test_central)
        player_human['health'] = -2
        result = dbc.will_continue(player_human, player_computer, test_central)
        self.assertEquals(result, False,
                          msg="Error occurs when judging winner %s" %result)





sdc = [4 * [Card('Archer', (3, 0), 2)], 4 * [Card('Baker', (0, 3), 2)], \
           3 * [Card('Swordsman', (4, 0), 3)], 2 * [Card('Knight', (6, 0), 5)], \
           3 * [Card('Tailor', (0, 4), 3)], 3 * [Card('Crossbowman', (4, 0), 3)], \
           3 * [Card('Merchant', (0, 5), 4)], 4 * [Card('Thug', (2, 0), 1)], \
           4 * [Card('Thief', (1, 1), 1)], 2 * [Card('Catapault', (7, 0), 6)], \
           2 * [Card('Caravan', (1, 5), 5)], 2 * [Card('Assassin', (5, 0), 4)]]
supplement = [10 * [Card('Levy', (1, 2), 2)]]
init_cards = [8 * [Card('Serf', (0, 1), 0)], 2 * [Card('Squire', (1, 0), 0)]]
player_human = {'name':'player human'}
player_computer = {'name':'player computer'}
test_central = {}

if __name__ == '__main__':
    test_dbc.main()