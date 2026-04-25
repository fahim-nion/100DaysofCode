#multilevel inheritance


class Dad:
    basketball = 1


class Son(Dad):
    dance = 1
    
    def isDance(self):
        return f"yes i dance {self.dance} no. of times"


class GrandSon(Son):
    dance = 6
    
    # def isDance(self):
    #     return f"yes i dance very awesomely {self.dance} no. of times"



darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.isDance())
print(harry.basketball)