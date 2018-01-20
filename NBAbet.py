import sqlite3
import datetime
import time

conn = sqlite3.connect('nba.db')

today = datetime.datetime.now()

print(conn)

teams = {"Boston Celtics":[], "Brooklyn Nets":[],"New York Knicks":[], "Philadelphia 76ers":[],"Toronto Raptors":[], "Golden State Warriors":[], "Los Angeles Clippers":[], "Los Angeles Lakers":[], "Phoenix Suns":[], "Sacramento Kings":[], "Chicago Bulls":[], "Cleveland Cavaliers":[], "Detroit Pistons":[], "Indiana Pacers":[], "Milwaukee Bucks":[], "Dallas Mavericks":[], "Houston Rockets":[], "Memphis Grizzlies":[], "New Orleans Pelicans":[], "San Antonio Spurs":[], "Atlanta Hawks":[], "Charlotte Hornets":[], "Miami Heat":[], "Orlando Magic":[], "Washington Wizards":[], "Denver Nuggets":[], "Minnesota Timberwolves":[], "Oklahoma City Thunder":[], "Portland Trail Blazers":[], "Utah Jazz":[]}

class teamOff:
    def __init__(self, rows):
        self.rows = rows
        self.parse(self.rows)
    
    def parse(self,rows):
        global teams
        offRating = ((rows[23]/(rows[5]-rows[16]+rows[21]+(0.4*rows[14])))*100)
        print(offRating)
        teams[rows[1]].append(offRating)
        print(teams[rows[1]])
        
            
c = conn.cursor()
for rows in c.execute('SELECT * from standings order by games'):
    past = datetime.datetime.strptime(rows[0], '%Y-%m-%d')
    if(past.day<today.day):
        nba = teamOff(rows)
        
        print(rows)
    elif(past.day>today.day and past.month != today.month):
        nba = teamOff(rows)
        
        print(rows)
        

            
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
    