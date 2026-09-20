from dataclasses import dataclass

MOVE = "move"
MOVE_NEAREST = "move_nearest"
MOVE_BACK = "move_back"
GAIN = "gain"
PAY = "pay"
GAIN_EACH = "gain_each"
PAY_EACH = "pay_each"
JAIL_CARD = "jail_card"
GO_JAIL = "go_jail"
REPAIRS = "repairs"


@dataclass(frozen=True)
class Card:
    text: str
    kind: str
    value: int = 0
    extra: int = 0


CHANCE_CARDS = (
    Card("Advance to Go", MOVE, 0),
    Card("Advance to Illinois Avenue", MOVE, 24),
    Card("Advance to St. Charles Place", MOVE, 11),
    Card("Advance to nearest Utility, pay 10x dice", MOVE_NEAREST, 1),
    Card("Advance to nearest Railroad, pay double rent", MOVE_NEAREST, 0),
    Card("Advance to nearest Railroad, pay double rent", MOVE_NEAREST, 0),
    Card("Bank pays you dividend of 50", GAIN, 50),
    Card("Get out of jail free", JAIL_CARD),
    Card("Go back three spaces", MOVE_BACK, 3),
    Card("Go directly to Jail", GO_JAIL),
    Card("General repairs: 25 per house, 100 per hotel", REPAIRS, 25, 100),
    Card("Speeding fine 15", PAY, 15),
    Card("Take a trip to Reading Railroad", MOVE, 5),
    Card("Advance to Boardwalk", MOVE, 39),
    Card("Elected chairman, pay each player 50", PAY_EACH, 50),
    Card("Building loan matures, collect 150", GAIN, 150),
)

CHEST_CARDS = (
    Card("Advance to Go", MOVE, 0),
    Card("Bank error in your favour, collect 200", GAIN, 200),
    Card("Doctor's fee, pay 50", PAY, 50),
    Card("From sale of stock you get 50", GAIN, 50),
    Card("Get out of jail free", JAIL_CARD),
    Card("Go directly to Jail", GO_JAIL),
    Card("Holiday fund matures, collect 100", GAIN, 100),
    Card("Income tax refund, collect 20", GAIN, 20),
    Card("It is your birthday, collect 10 from each player", GAIN_EACH, 10),
    Card("Life insurance matures, collect 100", GAIN, 100),
    Card("Hospital fees, pay 100", PAY, 100),
    Card("School fees, pay 50", PAY, 50),
    Card("Receive consultancy fee of 25", GAIN, 25),
    Card("Street repairs: 40 per house, 115 per hotel", REPAIRS, 40, 115),
    Card("Second prize in a beauty contest, collect 10", GAIN, 10),
    Card("You inherit 100", GAIN, 100),
)


class Deck:
    def __init__(self, cards, rng):
        self.rng = rng
        self.draw_pile = list(cards)
        self.discard = []
        self.rng.shuffle(self.draw_pile)

    def draw(self):
        if not self.draw_pile:
            self.draw_pile = self.discard
            self.discard = []
            self.rng.shuffle(self.draw_pile)
        return self.draw_pile.pop()

    def put_back(self, card):
        self.discard.append(card)
