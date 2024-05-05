class City():
    def __init__(self, name, population):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name 
        self.population = population 
    
        #..... YOUR CODE ENDS HERE .....
        
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        
        print(f"City: {self.name}, Population: {self.population}")
    
        #..... YOUR CODE ENDS HERE .....


class District(City):
    def __init__(self, name, population, num_cities):
        #..... YOUR CODE STARTS HERE .....
    
        super().__init__(name, population)
        self.num_cities = num_cities 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"District: {self.name}, Population: {self.population}, Number of Cities: {self.num_cities}")
    
        #..... YOUR CODE ENDS HERE .....


class TamilNadu(District):
    def __init__(self, name, population, num_districts):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        self.population = population 
        self.num_districts = num_districts
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"State: {self.name}, Population: {self.population}, Number of Districts: {self.num_districts}")
    
        #..... YOUR CODE ENDS HERE .....

def clean_input(value):
    return str(value.strip())

def main():
    city_name, city_population = map(clean_input, input().strip().split(","))
    city = City(city_name, int(city_population))

    district_name, district_population, num_cities = map(clean_input, input().strip().split(","))
    district = District(district_name, int(district_population), int(num_cities))

    state_name, state_population, num_districts = map(clean_input, input().strip().split(","))
    state = TamilNadu(state_name, int(state_population), int(num_districts))
    
    city.print_details()
    district.print_details()
    state.print_details()


if __name__ == "__main__":
    main()