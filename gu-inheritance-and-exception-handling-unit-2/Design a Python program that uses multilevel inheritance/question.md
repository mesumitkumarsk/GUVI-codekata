Design a Python program that uses multilevel inheritance to model the administrative divisions of Tamil Nadu. Tamil Nadu is divided into districts, and each district is divided into cities. All divisions have a name and a population. However, a district also has a number of cities, and Tamil Nadu has a number of districts.

Create classes to represent Tamil Nadu, a district, and a city, and use multilevel inheritance to avoid code duplication. Write a method in each class to print the details of the division.

Sample Input:

Coimbatore, 1064000
Coimbatore District, 3472578, 2
Tamil Nadu, 77841267, 38

Sample Output:

City: Coimbatore, Population: 1064000
District: Coimbatore District, Population: 3472578, Number of Cities: 2
State: Tamil Nadu, Population: 77841267, Number of Districts: 38

Explanation:

Multilevel inheritance is used to model the hierarchical relationship between a state, its districts, and the cities within those districts.

The City class is the base level in this hierarchy. It has properties like name and population.
The District class inherits from the City class, making it the next level in the hierarchy. It has all the properties of a City, plus an additional property: the number of cities. When we create a District object and call its print_details() method, it prints the details specific to that district, including the number of cities.
The TamilNadu class inherits from the District class, making it the top level in the hierarchy. It has all the properties of a District, plus an additional property: the number of districts. When we create a TamilNadu object and call its print_details() method, it prints the details specific to the state, including the number of districts.
This is an example of multilevel inheritance, where a derived class inherits from a base class, which in turn inherits from another base class. In this case, TamilNadu is a derived class that inherits from District, which is a derived class that inherits from City.

Constraints:

The name of the city, district, or state is a string and can contain any printable ASCII characters.
The population of the city, district, or state is an integer and can be any positive integer.
The number of cities in a district is an integer and can be any positive integer.
The number of districts in Tamil Nadu is an integer and can be any positive integer.