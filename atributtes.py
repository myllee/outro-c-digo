class Attribute:
    def __init__(self):
        self.streng = int
        self.dexte = int
        self.consti = int
        self.wisd = int
        self.intell= int
        self.char = int

    @property
    def streng(self) :
        return self.streng
    
    @streng.setter
    def streng(self, streng):
        self.streng = streng

    @property
    def dexte(self) :
        return self.dexte
    
    @dexte.setter
    def dexte(self,dexte):
        self.dexte = dexte

    @property
    def consti(self) :
        return self.consti
    
    @consti.setter
    def consti(self,consti):
        self.consti = consti

    @property
    def wisd(self) :
        return self.wisd
    
    @wisd.setter
    def wisdom(self,wisd):
        self.wisd = wisd

    @property
    def intell(self) :
        return self.intell
    
    @intell.setter
    def intell(self,intell):
        self.intell = intell

    @property
    def char(self) :
        return self.char
    
    @char.setter
    def char(self, char):
        self.char = char

    def define_streng(self,streng):
        self.strength = streng
        
        if streng == 0:
            return f"Nível de Força igual a {streng}: Incorpório"
        elif streng >= 1 and streng <= 5 :
            return f"Nível de Força igual a {streng}: Incapaz"
        elif streng >=6 and streng <=9:
            return f"Nível de Força igual a {streng}: Fraco"
        elif streng >=10 and streng <=11:
            return f"Nível de Força igual a {streng}: Medino"
        elif streng >=12 and streng <=15:
            return f"Nível de Força igual a {streng}: Forte"
        elif streng >=16 and streng <=20:
            return f"Nível de Força igual a {streng}: Super poderoso"
        else:
            return f"Nível de Força igual a {streng}: Inbatível"

    def define_dexte(self, dexte):
        self.dexte = dexte
        
        if dexte ==0:
            return f"Nível de Destreza igual a {dexte}: Desacordado"
        elif dexte >=1 and dexte <=5:
            return f"Nível de Destreza igual a {dexte}: Abatido"
        elif dexte >=6 and dexte <=9:
            return f"Nível de Destreza igual a {dexte}: Desajeitado"
        elif dexte >=10 and dexte <=11:
            return f"Nível de Destreza igual a {dexte}: Regular"
        elif dexte >=12 and dexte <=15:
            return f"Nível de Destreza igual a {dexte}: Ágil"
        elif dexte >=16 and dexte <=20:
            return f"Nível de Destreza igual a {dexte}: Ninja"
        else:
            return f"Nível de Destreza igual a {dexte}: Inperceptível"
    
    def define_consti(self,consti):
        self.consti = consti
        
        if consti ==0:
            return f"Nível de Costituição igual a {consti}: Espectro"
        elif consti >=1 and consti <=5:
            return f"Nível de Costituição igual a {consti}: Enfermo"
        elif consti >=6 and consti <=9:
            return f"Nível de Costituição igual a {consti}: Frági"
        elif consti >=10 and consti <=11:
            return f"Nível de Costituição igual a {consti}: Saudável"
        elif consti >=12 and consti <=15:
            return f"Nível de Costituição igual a {consti}: Durão"
        elif consti >=16 and consti <=20:
            return f"Nível de Costituição igual a {consti}: Super resistênte"
        else:
            return f"Nível de Costituição igual a {consti}: Imortal"
    
    def definition_wisd(self,wisd):
        self.wisd = wisd
    
        if wisd ==0:
            return f"Nível de Sabedoria igual a {wisd}: Inconscinte"
        elif wisd >=1 and wisd <=5:
            return f"Nível de Sabedoria igual a {wisd}: Irracional"
        elif wisd >=6 and wisd <=9:
            return f"Nível de Sabedoria igual a {wisd}: Desatento"
        elif wisd >=10 and wisd <=11:
            return f"Nível de Sabedoria igual a {wisd}: Simples"
        elif wisd >=12 and wisd <=15:
            return f"Nível de Sabedoria igual a {wisd}: Perspcaz"
        elif wisd >=16 and wisd <=20:
            return f"Nível de Sabedoria igual a {wisd}: Filósofo"
        else:
            return f"Nível de Sabedoria igual a {wisd}: Iluminado"

    def define_intell(self,intell):
        self.intell = intell
        
        if intell ==0:
            return f"Nível de Inteligencia igual a {intell}: Inanimado"
        elif intell >=1 and intell <=5:
            return f"Nível de Inteligencia igual a {intell}: Incivilizado"
        elif intell >=6 and intell <=9:
            return f"Nível de Inteligencia igual a {intell}: Parvo"
        elif intell >=10 and intell <=11:
            return f"Nível de Inteligencia igual a {intell}: Medíocre"
        elif intell >=12 and intell <=15:
            return f"Nível de Inteligencia igual a {intell}: Estuado"
        elif intell >=16 and intell <=20:
            return f"Nível de Inteligencia igual a {intell}: Gênio"
        else:
            return f"Nível de Intelicencia igual a {intell}: Onisciente"

    def define_char(self,char):
        self.char = char
        
        if char ==0:
            return f"Nível de Carisma igual a {char}: Aberração:"
        elif char >=1 and char <=5:
            return f"Nível de Carisma igual a {char}: Inexprecivo"
        elif char >=6 and char <=9:
            return f"Nível de Carisma igual a {char}: Rude"
        elif char >=10 and char <=11:
            return f"Nível de Carisma igual a {char}: Socíavel"
        elif char >=12 and char <=15:
            return f"Nível de Carisma igual a {char}: Persuasivo"
        elif char >=16 and char <=20:
            return f"Nível de Carisma igual a {char}: Influente"
        else:
            return f"Nível de Carisma igual a {char}: Ídolo"