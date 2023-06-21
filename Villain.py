class Villain:
    def __init__(self, villain_name, villain_introduction, villain_max_dmg):
        
        self.name = villain_name #variable for villain name
        
        self.introduction = villain_introduction #variable for introduction of the villain
        
        self.maxDmg = villain_max_dmg #max damage a villain can do to you
    
    #presents the villain when printing an object
    def __str__(self):
        
        ret = self.name
        ret += ". "
        ret += self.introduction
        return ret
    #return the name of the villain
    def getName(self):
        return self.name
    #return max damage a villain can do
    def getDmg(self):
        return self.maxDmg