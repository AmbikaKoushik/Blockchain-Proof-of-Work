def sol(inputtxt, targettxt, solution): #define Solution Generation function
       from Crypto.Hash import SHA256
       f1 = open (inputtxt,'r') #Opening the inputtxt.txt file in read mode
       message = f1.read().strip('\n') #Reading the message
       f1.close() #Closing the inputtxt.txt file
       m = str.encode(message)

       f2 = open (targettxt,'r') #Opening the targettxt.txt file in read mode
       target = f2.read().strip('\n') #Reading the target
       f2.close() #Closing the targettxt.txt file
       t = int(target,2)

       s = 0
       while (1):
              s_bytes = s.to_bytes(int((len(bin(s))-1)/8) + 1, byteorder='big')
              h = SHA256.new() #Creating a new SHA256 object
              h.update(m + s_bytes) #Hashing the (message||solution)
              if (int(h.hexdigest(),16) <= t): #Comparing the Hash value with the Target
                     break
              s = s + 1
              
       print('Solution:'+'  '+ str(s)) #Printing the Solution to the command prompt
       f3 = open(solution,'w') #Opening the solution.txt file in write mode
       f3.write(str(s)) #Writing the solution
       f3.close() #Closing the solution.txt file
