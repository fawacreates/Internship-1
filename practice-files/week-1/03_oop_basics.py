# Week 1 Practice: Object-Oriented Programming
# OOP is fundamental for building modular aerospace software

"""
Part 1: Classes and Objects
"""

class Aircraft:
    """Represents an aircraft with basic properties"""
    
    # Class variable (shared by all instances)
    total_aircraft = 0
    
    def __init__(self, model, manufacturer, max_altitude):
        """Constructor: initialize aircraft properties"""
        self.model = model
        self.manufacturer = manufacturer
        self.max_altitude = max_altitude  # meters
        self.current_altitude = 0
        self.speed = 0  # m/s
        self.is_flying = False
        
        # Increment class counter
        Aircraft.total_aircraft += 1
    
    def takeoff(self):
        """Simulate takeoff"""
        if not self.is_flying:
            self.is_flying = True
            self.current_altitude = 100
            print(f"{self.model} is taking off...")
        else:
            print("Already flying!")
    
    def climb(self, altitude_change):
        """Increase altitude"""
        if self.is_flying:
            new_altitude = self.current_altitude + altitude_change
            if new_altitude <= self.max_altitude:
                self.current_altitude = new_altitude
                print(f"{self.model} climbed to {self.current_altitude}m")
            else:
                print(f"Cannot exceed max altitude of {self.max_altitude}m")
        else:
            print("Aircraft must be flying to climb")
    
    def land(self):
        """Simulate landing"""
        if self.is_flying:
            self.current_altitude = 0
            self.speed = 0
            self.is_flying = False
            print(f"{self.model} has landed")
        else:
            print("Aircraft is not flying")
    
    def __str__(self):
        """String representation"""
        status = "Flying" if self.is_flying else "On ground"
        return f"{self.manufacturer} {self.model} - {status} at {self.current_altitude}m"


print("=== Aircraft Class Demo ===")
aircraft1 = Aircraft("Cessna 172", "Cessna", 4267)
aircraft2 = Aircraft("Airbus A380", "Airbus", 43000)

print(aircraft1)
print(aircraft2)
print(f"Total aircraft created: {Aircraft.total_aircraft}\n")

# Simulate flight
aircraft1.takeoff()
aircraft1.climb(500)
aircraft1.climb(1000)
aircraft1.land()
print()

"""
Part 2: Inheritance
"""

class Drone(Aircraft):
    """Drone class inheriting from Aircraft"""
    
    def __init__(self, model, manufacturer, max_altitude, battery_capacity):
        """Initialize drone with additional properties"""
        super().__init__(model, manufacturer, max_altitude)
        self.battery_capacity = battery_capacity  # mAh
        self.battery_level = 100  # percent
    
    def discharge_battery(self, percent):
        """Simulate battery drain"""
        self.battery_level = max(0, self.battery_level - percent)
        print(f"Battery level: {self.battery_level}%")
    
    def return_to_home(self):
        """Drone-specific feature"""
        if self.is_flying:
            print(f"{self.model} returning to home...")
            self.current_altitude = 0
            self.is_flying = False
        print(f"{self.model} has returned home")
    
    def __str__(self):
        """Override string representation"""
        base = super().__str__()
        return f"{base} [Battery: {self.battery_level}%]"


print("=== Drone Class Demo (Inheritance) ===")
drone = Drone("DJI Phantom 4", "DJI", 6000, 5250)
print(drone)
print()

drone.takeoff()
drone.climb(500)
drone.discharge_battery(5)
drone.climb(500)
drone.discharge_battery(10)
drone.return_to_home()
print()

"""
Part 3: Encapsulation (Private/Protected Members)
"""

class FlightController:
    """Flight controller with private attributes"""
    
    def __init__(self, pid_kp=1.0, pid_ki=0.1, pid_kd=0.5):
        # Private attributes (convention: prefix with _)
        self._kp = pid_kp
        self._ki = pid_ki
        self._kd = pid_kd
        self._error_integral = 0
        self._last_error = 0
    
    def set_gains(self, kp, ki, kd):
        """Setter method - validate before setting"""
        if kp > 0 and ki > 0 and kd > 0:
            self._kp = kp
            self._ki = ki
            self._kd = kd
            print(f"Gains updated: Kp={kp}, Ki={ki}, Kd={kd}")
        else:
            print("Error: All gains must be positive")
    
    def get_gains(self):
        """Getter method"""
        return self._kp, self._ki, self._kd
    
    def compute_pid(self, error, dt):
        """Compute PID output"""
        self._error_integral += error * dt
        derivative = (error - self._last_error) / dt
        self._last_error = error
        
        output = self._kp * error + self._ki * self._error_integral + self._kd * derivative
        return output


print("=== Encapsulation Demo ===")
fc = FlightController()
print(f"Current gains: {fc.get_gains()}")
fc.set_gains(1.2, 0.15, 0.6)
print()

"""
Part 4: Polymorphism
"""

class Sensor:
    """Base sensor class"""
    
    def read(self):
        raise NotImplementedError("Subclasses must implement read()")


class GPS(Sensor):
    def read(self):
        return {"latitude": 40.7128, "longitude": -74.0060, "altitude": 100}


class IMU(Sensor):
    def read(self):
        return {"ax": 0.1, "ay": 0.2, "az": 9.8}


class Barometer(Sensor):
    def read(self):
        return {"altitude": 1000, "temperature": 25.5, "pressure": 101325}


print("=== Polymorphism Demo ===")
sensors = [GPS(), IMU(), Barometer()]

for sensor in sensors:
    data = sensor.read()
    print(f"{sensor.__class__.__name__}: {data}")

print()

"""
Part 5: Static Methods and Class Methods
"""

class MathUtils:
    """Utility class with static methods"""
    
    PI = 3.14159
    
    @staticmethod
    def degrees_to_radians(degrees):
        """Static method - no self parameter"""
        return degrees * (MathUtils.PI / 180)
    
    @classmethod
    def from_radians(cls, radians):
        """Class method - receives class as first argument"""
        degrees = radians * (180 / cls.PI)
        return degrees


print("=== Static and Class Methods ===")
print(f"45° = {MathUtils.degrees_to_radians(45):.4f} radians")
print(f"π/4 radians = {MathUtils.from_radians(MathUtils.PI/4):.1f}°")
