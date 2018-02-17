

### Sense HAT Olympic Medal Thingy IOT

from sense_hat import SenseHat

### Imports

from BeautifulSoup import BeautifulSoup
import requests
import time

### Data Class For The Container

class record:
    def __init__(self, rank,gold,silver,bronze,total,country):
        self.rank = []
        self.gold = []
        self.silver = []
        self.bronze = []
        self.total = []
        self.country = []

## Flag IDs

flag_ID = ["CAN_FLAG.png", 
           "USA_FLAG.png",
           "NOR_FLAG.png",
           "GER_FLAG.png",
           "NED_FLAG.png",
           "UKN_FLAG.png",
           "AUT_FLAG.png",
           "CZE_FLAG.png",
           "FIN_FLAG.png",
           "FRA_FLAG.png",
           "ITA_FLAG.png",
           "KAZ_FLAG.png",
           "KOR_FLAG.png",
           "SWE_FLAG.png",
           "JPN-FLAG.png",
           "SUI-FLAG.png",
           "AUS-FLAG.png",
           "CHN-FLAG.png",
           "SVK-FLAG.png",
           "SLO-FLAG.png",
           "ESP_FLAG.png",
           "BLR-FLAG.png"
           

           ]

gold = (255,215,0)
silver = (192,192,192)
bronze = (205,127,50)
white = (255,255,255)


## Functions and Defines

def RankCreate():
    for i in range(0, len(test),6):
        print test[i]
        record1.rank.extend(test[i])


def GoldCreate():
    for i in range(1, len(test),6):
        print test[i]
        record1.gold.extend(test[i])

def SilverCreate():
    for i in range(2, len(test),6):
        print test[i]
        record1.silver.extend(test[i])

def BronzeCreate():
    for i in range(3, len(test),6):
        print test[i]
        record1.bronze.extend(test[i])

def TotalCreate():
    for i in range(4, len(test),6):
        print test[i]
        record1.total.extend(test[i])

def CountryCreate():
    for i in range(5, len(test),6):
        print test[i]
        record1.country.extend(test[i])

def create():
    RankCreate()
    GoldCreate()
    SilverCreate()
    BronzeCreate()
    TotalCreate()
    CountryCreate()


def DCC(x):
    val = str(record1.country[x])
    start = val.find('title="')+7
    end = val.find('" href')
    return val[start:end]

def RC(x):
    val = str(record1.rank[x])
    start = val.find('">')+2
    end = val.find('/span')-1
    return int(val[start:end])


def filter_data():

## Country Fixes
    for x in range(0, len(record1.country)):
        record1.country[x] = DCC(x)
## Int Metal Fixes
    for x in range(0, len(record1.gold)):
        record1.gold[x] = int(record1.gold[x])
    for x in range(0, len(record1.silver)):
        record1.silver[x] = int(record1.silver[x])
    for x in range(0, len(record1.bronze)):
        record1.bronze[x] = int(record1.bronze[x])
    for x in range(0, len(record1.total)):
        record1.total[x] = int(record1.total[x])

## Rank To Deal with Shared Rank

    for x in range(0, len(record1.rank)):
        record1.rank[x] = RC(x)


#for x in range(0, len(record1.rank)):
#        record1.total[x] = int(record1.rank[x])


def display_flag(country_id,index):
    sense.clear()
    sense.load_image(country_id)
    time.sleep(2.5)
    sense.clear()
    sense.show_message("Total "+ str(record1.total[index]), scroll_speed=0.2)
    sense.clear()
    sense.load_image(country_id)
    time.sleep(2.5)
    #sense.show_message("Gold %d  Silver %d  Bronze %d" % (record1.gold[index],record1.silver[index],record1.bronze[index]), scroll_speed=0.2)
    metal_peg(gold,record1.gold[index])
    time.sleep(2.5)
    sense.clear()
    metal_peg(silver,record1.silver[index])
    time.sleep(2.5)
    sense.clear()
    metal_peg(bronze,record1.bronze[index])
    time.sleep(2.5)
    sense.clear()



