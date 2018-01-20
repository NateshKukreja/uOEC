import sqlite3
import datetime
import time
import csv
import pandas as pd

conn = sqlite3.connect('nba.db')

today = datetime.datetime.now()

print(conn)

allScores = []

teamsOff = {"Boston Celtics":[], "Brooklyn Nets":[],"New York Knicks":[], "Philadelphia 76ers":[],"Toronto Raptors":[], "Golden State Warriors":[], "Los Angeles Clippers":[], "Los Angeles Lakers":[], "Phoenix Suns":[], "Sacramento Kings":[], "Chicago Bulls":[], "Cleveland Cavaliers":[], "Detroit Pistons":[], "Indiana Pacers":[], "Milwaukee Bucks":[], "Dallas Mavericks":[], "Houston Rockets":[], "Memphis Grizzlies":[], "New Orleans Pelicans":[], "San Antonio Spurs":[], "Atlanta Hawks":[], "Charlotte Hornets":[], "Miami Heat":[], "Orlando Magic":[], "Washington Wizards":[], "Denver Nuggets":[], "Minnesota Timberwolves":[], "Oklahoma City Thunder":[], "Portland Trail Blazers":[], "Utah Jazz":[]}

teamsWon = {"Boston Celtics":[], "Brooklyn Nets":[],"New York Knicks":[], "Philadelphia 76ers":[],"Toronto Raptors":[], "Golden State Warriors":[], "Los Angeles Clippers":[], "Los Angeles Lakers":[], "Phoenix Suns":[], "Sacramento Kings":[], "Chicago Bulls":[], "Cleveland Cavaliers":[], "Detroit Pistons":[], "Indiana Pacers":[], "Milwaukee Bucks":[], "Dallas Mavericks":[], "Houston Rockets":[], "Memphis Grizzlies":[], "New Orleans Pelicans":[], "San Antonio Spurs":[], "Atlanta Hawks":[], "Charlotte Hornets":[], "Miami Heat":[], "Orlando Magic":[], "Washington Wizards":[], "Denver Nuggets":[], "Minnesota Timberwolves":[], "Oklahoma City Thunder":[], "Portland Trail Blazers":[], "Utah Jazz":[]}

months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}


class teamOff:
    def __init__(self, date, rows):
        self.rows = rows
        self.date = date
        self.parse(self.rows, self.date)
    
    def parse(self, rows, date):
        global teamsOff
        date = (int(date.year)*int(date.month)+int(date.day))
        offRating = ((rows[23]/(rows[5]-rows[16]+rows[21]+(0.4*rows[14])))*100)
        teamsOff[rows[1]].append({(date):offRating})
        
def func():            
    c = conn.cursor()
    for rows in c.execute('SELECT * from standings order by games'):
        past = datetime.datetime.strptime(rows[0], '%Y-%m-%d')
        if(past.day<today.day):
            nba = teamOff(past, rows)
        elif(past.day>today.day and past.month != today.month):
            nba = teamOff(past, rows)

def csvParser():
    
    with open('scores.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("Visitors: {}, Home: {}".format(row['Visitor/Neutral'], row['Home/Neutral']))
            month = row['Date'][4:7]
            d = row['Date'][8:]
            day = d[:d.index(" ")]
            year = d[d.index(" ")+1:]
            date_ = str((year))+"-"+str((months[month]))+"-"+str(((day)))
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            date = ((int(date_.year)*int(date_.month)+int(date_.day)))
            teamsWon[row['Visitor/Neutral']].append({date:1 if (row['VPTS']>row['HPTS']) else 0})
            teamsWon[row['Home/Neutral']].append({date:0 if (row['VPTS']>row['HPTS'])else 1})
            
            
        

#print(teamsWon['Boston Celtics'])


def visHome():
    global teamsOff
    homes = []
    away = []
    homeWin = []
    awayWin = []
    with open('scores.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            month = row['Date'][4:7]
            d = row['Date'][8:]
            day = d[:d.index(" ")]
            year = d[d.index(" ")+1:]
            date_ = str((year))+"-"+str((months[month]))+"-"+str(((day)))
            date_ = datetime.datetime.strptime(date_, '%Y-%m-%d')
            date = ((int(date_.year)*int(date_.month)+int(date_.day)))
            #print(row['Home/Neutral'])
            #print(row['Visitor/Neutral'])
            home = teamsOff[row['Home/Neutral']]
            visit = teamsOff[row['Visitor/Neutral']]
            homeWL = teamsWon[row['Home/Neutral']]
            visitWL = teamsWon[row['Visitor/Neutral']]
            
            for ind in homeWL:
                for i in ind:
                    homeWin.append(ind[i])
            
            for ind in visitWL:
                for i in ind:
                    awayWin.append(ind[i])
            
            #print(visit)
            for indList in home:
                for key in indList:
                    if key == (date+1):
                        homes.append(indList[date+1])
            for indList in visit:
                for key in indList:
                    if key == (date+1):
                        away.append(indList[date+1])
            for games in teamsWon:
                for won in teamsWon[games]:
                    for key in won:
                        if(key == date+1):
                            if(won[key] == 0):
                                awayWin.append(1)
                                homeWin.append(0)
                            else:
                                homeWin.append(1)
                                awayWin.append(0)
        for i in homeWin:
            print(i)
            #with open('scores.txt', 'w') as textfile:
            #    textfile.write((home))

    #print((homes))
    #print(away)
    #print(len(awayWin))
    #writeToCSV(homes, away)
        
def writeToCSV(home, away):
    df = pd.DataFrame(away)
    df.to_csv('allScore.csv', index = False)
        
        
csvParser()        
func()
print(teamsWon)
i = 0
#for games in teamsWon:
#    for won in teamsWon[games]:
#        for key in won:
#            print(won[key])
#        i+=1
#    print()
#print(i)
visHome()
#fuckIt()



class Scores():
    
    def __init__(self, team, outcome, date, visitor):
        self.team = team
        self.outcome = outcome
        self.date = date
        self.visitor = visitor
    

#class NBA(self, data, name, games, minutes, fg, fga, fgp, three_p, three_pa, three_pp, two_p, two_pa, two_pp, ft, fta, ftp, offr, defr, ass, stl, to, pf, points):
#    self.data = data
#    self.name = game
#    self.minutes = minutes
#    self.fg = fg
#    self.fga = fga
#    self.fgp = fgp
#    self.three_p = three_p
#    self.three_pa = three_pa
#    self.three_pp = three_pp
#    self.two_p = two_p
#    self.two_pa = two_pa
#    self.two_pp = two_pp
#    self.ft = ft
#    self.fta = fta
#    self.ftp = ftp
#    self.offr = offr
#    self.defr = defr
#    self.ass = ass
#    self.stl = stl
#    self.to = to
#    self.pf = pf
#    self.points = points
    
