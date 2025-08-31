Note : This challenge was part of El-djazairCTF (May 2025)

No writeups , let's fix that !

## Intro
During this CTF , I was unable to solve this challenge so I decided to try to solve it again.

## Steps
1. This is an ELF , try to run it , the program expects an input.

2. Using ghidra , I was able to go to the main function and find this :
   
   <img width="511" height="347" alt="1" src="https://github.com/user-attachments/assets/16d5fe19-39bd-4325-a2e1-cbdc00d337f2" />
   
   - I find that the result of the  maze function ( that I renamed ) need to be != 0 , so I tried to invert the branch using JNZ but I find again that the input is used as parameter in the
     flag function ( a function that decrypts the flag using the input ),so understanding the logic of maze function is a must.
     
4. Decompiling the maze function :
   
   <img width="335" height="261" alt="2" src="https://github.com/user-attachments/assets/e0471e56-3be6-4f42-aa3e-408da0a1df22" />

   - We can see that the initial values of variables are (3,0) and the maze function returns a value !=0 only if (3,0) became (4,7).
   
   - Using LLM
     1.  I found that the variable called DATA... is the maze :
     
     <img width="180" height="467" alt="kali-2025-08-31-12-52-19" src="https://github.com/user-attachments/assets/f0de8083-4c8a-4ca2-89c8-80bff57eb58d" />

     2. To get the right input ( the 32-bits decimal value that represents 16 * 2bits , and each 2 bits represent a mouvement (right,up,down,left) we must write a pathfinding algorithm to go from (3,0) to (7,4).
     
     3. Record the moves when writing the path and then encode the 16 moves to a 32 bits decimal value that represent our input !

5. Running the exploit and the program :
   
   <img width="888" height="87" alt="3" src="https://github.com/user-attachments/assets/5bba3540-f566-4308-962c-d2f745ed04f7" />

   <img width="589" height="455" alt="4" src="https://github.com/user-attachments/assets/64f8e639-56b7-4362-9e39-ac92a09dcde1" />

## FLAG : El-DjazairCTF{backtracking_b_3iniya_:p}


   

 
