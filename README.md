# Monty-Hall-Problem
Programming the Monty Hall Problem - probability theory

I originally saw the Monty Hall Problem explained on Youtube.
It took a while for me to grasp that there was a conundrum involving the probability of choosing between 3 possibilities which at first seemed to be an obvious no-brainer, but actually was a little more complicated than you might think.
The following link explains the conundrum.
https://www.linkedin.com/newsletters/the-uk-careers-fair-weekly-6965279854749437952/

My aim was to see if I could write a program to validate the theory based on probability.
I wrote the code in Python. For clarity, the comparison was made between 2 separate actions.
I wrote 2 separate programs. One of them performs a repeat process of the contestant sticking to their original choice. The other one performs a repeat process of the contestant always switching to the other choice option.

The conclusion: The results indicate a huge bias towards switching from the original choice to the alternative choice. The original choice always averaged out at 1/3 probability ie. 33%,  whereas the switched choice averaged 2/3 or 66%.

Explanation: At first glance, you might think that every door has an equal probability of 1/3. However, the game changes when the host eliminates 1 door. You see, the original pick could only ever be 1/3 chance of being correct. That means - 2/3 of probability lies (on average) with the other two doors. Now, if one of those doors gets eliminated, then the 2/3 probability must lie (on average) within the alternative (switch) case.

