import random
import datetime

class Parking:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.parked_vehicles = {}  # Dictionary to store vehicle info with token as key
        self.vehicle_types = {
            1: {"name": "Car", "price": 30},
            2: {"name": "Bike", "price": 20},
            3: {"name": "Scooty", "price": 20},
            4: {"name": "Jeep", "price": 25},
            5: {"name": "Bus", "price": 40}
        }
    
    def park(self, name, phno, veh_no, vehicle_type):
        """Park a vehicle and return token"""
        if len(self.parked_vehicles) >= self.total_slots:
            return None, "Parking is full!"
        
        # Check if vehicle is already parked
        for token, info in self.parked_vehicles.items():
            if info['vehicle_no'] == veh_no:
                return None, "Vehicle is already parked!"
        
        # Generate unique token
        token = str(random.randint(100000, 999999)) + "ABC"
        while token in self.parked_vehicles:
            token = str(random.randint(100000, 999999)) + "ABC"
        
        # Store vehicle information
        vehicle_info = {
            'name': name,
            'phone': phno,
            'vehicle_no': veh_no,
            'vehicle_type': self.vehicle_types[vehicle_type]['name'],
            'price_per_hour': self.vehicle_types[vehicle_type]['price'],
            'entry_time': datetime.datetime.now(),
            'token': token
        }
        
        self.parked_vehicles[token] = vehicle_info
        return token, f"Vehicle parked successfully! Token: {token}"
    
    def remove(self, token):
        """Remove a vehicle and calculate payment"""
        if token not in self.parked_vehicles:
            return None, "Invalid token!"
        
        vehicle_info = self.parked_vehicles[token]
        exit_time = datetime.datetime.now()
        entry_time = vehicle_info['entry_time']
        
        # Calculate parking duration
        duration = exit_time - entry_time
        hours = max(1, duration.total_seconds() / 3600)  # Minimum 1 hour
        
        # Calculate total cost
        total_cost = hours * vehicle_info['price_per_hour']
        
        # Remove vehicle
        del self.parked_vehicles[token]
        
        return {
            'vehicle_no': vehicle_info['vehicle_no'],
            'name': vehicle_info['name'],
            'duration_hours': round(hours, 2),
            'total_cost': round(total_cost, 2),
            'vehicle_type': vehicle_info['vehicle_type']
        }, "Vehicle removed successfully!"
    
    def show_queue(self):
        """Display all parked vehicles"""
        if not self.parked_vehicles:
            return "No vehicles currently parked."
        
        print("\n" + "="*80)
        print(f"{'Token':<12} {'Name':<15} {'Vehicle No':<15} {'Type':<10} {'Entry Time':<20}")
        print("="*80)
        
        for token, info in self.parked_vehicles.items():
            entry_time_str = info['entry_time'].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{token:<12} {info['name']:<15} {info['vehicle_no']:<15} {info['vehicle_type']:<10} {entry_time_str:<20}")
        
        print("="*80)
        return f"Total vehicles parked: {len(self.parked_vehicles)}"
    
    def remaining_slots(self):
        """Show remaining parking slots"""
        remaining = self.total_slots - len(self.parked_vehicles)
        return f"Available slots: {remaining}/{self.total_slots}"
    

        
    
    

def main():
    P = Parking(100)
    
    while True:
        print("\n" + "="*50)
        print("------Welcome to Vehicle Parking Management------")
        print("="*50)
        print("1. Park the vehicle")
        print("2. Remove the vehicle")
        print("3. See the queue")
        print("4. Remaining slots")
        print("5. Exit")
        print("="*50)
        
        try:
            option = int(input("Enter your option: "))
            
            if option == 1:
                print("\n--- PARK VEHICLE ---")
                name = input("Enter your name: ")
                phNumber = input("Enter your phone number: ")
                
                print("\nVehicle Types and Pricing:")
                print("1. Car    - Rs.30/hour")
                print("2. Bike   - Rs.20/hour")
                print("3. Scooty - Rs.20/hour")
                print("4. Jeep   - Rs.25/hour")
                print("5. Bus    - Rs.40/hour")
                
                choice = int(input("Enter your choice (1-5): "))
                if choice not in range(1, 6):
                    print("Invalid choice! Please select 1-5.")
                    continue
                
                vehicle_num = input("Enter the vehicle number: ")
                
                token, message = P.park(name, phNumber, vehicle_num, choice)
                if token:
                    print(f"\n✅ {message}")
                    print(f"Please keep your token safe: {token}")
                else:
                    print(f"\n❌ {message}")
            
            elif option == 2:
                print("\n--- REMOVE VEHICLE ---")
                token = input("Enter your token number: ")
                
                result, message = P.remove(token)
                if result:
                    print(f"\n✅ {message}")
                    print("\n--- PARKING RECEIPT ---")
                    print(f"Name: {result['name']}")
                    print(f"Vehicle Number: {result['vehicle_no']}")
                    print(f"Vehicle Type: {result['vehicle_type']}")
                    print(f"Duration: {result['duration_hours']} hours")
                    print(f"Total Cost: Rs.{result['total_cost']}")
                    print("Thank you for using our parking service!")
                else:
                    print(f"\n❌ {message}")
            
            elif option == 3:
                print("\n--- CURRENT PARKED VEHICLES ---")
                message = P.show_queue()
                print(f"\n{message}")
            
            elif option == 4:
                print("\n--- PARKING AVAILABILITY ---")
                print(P.remaining_slots())
            
            elif option == 5:
                print("\nThank you for using Vehicle Parking Management System!")
                print("Goodbye! 👋")
                break
            
            else:
                print("\n❌ Invalid option! Please select 1-5.")
        
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
