#MathDojo
#2018 09 19
#Cheung Anthony

# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# class MathDojo:
#     def __init__(self):
#         self.val=0
#     def add(self,valadd=''):
#         valaddstr=str(valadd)
#         if valaddstr.strip():
#             self.val=self.val + valadd   
#             return self          
#         if not valaddstr.strip():
#             print("blanky\n")
#             return self
#     def sub(self,valsub=''):
#         valsubstr=str(valsub)
#         if valsubstr.strip():
#             self.val=self.val - valsub 
#             return self          
#         if not valsubstr.strip():
#             print("blanky\n")
#             return self                
#     def result(self):        
#         print(str(self.val))
#         return self
# md=MathDojo().add(2).sub(1).result()

class Card:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def show(self):
        print("Value: ", self.value, "Type: ", self.type)
class Deck:
    def __init__(self, name):
        self.deck = []
        self.name = name
        for i in ["clubs", "diamonds", "hearts", "spades"]:
            for j in range(1,14):
                self.deck.append( Card(j, i ) )
    def show(self):
        print("\n", "*"*30, self.name, "*"*30)
        for card in self.deck:
            card.show()
d1 = Deck("First Deck")
d1.show()
d2 = Deck("Second Deck")
d2.show()