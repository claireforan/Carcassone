#!/usr/bin/python3

from getGameController import *
from cgitb import enable
enable()

print("Content-Type: text/plain")
print()

def tableCreator(GameController):
    Players=GameController._players
    Players.sort(key=lambda x: x._score,reverse=True)
    outstr=""
    outstr+=("""
        <table id ="scoreboard">
                <tr>
                    <th>Player</th>
                    <th>Score</th>
                    <th>Meeples Remaining</th>
                </tr>\n""")
    for i in Players:
        outstr+=("""
                <tr id='%s'>
                    <th>%s</th>
                    <th>%i</th>
                    <th>%i</th>
                </tr>\n"""%(i._id, i._name,i._score,len(i._inactiveMeeples)))
    outstr+=("""
        </table>""")
    return outstr

try:
    gc=getGameController()
    table=tableCreator(gc)
    print(table)
except Exception as e:
    print(e)
