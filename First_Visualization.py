import numpy as np
import matplotlib.pyplot as plt
#to increase the size of graph
plt.rcParams['figure.figsize']=8,4
#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
#Games
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])
#Points
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])
# Salaries
KobeBryant_Salary = [15946875, 17718750, 19490625, 21262500, 23034375, 24806250, 25244493, 27849149, 30453805, 23500000]
JoeJohnson_Salary = [12000000, 12744189, 13488377, 14232567, 14976754, 16324500, 18038573, 19752645, 21466718, 23180790]
LeBronJames_Salary = [4621800, 5828090, 13041250, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
CarmeloAnthony_Salary = [3713640, 4694041, 13041250, 14410581, 15779912, 17149243, 18518574, 19450000, 22407474,
                         22458000]
DwightHoward_Salary = [4493160, 4806720, 6061274, 13758000, 15202590, 16647180, 18091770, 19536360, 20513178, 21436271]
ChrisBosh_Salary = [3348000, 4235220, 12455000, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
ChrisPaul_Salary = [3144240, 3380160, 3615960, 4574189, 13520500, 14940153, 16359805, 17779458, 18668431, 20068563]
KevinDurant_Salary = [0, 0, 4171200, 4484040, 4796880, 6053663, 15506632, 16669630, 17832627, 18995624]
DerrickRose_Salary = [0, 0, 0, 4822800, 5184480, 5546160, 6993708, 16402500, 17632688, 18862875]
DwayneWade_Salary = [3031920, 3841443, 13041250, 14410581, 15779912, 14200000, 15691000, 17182000, 18673000, 15000000]
# Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary,
                   ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
plt.plot(Salary[0], c = 'Black', ls = '--', marker= 's', ms=5,label=Players[0]) #c for color ls for line space marker as square and ms as marker space as 7
plt.plot(Salary[1], c = 'Red', ls = '--', marker= 'o', ms=5,label=Players[1])
plt.plot(Salary[2], c = 'Green', ls = '--', marker= '>', ms=5,label=Players[2])
plt.plot(Salary[3], c = 'Blue', ls = '--', marker= 'D', ms=5,label=Players[3])
plt.plot(Salary[4], c = 'Magenta', ls = '--', marker= 'D', ms=5,label=Players[4])
plt.plot(Salary[5], c = 'Black', ls = '--', marker= 'D', ms=5,label=Players[5])
plt.plot(Salary[6], c = 'Red', ls = '--', marker= '<', ms=5,label=Players[6])
plt.plot(Salary[7], c = 'Green', ls = '--', marker= 'o', ms=5,label=Players[7])
plt.plot(Salary[8], c = 'Blue', ls = '--', marker= 's', ms=5,label=Players[8])
plt.plot(Salary[9], c = 'Magenta', ls = '--', marker= '>', ms=5,label=Players[9])
#create a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
#to change x axis numbers from 0 to 9 to years they have played
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
plt.show()
#same visualization for games
plt.plot(Games[0], c = 'Black', ls = '--', marker= 's', ms=5,label=Players[0]) #c for color ls for line space marker as square and ms as marker space as 7
plt.plot(Games[1], c = 'Red', ls = '--', marker= 'o', ms=5,label=Players[1])
plt.plot(Games[2], c = 'Green', ls = '--', marker= '>', ms=5,label=Players[2])
plt.plot(Games[3], c = 'Blue', ls = '--', marker= 'D', ms=5,label=Players[3])
plt.plot(Games[4], c = 'Magenta', ls = '--', marker= 'D', ms=5,label=Players[4])
plt.plot(Games[5], c = 'Black', ls = '--', marker= 'D', ms=5,label=Players[5])
plt.plot(Games[6], c = 'Red', ls = '--', marker= '<', ms=5,label=Players[6])
plt.plot(Games[7], c = 'Green', ls = '--', marker= 'o', ms=5,label=Players[7])
plt.plot(Games[8], c = 'Blue', ls = '--', marker= 's', ms=5,label=Players[8])
plt.plot(Games[9], c = 'Magenta', ls = '--', marker= '>', ms=5,label=Players[9])
#create a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
#to change x axis numbers from 0 to 9 to years they have played
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
plt.show()
#points per game
o = Points/Games
Pointspergame = np.matrix.round(o)
print(Pointspergame)
plt.plot(Pointspergame[0], c = 'Black', ls = '--', marker= 's', ms=5,label=Players[0]) #c for color ls for line space marker as square and ms as marker space as 7
plt.plot(Pointspergame[1], c = 'Red', ls = '--', marker= 'o', ms=5,label=Players[1])
plt.plot(Pointspergame[2], c = 'Green', ls = '--', marker= '>', ms=5,label=Players[2])
plt.plot(Pointspergame[3], c = 'Blue', ls = '--', marker= 'D', ms=5,label=Players[3])
plt.plot(Pointspergame[4], c = 'Magenta', ls = '--', marker= 'D', ms=5,label=Players[4])
plt.plot(Pointspergame[5], c = 'Black', ls = '--', marker= 'D', ms=5,label=Players[5])
plt.plot(Pointspergame[6], c = 'Red', ls = '--', marker= '<', ms=5,label=Players[6])
plt.plot(Pointspergame[7], c = 'Green', ls = '--', marker= 'o', ms=5,label=Players[7])
plt.plot(Pointspergame[8], c = 'Blue', ls = '--', marker= 's', ms=5,label=Players[8])
plt.plot(Pointspergame[9], c = 'Magenta', ls = '--', marker= '>', ms=5,label=Players[9])
#create a legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
#to change x axis numbers from 0 to 9 to years they have played
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
plt.show()