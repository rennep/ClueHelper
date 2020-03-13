def UpdatePlayersActual(card, name, actualhand = {}):
    actualhand[name].add(card)
    return actualhand[name]

def UpdateRumors(turn,name, rumor = {}, Rumors = {}):
    Rumors[name][turn] ={'weapon': rumor['weapon'], 'room': rumor['room'], 'character': rumor['character']}
    return Rumors[name] 