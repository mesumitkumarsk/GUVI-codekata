You're developing a Python program for a virtual pet simulation game. The game features various types of pets, each with its own unique abilities and needs. You need to implement a system to manage different types of pets and their actions. The program should support pets such as cats, dogs, and birds.

Write a Python script that demonstrates method overloading in the context of different pet classes. Your program should accomplish the following tasks:

Define a base class called Pet.
Implement different subclasses for various types of pets, such as Cat, Dog, and Bird.
Each pet class should have methods to perform actions such as eating, sleeping, and making sounds.
Demonstrate method overloading by implementing different versions of the eat(), sleep(), and make_sound() methods for each pet class.
Additionally, integrate some unique behaviors for each type of pet:

Cats should be able to purr when making a sound.
Dogs should be able to wag their tails when making a sound.
Birds should be able to chirp when making a sound.
Ensure the following operations can be performed:

Feed a pet and display a message indicating it's eating.
Put a pet to sleep and display a message indicating it's sleeping.
Prompt a pet to make a sound and display the appropriate message based on its type.
Your program should continuously prompt the user for pet actions until the "quit" command is entered.

Provide appropriate error handling for invalid inputs. Display a message in the following format for invalid inputs: "Invalid input. Please enter a valid action (feed/sleep/make_sound/quit)."

Sample Input:

cat
eat
dog
make_sound
bird
sleep
quit

Sample Output:

Cat is eating.
Dog is wagging its tail.
Bird is sleeping.
Quitting the program.

Explanation:

The user selects a pet and an action to perform.
The program executes the action based on the selected pet type and displays an appropriate message.
The process continues until the user enters "quit." If the user enters an invalid action, an appropriate error message is displayed.
