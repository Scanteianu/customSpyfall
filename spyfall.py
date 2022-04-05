import random
import csv
import os
#doc
###############################################################################
'''
A local, customizable version of spyfall, meant to be played on one shared
computer.
Built for python3, just run it from the command line (no args)

'''
#config:
###############################################################################

places = ['Airport', 'Cruise Ship', 'Submarine', 'Restaurant','Hospital','University']
#todo: it is possible to have a dictionary mapping from place to custom roles
roles = ['Student', 'Waiter/Bartender/Flight Attendant', 'Tourist/Patient','Bartender','Captain/Doctor/Professor']

playersCount = 5
spiesCount = 1

#logic:
###############################################################################
while True:
    print("press enter for new game")
    place = places[int(random.random()* len(places))]
    throwaway = input()
    os.system('clear')
    players = []
    for i in range(playersCount):
        players.append(False)
    localSpiesCount = spiesCount
    localRoles = roles [:]
    while localSpiesCount>0:
        player = int(random.random()*len(players))
        if(not players[player]):
            players[player]=True
            localSpiesCount-=1
    playerNum=1
    for i in players:
        print("next player")
        throwaway = input()
        os.system('clear')
        print("player"+str(playerNum))
        playerNum+=1
        if(i):
            print("you're a spy")
        else:
            print("place: "+place)
            print("role: "+ localRoles.pop(int(random.random()*len(localRoles))))
        throwaway = input()
        os.system('clear')
