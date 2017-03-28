import random
import time

def win():
    print "Congratulations!!!!!!!!!!!!!!!!! You saved the village!!!!! They give you the honorary obsidian daggers as a reward!"

def gameOver():
    print "Game OVER!!! Too Bad!"
    retry = raw_input("\n\nWant to try again? (yes or no)\n\n").lower()
    if retry == "yes":
        game()
    else:
        quit()

def game():
    gold = 50
    character_hp = 240
    weapon_damage = 15
    monster_damage = 25
    monster_payout = 80
    weapons = ["fists"]
    mistbornquiz=raw_input("\nAre you a mistborn?\n\n")
    if mistbornquiz == "yes":
        password=raw_input("\nWhat is the password?\n\n")
        if password == "death":
            passw=raw_input("\nWhat is the second password?\n\n")
            if passw == "endure":
                passd=raw_input("\nWhat is the third password?\n\n")
                if passd == "author":
                    passr=raw_input("\nWhat is the fourth password?\n\n")
                    if passr == "elite":
                        passo=raw_input("\nWhat is the fifth password?")
                        if passo == "pi":
                            word=raw_input("\nWhat is the sixth password?")
                            if word == "Marie Lu":
                                wrd=raw_input("\nWhat is the seventh password?")
                                if wrd == "Sara B. Larson":
                                    name=raw_input("\nWhat is your name?\n\n").title()
                                    while name == "":
                                        name=raw_input("\nWhat is your name?\n\n")
                                    if name == "Vin" or name == "Vin Venture" or name == "Elend" or name == "Elend Venture" or name == "Kelsier" or name == "Lord Ruler" or name == "The Lord Ruler" or name == "vin" or name == "vin venture" or name == "elend" or name == "elend venture" or name == "kelsier" or name == "June" or name == "June Iparis" or name == "june" or name == "june iparis" or name == "day" or name == "Day" or name == "Daniel Wing" or name == "daniel wing" or name == "Daniel Altan Wing" or name == "daniel altan wing" or name == "eden" or name == "Eden" or name == "Eden Wing" or name == "eden wing" or name == "Eden Bataar Wing" or name == "eden bataar wing":
                                        print "\nWelcome", name, ", Enjoy Your Adventure!\n"
                                        while character_hp > 0:
                                            WEAPONS_STORE = {
                                                "coins": 160,
                                                "axe": 120,
                                                "club": 75,
                                                "dagger": 50,
                                                "bat": 45,
                                                "book": 450
                                            }
                                            MONSTERS = {
                                                "soother/rioter":25,
                                                "seeker/smoker": 55,
                                                "tineye": 80,
                                                "coinshot/lurcher": 105,
                                                "pewterarm": 150,
                                                "mistborn":250,
                                                "the lord ruler": 340
                                            }
                                            while character_hp > 0:
                                                
                                                store = raw_input("\nDo you want to buy weapons? (yes or no)\n\n").lower()
                                                if store == "yes":
                                                    print "\nWEAPON\t\tCOST\n"
                                                    for items in WEAPONS_STORE:
                                                        print items, "\t\t", WEAPONS_STORE[items], "\n"
                                                    print "\nYou have", gold, "gold\n\n"
                                                    weapon_purchase = raw_input("Which weapon would you like to buy?\n\n").lower()
                                                    while weapon_purchase not in WEAPONS_STORE or weapon_purchase in weapons:
                                                        weapon_purchase = raw_input("Which weapon would you like to by?\n\n").lower()
                                                    
                                                    if weapon_purchase in WEAPONS_STORE and weapon_purchase not in weapons:
                                                        if gold >= WEAPONS_STORE[weapon_purchase]:
                                                            print "you bought a(n)", weapon_purchase, "\n"
                                                            gold -= WEAPONS_STORE[weapon_purchase]
                                                            weapons.append(weapon_purchase)
                                                            print "\nyou have", gold, "gold\n"
                                                            print "\nWeapon(s) you own\n"
                                                            for items in weapons:
                                                                print items

                                                        elif gold <= WEAPONS_STORE[weapon_purchase]:
                                                            print "not enough gold"

                                                elif store == "no":
                                                    print "\nTime to destroy a monster from the village!\n"
                                                    print "\nMONSTERS\tHEALTH\t\n"
                                                    for monster in MONSTERS:
                                                        print monster, "\t\t", MONSTERS[monster], "\n"
                                                    monchoice = raw_input("Which Monster do you want to destroy from the village?\n\n").lower()
                                                    if monchoice in MONSTERS:
                                                        print "\n Good Luck! Destroy the ", monchoice, " from the village."
                                                    else:
                                                            print "That monster is not in the village."

                                                            while monchoice not in MONSTERS:
                                                                monchoice = raw_input("Which Monster do you want to destroy from the village?\n\n").lower()
                                                    print "\nWEAPONS YOU OWN\n"
                                                    for weapon in weapons:
                                                        print weapon, "\n"
                                                    weapuse = raw_input("What weapon do you choose?\n\n").lower()
                                                    if weapuse in weapons:
                                                        print "\nWise choice ", name, ". You will use the ", weapuse, " against the ", monchoice
                                                        if weapuse == "fists" or weapuse == "bat":
                                                            while character_hp > 0 and MONSTERS[monchoice] > 0:
                                                                rand = random.randint(3, 7)
                                                                pdmg = weapon_damage + rand
                                                                mdmg = monster_damage
                                                                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                                                                time.sleep(0.5)
                                                                print "The", monchoice, "attacked YOU by", mdmg
                                                                character_hp -= mdmg
                                                                if character_hp <= 0:
                                                                    gameOver()
                                                                print name, ", your health is now", character_hp
                                                                time.sleep(0.5)
                                                                print "\nYou attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"
                                                                MONSTERS[monchoice] -= pdmg
                                                                time.sleep(0.5)
                                                        elif weapuse == "dagger" or weapuse == "axe" or weapuse == "club":
                                                            while character_hp > 0 and MONSTERS[monchoice]>0:
                                                                rand = random.randint(5,20)
                                                                pdmg = weapon_damage + rand
                                                                mdmg = monster_damage
                                                                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                                                                time.sleep(0.5)
                                                                print "The", monchoice, "attacked YOU by", mdmg
                                                                character_hp -= mdmg
                                                                if character_hp <= 0:
                                                                    gameOver()
                                                                print name, ", your health is now", character_hp
                                                                time.sleep(0.5)
                                                                print "\nYou attacked the", monchoice, "with the",
                                                                weapuse, "for", pdmg, "damage!"
                                                                MONSTERS[monchoice] -= pdmg
                                                                time.sleep(0.5)
                                                        elif weapuse == "coins":
                                                            while character_hp > 0 and MONSTERS[monchoice]>0:
                                                                rand = random.randint(10,50)
                                                                pdmg = weapon_damage + rand
                                                                mdmg = monster_damage
                                                                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                                                                time.sleep(0.5)
                                                                print "The", monchoice, "attacked YOU by", mdmg
                                                                character_hp -= mdmg
                                                                if character_hp <= 0:
                                                                    gameOver()
                                                                print name, ", your health is now", character_hp
                                                                time.sleep(0.5)
                                                                print "\nYou attacked the", monchoice, "with the",
                                                                weapuse, "for", pdmg, "damage!"
                                                                MONSTERS[monchoice] -= pdmg
                                                                time.sleep(0.5)
                                                        elif weapuse == "book":
                                                            while character_hp > 0 and MONSTERS[monchoice]>0:
                                                                rand = random.randint(400, 500)
                                                                pdmg = weapon_damage + rand
                                                                mdmg = monster_damage
                                                                print monchoice, "has", MONSTERS[monchoice], "health left\n\n"
                                                                timesleep(0.5)
                                                                print "The", monchoice, "attacked YOU by", mdmg
                                                                character_hp -= mdmg
                                                                if character_hp <= 0:
                                                                    gameOver()
                                                                print name, ", your health is now", character_hp
                                                                time.sleep(0.5)
                                                                print "\nYou attacked the", monchoice, "with the",
                                                                weapuse, "for", pdmg, "damage!"
                                                                MONSTERS[monchoice] -= pdmg
                                                                time.sleep(0.5) 
                                                                
                                                    else:
                                                        print name, "\nYou don't own the ", weapuse,"!"
                                                        while weapuse not in weapons:
                                                            weapuse = raw_input("\nWhat weapon will you use?\n\n").lower()
                                                        print "\nWise choice ", name, ". You will use the ", weapuse, " against the ", monchoice
                                                    if MONSTERS[monchoice] <= 0:
                                                        print "\nThe", monchoice, "has been destroyed. Good work,", name, "!"
                                                        character_hp = 240
                                                        gold += monster_payout
                                                        print "\nYou have", gold, "gold\n"
                                                        if monchoice == "the lord ruler":
                                                            win()
                                                        del MONSTERS[monchoice]
                                else:
                                    gameOver()
                            else:
                                gameOver()
                        else:
                            gameOver()
                    else:
                        gameOver()
                else:
                    gameOver()
            else:
                gameOver()
        else:
            gameOver()
    if mistbornquiz == "no":
        gameOver()
    else:
        gameOver()

game()
