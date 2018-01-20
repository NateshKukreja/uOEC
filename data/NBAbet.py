import sqlite3
import datetime
import time
import csv

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
        offRating = ((rows[23]/(rows[5]-rows[16]+rows[21]+(0.4*rows[14])))*100)
        print(offRating)
        teamsOff[rows[1]].append({(date.year, date.month, date.day):offRating})
        print(teamsOff[rows[1]])
        
            
c = conn.cursor()
for rows in c.execute('SELECT * from standings order by games'):
    past = datetime.datetime.strptime(rows[0], '%Y-%m-%d')
    if(past.day<today.day):
        nba = teamOff(past, rows)
        
        print(rows)
    elif(past.day>today.day and past.month != today.month):
        nba = teamOff(past, rows)
        
        print(rows)

def csvParser():
    
    with open('scores.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Visitors: {}, Home: {}".format(row['Visitor/Neutral'], row['Home/Neutral']))
            print(row['Date'][4:])
            month = months[row['Date'][4:7]]
            day = row['Date'].trim()
            year = row['Date'][11:]
            print(month, day, year)
            date = str(year)+"-"+str(month)+"-"+str(day)
            date_ = datetime.datetime.strptime(date, '%Y-%m-%d')
            #if today<date:
                
            print("{} won".format(row['Visitor/Neutral']) if (row['VPTS']>row['HPTS']) else "{} won".format(row['Home/Neutral']))
            
            
            
        
csvParser()

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
    
