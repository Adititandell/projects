def batscore(d):

   name=d.get('name')
   runs=d.get('runs')
   balls=d.get('balls')
   batscore=int(runs/2)
   four=d.get('4')
   six=d.get('6')

   batscore=int(runs/2)
   if batscore>=50: batscore+=5
   if batscore>=100: batscore+=10

   if runs>0:
       sr=runs*100/balls
       if sr>=80 and sr<100: batscore+=2
       if sr>=100:batscore+=4
       batscore=batscore+four
       batscore=batscore+2*six
       return {'name':name,'batscore':batscore}

def bowlscore(d):
    name=d.get('name')
    wkt=d.get('wkts')
    balls=d.get('overs')
    runs=d.get('runs')
    bowlscore=wkt*10
    if wkt>=3: bowlscore=bowlscore+5
    if wkt>=5: bowlscore=bowlscore=bowlscore+10

    if balls>0:
        er=runs/overs
        #print ("eco:",er)
        if er<=2: bowlscore=bowlscore+10
        if er>2 and er<=3.5: bowlscore=bowlscore+7
        if er>3.5 and er<=4.5: bowlscore=bowlscore+4
    return {'name':name,'bowlscore':bowlscore}

# functions used for score calculation

def batscore(x):
    runs = x['runs']
    strike_rate = runs/x['balls']
    score = runs//2 + (5 if runs >= 50 else 0) + (10 if runs >= 100 else 0) + (2 if strike_rate >= 80/100 and strike_rate <= 1 else 0) + (4 if strike_rate > 1 else 0) + x['4'] + x['6']*2
    return score
    return {'name':x['name'],'batscore':score}

def bowlscore(x):
    wkts = x['wkts']
    economy_rate = x['runs']/x['overs']
    fields=x['field']
    score = 10*wkts + (10*fields if fields>=1 else 0 ) +(5 if wkts>=3 else 0) + (10 if wkts>=5 else 0) + (4 if economy_rate>=3.5 and economy_rate<=4.5 else 0) + (7 if economy_rate>=2 and economy_rate<3.5 else 0) + (10 if economy_rate<2 else 0)
    return score
    return {'name':x['name'],'bowlscore':score}

