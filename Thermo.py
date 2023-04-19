
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

# Question 1

def findTemp(p0, alpha0):
    temperature = (p0 * alpha0) / Rd
    
    return temperature

# Question 2- Lucas Jones

def get_Work_Isobaric(pressure, alpha_initial, alpha_final):
    work = pressure * (alpha_final - alpha_initial)
    
    return work

def get_Work_Isochoric():
    return 0

# Question 3

def Total_Work(WorkAB, WorkBC, WorkCD, WorkDA):
    Net_Work = WorkAB + WorkBC + WorkCD + WorkDA
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

def NetHeat(q1, q2, q3, q4):
    totalHeat = q1 + q2 + q3 + q4
    
    return totalHeat

# Question 6

def InternalEnergy(TempA, TempB):
    EnergyChange = 718 * (TempB - TempA)
    return EnergyChange
   
# Question 7

def NetIntEnergy(u1, u2, u3, u4):
    totalIntEnergy = u1 + u2 + u3 + u4
    
    return totalIntEnergy

# Question 8

#----------------------------Main Program-------------------------------------#