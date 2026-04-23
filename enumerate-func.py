ll = ["Bhindi", "Alu", "ChopSticks","Chowmein"]

# i = 1
# for item in ll:
#     if i%2!= 0:
#         print(f"Please buy this {item}")
#     i+=1


for idx, item in enumerate(ll):
    if idx%2 == 0:
        print(f"Please buy this {item}")
        