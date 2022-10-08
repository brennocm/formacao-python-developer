len("Python") #Interagindo com o tipo string
len([10, 20, 30]) #Interagindo com o tipo int

class Passaro:
    def voar(self): pass
    
class Pardal(Passaro):
    def voar(self):
        print("Pardal voa!")
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa!")

def plano_de_voo(passaro):
    passaro.voar()
    
plano_de_voo(Pardal())
plano_de_voo(Avestruz())
    