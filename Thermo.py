
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

# Question 1- Whole group

def findTemp(p0, alpha0):
    temperature = (p0 * alpha0) / Rd
    
    return temperature


print("temperature 1: {} temperature 2: {}".format(findTemp(p0, alpha0), findTemp((2 * p0), alpha0)))


# Question 2- Lucas Jones

def get_Work_Isobaric(pressure, alpha_initial, alpha_final):
    work = pressure * (alpha_final - alpha_initial)
    
    return work

# Question 3-


# Question 4

# Question 5

# Question 6
 
# Question 7

# Question 8

#----------------------------Main Program-------------------------------------#