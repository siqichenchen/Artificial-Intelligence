# Artificial-Intelligence

1 CNF-converter:
To create a SAT solver, your input has to be in CNF. In this problem, you have to create a program, CNFconverter.py, which would convert any propositional logic sentence into its equivalent CNF sentence.
Input & Output format:
The input to the program would be a file consisting propositional sentences represented in lists as explained in Section 2. Input file “sentences.txt” is provided. The number n in the first line indicates the number of input propositional sentences in the file. The next n lines contain one propositional sentence per line. You can assume that the variables are one character strings i.e. “A”, “B”...”Z”.

The command to run your program would be in the following format:
python CNFconverter.py –i inputfilename
The output of the program would be the CNF sentences equivalent to the input propositional sentence. The output should be in the same format as described in Section 2, i.e. the list representation. The output file must be named “sentences_CNF.txt” containing the n lines where each line contains the equivalent CNF sentence for each input propositional sentence provided in the input file. Make sure that the output of your program can be converted into a nested list using the eval function as described in Section 2.

2 SAT-solver
In this problem you need to build a boolean satisfiability solver that takes a set of variables and connectives in CNF and returns either a satisfying assignment that would make the CNF sentence true or determines that no satisfying assignment is possible. In particular, we are asking you to create a program, DPLL.py , which would implement the DPLL algorithm.
Input & Output format:
The input to the program would be a file consisting propositional sentences in CNF format represented in lists as explained in Section 2. Input file “CNF_sentences.txt” is provided. The number n in the first line indicates the number of input propositional sentences in the file. The next n lines contain one propositional sentence in CNF format per line. You can assume that the variables are one character strings i.e. “A”, “B”...”Z”.

The command to run your program would be in the following format:
python DPLL.py –i inputfilename
The output of the program should be a file, named “CNF_satisfiability.txt”, containing n lines each containing a python list, where n is the number of

CNF sentences in the input file. The first element in the python list should be either true or false indicating the boolean satisfiability of that particular input sentence. If the first element is true then the list must contain m additional elements, where m is the number of variables in the input sentence. For each variable, the corresponding element in the list should indicate whether that variable is true or false to satisfy the boolean satisfiability of the input sentence as shown in the output format in Figure 4.
