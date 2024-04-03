class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.subrace = int

    @property
    def sub_race(self) :
        return self.subrace
    
    @sub_race.setter
    def strenght(self, subrace):
        self.subrace  = subrace

    def define_name(self, name_characteres):
        self.name = name_characteres
        return name_characteres 
    
    def define_race(self, race_characteres):
        self.race = race_characteres 
        return race_characteres
    
    def define_subrace(self,sub_race_characteres):
        self.subrace = sub_race_characteres
        return sub_race_characteres