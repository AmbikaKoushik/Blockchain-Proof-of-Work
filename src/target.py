def target(difficulty, target): #define Target Generation function
       t = format(pow(2, (256 - int(difficulty)))-1,'0256b')
       print('Target:'+'   '+str(t)) #Printing the Target to command prompt
       f = open(target,'w') #Opening the target.txt file in write mode
       f.write(t) #Writing the Target
       f.close() #Closing the target.txt file
        
