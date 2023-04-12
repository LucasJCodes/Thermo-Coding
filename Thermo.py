
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


# Question 3 - Jack Reed
def Total_Work(WorkAB, WorkBC, WorkCD, WorkDA):
    Net_Work = WorkBC + WorkDA
    return(Net_Work)
# Question 4

def findHeat1(Cv,TempA, TempB, TempC, TempD):
    HeatIsochoric = (Cv * (TempB-TempA))
    HeatIsochoric = (Cv * (TempD-TempC))
        
    return HeatIsochoric
    
def findHeat2(Cp,TempA, TempB, TempC, TempD):
    HeatIsobaric = (Cp * (TempC-TempB))
    HeatIsobaric = (Cp * (TempA-TempD))
    
    return HeatIsobaric


# Question 5

def NetHeat(u1, u2, u3, u4):
    totalHeat = u1 + u2 + u3 + u4
    
    return totalHeat

# Question 6
 
# Question 7

# Question 8

#----------------------------Main Program-------------------------------------#