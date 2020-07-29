class Location(object):
    def __init__(self, dimension, coords, niveau, lieu, num):
        self.dimension = dimension
        self.coords = coords
        self.niveau = niveau
        self.lieu = lieu
        self.num = num

    def __eq__(self, other: 'Location'):
        return all((self.dimension == other.dimension,
                    self.coords == other.coords,
                    self.niveau == other.niveau,
                    self.lieu == other.lieu,
                    self.num == other.num))


class Map(object):
    def __init__(self, loc: 'Location', screen_size: tuple, res: dict, exits: dict):
        self.loc = loc
        self.screen_size = screen_size  # width height
        self.res = res  # {'fer': [(0, 0)]}
        self.exits = exits


def mine_04_28():
    maps = []

    screen_size = (3840, 2160)

    loc1 = Location(dimension='monde12', coords=(4, 28), niveau=1, lieu='mine', num=1)
    loc2 = Location(dimension='monde12', coords=(4, 28), niveau=1, lieu='mine', num=2)
    loc3 = Location(dimension='monde12', coords=(4, 28), niveau=1, lieu='mine', num=3)

    # loc1
    res = {'fer': [(1218, 1071),
                   (1300, 1025),
                   (1648, 587),
                   (1752, 547),
                   (1834, 501),
                   (2618, 849)]}
    exits = {'out': [(1164, 1446)],
             'mine': [(2590, 1196, loc2)]}
    maps.append(Map(loc=loc1, screen_size=screen_size, res=res, exits=exits))

    # loc2
    res = {'fer': [(1574, 894),
                   (1662, 852),
                   (2104, 624),
                   (2186, 598),
                   (2272, 590)]}
    exits = {'out': [],
             'mine': [(997, 1179, loc1)]}
                      #(2581, 925, loc3)]}
    maps.append(Map(loc=loc2, screen_size=screen_size, res=res, exits=exits))

    # loc3
    res = {'cuivre': [(1303, 668),
                      (1389, 636),
                      (1573, 552)],
           'bronze': [(2649, 564)]}
    exits = {'out': [],
             'mine': [(1171, 1458, loc2)]}
    maps.append(Map(loc=loc3, screen_size=screen_size, res=res, exits=exits))

    return maps
