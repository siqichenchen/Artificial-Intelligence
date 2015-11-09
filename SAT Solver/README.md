# Artificial-Intelligence



SAT-solver
In this problem you need to build a boolean satisfiability solver that takes a set of variables and connectives in CNF and returns either a satisfying assignment that would make the CNF sentence true or determines that no satisfying assignment is possible. In particular, we are asking you to create a program, DPLL.py , which would implement the DPLL algorithm.
Input & Output format:
The input to the program would be a file consisting propositional sentences in CNF format represented in lists as explained in Section 2. Input file “CNF_sentences.txt” is provided. The number n in the first line indicates the number of input propositional sentences in the file. The next n lines contain one propositional sentence in CNF format per line. You can assume that the variables are one character strings i.e. “A”, “B”...”Z”.

The command to run your program would be in the following format:
python DPLL.py –i inputfilename
The output of the program should be a file, named “CNF_satisfiability.txt”, containing n lines each containing a python list, where n is the number of

