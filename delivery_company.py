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

            else:
                print("invalid choice please try again")
        
        