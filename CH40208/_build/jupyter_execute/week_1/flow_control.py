# Flow control

**First, run the cell below and watch the video lecture associated with this topic.**

from IPython.display import YouTubeVideo

YouTubeVideo('qZxhnHJxF08', width=560, height=315)

In order to make your code "intelligent" it is important that the code can make "decisions". 
This is achieved through a broad tool known as *flow control*, where different keywords are used to control the flow fo the program depending on certain values. 

The `if` statement is one of the simplest, and most powerful, operations that Python can perform.  
It allows the code to apply different operations *if* certain conditions are met. 
An example of a Pythonic *if statement* is shown below. 

# the if operator

highest_occupied_molecular_orbital = 's'

if highest_occupied_molecular_orbital == 's':
    print('Group 1 or 2')

In the Python language, the whitespace/indentation following the `:` is extremely important, it indicates what **is** and what **is not** part of the if statement. 
We will see more of this whitespace in other examples. 
The above codes askes the question, "does the variable `highest_occupied_molecular_orbital` have a value `'s'` ? If it does, print the string `'Group 1 or 2'`".

The `if` statement may be used in a more extended context, such as if the *logical arguement* in the if statement is not `True`, then `else` can be included (or even `elif`), as is shown below. 

# the other orbitals

if highest_occupied_molecular_orbital == 's':
    print('Group 1 or 2')
elif highest_occupied_molecular_orbital == 'p':
    print('Group 13 to 17')
elif highest_occupied_molecular_orbital == 'd':
    print('Transition metal')
elif highest_occupied_molecular_orbital == 'f':
    print('Lanthanide or actinide')
else:
    print('We only accept experimentally measured elements')

In the above code, the following sequence of questions is considered:

- Does `highest_occupied_molecular_orbital` have the value `'s'`? If yes print `'Group 1 or 2'` else go to the next step.
- Does `highest_occupied_molecular_orbital` have the value `'p'`? If yes print `'Group 13 or 17'` else go to the next step.
- Does `highest_occupied_molecular_orbital` have the value `'d'`? If yes print `'Transition metal'` else go to the next step.
- Does `highest_occupied_molecular_orbital` have the value `'f'`? If yes print `'Lanthanide or actinide'` else go to the next step.
- You have exhausted the discovered ground state orbitals (and probably your own patience!), print some explaination. 