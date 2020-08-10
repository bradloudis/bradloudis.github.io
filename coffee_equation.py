# function that returns weight of water for brewing


def kohi(weight):
    grams = 60.
    liter = 1000.
    ratio = liter / grams
    return ratio * weight


print(kohi(10.7))
