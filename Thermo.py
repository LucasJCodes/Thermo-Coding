
#Thermo Coding Assignment
#Group Members: 
#   Brianna DeFore
#   Haley Reeves
#   Katelynn Fisher
#   Lucas Jones
#   Nolan Armstrong
#   Jack Reed

p0 = 100000 # Pa
alpha0 = 10 # m^3
Rd = 287 # J/kg K
Cv = 718 # J/kg K
Cp = 1005 # J/kg K

#Question 1

def findTemps(p0, alpha0):
    temperature = (p0 * alpha0) / Rd
    
    return temperature

