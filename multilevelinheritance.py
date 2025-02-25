class Dad:
    def __init__(self, amount):
        self.amount = amount
 
    def dadWallet(self):
        print(f"Wallet amount of Dad: {self.amount}")
 
    def emptyPocket(self):
        self.amount = 0
        print("Dad's pocket is now empty.")
 
class Son(Dad):
    def __init__(self, sonWallet, amount):
        super().__init__(amount)  
        self.sonWallet = sonWallet
 
    def theft(self):
        self.sonWallet += self.amount
        print(f"Son wallet after theft: {self.sonWallet}")
 
    def theftAmount(self):
        print(f"The Amount Stolen: {self.sonWallet}")
    
    def emptyPocket(self):
        self.amount = 0
        print("son's pocket is now empty.")

class Grandson(Son):
    def __init__(self, grandsonWallet,sonWallet,amount):
        super().__init__(sonWallet,amount)  
        self.grandsonWallet = grandsonWallet
 
    def theft(self):
        self.grandsonWallet += self.amount
        print(f"GrandSon wallet after theft: {self.grandsonWallet}")
 
    def theftAmount(self):
        print(f"The Amount Stolen: {self.grandsonWallet}")        
dada = Dad(10000)
dada.dadWallet()
s1 = Son(0, 5000)
s1.theft()
s1.theftAmount()
s1.emptyPocket()
s2=Grandson(0,5000,5000)
s2.theft()
s2.theftAmount()
dada.emptyPocket()
dada.dadWallet()
