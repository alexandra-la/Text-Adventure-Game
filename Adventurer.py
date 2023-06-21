class Adventurer:
    #variables for the class
    def __init__(self, adventurer_name = "Cal Kestis" , health_points = 100, adventurer_position = 0):
        
        self.name = adventurer_name #holds name of character
        self.position = adventurer_position #holds position of character
        self.health = health_points #holds health of character
        self.seeds = 0
        
    def __str__(self):
        #Lets player know how many health points you have and how many seeds you have collected
        ret = self.name + " has "+ str(self.health) + " health points and has collected "+ str(self.seeds) + " seeds."
        return ret
    
    def addSeeds(self, new_seeds):
        #adds seeds/treasure item to the current count
        self.seeds += new_seeds
        
    def subHealthPoints(self, dmg):
        #subtracts health points from the player's health
        self.health = self.health - dmg
        
        if (self.health < 0):
            self.health = 0
    
    def addHealthPoints(self, heal):
        #add health points to the player's health
        self.health += heal
        #prevents the player's health from exceeding 100
        if(self.health > 100):
            self.health = 100
    
    def isAlive(self):
        #checks if the player is currently alive
        if (self.health > 0):
            return True
        else:
            return False
    
    def moveStep(self):
        #Increments the player's position
        self.position += 1
    
    def getName(self):
        #returns the character's name
        return self.name
    
    def getPos(self):
        #returns player's position
        return self.position
    
    def getHealth(self):
        #returns player's health
        return self.health
    
    def getSeeds(self):
        #returns the current number of seeds a player has collected/
        return self.seeds
    
    