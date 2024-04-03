import random
from atributtes import Attribute
from characteres import Character

attribute = Attribute()
name = input("VAMOS LÁ, GUERREIRO! ESCOLHA O NOME DO SEU PERSONAGEM: ")
print("ESTAS SÃO CLASSES DISPONIVEIS! ROLE O DADO E ESCOLHA APENAS UMA")
print("dwarf( ganhamos +2 em constituição)")
print("Elf( ganhamos +2 em destreza)")
print("Human( ganhamos +1 em todos os atributos)")
print("Barbaro( ganhamos +2 em destreza)")
print("Dragonborn( ganhamos +2 em força e +1 em carisma)")
print("Gnome( ganhamos +2 em inteligencia)")
print("tieling( ganhamos +1 em inteligencia e +2 em carisma)")
race = int(input("AGORA, ROLE O DADO E ESCOLHA A RAÇA DO SEU PERSONAGEM: "))
sub_races = int
character = Character(name, race)
stren = random.randint(1,21)
dexte = random.randint(1,21)
consti = random.randint(1,21)
wisd = random.randint(1,21)
intell = random.randint(1,21)
char = random.randint(1,21)
match race:
    case 1:
        consti +=2
        print("ROLE O DADO E ESCOLHA UMA SUBCLASSE")
        print(" (1) Anão da Colina(+1 de sabedoria)")
        print(" (2) Anão da Montanha(+2 de força)")
        sub_race = input("QUAL NUMÉRO CAIU?: ")
        if sub_races == 1:
            wisd +=1
        else:
            stren+=2
    case 2:
        dexte+=2
        print("ROLE NOVAMENTE")
        print(" (1) Alto Elfo(+1 de inteligencia)")
        print(" (2) Elfo da floresta(+1 de sabedoria)")
        sub_race = input("QUAL NÚMERO?: ")
        if sub_race == 1:
            intell +=1
        else:
            wisd+=1
    case 3:
        stren += 1 
        dexte += 1
        consti += 1
        wisd += 1
        intell += 1
        char += 1    
    case 4:
        dexte+=2
        print("ROLE O DADO NOVAMENTE")
        print(" (1) Pés leves(+1 em carisma)")
        print(" (2) Parrudos(+1 em constituição)")
        sub_race = input("QUAL NÚMERO TEMOS?: ")
        if sub_race == 1:
            char +=1
        else:
            consti+=1
    case 5:
        stren +=2
        char +=1
    case 6:
        intell+=2
        print("ROLE O DADO NOVAMENTE")
        print(" (1) Gnomo da Floresta(+1 em destreza)")
        print(" (2) Gnomo da Pedra(+1 em constituição)")
        sub_race = input("QUAL NÚMERO TEMOS?: ")
        if sub_race == 1:
            dexte +=1
        else:
            consti+=1
    case 7:
        intell+=1
        char+=2        
print("PARABÉNS GUERREIRO VOCÊ CHEGOU NO PRÓXIMO NÍVEL")
print("NAME: ",character.definition_name(name))
match race:
    case 1:
        race = "Dwarf"
        print("Classe: ",character.definition_race(race))
    case 2:
        race = "Elf"
        print("Classe: ",character.definition_race(race))
    case 3:
        race = "Human"
        print("Classe: ",character.definition_race(race))
    case 4:
        race = "Barbaro"
        print("Classe: ",character.definition_race(race))
    case 5:
        race = "Dragonborn"
        print("Classe: ",character.definition_race(race))
    case 6:
        race = "Gnome"
        print("Classe: ",character.definition_race(race))
    case 7:
        race = "tiegling"
        print("Classe: ",character.definition_race(race))
if race == "Anão" or race == "Elfo" or race == "Barbaro" or race =="Gnomo":
    print("Sub-Classe: ",character.definitios_sub_race(sub_race))
print(attribute.definition_strength(stren))
print(attribute.definition_dexterity(dexte))
print(attribute.definition_constitution(consti))
print(attribute.definition_wisdom(wisd))
print(attribute.definition_intelligence(intell))
print(attribute.definition_charisma(char))