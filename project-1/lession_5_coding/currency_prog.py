import sys
from locale import currency

'''  
class Currency_converter:
    def __init__(self, a: str, b: str, c: float):
        self.a = a
        self.b = b
        self.c = c

    def test_convert(self) -> float:
        result= "not able to change"
        if self.a == "EUR" and self.b == 'USD':
            result=  self.c - 1
        return result

currency_converter1 = Currency_converter("EUR","USD",100)
changed=currency_converter1.test_convert()

print(changed)
'''

###--------------------------------------------------
class Currency_converter:
    def __init__(self):
        self.rates = {"EURUSD": 0.9, "USDEUR": 0.9, "SYRUSD": 0.5}




    def conversion(self,input_from,input_to,mount) -> float:
        result= "not able to change, you have to add string"
        #if a != type(str) and b != type(str) :
        if not isinstance(input_from, str) and not isinstance(input_to, str) and not isinstance(mount, float):
            #result= "not able to change, you have to add string"
            return result
        else:
            together_string = input_from + input_to
            #self.rates[together_string] = self.rates[together_string]
            if not together_string in self.rates:
                result = "we dont can change"
            else:
                result = self.rates[together_string] * mount

        return result


currency_converter1 = Currency_converter()
changed=currency_converter1.conversion("EUR","USD",100)
changed2=currency_converter1.conversion("USD","EUR",900)
changed3=currency_converter1.conversion("SYR","EUR",900)

#changed=currency_converter1.conversion(11,"USD",100)
print(changed)
print(changed2)
print(changed3)
#print()
#print(type("EUR"))



'''
x= True
while x:
    print("giv q to exit")
    input1= input("enter the init")
    if input1 == "q":
        sys.exit(0)
    input2 = input("enter another init")
    if input2 == "q":
        sys.exit(0)
    input3 = input("enter the mount")
    if input3 == "q":
        sys.exit(0)
    currency_converter2 = Currency_converter()
    print(currency_converter2.conversion(input1,input2,input3))
'''