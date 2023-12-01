from math import sqrt,pi

def planet_vol(name:str,R):
    volume=4*pi*(R**3)//3
    print("{} has volume of {}".format(name,volume))

# planet_vol("earth",6.371e+6)

def mdv(name:str,density=None,volume=None,mass=None):
    if density is None:
        find="density"
        unit="kg/m\u00b3"
        fi=mass/volume
    if mass is None:
        find="mass"
        unit="kg"
        fi=density*volume
    if volume is None:
        find="volume"
        unit="m\u00b3"
        fi=mass/density
    print("{} has {} of {} {}".format(name,find,fi,unit))

# mdv("ob1", mass=50,volume=250)
# mdv("ob2",mass=50,density=65)
# mdv("ob3",density=65,volume=300)

def newton_gravity(ob1:str,ob2:str,m1,m2,r):
    G = 6.67430e-11   # gravitational constant (G)
    F = G * (m1 * m2) / r**2
    print("gravity between {} and {} is {} ".format(ob1,ob2,F))

# newton_gravity("h","e",51,65,500)

def escape_v(name:str,mass,r):
    G = 6.67430e-11
    ev = sqrt(2*G*mass/r)
    print("escape velocity of {} is {} m/s".format(name,ev))

earth_m=5.972*(10**24)
escape_v("earth",mass=earth_m,r=6.371e+6)

def planet_orbday(name:str,a:float):
    p=sqrt(a**3)
    days=p*365
    print("{} take {} days to complete one rotation".format(name,days))

# planet_orbday("mars",1.524)

def calculate_planet_mass(name:str,r,d):
    G = 6.67430e-11   # gravitational constant (G)
    M = (4/3) *pi * r**3 * d
    print("The mass of the planet is approximately",M, "kilograms.")

# calculate_planet_mass(6.371e+6, 5.514)

