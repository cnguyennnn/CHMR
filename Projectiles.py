import numpy as np
import matplotlib.pylab as plt


def convert_degrees_to_radians(angle_in_degrees):
    """
    Returns a given angle_in_degrees to radians.
    """
    angle = angle_in_degrees * np.pi / 180
    return angle


def time_at_maximum_height(initial_velocity, angle):
    """
    Returns the time of object at maximum height of the projectile motion.

    It assumes that the object is launched in a drag free enviroment, where only gravity is acting on the object with no air resistance.

    It takes the initial_velocity (in ms(^-2)) and angle with the horizon (in degrees). 
    """
    g = 9.8
    vy = initial_velocity * np.sin(angle)
    time_of_maximum_height = vy / g
    print(time_of_maximum_height, 's')
    return
    

def time_of_flight(initial_velocity, angle):
    """
    Returns the time of flight of the projectile motion.

    It assumes that the object is launched in a drag free enviroment, where only gravity is acting on the object with no air resistance.

    It takes the initial_velocity (in ms(^-2)) and angle with the horizon (in degrees). 
    """
    g = 9.8
    time_of_flight = 2 * (initial_velocity * np.sin(angle) / g)
    print(time_of_flight, "s")
    return 

def maximum_height(initial_velocity, angle):
    """
     Returns the maximum height of the projectile motion.

    It assumes that the object is launched in a drag free enviroment, where only gravity is acting on the object with no air resistance.

    It takes the initial_velocity (in ms(^-2)) and angle with the horizon (in degrees). 
    """
    g = 9.8
    vy = initial_velocity * np.sin(angle)
    t = vy / g
    maximum_height = vy *t - (g * (t ** 2)) / 2
    print(maximum_height, "m")
    return 

def horizontal_range(initial_velocity, angle):
    """
    Returns the horizontal range of the projectile motion.

    It assumes that the object is launched in a drag free enviroment, where only gravity is acting on the object with no air resistance.

    It takes the initial_velocity (in ms(^-2)) and angle with the horizon (in degrees). 
    """
    g = 9.8
    horizontal_range = ((initial_velocity ** 2) * np.sin(2*angle) / g)
    print(horizontal_range, "m")
    return



def plot_projectile_motion(initial_velocity,angle):
    g = 9.8
    x1 = []
    y1 = []

    t = np.linspace(0, 50, num=10000) 
    for i in t: 
        x_temp = (initial_velocity*i)*np.cos(angle)
        y_temp = ((initial_velocity*i)*np.sin(angle))-((0.5*g)*(i**2))
        x1.append(x_temp)
        y1.append(y_temp)
    
    p = [i for i, j in enumerate(y1) if j < 0]    
    for i in sorted(p, reverse = True):
        del x1[i]  
        del y1[i]  
    plt.plot(x1, y1) 
    plt.title("Projectile motion")
    plt.xlabel("Horizontal displacement ($m$)")
    plt.ylabel("Height ($m$)")
    plt.show()
