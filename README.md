# AffirmChallenge

### Getting Started
Good code challenge for an Engineer.  

Feature file resides in ./features/Loans.feature  
Code resides in ./features/steps/loans.py  

### Challenge Questions & Answers

1. How long did you spend working on the problem? What did you find to be the most
difficult part?  **Spent approximately 5hrs, spent two hours trying to understand the calculations. Challenge for me is coding as its been awhile that I have spent full time coding.**  
2. How would you modify your data model or code to account for an eventual introduction
of new, as of yet unknown types of covenants, beyond just maximum default likelihood
and state restrictions?  **I would assume it's an additional rules that you can include in a function**  
3. How would you architect your solution as a production service wherein new facilities can
be introduced at arbitrary points in time. Assume these facilities become available by the
finance team emailing your team and describing the addition with a new set of CSVs.  
4. Your solution most likely simulates the streaming process by directly calling a method in
your code to process the loans inside of a for loop. What would a REST API look like for
this same service? Stakeholders using the API will need, at a minimum, to be able to
request a loan be assigned to a facility, and read the funding status of a loan, as well as
query the capacities remaining in facilities.  **Don't know the answer and would have to reach out to Sr. Devs**  
5. How might you improve your assignment algorithm if you were permitted to assign loans
in batch rather than streaming? We are not looking for code here, but pseudo code or
description of a revised algorithm appreciated.  **Don't know the answer and would have to reach out to Sr. Devs**  
6. Because a number of facilities share the same interest rate, it’s possible that there are a
number of equally appealing options by the algorithm we recommended you use
(assigning to the cheapest facility). How might you tiebreak facilities with equal interest
rates, with the goal being to maximize the likelihood that future loans streaming in will be
assignable to some facility?  **Don't know the answer and would have to reach out to Sr. Devs**  
