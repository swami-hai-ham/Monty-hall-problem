# Monty-hall-problem
This is a Python code that simulates the Monty Hall problem, a famous probability puzzle. 


# Monty Hall Problem Simulation
This is a Python code that simulates the Monty Hall problem, a famous probability puzzle. In this problem, a contestant is asked to choose one of three doors, behind one of which there is a prize, and behind the other two there are goats. After the contestant chooses a door, the host, who knows what is behind each door, opens one of the remaining two doors to reveal a goat. Then, the contestant is given the option to switch to the other unopened door or stick with the original choice.

The surprising answer to the problem is that the contestant should switch, as it increases the probability of winning the prize from 1/3 to 2/3. This is because when the contestant first chooses a door, the probability of the prize being behind that door is 1/3. Therefore, the probability of the prize being behind one of the other two doors is 2/3. When the host opens one of these two doors, the probability of the prize being behind the unopened door increases to 2/3, since the host knows where the prize is and will never open the door that hides the prize.

To verify this counterintuitive result, the code simulates the problem by randomly choosing a winning door and a player's choice in each trial, and then implementing the switching or non-switching strategy. The simulation is run for 1001 trials, and the proportion of wins for each strategy is calculated and displayed as a percentage.

# Requirements
Python IDLE

# Usage
Clone or download the repository to your local machine.
Navigate to the directory containing the monty_hall.py file.
Run the file using the Python interpreter:

python monty_hall.py

The program will output the percentage of wins for the switching and non-switching strategies.
Results
After running the simulation for 1001 trials, the code consistently produces results in the range of 33% for non-switching and 67% for switching, which confirms the theoretical probability of winning.


