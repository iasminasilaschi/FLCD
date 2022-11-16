https://github.com/iasminasilaschi/FLCD.git

# Scanner

#### init(self):
__Description:__ The constructor for the Scanner calls the populate_tables() function in order to set up the necessary information.  
__Input:__ none  
__Output:__ none

#### populate_tables(self):
__Description:__ This method reads the token.in file and stores the data of all the possible characters, digits, separators, operators and reserved keywords of the language.  
__Input:__ none  
__Output:__ none

#### scan(self, program):
__Description:__ The scan method opens the file where the program is written, reads it line by line, tokenizes each line, retains in a list all the tokens and in case a part is a symbol, also retains its line and position. If there is a lexical error, an exception is thrown and the line where it occurred is stored in an array of errors.  
__Input:__ program: the path to a program (ex: p1, p1-err, p2, p3)   
__Output:__ writes the output to the PIF.out and ST.out  

#### tokenize(self, line):
__Description:__ It separates the parts of the line by splitting for each separator and operator found.  
__Input:__ a line of the program  
__Output:__ a list of tokens

#### valid_symbol(self, part):
__Description:__ Checks to see if the given part is a valid symbol: does not have any not allowed characters (case in which an exception is thrown) and does not start with a digit.  
__Input:__ string, the part we want to check if it is a symbol  
__Output:__ true if it is a valid symbol, false if it is a number  
__Throws:__ throws an exception if there is a character that is not in the token.in file (not allowed)