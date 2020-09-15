# Proof-Bot

This is a (currently text based) program that takes as input a statement to prove in the form of quantifiers and equations. The following are valid examples.
```
Ax, x = x
Ex, x <= 2
Ax Ey, x = y + 2 
```
The program determines the best method of proof (Direct, Contrapositive, Contradiction, Induction) and prints the procedure it takes to reach its conclusion.
If the proposition is false, it will give a counterexample.
