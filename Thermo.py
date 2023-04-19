
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

# Question 2

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

def findNetIntEnergy(u1, u2, u3, u4):
    totalIntEnergy = u1 + u2 + u3 + u4
    
    return totalIntEnergy

# Question 8
def findEfficiency (Cv, Cp, TempA, TempB, TempC, TempD):
    Efficiency = (((Cv*(TempB-TempA))+(Cp*(TempC- TempB))-(Cv*(TempD- TempC))+(Cp*(TempA-TempD)))/(Cv*(TempB-TempA)+(Cp*(TempC-TempB))))
    
    return Efficiency

#----------------------------Main Program-------------------------------------#

# Find and print out all the temperature values

print("Question 1:")

tempA = findTemp(p0, alpha0)
print("Temperature A: {}".format(tempA))

tempB = findTemp(2 * p0, alpha0)
print("Temperature B: {}".format(tempB))

tempC = findTemp(2 * p0, 2 * alpha0)
print("Temperature C: {}".format(tempC))

tempD = findTemp(p0, 2 * alpha0)
print("Temperature C: {}".format(tempD))

# Get work

print("Problem 2")

workAB = get_Work_Isochoric()
print("Work AB: {}".format(workAB))

workBC = get_Work_Isobaric(2 * p0, alpha0, 2 * alpha0)
print("Work BC: {}".format(workBC))

workCD = get_Work_Isochoric()
print("Work CD: {}".format(workCD))

workDA = get_Work_Isobaric(p0, 2 * alpha0, alpha0)
print("Work DA: {}".format(workDA))

# Get net work
print("Problem 7")



# Get heat

# Get net heat

# Get internal energy
print("\nQuestion 6")

EnergyAB = InternalEnergy(tempA, tempB)
print("Change in Internal Energy from A to B: ", EnergyAB, "J")

EnergyBC = InternalEnergy(tempB, tempC)
print("Change in Internal Energy from B to C: ", EnergyBC, "J")

EnergyCD = InternalEnergy(tempC, tempD)
print("Change in Internal Energy from C to D: ", EnergyCD, "J")

EnergyDA = InternalEnergy(tempD, tempA)
print("Change in Internal Energy from D to A: ", EnergyDA, "J")

# Get net internal energy
NetIntEnergy = findNetIntEnergy(EnergyAB, EnergyBC, EnergyCD, EnergyDA)
print("Problem 7. \n Net Internal Energy: {}".format(NetIntEnergy) "J") 

# Get efficiency
Efficiency = findEfficiency (Cv, Cp, tempA, tempB, tempC, tempD)
print("Efficiency: {}".format(Efficiency))


