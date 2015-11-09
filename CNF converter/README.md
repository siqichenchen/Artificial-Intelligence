# Artificial-Intelligence

1 CNF-converter:
To create a SAT solver, your input has to be in CNF. In this problem, you have to create a program, CNFconverter.py, which would convert any propositional logic sentence into its equivalent CNF sentence.
Input & Output format:
The input to the program would be a file consisting propositional sentences represented in lists as explained in Section 2. Input file “sentences.txt” is provided. The number n in the first line indicates the number of input propositional sentences in the file. The next n lines contain one propositional sentence per line. You can assume that the variables are one character strings i.e. “A”, “B”...”Z”.

The command to run your program would be in the following format:
python CNFconverter.py –i inputfilename
The output of the program would be the CNF sentences equivalent to the input propositional sentence. The output should be in the same format as described in Section 2, i.e. the list representation. The output file must be named “sentences_CNF.txt” containing the n lines where each line contains the equivalent CNF sentence for each input propositional sentence provided in the input file. Make sure that the output of your program can be converted into a nested list using the eval function as described in Section 2.

