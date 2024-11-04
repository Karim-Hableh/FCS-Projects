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
    

    def viewDrivers(self): #O(n)
        print("The list of drivers is:")#O(1)
        if not self.drivers:#O(1)
            print("No drivers in the system")
        else:
            for driver_id,(name,startCity) in self.drivers.items():#O(n)
                print(f"{driver_id},{name},{startCity}")

    def addDrivers(self):#O(1)
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

    def checkSimilarDrivers(self):#O(n+n)=O(n)
        city_drivers={}#O(1)

        for driver_id,(name,startCity) in self.drivers.items():#O(n)
            if startCity not in city_drivers:
                city_drivers[startCity] = []  # Initialize with an empty list if the city is not in the dictionary
            city_drivers[startCity].append(name)  # Append the driver's name to the city's list of drivers


        print("/n Similar drivers by city")
        for city,drivers in city_drivers.items():#O(n)
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

    def showCities(self):#O(nlogn)
        # Extract city names, sort them in descending alphabetical order (Z to A)
        sortedCities=sorted(self.cities.keys(),reverse=True)#O(nlogn)

         # Display the sorted list of cities
        print("Cities (sorted from Z to A):")
        for city in sortedCities:#O(n)
            print(city)

    #Using insertion sorting
    # def showCities(self):O(n+n^2+n)=O(n^2)
    #     # Extract city names
    #     city_names = list(self.cities.keys()) #O(n)
        
    #     # Sort city names in descending alphabetical order using insertion sort
    #     for i in range(1, len(city_names)):#O(n)
    #         current_city = city_names[i]
    #         j = i - 1
    #         # Move elements of city_names[0..i-1], that are less than current_city,
    #         # one position ahead of their current position
    #         while j >= 0 and city_names[j] < current_city:#O(n)
    #             city_names[j + 1] = city_names[j]
    #             j -= 1
    #         city_names[j + 1] = current_city

    #     # Print the sorted list of city names
    #     print("Cities (sorted from Z to A):")
    #     for city in city_names:#O(n)
    #         print(city)

    def searchCity(self):#O(m.c+m.k)
        key=input("Enter a search key:").lower()#O(k)
        for city in self.cities.keys():#O(m*(c+k))--loop runs m times
            if key in city.lower():#O(c+k)
                print(f"The cities found,{city}")
            else:
                print("No cities found with that key.")


    def printNeighboringCity(self):
        city_connections={
            "Beirut":["Jbeil","Zahle","Sidon"],
            "Jbeil":["Beirut"],
            "Zahle":["Beirut"],
            "Sidon":["Beirut","Tripoli"],
            "Tripoli":["Sidon"],
        }
        target_city=input("Enter a city").lower()
        found=False
        for city,neighbors in city_connections.items():
            if city.lower()==target_city:
                print(f"Neighboring cities of {city}: {', '.join(neighbors)}")
                found=True
                break
        if not found:
            print("City not found.")
            

    # def printDriversDeliveringToCity(self):
    #     target_city = input("Enter city name: ")
    #     reachable_drivers = set()

    #     # BFS to find all reachable cities from each driver's start city
    #     for driver_id, (name, start_city) in self.drivers.items():
    #         visited = set()
    #         queue = deque([start_city])

    #         while queue:
    #             city = queue.popleft()
    #             if city == target_city:
    #                 reachable_drivers.add(name)
    #                 break

    #             for neighbor in self.cities[city]:
    #                 if neighbor not in visited:
    #                     visited.add(neighbor)
    #                     queue.append(neighbor)

    #     if reachable_drivers:
    #         print(f"Drivers delivering to {target_city}: {', '.join(reachable_drivers)}")
    #     else:
    #         print(f"No drivers found delivering to {target_city}.")

system = WeDeliver()
system.main_menu()