def ClearPossibleHand(name, rumor={}, PossibleHand={}):

    if rumor['weapon'] in PossibleHand[name]['weapons']:
        PossibleHand[name]['weapons'].remove(rumor['weapon'])

    if rumor['room'] in PossibleHand[name]['rooms']:
        PossibleHand[name]['rooms'].remove(rumor['room'])

    if rumor['character'] in PossibleHand[name]['characters']:
        PossibleHand[name]['characters'].remove(rumor['character'])

    return PossibleHand[name]

def ClearRumors(name, rumor = {}, Rumors={}):
    return 3