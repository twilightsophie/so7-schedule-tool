# DESCRIPTION
A Python script built to build custom modded schedules for the game Starters Orders 7.  

The script will take input from the command line and print formatted entries to the required schedule and feature race files. Entries will be saved to a SQLite database and present an error if a duplicate race name is entered.

# PREREQUISITES

* SQLite3
* Python 3+

# USAGE
Races must be entered in chronological order with each argument representing a part of the feature race information. The script will not order the races and all new entries will be added to the bottom of the documents.

To delete a race, it must be deleted in the schedule file, the feature race file, the racearchive.txt file and from the SQLite database. See DELETING A RACE for instructions below.

## Result

This will turn out a formatted entry in both the schedule file and the feature race file for the country. As per the instructions in the Starters Orders 7 manual, this is the format:

**Schedule File**  
```
[day], [month number]
[racecourse]
[name]
```

**Feature Race File**  
```
<NAME>[name]<RACECOURSE>[course][:cc_going]
<MONTH>[MON]<PRIZE>[00000]<EXTFIELDSPEC>[international]<FORCEFIELD>[field]<DISTANCE>[distance]<RACECATAG>[raceclass]<AGE>[age]<SEX>[sex]<CONDITIONS>[condition type]=[condition number]
```

The script will only populate the optional parts of the format if the argument is called.

# OPTIONS

Required options must be entered. The information can be entered in any order. 

Racecourse must also be entered. Valid choices are the default racecourses offered as part of the base game. This will ensure that the feature race information is printed to the right file.

Conditions must be entered with both the conditions type and connection number. It is combined to fit the format of ```--conds```=```-c```. If the race catagory is ```COND``` and there are no conditions attched, script will error out.

## Required
```
-n      RACE NAME               enter as text inside ""
-d      DAY OF THE MONTH        a single number
-m      MONTH                   name of month as Mon
-f      DISTANCE                as XmXf
-r      RACE CATAGORY           in SO6 shorthand
-p      PRIZE                   without currency sign
-a      AGE                     in SO6 shorthand
-g      GOING                   T = turf or D = dirt
```

## Optional
```
--conds     TYPE OF CONDITION   condition of race
-c          CONDITION NUMBER    amount for condition
--field     FORCEFIELD          force field using size or fixed:X
--preps     PREP RACE(S)        the name of prep race,races
-i          HOME FIELD          use 'home' to force home field
```

## Racecourses
```
--aus   AUSTRALIAN
--can   CANADA
--fr    FRANCE
--ger   GERMANY
--hk    HONG KONG
--ire   IRELAND
--jap   JAPAN
--nz    NEW ZEALAND
--sa    SOUTH AFRICA
--sgp   SINGAPORE
--uae   UNITED ARAB EMPIRE/DUBAI
--uk    UNITED KINGDOM
--usa   USA
```

# DELETING RACES
If you have entered a race incorrectly or in the wrong place, it must be manually deleted from the files. **This script is output-only**. 

## Deleting from Schedule and Feature Race Files

## Deleting from Race Archive

## Deleting from SQLite Database

If you need to delete a race from the database, you have the option of doing so by the database entry ID or by a search term. You must access the database through the command line or the terminal of your PC.

If you know the ID of the race:
```
DELETE FROM races
WHERE ID = [id number];
```
If you know the name:
```
DELETE FROM races
WHERE name LIKE %[name of race]%;
```

# FUTURE FIXES
- Add choices to readme
- **IMPORTANT** - change duplicate checker to compare both racecourse and name, as game will allow a duplicate name if at a different track.
