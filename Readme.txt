/usr/local/lib/python3.6/dist-packages/Crypto

﻿I am using the python language for this project. Since python is an interpreted language no compiler is needed to run the code.

Steps followed for the execution:

1. Install Python 3 using the below command
sudo apt-get install python3.6

2. Verifying the python version using the below command
python3 --version

3. By default when you call the 'python' keyword in Linux terminal python2 will be invoked. To open python3 with 'python' keyword use the below command:
cd ~
sudo gedit .bashrc

4. Add the below line at the end of the file
alias python=python3

5. save and close the file

6. Go to terminal and excute the below command:
source ~/.bashrc

7. Go to /pow_m12507845/build/pycrypto-master folder and execute the below commands to add PyCrypto library to your local

python setup.py build" to build the package
and "python setup.py install" to install it.


8. Go to Source folder: /pow_m12507845/src



9. Execute the below commands for respective functions :



a) For running the Target function, execute the below command:
python pow.py target d ../data/target.txt



b) For running the Solution function, execute the below command:
python pow.py sol ../data/input.txt ../data/target.txt ../data/solution.txt



c)For running the Verify function, execute the below command:
python pow.py verify ../data/input.txt ../data/target.txt ../data/solution.txt



d) For running the Performance function, execute the below command:
python pow.py performance ../data/input.txt