def display_loop():
    print(str(len(record1.rank)) + " Countries In Loop")
    for x in range (0, len(record1.rank)):

        if (record1.country[x].startswith('Canada')):
            print("Canada " + str(x))
            display_flag(flag_ID[0],x)
        elif (record1.country[x].startswith('United States')):
            print("USA " + str(x))
            display_flag(flag_ID[1],x)
        elif (record1.country[x].startswith('Norway')):
            print("Norway " + str(x))
            display_flag(flag_ID[2],x)
        elif (record1.country[x].startswith('Germany')):
            print("Germany " + str(x))
            display_flag(flag_ID[3],x)
        elif (record1.country[x].startswith('Netherlands')):
            print("Netherlands " + str(x))
            display_flag(flag_ID[4],x)
        elif (record1.country[x].startswith('Switzerland')):
            print("Switzerland  " + str(x))
            display_flag(flag_ID[5],x)
        elif (record1.country[x].startswith('Austria')):
            print("Austria " + str(x))
            display_flag(flag_ID[6],x)
        elif (record1.country[x].startswith('Czech')):
            print("Czech Republic " + str(x))
            display_flag(flag_ID[7],x)
        elif (record1.country[x].startswith('Findland')):
            print("Findland " + str(x))
            display_flag(flag_ID[8],x)
        elif (record1.country[x].startswith('France')):
            print("France " + str(x))
            display_flag(flag_ID[9],x)
        elif (record1.country[x].startswith('Italy')):
            print("Italy " + str(x))
            display_flag(flag_ID[10],x)
        elif (record1.country[x].startswith('Kazak')):
            print("Kazakhstan " + str(x))
            display_flag(flag_ID[11],x)
        elif (record1.country[x].startswith('South Korea')):
            print("South Korea " + str(x))
            display_flag(flag_ID[12],x)
        elif (record1.country[x].startswith('Sweden')):
            print("Sweden " + str(x))
            display_flag(flag_ID[13],x)
        elif (record1.country[x].startswith('Japan')):
            print("Japan" + str(x))
            display_flag(flag_ID[14],x)
        elif (record1.country[x].startswith('China')):
            print("China" + str(x))
            display_flag(flag_ID[15],x)
        elif (record1.country[x].startswith('Australia')):
            print("Australia" + str(x))
            display_flag(flag_ID[16],x)
        elif (record1.country[x].startswith('Slovakia')):
            print("Slovakia" + str(x))
            display_flag(flag_ID[17],x)
        elif (record1.country[x].startswith('Slovenia')):
            print("Slovenia" + str(x))
            display_flag(flag_ID[18],x)
        elif (record1.country[x].startswith('Spain')):
            print("Spain" + str(x))
            display_flag(flag_ID[19],x)
        elif (record1.country[x].startswith('Bellarus')):
            print("Bellarus" + str(x))
            display_flag(flag_ID[20],x)
        #elif (record1.country[x].startswith('Netherlands')):
        #    print("Netherlands" + str(x))
        #    display_flag(flag_ID[4],x)
        else: 
            print("UNKNOWN " + str(x) + " " + str(record1.total[x]) )
            display_flag(flag_ID[5],x)

def metal_peg(type, length):
    sense.clear()
    for m in range (0,8):
        sense.set_pixel(m,0,type)
        sense.set_pixel(m,1,type)
    for x in range (0,(length*2),2):
        if (x < 8): 
            sense.set_pixel(x,3,white)
        if (x >= 8 | x < 16):
            print x
            sense.set_pixel(x-7,4,white)
        if (x >=16 | x < 24):
            print x
            sense.set_pixel(x-16,5,white)
        if (x >= 24 | x < 32):
            print x
            sense.set_pixel(x-23,6,white)
        if (x >= 32 | x < 40):
            print x
            sense.set_pixel(x-32,7,white)






## Init Stuff

record1 = record(0,0,0,0,0,0)		# Data Set Look at dropping zeros

sense = SenseHat()					# StartUp SenseHat]

## Scrape CBC Site

def scrape():
    
    r = requests.get('https://olympics.cbc.ca/medals/index.html')
    soup = BeautifulSoup(r.content)
    test = soup.findAll('td')
    return test


### Main Program

while(1):
    
    test = scrape()

    create()		# Build Data Container
    filter_data()		# Make it All Human Readble
    display_loop()
    del(record1)
    record1 = record(0,0,0,0,0,0)






