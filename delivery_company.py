class WeDeliver:
    def __init__(self):
        self.drivers={}
        self.cities={}
        self.driver_id_counter=1

    def main_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers menu")
            print("2. To go to the cities menu")
            print("3. To exit the system")

            choice=int(input("Enter your choice:"))

            if choice==1:
                self.drivers_menu()
            elif choice==2:
                self.cities_menu()
            elif choice==3:
                print("good bye!")
                break

            else:
                print("invalid choice please try again")

    def drivers_menu(self):
        while True:
            print("Enter")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. Check similar drivers")
            print("4. To go back to the main menu")

            choice=int(input("Enter choice:"))

            if choice==1:
                self.viewDrivers()
            elif choice==2:
                self.addDrivers()
            elif choice==3:
                self.checkSimilarDrivers()
            elif choice==4:
                break
            else:
                print("invalid choice please try again")

    def generate_driver_id(self):
        driver_id=f"ID{self.driver_id_counter:03}"
        self.driver_id_counter+=1
        return driver_id
    

    def viewDrivers(self):
        print("The list of drivers is:")
        if not self.drivers:
            print("No drivers in the system")
        else:
            for driver_id,(name,startCity) in self.drivers.items():
                print(f"{driver_id},{name},{startCity}")

    def addDrivers(self):
        name=input("Enter the driver name")
        city=input("Enter the driver start city")

        if city not in self.cities:
            add_city=input(f"{city} is not in the city list do you want to add it? y/n:")
            if add_city.lower()=='yes':
                self.cities[city]=[]
            else:
                print("driver is not added as the city is not available")

        driver_id=self.generate_driver_id()
        self.drivers[driver_id]=(name,city)
        print(f"Driver {name} added with id {driver_id}")

    def checkSimilarDrivers(self):
        city_drivers={}

        for driver_id,(name,startCity) in self.drivers.items():
            if startCity not in city_drivers:
                city_drivers[startCity] = []  # Initialize with an empty list if the city is not in the dictionary
            city_drivers[startCity].append(name)  # Append the driver's name to the city's list of drivers


        print("/n Similar drivers by city")
        for city,drivers in city_drivers.items():
            print(f"{city}: {','.join(drivers)}")

    def cities_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. Show cities")
            print("2. Search city")
            print("3. Print neighboring cities ")
            print("4. Print Drivers delivering to city ")
            print("5. To go back to the main menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.showCities()
            elif choice == 2:
                self.searchCity()
            elif choice == 3:
                self.printNeighboringCities()
            elif choice == 4:
                self.printDriversDeliveringToCity()
            elif choice == 5:
                break
            else:
                print("Invalid choice.Please try again.")

    def showCities(self):
        # Extract city names, sort them in descending alphabetical order (Z to A)
        sortedCities=sorted(self.cities.keys(),reverse=True)

         # Display the sorted list of cities
        print("Cities (sorted from Z to A):")
        for city in sortedCities:
            print(city)

    def searchCity(self):
        key=input("Enter a search key:").lower()
        for city in self.cities.keys():
            if key in city.lower():
                print(f"The cities found,{city}")
            else:
                print("No cities found with that key.")

    # def searchCity(self):
    #     key = input("Enter search key: ").lower()
    #     results = [city for city in self.cities.keys() if key in city.lower()]
        
    #     if results:
    #         print("Cities found:", ", ".join(results))
    #     else:
    #         print("No cities found with that key.")

    def printNeighboringCities(self):
        city=input("Enter city name:").lower()
        if city in self.cities:
            print(f"Neighboring cities for {city}: {', '.join(self.cities[city])}")
        else:
            print("City not found")

    def printDriversDeliveringToCity(self):
        city = input("Enter city name: ")
        visited = set()
        drivers = set()

        def bfs(start_city):
            queue = deque([start_city])
            visited.add(start_city)
            
            while queue:
                current_city = queue.popleft()
                for driver_id, (name, start_city) in self.drivers.items():
                    if current_city == start_city:
                        drivers.add(name)

                for neighbor in self.cities[current_city]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        bfs(city)

        if drivers:
            print(f"Drivers delivering to {city}: {', '.join(drivers)}")
        else:
            print("No drivers found for that city.")

system = WeDeliver()
system.main_menu()