# it's tidious to write many lines of code like shown in first_visualization
# hence we create a function and use that function whenever we need it
import numpy as np
import matplotlib.pyplot as plt

# Seasons
Seasons = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
Sdict = {"2005": 0, "2006": 1, "2007": 2, "2008": 3, "2009": 4, "2010": 5, "2011": 6, "2012": 7, "2013": 8, "2014": 9}

# Players
Players = ["KobeBryant", "JoeJohnson", "LeBronJames", "CarmeloAnthony", "DwightHoward", "ChrisBosh", "ChrisPaul",
           "KevinDurant", "DerrickRose", "DwayneWade"]
Pdict = {"KobeBryant": 0, "JoeJohnson": 1, "LeBronJames": 2, "CarmeloAnthony": 3, "DwightHoward": 4, "ChrisBosh": 5,
         "ChrisPaul": 6, "KevinDurant": 7, "DerrickRose": 8, "DwayneWade": 9}
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
# Games
KobeBryant_G = [80, 77, 82, 82, 73, 82, 58, 78, 6, 35]
JoeJohnson_G = [82, 57, 82, 79, 76, 72, 60, 72, 79, 80]
LeBronJames_G = [79, 78, 75, 81, 76, 79, 62, 76, 77, 69]
CarmeloAnthony_G = [80, 65, 77, 66, 69, 77, 55, 67, 77, 40]
DwightHoward_G = [82, 82, 82, 79, 82, 78, 54, 76, 71, 41]
ChrisBosh_G = [70, 69, 67, 77, 70, 77, 57, 74, 79, 44]
ChrisPaul_G = [78, 64, 80, 78, 45, 80, 60, 70, 62, 82]
KevinDurant_G = [35, 35, 80, 74, 82, 78, 66, 81, 81, 27]
DerrickRose_G = [40, 40, 40, 81, 78, 81, 39, 0, 10, 51]
DwayneWade_G = [75, 51, 51, 79, 77, 76, 49, 69, 54, 62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G,
                  KevinDurant_G, DerrickRose_G, DwayneWade_G])


# create a function playerlist
def myplot(playerlist):
    #create dictionary for different colors
    Colors = {"KobeBryant": 'Black', "JoeJohnson": 'Red', "LeBronJames": 'Green', "CarmeloAnthony": 'Blue', "DwightHoward": 'Magenta', "ChrisBosh": 'Black',
         "ChrisPaul": 'Red', "KevinDurant": 'Green', "DerrickRose": 'Blue', "DwayneWade": 'Magenta'}
    DiffMarker = {"KobeBryant": 's', "JoeJohnson": 'o', "LeBronJames": '<', "CarmeloAnthony": 'd', "DwightHoward": '>', "ChrisBosh": 's',
         "ChrisPaul": 'o', "KevinDurant": 'd', "DerrickRose": '<', "DwayneWade": '>'}
    for name in playerlist:
        plt.plot(Games[Pdict[name]], c=Colors[name], ls='--', marker=DiffMarker[name], ms=7, label=name)
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()
myplot(["KobeBryant", "DwightHoward", "DerrickRose"])
#if we want to use above function for different values like points, games, salaries add data as input inside the function
#declare whatever data to put at the end of the function and change the value inside plot
#for salary
def myplot(data, playerlist):
    #create dictionary for different colors
    Colors = {"KobeBryant": 'Black', "JoeJohnson": 'Red', "LeBronJames": 'Green', "CarmeloAnthony": 'Blue', "DwightHoward": 'Magenta', "ChrisBosh": 'Black',
         "ChrisPaul": 'Red', "KevinDurant": 'Green', "DerrickRose": 'Blue', "DwayneWade": 'Magenta'}
    DiffMarker = {"KobeBryant": 's', "JoeJohnson": 'o', "LeBronJames": '<', "CarmeloAnthony": 'd', "DwightHoward": '>', "ChrisBosh": 's',
         "ChrisPaul": 'o', "KevinDurant": 'd', "DerrickRose": '<', "DwayneWade": '>'}
    for name in playerlist:
        plt.plot(data[Pdict[name]], c=Colors[name], ls='--', marker=DiffMarker[name], ms=7, label=name)
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()
myplot(Salary, ["KobeBryant", "DwightHoward", "DerrickRose"]) #here salary can be replaced with games or points or anything else
#salary will go in as input to data, then it is considered as salary inside plot
#if we give a value inside function and we don't pass values at the end of the function, it takes the default vale
#pass all players to playerlist and removes players at the end of the function
def myplot(data, playerlist = Players):
    #create dictionary for different colors
    Colors = {"KobeBryant": 'Black', "JoeJohnson": 'Red', "LeBronJames": 'Green', "CarmeloAnthony": 'Blue', "DwightHoward": 'Magenta', "ChrisBosh": 'Black',
         "ChrisPaul": 'Red', "KevinDurant": 'Green', "DerrickRose": 'Blue', "DwayneWade": 'Magenta'}
    DiffMarker = {"KobeBryant": 's', "JoeJohnson": 'o', "LeBronJames": '<', "CarmeloAnthony": 'd', "DwightHoward": '>', "ChrisBosh": 's',
         "ChrisPaul": 'o', "KevinDurant": 'd', "DerrickRose": '<', "DwayneWade": '>'}
    for name in playerlist:
        plt.plot(data[Pdict[name]], c=Colors[name], ls='--', marker=DiffMarker[name], ms=7, label=name)
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()
myplot(Salary)
myplot(Salary/Games)
plt.show()