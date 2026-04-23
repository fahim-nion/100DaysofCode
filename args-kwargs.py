def names(*args, **kwargs):
    # print(args[0])
    # for i in args:
    #     print(i)
    print("Meet me and my wife:")
    for k,v in kwargs.items():
        print(k)
    
    

boys = ["Harry","Hammad","Rohan","Fahim","Nion","Morshed","Al-Hassan","Taju"]

kw = {
    "Nion": "Boy",
    "Taju" : "Girl"
}
names(*boys,**kw)  #ekahane asteric na dile pura list tai print hoto

#firstly normal argument er por args er por kwargs pathate hoy
