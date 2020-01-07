
from pathlib import Path
import argparse
import sys
from dictionary import (
    country,
    surface,
    distance,
    age,
    raceclass,
    schedgoing,
    number,
    codict
)
import sqlite3

# open output file and automatically close after run
with open('_sched_f.db', 'a+t') as schedule, \
    open('aus_featureRaces.db', 'a+') as ausdb, \
    open('can_featureRaces.db', 'a+') as candb, \
    open('fr_featureRaces.db', 'a+') as frdb, \
    open('ger_featureRaces.db', 'a+') as gerdb, \
    open('hk_featureRaces.db', 'a+') as hkdb, \
    open('ire_featureRaces.db', 'a+') as iredb, \
    open('usa_featureRaces.db', 'a+') as usadb, \
    open('uk_featureRaces.db', 'a+') as ukdb, \
    open('uae_featureRaces.db', 'a+') as uaedb, \
    open('sgp_featureRaces.db', 'a+') as sgpdb, \
    open('sa_featureRaces.db', 'a+') as sadb, \
    open('nz_featureRaces.db', 'a+') as nzdb, \
    open('jap_featureRaces.db', 'a+') as japdb, \
    open('racearchive.txt', 'r+') as racenames:

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog='sosched')
    basic = parser.add_argument_group('basic')
    basic.add_argument("-n", "--name",
                    type=str,
                    help="name of race"
                    )
    basic.add_argument("-g", "--surface",
                    required=True,
                    type=str,
                    help="enter the surface type",
                    choices=(
                        'T',
                        'D'
                    )
                    )
    basic.add_argument("-m", "--month",
                    required=True,
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
                    required=True,
                    type=int,
                    help="day of race",
                    )
    basic.add_argument("-p", "--prize",
                    required=True,
                    type=int,
                    help="prize money"
                    )
    basic.add_argument("-f", "--distance",
                    type=str,
                    required=True,
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
                    required=True,
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
                    required=True,
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
                            '10up',
                            )
                    )
    basic.add_argument("-t", "--track",
                       type=str,
                       required=True,
                       help="racetrack name",
                       choices=(
                                'Ascot',
                                'Brisbane',
                                'Caulfield',
                                'Doomben',
                                'Flemington',
                                'Moonee Valley',
                                'Morphettville',
                                'Randwick',
                                'Rosehill',
                                'Warrnambool',
                                'Warwick Farm',
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
                                'New Jersey',
                                'New York',
                                'Oceanport',
                                'Ohio',
                                'Oklahoma',
                                'Oregon',
                                'Phoenix',
                                'Pomana',
                                'Saratoga Springs',
                                'Selma',
                                'Texas',
                                'Tuscon',
                                'Vancouver',
                                'Virginia',
                                'Washington',
                                'Ascot-uk',
                                'Ayr',
                                'Bath',
                                'Beverly',
                                'Brighton',
                                'Carlisle',
                                'Catterick',
                                'Chelmsford City',
                                'Chepstow',
                                'Chester',
                                'Doncaster',
                                'Epsom',
                                'Ffos Las',
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
                                'Gowran Park',
                                'Leopardstown',
                                'Limerick',
                                'Navan',
                                'Tipperary',
                                'Sha Tin',
                                'Baden-Baden',
                                'Chantilly',
                                'Deauville',
                                'Longchamp',
                                'Maisons Laffitte',
                                'Saint Cloud',
                                'Toronto'
                       )
                       )
    
    optional = parser.add_argument_group('optional')
    optional.add_argument("--field",
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
                        help="force home field"
                        )
    optional.add_argument("--preps",
                        type=str,
                        help="prep races name,name")
    optional.add_argument("--conds",
                        type=str,
                        help="conditions for race. must be used with CONDS race type.",
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

    country = (country.get(args.track))
    name = args.name
    going = (surface.get(args.surface))
    distance = (distance.get(args.distance))
    age = (age.get(args.age))
    raceclass = (raceclass.get(args.racecatag))
    prize = str(args.prize)
    month = args.month
    scourse = (schedgoing.get(args.surface))
    smon = (number.get(args.month))
    day = str(args.day)
    # defining optional args
    field = args.field
    sex = args.sex
    international = args.int

    # qa test of conditions
    if args.conds:
        conditions = (codict.get(args.conds)) + args.c
        conjoin = ''.join(conditions)
    else:
        conjoin = args.conds

    if raceclass == "CONDITIONS":
        if not args.conds:
            sys.exit("Conditions must be assigned to this race")


    def RaceNames():
        def checkIfDuplicate():
            # define empty list
            races = []
            #open file and read content in a list
            races = [race_name.rstrip() for race_name in racenames.readlines()]
            setOfRaces = set(races)
            if name  in setOfRaces:
                return True
            else:
                return False

        result = checkIfDuplicate()

        if result:
            sys.exit('Race name is duplicate')
        else:
            print(name, file=racenames)
        return
    

    RaceNames()

    feature = "<MONTH>{0}<PRIZE>{1}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}"
    base= "<NAME>{0}<RACECOURSE>{1}{2}"

    # construct the feature race information based on what arguments exist
    if args.field:
        feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}"
        if args.sex:
            feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}"
            if args.int:
                feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}"
                if args.conds:
                    feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}<CONDITIONS>{8}"    
        elif args.int:
            feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<EXTFIELDSPEC{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}"
            if args.conds:
                feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<EXTFIELDSPEC{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<CONDITIONS>{8}"
        elif args.conds:
            feature = "<MONTH>{0}<PRIZE>{1}<FORCEFIELD>{5}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<CONDITIONS>{8}"
    else:
        if args.sex:
            if args.int:
                feature = "<MONTH>{0}<PRIZE>{1}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}"
                if args.conds:
                    feature = "<MONTH>{0}<PRIZE>{1}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}<CONDITIONS>{8}"
            else:
                feature = "<MONTH>{0}<PRIZE>{1}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}"
                if args.conds:
                    feature = "<MONTH>{0}<PRIZE>{1}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<SEX>{6}<CONDITIONS>{8}"
        else:
            if args.int:
                feature = "<MONTH>{0}<PRIZE>{1}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}"
                if args.conds:
                    feature = "<MONTH>{0}<PRIZE>{1}<EXTFIELDSPEC>{7}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<CONDITIONS>{8}"
            else:
                if args.conds:
                    feature = "<MONTH>{0}<PRIZE>{1}<DISTANCE>{2}<RACECATAG>{3}<AGE>{4}<CONDTIONS>{8}"

    based = base.format(name, racecourse, going)
    featurerace = feature.format(month, prize, distance, raceclass, age, field, sex, international, conjoin)

    def sqlite3Entry():
        try:
            so7 = sqlite3.connect('so7.db')
            cursor = so7.cursor()

            cursor.execute('''INSERT INTO races (ID, Day, Month, Name, Course, Going, Country, Distance, Prize, Sex, Age, Field, International, Conditions, Class) VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(day, month, name, racecourse, going, country, distance, prize, sex, age, field, international, conjoin, raceclass))

            so7.commit()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (so7):
                so7.close()
    
    # run this before printing otherwise have to wipe files if error
    sqlite3Entry()
    
    # assign feature race file based on which country racecourse
    if args.usa:
        print(based, file=usadb)
        print(featurerace, file=usadb)
    elif args.uk:
        print(based, file=ukdb)
        print(featurerace, file=ukdb)
    elif args.uae:
        print(based, file=uaedb)
        print(featurerace, file=uaedb)
    elif args.sgp:
        print(based, file=sgpdb)
        print(featurerace, file=sgpdb)
    elif args.sa:
        print(based, file=sadb)
        print(featurerace, file=sadb)
    elif args.nz:
        print(based, file=nzdb)
        print(featurerace, file=nzdb)
    elif args.jap:
        print(based, file=japdb)
        print(featurerace, file=japdb)
    elif args.ire:
        print(based, file=iredb)
        print(featurerace, file=iredb)
    elif args.hk:
        print(based, file=hkdb)
        print(featurerace, file=hkdb)
    elif args.ger:
        print(based, file=gerdb)
        print(featurerace, file=gerdb)
    elif args.fr:
        print(based, file=frdb)
        print(featurerace, file=frdb)
    elif args.can:
        print(based, file=candb)
        print(featurerace, file=candb)
    elif args.aus:
        print(based, file=ausdb)
        print(featurerace, file=ausdb)
    else:
        print("Unsuccessful")
    
    print(f"{smon},{day}", file=schedule)
    print(f"{racecourse}{scourse}", file=schedule)
    if args.preps:
        print(f"_preps,{args.preps}", file=schedule)
    print(f"{name}", file=schedule)
    
    print("Success")
