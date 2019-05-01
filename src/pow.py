from target import target #importing Target Generation module
from sol import sol #importing Solution module
from verify import verify #importing verify module
from performance import performance #importing performance module




if __name__ == '__main__': #calling main function
        import sys #importing sys module
        import os #importing os module
        #First argument i.e sys.argv[0] is always aes.py
        #Second argument i.e sys.argv[1] is the called function
        #Comparing the second command line argument with respective functions to call
        if sys.argv[1] == 'target': #Comparing with target
                target(sys.argv[2], sys.argv[3]) #Calling target function
        elif sys.argv[1] == 'sol': #Comparing with sol
                sol(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling sol function
        elif sys.argv[1] == 'verify': #Comparing with verify
                verify(sys.argv[2], sys.argv[3], sys.argv[4]) #Calling verify function
        elif sys.argv[1] == 'performance': #Comparing with performance
                performance(sys.argv[2]) #Calling performance function
        
