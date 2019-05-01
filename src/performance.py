def performance(inputtxt): #define Performance for POW
   from target import target #importing Target Generation module
   from sol import sol #importing Solution module

   import time #Importing time module
   
   s = [0]*6 #Initializing an array of 6 integers for Solutions
   s_time = [0]*6 #Initializing an array of 6 integers for Solution Time
   
   for i in range(0,6): #Iterating the array
      sol_start = time.time() #Noting the Start time
      target(21+i, '../data/target.txt') #Calling target function
      sol(inputtxt, '../data/target.txt', '../data/solution.txt') #Calling sol function
      sol_end = time.time() #Noting the end time

      f3 = open ('../data/solution.txt','r') #Opening the solution.txt file in read mode
      s[i] = int(f3.read().strip('\n')) #storing the solution in the array
      f3.close()
      
      s_time[i] = sol_start - sol_end #Calculate the time elapsed for solution function

   for i in range(0,6):
      print('\nSolution'+str(i)+ ' is '+ str(s[i]))
      print('Time taken for S'+str(i)+ ' is '+ str(s_time[i])+' seconds')
