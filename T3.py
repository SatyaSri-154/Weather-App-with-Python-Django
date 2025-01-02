class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} miles")

# Get input from the user
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of manufacture of the car: ")
mileage = input("Enter the current mileage of the car: ")

# Convert year and mileage to integers
try:
    year = int(year)
    mileage = int(mileage)
except ValueError:
    print("Invalid input for year or mileage. Please enter numeric values.")
    exit()

# Create an instance of the Car class with user input
my_car = Car(make, model, year, mileage)

# Display initial information
print("\nInitial Car Information:")
my_car.display_info()

# Get input for driving distance
distance = input("\nEnter the distance to drive the car: ")

# Convert distance to integer
try:
    distance = int(distance)
except ValueError:
    print("Invalid input for distance. Please enter a numeric value.")
    exit()

# Drive the car
my_car.drive(distance)

# Display updated information
print("\nUpdated Car Information:")
my_car.display_info()

