from project2 import person, bcolors
from magic import spell
from inventory import Item
import random
'''
print("\n\n")
print("NAME             HP                                  MP")
print("                 _________________________           ___________")
print(bcolors.BOLD+"Valos:   "+"350/460"+bcolors.FAIL+"|███████████              "+bcolors.ENDC+"|    "+"65/65|"+bcolors.OKBLUE+"███████████"+bcolors.ENDC+"|")

print("                 _________________________           ___________")
print("Valos:   400/460|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       |    45/65|▓▓▓▓▓▓▓    |")'''

# use these bars from ASCII CODE 219. you can use them in html also.

#black magic

fire=spell("Fire",5,100,"Black")
thunder=spell("Thunder",10,130,"Black")
bizzard=spell("Bizzard",15,150,"Black")
meteor=spell("Meteor",20,200,"Black")
quake=spell("Quake",30,300,"Black")

#white magic
cure=spell("Cure",16,120,"White")
cura=spell("Cura",18,178,"White")

#create some item

potion=Item("Potion","potion","Heals 100 HP",100)
hipotion=Item("Hipotion","hipotion","Heals 300 HP",300)
superpotion=Item("Superpotion","superpotion","Heals 500 HP",500)
elixer=Item("Elixer","elixer","fully restores HP/MP of one party memeber",9999)
hielixer=Item("MegaElixer","elixer","Fully restore party's HP/MP",9999)

grenade=Item("Grenade","Attack","Deals 500 damage",500)

player_spells=[fire,thunder,bizzard,meteor,quake,cure,cura]
enemy_spells=[thunder,quake,cura]

player_items=[{"item": potion,"Quantity":10},{"item":hipotion,"Quantity":8},{"item":superpotion,"Quantity":6},{"item":elixer,"Quantity":4},{"item":hielixer,"Quantity":3},{"item":grenade,"Quantity":2}]


'''magic=[{"name": "Fire", "cost":10, "dmg":100},
       {"name": "Thunder", "cost":20, "dmg":124},
       {"name": "Bizzard", "cost":30, "dmg":130}]
'''
#instantiate poeple

player1=person("David :",4160,100,60,34,player_spells,player_items)
player2=person("Warner:",3960,150,60,34,player_spells,player_items)
player3=person("Finch :",3860,200,60,34,player_spells,player_items)

enemy1=person("Robot :",20000,65,500,25,enemy_spells,[])
enemy2=person("Jombie:",4000,65,500,25,enemy_spells,[])
enemy3=person("Hacker:",7000,65,500,25,enemy_spells,[])

enemies=[enemy1,enemy2,enemy3]
players=[player1,player2,player3]

running=True
print(bcolors.FAIL + bcolors.BOLD +"AN ENEMY ATTACKS!"+bcolors.ENDC)

