class Agent:
    def __init__(self,code_name:str,clearance_level:int):
        self.code_name=code_name
        self.clearance_level=clearance_level
    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.clearance_level}")
    def getters(self):
        return self.clearance_level
    def setter(self,value):
        if 0<self.clearance_level<10:
            self.clearance_level=value

agent1=Agent("dani",1)

agent1.setter(8)
agent1.report()


class Mission:
    def __init__(self, mission_name:str, target_location:str,assigned_agent:Agent):
        self.mission_name=mission_name
        self.target_location=target_location
        self.assigned_agent=assigned_agent
    def brief(self):
        print(f"Mission:{self.mission_name},Targel:{self.target_location},Agent:{self.assigned_agent.code_name}")
mission=Mission("holp","isrel",agent1)   
print(mission.brief())     

class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level , region:str):
        super().__init__(code_name, clearance_level)
        self.region=region
        
    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.clearance_level},region {self.region}")

fieldAgent=FieldAgent("gold",5,"north")
print(fieldAgent.report())

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level,hacking):
        super().__init__(code_name, clearance_level)
        self.hacking=hacking
    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self.clearance_level},hacking{self.hacking}") 

def agent():
    agent_list=[Agent("dani",2),FieldAgent("yossi",4,"hife"),CyberAgent("avi",8,"boom")] 
    for i in agent_list:
        obj = i
        obj.report()

agent()