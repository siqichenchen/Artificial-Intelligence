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


Bayes Disease Judger:

Bayesian Networks, also called Belief or Causal Networks, are a part of probability theory and are important for reasoning in AI. They are a powerful tool for modeling decision-making under uncertainty. In this assignment you will implement code for computing inferences in Bayesian networks of discrete random variables.
You are a newly hired AI specialist at a large urban hospital. The hospital management has heard about the recent advances in AI technology and would like to see if it could be used in context of the hospital. In particular, management is interested in seeing AI approaches could be used to help doctors make more correct diagnoses.
The hospital already has a fairly extensive electronic medical record system, and they know for various diseases, what the priori probability of the diseases, P(D). In addition, they have also been able to determine the probability of various lab results, given one of the particular diseases P(F | D). You can assume that these probabilities are conditionally independent. The lab results, also called Findings, are binary random variables, that is, they are either present(true) or absent(false). Because some of the lab results are very expensive and others take a while to run, not all patients have all results available.

Symptoms are similar to findings, but they are things that a patient would report (such as “sore throat”) rather than something that is determined by lab results (such as “hypokalemia”). Here, we treat findings and symptoms interchangeably.
Your job is to write a program that will accept as input the priori probabilities of a set of diseases and the conditional probability of a symptom (or finding) given each of the diseases.
2. Input:
The input file will contain the probabilities and inputs for Bayesian networks similar to shown in Figure 1. All the diseases have findings and symptoms attached with them. You can assume that the findings and symptoms for all the diseases are distinct.
The first line in the input file will have two numbers (n and k) separated by a white space specifying the number of diseases and number of patients respectively. Next 4*n lines will have the details about the diseases and their findings/symptoms, 4 lines for each disease. The first line for each disease will contain the name of the disease (Cancer, Hepatitis, etc), its number of findings/symptoms (m) and the priori probability of the disease P(D), all separated by a white space. The second line will contain a python list of m finding/symptom names for the disease. You can assume that these names are distinct. The third line will contain a python list of m elements giving the probability of the findings/symptoms to be present (true) if the disease is present. The forth line will contain a python list of m elements giving the probability of the findings/symptoms to be present(true) if the disease is not present.
The next n*k lines will have the inputs for various patients. For each patient, we have n lines representing the status of the findings for each disease. Each line will contain the value of the available findings/symptoms for a disease, represented as a python list of values. The values can be T, F or U where T means that the finding for the patient is present(true), F means that the finding for the patient is absent(false) and U means that the finding for the patient is not available. You can assume that the values in this list correspond to the order of the findings listed in the disease description.
Example input:

Explanation of the example:
 diabetes has 3 findings/symptoms: thirst, weightloss, blurredvision
 P(thirst | diabetes) = 0.6, P(weightloss | ¬diabetes) = 0.3
 There are inputs for 2 patients
 First patient has thirst, doesn’t have weightloss and we don’t know about the blurredvision
Notes:
 You can assume that the input file is without any error i.e. all the inputs provided are in the correct format.
 For each patient, for each disease, we have at least one test result available, either true of false.

 Like the previous assignment, you can use eval function of python to read the inputs which are in the list.
 In the final testing inputs, there will be at most 10 diseases and at most 10 findings/symptoms per disease.
 The command line for the program will be:
python bayes.py –i inputfilename
3. Output:
Your output file will contain the answers for the following questions for each patient. Your output should start with the patient number, for e.g. “Patient-1:” (start with 1). You should have 3 lines per patient. Each line is the answer to one of the questions below. If the input file name is “abc.txt” then the output file name for that input file must be “abc_inference.txt”.
Question-1:
For each of the diseases, what is the probability that the patient has the disease? Note that a patient could have more than one disease at a time, so the probabilities of the diseases will not necessarily sum to 1. Also, because some of the lab tests are expensive, not all the patients will have all the lab results available, but your program should still produce correct results. The output will be a python dictionary with the name of the diseases as keys and a number specifying the probability of the patient having that disease as value.
 Present the values with 4 digit precision
 As you know, python dictionaries have no order. So output order of the elements is not fixed.

Question-2:
If not all the test results are available for a particular disease for a patient, your program should search the values for the unknown tests that would produce the maximum and minimum probabilities for each disease. This information could be used to help guide the patient, doctor (and insurance company) in deciding whether or not further tests are needed. The output will be a python dictionary with name of the diseases as keys and a list of 2 elements specifying the minimum and maximum probabilities for that disease as the value.
 These probabilities will be the same as Q-1 for diseases for which all the test results are available.
 Present the values with 4 digit precision.
Question-3:
In the case that there are undetermined lab values, to help the doctor decide which test to run next, the program should figure out which of the tests not done yet for each disease (result either true or false) would produce the biggest increase and which would produce the biggest decrease in the probabilities for that diseases. Your program should output a python dictionary with name of the diseases as keys and list of 4 elements as values. The first element in the list would produce the biggest increase in the probability of the disease. The second element is the value of the first element. The third element would result in the biggest decrease in the probability for the disease. And the forth element is the value of the third element.
 In case of ties, report the finding that comes earlier in the alphabetical order.

 If no findings would increase or decrease the probability of the disease or if all the findings for the disease are already available, report “none” as 1st and 3rd elements and ‘N’ as 2nd and 4th elements.
Example output:

Explanation of the example:
 The first patient has the chickenpox with the probability of 0.3580 and diabetes with the probability of 0.1612.
 If all the unknown symptoms were known in a way that minimized the probability of chickenpox, the minimum probability of the first patient having chickenpox will reduce to 0.0850 and correspondingly if all the unknowns were known with values that maximized the disease probability, the maximum probability will be 0.9213.
 In case of chickenpox for the first patient, sorethroat and cough are unknown. Having sorethroat = True, will produce the biggest increase in the probability that this patient has chickenpox (resulting in symptoms = [‘T’, ‘T’, ‘F’, ‘U’]). If we have cough = False, it will result in the biggest decrease in the probability of him having chickenpox (resulting in symptoms = [‘T’, ‘U’, ‘F’, ‘F’]).