while running:
     print("=================")

     print("\n")
     
     print("NAME                HP                                   MP")
     for player in players:
      player.get_stats()
    
     print("\n")
     print(bcolors.BOLD+bcolors.FAIL+"ENEMY"+bcolors.ENDC+"                  HP")
     for enemy in enemies:
      enemy.get_stats_enemy()
      
     for player in players:
         
      player.choose_action()
      choice=input("Choose action: ")
      index=int(choice)-1
      
      if index==0:
         dmg=enemy.generate_damage()
         chic=player.choose_target(enemies)
         enemies[chic].take_damage(dmg)
         print("You attacked  "+enemies[chic].name+" for ",dmg,"points of damage")
 
         if enemies[chic].get_hp()==0:
               print(enemies[chic].name,"died!")
               del enemies[chic]
   
      elif index==1:
       #for player in players:
         player.choose_magic()
         magic_choice=int(input("Choose Magic: "))-1
         if magic_choice==-1:
               continue
         '''magic_dmg=player.generate_spell_damage(magic_choice)
         spell=player.get_spell_name(magic_choice)
         cost=player.get_spell_mp_cost(magic_choice)'''

         spell=player.magic[magic_choice]
         magic_dmg=spell.generate_damage()

         current_mp=player.get_mp()
         if spell.cost > current_mp:
               print(bcolors.FAIL + "\n No Enough MP\n" + bcolors.ENDC)
               continue
         player.reduce_mp(spell.cost)

         if spell.type=="white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE+"\n"+spell.name+"heals for",str(magic_dmg),"HP"+bcolors.ENDC)
         elif spell.type=="Black":
            chic=player.choose_target(enemies)
            enemies[chic].take_damage(magic_dmg)
      
            print(bcolors.OKBLUE + "\n" + spell.name + "deals ",str(magic_dmg),"points of damage to "+enemies[chic].name + bcolors.ENDC)

            
            if enemies[chic].get_hp()==0:
               print(enemies[chic].name,"died!")
               del enemies[chic]

      elif index==2:
         player.choose_item()
         item_choice=int(input("Choose Item: "))-1
         if item_choice==-1:
            continue
         item=player.items[item_choice]["item"]
         if (player.items[item_choice]["Quantity"]<=0):
            print(bcolors.FAIL+"\n"+"None Left......"+bcolors.ENDC)
         player.items[item_choice]["Quantity"]-=1
         if item.type=="potion":
            player.heal(item.prop)	
            print(bcolors.OKGREEN+"\n"+item.name+"heals for",str(item.prop),"HP"+bcolors.ENDC)
         elif item.type=="elixer":
            if item.name=="MegaElixer":
               for i in players:
                   i.hp=i.maxhp
                   i.mp=i.maxmp
            else:
               player.hp=player.maxhp
               player.mp=player.maxmp
            print(player.hp)
            print(bcolors.OKGREEN+"\n"+item.name+"Restores HP/MP"+bcolors.ENDC)
         elif item.type=="attack":
            player.choose_target(enemies)
            enemies[enemy].take_damage(item.prop)
            #enemy.take_damage(item.prop)
            print(bcolors.FAIL+"\n"+item.name+"deals with",str(item.prop),"points of damage to"+enemies[enemy].name+bcolors.ENDC)
            
            if enemies[chic].get_hp()==0:
               print(enemies[chic].name,"died!")
               del enemies[chic]

      #check if battle is over
     defeated_enemy=0
     defeated_player=0

     for enemy in enemies:
            
            if enemy.get_hp()==0:
               defeated_enemy+=1

     for player in players:

            if player.get_hp()==0:              
               defeated_player+=1
       
     #check if player win
     if defeated_enemy==2:
            print(bcolors.OKBLUE+"You Win!. Play Again"+bcolors.ENDC)
            running=False

     #check if enemy win
     elif defeated_player==2:
            print(bcolors.WARNING+"You Lose!"+bcolors.ENDC+"#"+bcolors.OKGREEN+"Play Again"+bcolors.ENDC)
            running=False


     #enemy attack phase
     for enemy in enemies:
         enemy_choice=random.randrange(0,2)
         if enemy_choice==0: 
               target=random.randrange(0,3)
               enemy_dmg= enemy	.generate_damage()
               players[target].take_damage(enemy_dmg)
               print(enemy.name+" attacks "+players[target].name+" for "+str(enemy_dmg))

         elif enemy_choice==1:
              spell, magic_dmg=enemy.choose_enemy_spell()
              enemy.reduce_mp(spell.cost)
              
              if spell.type=="white":
                  enemy.heal(magic_dmg)
                  print(bcolors.OKBLUE+"\n"+spell.name+"heals"+enemy.name+"for",str(magic_dmg),"HP"+bcolors.ENDC)
              elif spell.type=="Black":
                  target=random.randrange(0,3)
                  players[target].take_damage(magic_dmg)
      
                  print(bcolors.OKBLUE + "\n" +enemy.name+"'s "+ spell.name + "deals ",str(magic_dmg),"points of damage to "+players[target].name+bcolors.ENDC) 
                         
                  if players[target].get_hp()==0:
                      print(players[target].name,"died!")
                      del players[target]
            
            

