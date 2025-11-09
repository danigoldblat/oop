class  Weapon:
    total_weapons=0
    def __init__(self,name:str,ammo:int):
        self.name=name
        self.ammo=ammo
        Weapon.total_weapons+=1
    def __str__(self):
        return f"{self.name} {self.ammo}"
weapon=Weapon("m16", 200)

class Soldier:
    def __init__(self,name:str,rank:str,weapon:Weapon):
        self.name=name
        self.rank=rank
        self.weapon=weapon

    def report(self):
        return f"Soldier {self.name}, rank {self.rank}, with weapon {self.weapon}"
soldier=Soldier("dani","commander",weapon)
soldier1=Soldier("avi","soldier",weapon)

class Unit:
    def __init__(self,unit_name:str,commander:Soldier,soldiers:list[Soldier],strike_opttion:StrikeOption):
        self.unit_name=unit_name
        self.commander=commander
        self.soldiers=soldiers
        self.strike_opttion=strike_opttion 
    def briefing(self):
        print(self.unit_name,self.commander.report(),self.strike_opttion.strike())
unit=Unit("golany",soldier,[soldier],)
unit.briefing()


class StrikeOption:
    def __init__(self,name:str,ammo:int):
        self.name=name
        self.ammo=ammo
    def strike(self):
        pass
class Tank(StrikeOption):
    def strike(self):
        print("The attack from the tank was carried out with a rescue")
        
class Drone(StrikeOption):
    def strike(self):
       print("The drone attack was carried out with a rescue")
strikeOption=Tank("marcve",20)
for _ in range(100):
    