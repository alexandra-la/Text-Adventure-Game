import random
from Villain import Villain
from Adventurer import Adventurer

class AdventureGame:
    
    maxMoves = 10
    #List of planets a player can travel too
    travelList = ["Dathomir", "Zeffo", "Bogano", "Kashyyk", "Bracca", "Ilum"]
    villainList = []
    #adds villains that the player can defeat
    villainList.append(Villain("Stormtrooper", "One of the soliders for the Empire!", 15))
    villainList.append(Villain("Second Sister", "A relentless Imperial Inquisitor looking for Jedi!", 50))
    villainList.append(Villain("Rancor", "A wild Dathomirin Rancor looking for food!", 25))
    villainList.append(Villain("Scout Trooper", "Highly trained stormtroopers with stun sticks!", 20))
    villainList.append(Villain("Oggdo Bogdo", "A three eyed lizard who attacks with its tongue...gross!", 30))
    villainList.append(Villain("Ninth Sister", "A dangerous former Jedi turned inquisitor.", 50))
    
    def __init__(self):
        
        self.adventurer = Adventurer()
        self.currentPlanet = "Bogano" #sets the starting planet of the character
        self.playGame() #calls method to play game
    
    def playGame(self):
        #introduction to the game for player
        print("You are", self.adventurer.getName(),
              "and while travelling around the universe with your captain Greez Dritus and partner Cere Junda, Greez has asked",
              "that you actually pick up some new seeds for his terrarium inbetween fighting for your life as a small token of" ,
              "your appreciation. You are currently on Bogano with your ship the Mantis. Good luck!\n")
        for move in range(1, AdventureGame.maxMoves+1): #keeps player from going over 10 steps
            
            if(self.adventurer.isAlive() == False): #checks if player is alive and if not ends the game.
                print(self.adventurer,
                      "\nOh no! You have fallen in battle! BD-1 is signaling the Mantis for help.\nGame Over!")
                break
            self.promptMove() 
            encounter = random.randrange(1,8) #randomly creates a number to decide what a player will encounter based on chance programmed in
            if (encounter == 7): #creates a travel encounter with a 14% chance of happening
                self.showTravel()
                self.getTravelSeeds()
                self.showTravelOptions()
                self.showTravelOutcome()
            elif(encounter == 2 or encounter == 5): #creates a meditation encounter for player with 28% chance of happening
                self.showMeditation()
                self.getMedRewards()
                self.showMeditationOptions()
                self.showMeditationOutcome()
            else: #creates a villain encounter for the player with a 57% chance of this
                self.showVillain()
                self.getVilTreasureItem()
                self.showFightActionOptions()
                self.showFightActionOutcome()
        if (self.adventurer.getSeeds() > 0): #sees if player has collected any seeds
            print("You have sucessfully survived travel through the galaxy!", self.adventurer,
              "Greez is very happy to have new seeds in his terrarium!")
        else: #option if player decides to skip all chances to collect seeds 
            print("You have sucessfully survived travel through the galaxy!", self.adventurer,
              "Greez is annoyed by your failure to collect new seeds for his terrarium. Better luck next time!")
        
    def promptMove(self): #prompts player to continue the game and increments count
        input("Hit the Enter key to make a move!")
        self.adventurer.moveStep()
        
    def showVillain(self): #chooses a random villain for the player to encounter and presents them to the player.
        self.currentVillain = random.choice(AdventureGame.villainList)
        print("You have encountered", self.currentVillain)
        print()
        
    def getVilTreasureItem(self):#randomly creates the number of seeds a player could collect
        self.treasureItemWorth = random.randint(1,self.currentVillain.getDmg())
        
    def showFightActionOptions(self):
        while True:#waits for player to decide if they want to attack or avoid the villain
            self.adventurerFightAction = int(input("Do you want to (1) attack or (2) avoid? "))
            print()
            if(self.adventurerFightAction == 1 or self.adventurerFightAction ==2):
                break
    
    def showFightActionOutcome(self): 
        if (self.adventurerFightAction == 1):#shows player that the beat the villain they were attacking
            dmgPoints = random.randint(5, self.currentVillain.getDmg())
            self.adventurer.subHealthPoints(dmgPoints) #removes points from player's health
            self.adventurer.addSeeds(self.treasureItemWorth) #adds seeds to player's inventory
            
            print("You beat", self.currentVillain.getName(), "who did", str(dmgPoints),
                  "points of damage to your health, but you collected", str(self.treasureItemWorth), "seeds!") #shows results of encounter
        
        else:
            print("You succesfully avoided", self.currentVillain.getName(), "but didn't manage to pick up any seeds for Greez.")
            
        print()
        print("Your current health is", str(self.adventurer.getHealth()))
    
    def showMeditation(self): #Presents player with the current encounter
        print("You have found a safe spot for meditating on", self.currentPlanet)
        print()
        
    def getMedRewards(self): #randomly decides the health and seeds a player could gain
        self.treasureItemWorth = random.randint(0,6)
        self.healPoints = random.randint(1,50)
        
    def showMeditationOptions(self):
        while True: #waits for player to decide to meditate or continue
            self.adventurerMeditationAction = int(input("Would you like to (1) stop and meditate or (2) continue on your journey? "))
            print()
            if(self.adventurerMeditationAction == 1 or self.adventurerMeditationAction == 2):
                break
        
    def showMeditationOutcome(self):
        if(self.adventurerMeditationAction == 1):
            self.adventurer.addSeeds(self.treasureItemWorth) #adds seeds to player's inventory
            self.adventurer.addHealthPoints(self.healPoints) #heals player's health
            
            print("You stopped to meditate on", self.currentPlanet, "which healed you", str(self.healPoints), "health points and you managed to find",
                  str(self.treasureItemWorth), "seeds while getting up from meditating.\n") #shows player the results of the encounter
            print("Your current health is", str(self.adventurer.getHealth()))
        else:
            print("You continue on your journey through", self.currentPlanet +".")
        print()
        
    def showTravel(self):
        self.newPlanet = random.choice(AdventureGame.travelList) #randomly decides a planet the player could travel to
        if(self.currentPlanet == self.newPlanet): #ensures the new planet being traveled to is not the same as the current planet
            while(self.currentPlanet == self.newPlanet):
                self.newPlanet = random.choice(AdventureGame.travelList)
        self.proposer = random.randint(1,3) #randomly decides which character proposes you travel to a new planet
        if self.proposer == 1:
            print("Cere proposes that you and the Mantis crew should travel to", self.newPlanet, "to look for seeds.")
        else:
            print("Greez proposes that you and the Mantis crew should travel to", self.newPlanet, "to look for seeds.")
        print()
    
    def getTravelSeeds(self):
        self.treasureItemWorth = random.randint(1,10) #randomly determines number of seeds player could collect
    
    def showTravelOptions(self):
        while True: #waits for player to decide if they would like to travel to the new planet or not
            self.adventurerTravelAction = int(input("Would you like to (1) travel to the new planet or (2) stay on the current planet? "))
            print()
            if(self.adventurerTravelAction == 1 or self.adventurerTravelAction == 2):
                break
    
    def showTravelOutcome(self):
        if(self.adventurerTravelAction == 1):
            self.adventurer.addSeeds(self.treasureItemWorth) #adds seeds to player's inventory
            #shows outcome of travelling to a new planet
            print("You decide that you want to leave", self.currentPlanet, "and that you will head to", self.newPlanet, "instead.",
                  "Upon landing on", self.newPlanet, "you find", str(self.treasureItemWorth), "seeds near your landing site!") 
            self.currentPlanet = self.newPlanet
        else:
            print("You decide to stay on", self.currentPlanet, "to continue looking for seeds.") #shows outcome of not leaving the planet
        print()
        