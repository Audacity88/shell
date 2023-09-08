scores = {}
champs = []
threshold = 100
num_champs = 6
ledger = [("Huff", 10),
          ("Griff", 50),
          ("RC", 40),
          ("Huff", 90),
          ("Sly", -10),
          ("Griff", 100),
          ("Griff", -60),
          ("RC", 80),
          ("Griff", 50)]

def champions(ledger, threshold, num_champs):
    '''
    Computes the first num_champs houses to reach a score
    of at least threshold.

    Inputs:
        ledger: a list of scoring events, where each scoring
            event is a (string, integer) pair consisting of
            the name of the house and the number of points
            that is added to that house's score (which may
            be negative).
        threshold: (positive integer) a house has completed
            the house cup when they meet or exceed this score.
        num_champs: (positive integer) The maximum number
            of houses to include in the list of champions

    Returns: (list of strings) A list of the first num_champs
        houses to complete the house cup, in order.
    '''

    for i in range(len(ledger)):
        if scores.get(ledger[i][0]) == None:
            scores[ledger[i][0]] = [ledger[i][1], 'n']
        else:
            scores[ledger[i][0]][0] += ledger[i][1]
        if scores.get(ledger[i][0])[0] >= threshold and scores.get(ledger[i][0])[1] == 'n':
            champs.append(ledger[i][0])
            scores[ledger[i][0]][1] = 'y'
            if len(champs) == num_champs:
                break
    return champs

def champions2(ledger, threshold, num_champs):
    for item in ledger:
        if item[0] not in scores:
            scores[item[0]] = 0
        scores[item[0]] += item[1]
        if scores[item[0]] >= threshold:
            champs.append(item[0])
            if len(champs) == num_champs:
                break
    return champs

def champions3(ledger, threshold, num_champs):
    for i in range(len(ledger)):
        if ledger[i][0] not in scores:
            scores[ledger[i][0]] = ledger[i][1]
        else:
            scores[ledger[i][0]] += ledger[i][1]
    for house in scores:
        if scores[house] >= threshold:
            champs.append(house)
    return champs[:num_champs]

def champions4(ledger, threshold, num_champs):
#use classes to make this easier
    class House:
        def __init__(self, name):
            self.name = name
            self.score = 0
        def add_score(self, score):
            self.score += score
        def __repr__(self):
            return self.name + ": " + str(self.score)
    #make a dictionary of houses
    for event in ledger:
        if event[0] not in scores:
            scores[event[0]] = House(event[0])
        scores[event[0]].add_score(event[1])
    #sort the houses by score
    houses = sorted(scores.values(), key=lambda x: x.score, reverse=True)
    #return the first num_champs houses
    return [house.name for house in houses[:num_champs]]

def champions5(ledger, threshold, num_champs):
#use classes to make this easier
  
    #make a list of the houses
    houses = []
    #make a list of the ledger
    ledger = []
    #make a list of the champions
    champions = []

    #loop through the ledger
    for house in ledger:
        #if the house is not in the list of houses
        if house not in houses:
            #add the house to the list of houses
            houses.append(house)
            #add the house to the list of champions
            champions.append(house)
        #if the house is in the list of houses
        if house in houses:
            #add the points to the house's score
            house[1] += house[1]
            #if the house's score is greater than or equal to the threshold
            if house[1] >= threshold:
                #add the house to the list of champions
                champions.append(house)
            #if the house's score is less than the threshold
            if house[1] < threshold:
                #add the house to the list of champions
                champions.append(house)
                #remove the house from the list of champions
                champions.remove(house)
    #return the list of champions
    return champions

def champions6(ledger, threshold, num_champs):
#Use classes to make this easier
    class House:
        def __init__(self, name, score):
            self.name = name
            self.score = score
        def add_score(self, points):
            self.score += points
        def __repr__(self):
            return self.name + " " + str(self.score)
        def __lt__(self, other):
            return self.score < other.score
        def __eq__(self, other):
            return self.score == other.score
        def __gt__(self, other):
            return self.score > other.score

    for event in ledger:
        if event[0] in scores:
            scores[event[0]].add_score(event[1])
        else:
            scores[event[0]] = House(event[0], event[1])

    for house in scores.values():
        if house.score >= threshold:
            champs.append(house)

    champs.sort(reverse=True)

    return [house.name for house in champs[:num_champs]]

a = champions(ledger, threshold, num_champs)
#champions2(ledger, threshold, num_champs)
#champions3(ledger, threshold, num_champs)
#champions4(ledger, threshold, num_champs)
b = champions5(ledger, threshold, num_champs)
#champions6(ledger, threshold, num_champs)
print(champs, a, b)