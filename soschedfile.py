import argparse
import sys
from dictionary import (
    country,
    surface,
    distance,
    age,
    raceclass,
    number,
    codict,
    track
)
import sqlite3


def sqlite3Entry():
    try:
        so7 = sqlite3.connect('so7.db')
        cursor = so7.cursor()

        cursor.execute(
            '''INSERT INTO races (ID, Day, Month, Name, Course, Going, Country, Distance, Prize, Sex, Age, Field, International, Conditions, Class) VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (day, month, name, racecourse, going, country, distance, prize, sex, age, field, international, conjoin,
             raceclass))

        so7.commit()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (so7):
            so7.close()


def RaceNames():
    def checkIfDuplicate():
        # define empty list
        races = []
        # open file and read content in a list
        races = [race_name.rstrip() for race_name in racenames.readlines()]
        setOfRaces = set(races)
        if name in setOfRaces:
            return True
        else:
            return False

    result = checkIfDuplicate()

    if result:
        sys.exit('Race name is duplicate')
    else:
        print(name, file=racenames)
    return


# assign feature race file based on which country racecourse
def printRaces():
    if country == "AUS":
        with open('aus_featureRaces.db', 'a+') as ausdb:
            print(based, file=ausdb)
            print(featurerace, file=ausdb)
    elif country == "USA":
        with open('usa_featureRaces.db', 'a+') as usadb:
            print(based, file=usadb)
            print(featurerace, file=usadb)
    elif country == "UK":
        with open('uk_featureRaces.db', 'a+') as ukdb:
            print(based, file=ukdb)
            print(featurerace, file=ukdb)
    elif country == "UAE":
        with open('uae_featureRaces.db', 'a+') as uaedb:
            print(based, file=uaedb)
            print(featurerace, file=uaedb)
    elif country == "SGP":
        with open('sgp_featureRaces.db', 'a+') as sgpdb:
            print(based, file=sgpdb)
            print(featurerace, file=sgpdb)
    elif country == "SA":
        with open('sa_featureRaces.db', 'a+') as sadb:
            print(based, file=sadb)
            print(featurerace, file=sadb)
    elif country == "NZ":
        with open('nz_featureRaces.db', 'a+') as nzdb:
            print(based, file=nzdb)
            print(featurerace, file=nzdb)
    elif country == "JAP":
        with open('jap_featureRaces.db', 'a+') as japdb:
            print(based, file=japdb)
            print(featurerace, file=japdb)
    elif country == "IRE":
        with open('ire_featureRaces.db', 'a+') as iredb:
            print(based, file=iredb)
            print(featurerace, file=iredb)
    elif country == "HK":
        with open('hk_featureRaces.db', 'a+') as hkdb:
            print(based, file=hkdb)
            print(featurerace, file=hkdb)
    elif country == "GER":
        with open('ger_featureRaces.db', 'a+') as gerdb:
            print(based, file=gerdb)
            print(featurerace, file=gerdb)
    elif country == "FR":
        with open('fr_featureRaces.db', 'a+') as frdb:
            print(based, file=frdb)
            print(featurerace, file=frdb)
    elif country == "CAN":
        with open('can_featureRaces.db', 'a+') as candb:
            print(based, file=candb)
            print(featurerace, file=candb)

    with open('_sched_f.db', 'a+t') as schedule:
        print(f"{smon},{day}", file=schedule)
        print(f"{racecourse}", file=schedule)
        if args.time:
            print(time, file=schedule)
        if args.preps:
            print(f"_preps,{args.preps}", file=schedule)
        print(f"{name}", file=schedule)


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    fromfile_prefix_chars='@',
    prog='soschedfile'
)
parser.add_argument("--file")
basic = parser.add_argument_group('basic')
basic.add_argument("-n", "--name",
                   type=str,
                   help="name of race",
                   nargs='*'
                   )
basic.add_argument("-g", "--surface",
                   type=str,
                   help="enter the surface type",
                   choices=(
                       'T',
                       'D'
                   )
                   )
basic.add_argument("-m", "--month",
                   type=str,
                   help="month of race",
                   metavar='MON',
                   choices=(
                       'Jan',
                       'Feb',
                       'Mar',
                       'Apr',
                       'May',
                       'Jun',
                       'Jul',
                       'Aug',
                       'Sep',
                       'Oct',
                       'Nov',
                       'Dec'
                   )
                   )
basic.add_argument("-d", "--day",
                   type=int,
                   help="day of race",
                   )
basic.add_argument("-p", "--prize",
                   type=int,
                   help="prize money"
                   )
basic.add_argument("-f", "--distance",
                   type=str,
                   help="distance of race in miles and furlongs",
                   metavar='XmXf',
                   choices=('5f',
                            '6f',
                            '7f',
                            '1m',
                            '1m1f',
                            '1m2f',
                            '1m3f',
                            '1m4f',
                            '1m5f',
                            '1m6f',
                            '1m7f',
                            '2m'
                            )
                   )
basic.add_argument("-r", "--racecatag",
                   type=str,
                   help="class of race",
                   metavar='CLASS IN SO6',
                   choices=(
                       '60',
                       '65',
                       '70',
                       '75',
                       '80',
                       '85',
                       '90',
                       '95',
                       '100',
                       '105',
                       '110',
                       '120',
                       'M',
                       'N',
                       'COND',
                       'LH',
                       'L',
                       'G3H',
                       'G3',
                       'G2H',
                       'G2',
                       'G1H',
                       'G1'
                   )
                   )
basic.add_argument("-a", "--age",
                   type=str,
                   help="restricted to these ages. default 3YOUP",
                   default='3up',
                   metavar='AGE IN SO6',
                   choices=('2',
                            '3',
                            '4',
                            '5',
                            '23',
                            '34',
                            '3up',
                            '4up',
                            '5up',
                            '6up',
                            '7up',
                            '8up',
                            '9up',
                            '10up'
                            )
                   )
basic.add_argument("-t", "--track",
                   type=str,
                   help="racetrack name",
                   action='store',
                   choices=(
                       'Ascot',
                       'Brisbane',
                       'Caulfield',
                       'Doomben',
                       'Flemington',
                       'Moonee_Valley',
                       'Morphettville',
                       'Randwick',
                       'Rosehill',
                       'Warrnambool',
                       'Warwick_Farm',
                       'Oakbank',
                       'Albany',
                       'Alberta',
                       'Albuquerque',
                       'Arcadia',
                       'Arkansas',
                       'Baltimore',
                       'Boston',
                       'Brooklyn',
                       'California',
                       'Chicago',
                       'Columbus',
                       'Delaware',
                       'Farmington',
                       'Florence',
                       'Florida',
                       'Hollywood',
                       'Houston',
                       'Illinois',
                       'Iowa',
                       'Kentucky',
                       'Louisiana',
                       'Louisville',
                       'Maryland',
                       'Monticello',
                       'New_Jersey',
                       'New_York',
                       'Oceanport',
                       'Ohio',
                       'Oklahoma',
                       'Oregon',
                       'Phoenix',
                       'Pomana',
                       'Saratoga_Springs',
                       'Selma',
                       'Texas',
                       'Tuscon',
                       'Vancouver',
                       'Virginia',
                       'Washington',
                       'Ascot_uk',
                       'Ayr',
                       'Bath',
                       'Beverly',
                       'Brighton',
                       'Carlisle',
                       'Catterick',
                       'Chelmsford_City',
                       'Chepstow',
                       'Chester',
                       'Doncaster',
                       'Epsom',
                       'Ffos_Las',
                       'Goodwood',
                       'Hamilton',
                       'Haydock',
                       'Kempton',
                       'Leicester',
                       'Lingfield',
                       'Musselburgh',
                       'Newbury',
                       'Newcastle',
                       'Newmarket',
                       'Nottingham',
                       'Pontefract',
                       'Redcar',
                       'Ripon',
                       'Salisbury',
                       'Sandown',
                       'Southwell',
                       'Thirsk',
                       'Warwick',
                       'Windsor',
                       'Wolverhampton',
                       'Yarmouth',
                       'York',
                       'Dubai',
                       'Kranji',
                       'Durbanville',
                       'Kenilworth',
                       'Turffontein',
                       'Ellerslie',
                       'Hastings',
                       'Otaki',
                       'Trentham',
                       'Hanshin',
                       'Kyoto',
                       'Nakayama',
                       'Tokyo',
                       'Curragh',
                       'Dundalk',
                       'Fairyhouse',
                       'Galway',
                       'Gowran_Park',
                       'Leopardstown',
                       'Limerick',
                       'Navan',
                       'Tipperary',
                       'Sha_Tin',
                       'Baden-Baden',
                       'Chantilly',
                       'Deauville',
                       'Longchamp',
                       'Maisons_Laffitte',
                       'Saint_Cloud',
                       'Toronto'
                   )
                   )

optional = parser.add_argument_group('optional')
optional.add_argument("-F", "--field",
                      type=str,
                      help="force field size in full word"
                      )
optional.add_argument("-s", "--sex",
                      type=str,
                      help="restricted to sex",
                      metavar='SEX',
                      choices=('F', 'FM', 'CF', 'CG', 'M')
                      )
optional.add_argument("-i", "--int",
                      type=str,
                      help="force home field",
                      choices=(
                          'home',
                          'international'
                      )
                      )
optional.add_argument("-P", "--preps",
                      type=str,
                      help="prep races name,name",
                      nargs='*'
                      )
optional.add_argument("-T", "--time",
                      help="for evening races",
                      action='store_true'
                      )
optional.add_argument("-C", "--conds",
                      type=str,
                      help="conditions for race. must be used with CONDS.",
                      metavar='COND',
                      choices=(
                          'mw',
                          'mhr',
                          'mr',
                          'nwc',
                          'nwg',
                      )
                      )
optional.add_argument("-c",
                      type=str,
                      help="number of races/wins for conds",
                      )
args = parser.parse_args()
args.file = str(args.file)

with open(args.file, 'r') as f:
    for line in f.readlines():
        args = parser.parse_args(line.split())

        track = (track.get(args.track))
        args.name = ' '.join(args.name)
        if args.preps:
            args.preps = ''.join(args.preps)

        country = (country.get(track))
        racecourse = args.track
        name = args.name
        going = (surface.get(args.surface))
        distance = (distance.get(args.distance))
        age = (age.get(args.age))
        raceclass = (raceclass.get(args.racecatag))
        prize = str(args.prize)
        month = args.month
        smon = (number.get(args.month))
        day = str(args.day)
        # defining optional args
        field = args.field
        sex = args.sex
        international = args.int
        if args.time:
            time = "_evening"

        # qa test of conditions
        if args.conds:
            conditions = (codict.get(args.conds)) + args.c
            conjoin = ''.join(conditions)
        else:
            conjoin = args.conds

        if raceclass == "CONDITIONS":
            if not args.conds:
                sys.exit("Conditions must be assigned to this race")

        # construct the feature race information based on what arguments exist
        featurerace = f"<MONTH>{month}<PRIZE>{prize}"
        if field:
            featurerace += f"<FORCEFIELD>{field}"
        if international:
            featurerace += f"<EXTFIELDSPEC>{international}"
        featurerace += f"<DISTANCE>{distance}<RACECATAG>{raceclass}<AGE>{age}"
        if sex:
            featurerace += f"<SEX>{sex}"
        if conjoin:
            featurerace += f"<CONDITIONS>{conjoin}"

        based = f"<NAME>{name}<RACECOURSE>{racecourse}{going}"

        # run this before printing otherwise have to wipe files if error
        # with open('racearchive.txt', 'r+') as racenames:
        # RaceNames()

        # sqlite3Entry()

        # printRaces()

        print(name)
        # print(featurerace)
        continue
