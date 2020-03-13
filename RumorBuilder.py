def RumorBuilder():
    rumor = {}
    rumor['weapon'] = input("Enter the rumor weapon:  ").lower()
    rumor['room'] = input('Enter the rumor room:  ').lower()
    rumor['character'] = input("Enter the rumor character:  ").lower()
    return rumor