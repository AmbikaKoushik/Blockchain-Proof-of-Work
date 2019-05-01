def verify(inputtxt, targettxt, solution): #define Verify function
        from Crypto.Hash import SHA256
        f1 = open (inputtxt,'r') #Opening the inputtxt.txt file in read mode
        message = f1.read().strip('\n') #Reading the message
        f1.close() #Closing the inputtxt.txt file
        m = str.encode(message)

        f2 = open (targettxt,'r') #Opening the targettxt.txt file in read mode
        target = f2.read().strip('\n') #Reading the target
        f2.close() #Closing the targettxt.txt file
        t = int(target,2)

        f3 = open (solution,'r') #Opening the targettxt.txt file in read mode
        solution = int(f3.read().strip('\n')) #Reading the proposed solution
        f3.close() #Closing the targettxt.txt file
        s = solution.to_bytes(int((len(bin(solution))-1)/8) + 1, byteorder='big')
        
        h = SHA256.new()
        h.update(m + s)
        if (int(h.hexdigest(),16) <= t): #Check if the proposed solution is correct
                print('Valid')
        else:
                print('Invalid')
