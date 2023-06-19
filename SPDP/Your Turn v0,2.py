import math
# ^This module is used in rounding, which happens mainly when a hero attacks in a weakened or bolstered state with an odd attack value that then becomes X.5 and could cause somebody being alive at .5 health.

hero_options = ['Squire', 'Markswoman', 'Apprentice', 'Priest'] #the name of the heros you can choose
hero_options_static = [hero_options] #the same list as hero_options, but it doesn't change and is used as reference to reset hero options as needed during deck creation
hero_stats =   [(100, 10), (90, 9), (80, 8), (70, 7)] # The max hp and attack value of the heroes. each () is one hero [(hp, attack), (hp, attack),...]
gear_options = ['Barrier Orb', 'Reflux Glove', 'Lightning Coil', 'Fruit Of Life'] # gears availilble for the heros to use

CardList =     [ 'Defensive Stance',                          'Shield Block',                  'Overpower Strike',                           'Squire Attack',                               'Incendiary Shot',                                 'Multiple Shots',                                  'Aimed Shot',                                  'Markswoman Attack',                              'Ice Scroll',                                                  'Flame Scroll',                                        'Lightning Scroll',                                          'Apprentice Attack',                              'Cleansing Touch',                                                           'Prayer of Healing',                  'Healing Spell',                               'Priest Attack']
# ^Lists all the cards that can be used
CardListDesc = [('Taunt self and draw a card', 0, 'Squire'), ('Shield self 40', 1, 'Squire'), ('15 damage and weaken target', 3, 'Squire'), ('Deal 10 damage to front hero', 0, 'Squire'), ('Deal 5 Fire damage to target', 1, 'Markswoman'), ('Deal 9 damage to all enemies', 2, 'Markswoman'), ('Deal 18 damage to target', 5, 'Markswoman'), ('Deal 9 damage to front hero', 0, 'Markswoman'), ('Deal 12 Frost damage to target; Volatile', 3, 'Apprentice'), ('Deal 12 Fire to target; Volatile', 3, 'Apprentice'), ('Deal 8 damage to all enemies; Volatile', 3, 'Apprentice'), ('Deal 8 damage to front hero', 0, 'Apprentice'), ('Dispel debuffs from an ally, or dispel buffs from an enemy', 1, 'Priest'), ('Heal all allies 11 health', 1, 'Priest'), ('Heal an ally 21 health', 1, 'Priest'), ('Deal 7 damage to the front hero', 0, 'Priest')]
# ^Infor pertaining to all the cards that can be used. Arranged to match with the card names above. info is [(desc, mana cost, casting hero), (repeat)]

P1Front = 'Undefined'
P1Second = 'Undefined'
P1Third = 'Undefined'
P1Back = 'Undefined'
P1FrontGear = 'Undefined'
P1SecondGear = 'Undefined'
P1ThirdGear = 'Undefined'
P1BackGear = 'Undefined'
P2Front = 'Undefined'
P2Second = 'Undefined'
P2Third = 'Undefined'
P2Back = 'Undefined'
P2FrontGear = 'Undefined'
P2SecondGear = 'Undefined'
P2ThirdGear = 'Undefined'
P2BackGear = 'Undefined'
# ^This is the lineup, i think it can be removed but im leaving it here until I code in a proper workaround that doesnt need them.

P1Deck = []
P2Deck = []
# ^These will be full of what cards are in your deck.

P1Hand = []
P2Hand = []
# ^These will be full of the cards that are in your hand
# Hopefully, moving cards from hand to deck will be easy. There is probably a way to combine the two by adding and extra item to each card name noting the location of the card, but thats something for another time.

P1FrontHP = 0
P1FrontMaxHP = 0
P1FrontAT = 0
P1FrontEX = 0
P1SecondHP = 0
P1SecondMaxHP = 0
P1SecondAT = 0
P1SecondEX = 0
P1ThirdHP = 0
P1ThirdMaxHP = 0
P1ThirdAT = 0
P1ThirdEX = 0
P1BackHP = 0
P1BackMaxHp = 0
P1BackAT = 0
P1BackEX = 0
P2FrontHP = 0
P2FrontMaxHP = 0
P2FrontAT = 0
P2FrontEX = 0
P2SecondHP = 0
P2SecondMaxHP = 0
P2SecondAT = 0
P2SecondEX = 0
P2ThirdHP = 0
P2ThirdMaxHP = 0
P2ThirdAT = 0
P2ThirdEX = 0
P2BackHP = 0
P2BackMaxHP = 0
P2BackAT = 0
P2BackEX = 0
# ^These are the stats of each hero, which are probably also unnecessary but I'm leaving here until I get a workaround working.

P1Lineup = []
P2Lineup = []
# ^These are the lineups, which will include the hero name of each slot, the gear with them, as well as buffs/debuffs and other items.
# Format for these is planend to be [(Hero, HP, HPmax, EX, and then a thing for each buff/debuff status)]

counter = 0
# ^This is a misc counter variable I need because im too stupid to do it without it. 

# Here is a cool intro thing I might eventually make.
print("Welcome to Your Turn, a remake of My Turn in python that is not as good quality but hopefully good enough to help with those sudden urges to combo Markswoman's ulti 4 times in one turn.")
print("Enjoy.")

# Below is the lineup setup. This is pretty unnecessary right now and will probably get commented out until more heros and gears are added when it will be needed to make different decks.
print('')
print('-----')
print('')

# print('Here are the heroes availible for you to choose:', hero_options)
# choice = input('What hero would you like to put in your lineup? ')
# for item in hero_options:
#     if choice.title() == hero_options[counter]:
#         choice = input('Alright. What location would you like', hero_options[counter], 'to go in? 1 is the front, and 4 is the back.')
#         #need more stuff here to put the hero in its spot
#         break
#     else:
#         counter += 1
#         if counter == len(hero_options):
#             print("Sorry, but that's not an option. Check spelling and try again?")

#until I have more heroes, I won't bother working on the lineup setup. Once that is added tho, these next few lines should be removed.

P1Lineup = [('Squire', 100, 100, 0, 0, 1, 0, 0, 0), ('Markswoman', 90, 9, 0, 0, 1, 0, 0, 0), ('Apprentice', 80, 8, 0, 0, 1, 0, 0, 0), ('Preist', 70, 7, 0, 0, 1, 0, 0, 0)]
P2Lineup = [('Squire', 100, 100, 0, 0, 1, 0, 0, 0), ('Markswoman', 90, 9, 0, 0, 1, 0, 0, 0), ('Apprentice', 80, 8, 0, 0, 1, 0, 0, 0), ('Preist', 70, 7, 0, 0, 1, 0, 0, 0)]
#(Hero, HP, HPmax, EX, shield, strengthened/weakened, stun, fire, ice)
#strengthened/weakened is a multiplier, and so is either 1.5 or .5