class Pet:
    #..... YOUR CODE STARTS HERE .....

    def eat(self):
       pass
    
    def sleep(self):
        pass
    
    def make_sound(self):
        pass 
    
    #..... YOUR CODE ENDS HERE .....


class Cat(Pet):
    #..... YOUR CODE STARTS HERE .....
    
    def eat(self):
        print("Cat is eating.")
        
    def sleep(self):
        print("Cat is sleeping.")
        
    def make_sound(self): 
        print("Cat is purring.")
    
    #..... YOUR CODE ENDS HERE .....

class Dog(Pet):
    #..... YOUR CODE STARTS HERE .....
    
    def eat(self):
        print("Dog is eating:")
    def sleep(self):
        print("Dog is sleeping.")
    def make_sound(self):
        print("Dog is wagging its tail.")
    
    #..... YOUR CODE ENDS HERE .....

class Bird(Pet):
    #..... YOUR CODE STARTS HERE .....
    
    def eat(self):
        print("Bird is eating.")
    def sleep(self):
        print("Bird is sleeping.")
    def make_sound(self):
        print("Bird is chirping.")
    
    #..... YOUR CODE ENDS HERE .....

def main():
    while True:
        pet_type = input("").lower()
        if pet_type == 'quit':
            print("Quitting the program.")
            break
        elif pet_type not in ['cat', 'dog', 'bird']:
            print("Invalid input. Please enter a valid pet type (cat/dog/bird).")
            continue

        pet_action = input("").lower()
        if pet_action == 'quit':
            print("Quitting the program.")
            break
        elif pet_action not in ['eat', 'sleep', 'make_sound']:
            print("Invalid input. Please enter a valid action (eat/sleep/make_sound/quit).")
            continue

        if pet_type == 'cat':
            cat = Cat()
            if pet_action == 'eat':
                cat.eat()  # Output: "Cat is eating."
            elif pet_action == 'sleep':
                cat.sleep()  # Output: "Cat is sleeping."
            elif pet_action == 'make_sound':
                cat.make_sound()  # Output: "Cat is purring."
        elif pet_type == 'dog':
            dog = Dog()
            if pet_action == 'eat':
                dog.eat()  # Output: "Dog is eating."
            elif pet_action == 'sleep':
                dog.sleep()  # Output: "Dog is sleeping."
            elif pet_action == 'make_sound':
                dog.make_sound()  # Output: "Dog is wagging its tail."
        elif pet_type == 'bird':
            bird = Bird()
            if pet_action == 'eat':
                bird.eat()  # Output: "Bird is eating."
            elif pet_action == 'sleep':
                bird.sleep()  # Output: "Bird is sleeping."
            elif pet_action == 'make_sound':
                bird.make_sound()  # Output: "Bird is chirping."

if __name__ == "__main__":
    main()