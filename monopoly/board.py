from dataclasses import dataclass

STREET = "street"
RAIL = "rail"
UTIL = "util"
GO = "go"
TAX = "tax"
CHANCE = "chance"
CHEST = "chest"
JAIL = "jail"
FREE = "free"
GOTOJAIL = "gotojail"

BUYABLE = (STREET, RAIL, UTIL)


@dataclass(frozen=True)
class Space:
    idx: int
    name: str
    kind: str
    group: str = ""
    price: int = 0
    rents: tuple = ()
    house_cost: int = 0
    mortgage: int = 0
    amount: int = 0


def _s(idx, name, group, price, rents, house_cost):
    return Space(idx, name, STREET, group, price, tuple(rents), house_cost, price // 2)


def _r(idx, name):
    return Space(idx, name, RAIL, "rail", 200, (), 0, 100)


def _u(idx, name):
    return Space(idx, name, UTIL, "util", 150, (), 0, 75)


BOARD = (
    Space(0, "Go", GO),
    _s(1, "Mediterranean Avenue", "brown", 60, [2, 10, 30, 90, 160, 250], 50),
    Space(2, "Community Chest", CHEST),
    _s(3, "Baltic Avenue", "brown", 60, [4, 20, 60, 180, 320, 450], 50),
    Space(4, "Income Tax", TAX, amount=200),
    _r(5, "Reading Railroad"),
    _s(6, "Oriental Avenue", "lightblue", 100, [6, 30, 90, 270, 400, 550], 50),
    Space(7, "Chance", CHANCE),
    _s(8, "Vermont Avenue", "lightblue", 100, [6, 30, 90, 270, 400, 550], 50),
    _s(9, "Connecticut Avenue", "lightblue", 120, [8, 40, 100, 300, 450, 600], 50),
    Space(10, "Jail", JAIL),
    _s(11, "St. Charles Place", "pink", 140, [10, 50, 150, 450, 625, 750], 100),
    _u(12, "Electric Company"),
    _s(13, "States Avenue", "pink", 140, [10, 50, 150, 450, 625, 750], 100),
    _s(14, "Virginia Avenue", "pink", 160, [12, 60, 180, 500, 700, 900], 100),
    _r(15, "Pennsylvania Railroad"),
    _s(16, "St. James Place", "orange", 180, [14, 70, 200, 550, 750, 950], 100),
    Space(17, "Community Chest", CHEST),
    _s(18, "Tennessee Avenue", "orange", 180, [14, 70, 200, 550, 750, 950], 100),
    _s(19, "New York Avenue", "orange", 200, [16, 80, 220, 600, 800, 1000], 100),
    Space(20, "Free Parking", FREE),
    _s(21, "Kentucky Avenue", "red", 220, [18, 90, 250, 700, 875, 1050], 150),
    Space(22, "Chance", CHANCE),
    _s(23, "Indiana Avenue", "red", 220, [18, 90, 250, 700, 875, 1050], 150),
    _s(24, "Illinois Avenue", "red", 240, [20, 100, 300, 750, 925, 1100], 150),
    _r(25, "B&O Railroad"),
    _s(26, "Atlantic Avenue", "yellow", 260, [22, 110, 330, 800, 975, 1150], 150),
    _s(27, "Ventnor Avenue", "yellow", 260, [22, 110, 330, 800, 975, 1150], 150),
    _u(28, "Water Works"),
    _s(29, "Marvin Gardens", "yellow", 280, [24, 120, 360, 850, 1025, 1200], 150),
    Space(30, "Go To Jail", GOTOJAIL),
    _s(31, "Pacific Avenue", "green", 300, [26, 130, 390, 900, 1100, 1275], 200),
    _s(32, "North Carolina Avenue", "green", 300, [26, 130, 390, 900, 1100, 1275], 200),
    Space(33, "Community Chest", CHEST),
    _s(34, "Pennsylvania Avenue", "green", 320, [28, 150, 450, 1000, 1200, 1400], 200),
    _r(35, "Short Line"),
    Space(36, "Chance", CHANCE),
    _s(37, "Park Place", "darkblue", 350, [35, 175, 500, 1100, 1300, 1500], 200),
    Space(38, "Luxury Tax", TAX, amount=100),
    _s(39, "Boardwalk", "darkblue", 400, [50, 200, 600, 1400, 1700, 2000], 200),
)

GROUPS = {}
for _sp in BOARD:
    if _sp.kind in BUYABLE:
        GROUPS.setdefault(_sp.group, []).append(_sp.idx)
GROUPS = {k: tuple(v) for k, v in GROUPS.items()}

STREET_GROUPS = tuple(g for g in GROUPS if g not in ("rail", "util"))
BUYABLE_IDX = tuple(s.idx for s in BOARD if s.kind in BUYABLE)
RAIL_IDX = GROUPS["rail"]
UTIL_IDX = GROUPS["util"]
RAIL_RENT = (25, 50, 100, 200)

GO_SALARY = 200
JAIL_IDX = 10
JAIL_FINE = 50
MAX_HOUSES = 32
MAX_HOTELS = 12


def space(idx):
    return BOARD[idx]
