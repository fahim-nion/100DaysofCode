import time

# initial = time.time()
# # print(initial)
# k= 0

# while (k<=99):
#     print("Hi")
#     k+=1
# print(f"While loop took {time.time()-initial}")

# initial2= time.time()

# for i in range(100):
#     print("I am for loop")
# print(f"For loop took {time.time()-initial2}")


localTime = time.asctime(time.localtime(time.time()))
print(localTime)

for i in range(5):
    print("Hello Fahim!")
    time.sleep(2)