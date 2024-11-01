class WeDeliver:
    def __init__(self):
        self.drivers={}
        self.cities={}
        self.driver_id_counter=1

    def main_menu():
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers’ menu")
            print("2. To go to the cities’ menu")
            print("3. To exit the system")

            choice=input("Enter your choice")

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

            choice=input("Enter choice:")

            if choice==1:
                self.viewDrivers()
            elif choice==2:
                self.addDrivers()
            elif choice==3:
                self.checkDrivers()
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
        if self.drivers==0:
            print("No drivers in the system")
        else:
            for driver_id,(name,startCity) in self.drivers.items():
                print(f"{driver_id},{name},{startCity}")