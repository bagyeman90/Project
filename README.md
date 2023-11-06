# Quiz Game Readme

Welcome to the Quiz Game! This is a straightforward text-based quiz game designed to assess your knowledge of computer hardware and its components. This readme provides an introduction to the game, instructions on how to play, and what to anticipate.

## Getting Started

1. To commence the Quiz Game, execute the program. It will greet you with a welcoming message:

   ```python
   print("Welcome to the Quiz Game")
   ```

2. You will then be asked if you wish to play:

   ```python
   first_question = input("Do you wish to participate? ")
   ```

3. You can reply with "yes" to initiate the game or "no" to exit. If you choose "yes," the game will begin, and selecting "no" will conclude the game.

## Playing the Game

If you decide to play, you will enter the main quiz section of the game:

1. The game will display "OKAY!!!" and "Let's play."

2. Your score will start at 0.

3. A series of questions regarding computer hardware components will be presented to you:

   - The first question pertains to the CPU (Central Processing Unit):

     ```python
     answer = input("What is the full form of CPU? ")
     ```

   - The second question relates to the GPU (Graphics Processing Unit):

     ```python
     answer = input("What does GPU stand for? ")
     ```

   - The third question concerns RAM (Random Access Memory):

     ```python
     answer = input("What is the acronym for RAM? ")
     ```

   - The fourth question is about the PSU (Power Supply Unit):

     ```python
     answer = input("What does PSU stand for? ")
     ```

4. You can input your answers to these questions, and the game will inform you whether your response is accurate or not.

   - Correct answers will be followed by "Correct" and an increase in your score.
   - Incorrect answers will be followed by "Incorrect!"

5. After responding to all the questions, the game will display your final score:

   ```python
   print("You answered " + str(score) + " questions correctly")
   ```

   It will also calculate and display your percentage score based on the number of correct answers out of the total questions (in this case, 4 questions):

   ```python
   print("You answered " + str(score) / 4 * 100 + " % correctly.")
   ```

## Exiting the Game

At any point during the game, you can opt to exit by typing "no" when asked if you want to play. The game will conclude with the message:

```python
print("This marks the end of the game.")
```

## Enjoy the Game!

Have fun playing the Quiz Game and challenging yourself on your knowledge of computer hardware components. Aim to answer as many questions correctly as possible and even compete with friends to see who can achieve the highest score!
