import random

number = random.randint(1,100)

#initializing some values 
attempts = 0
totalWons = 0
totallosts = 0



while attempts != number:
     attempts = int(input("Enter Guess: "))

     if(attempts==number):
         print("Guess is correct and it is = ")
         print(attempts)

         totalWons +=1
         print("Total Wons= ")
         print(totalWons)

         print("Total Loss= ")
         print(totallosts)

     elif(attempts>number):
         print("Guess is high!")
          
         totallosts+=1
         print("Total Loss= ")
         print(totallosts)

         print("Total Wons= ")
         print(totalWons)

     else:
         print("Guess is low!")   

         totallosts+=1
         print("Total Loss= ")
         print(totallosts)  

         print("Total Wons= ")
         print(totalWons)

    

      

              


    
     
