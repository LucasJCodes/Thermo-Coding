
#Thermo Coding Assignment
#Group Members: 
#   Brianna DeFore
#   Haley Reeves
#   Katelynn Fisher
#   Lucas Jones
#   Nolan Armstrong
#   Jack Reed

# Define constants

p0 = 100000 # Pa
alpha0 = 10 # m^3/Kg
Rd = 287 # J/kg K
Cv = 718 # J/kg K
Cp = 1005 # J/kg K

# Question 1
# Define function to calculate temperature

def findTemp(p0, alpha0):
    temperature = (p0 * alpha0) / Rd
    
    return temperature

# Question 2
# Define function to caluclate work for isobaric and isochoric processes

def get_Work_Isobaric(pressure, alpha_initial, alpha_final):
    work = pressure * (alpha_final - alpha_initial)
    
    return work

def get_Work_Isochoric():
    return 0

# Question 3
# Define function to calculate Net Work

def Total_Work(WorkAB, WorkBC, WorkCD, WorkDA):
    Net_Work = WorkAB + WorkBC + WorkCD + WorkDA
    
    return(Net_Work)

# Question 4
# Define function to calculate heat for isochoric and isobaric processes

def findHeat1(Cv, Temp2, Temp1):
    HeatIsochoric = (Cv * (Temp2-Temp1))
        
    return HeatIsochoric
    
def findHeat2(Cp, Temp2, Temp1):
    HeatIsobaric = (Cp * (Temp2-Temp1)) 
    
    return HeatIsobaric

# Question 5
# Define function to caluclate Net Heat

def NetHeat(q1, q2, q3, q4):
    totalHeat = q1 + q2 + q3 + q4
    
    return totalHeat

# Question 6
# Define function to calculate internal energy

def InternalEnergy(TempA, TempB):
    EnergyChange = Cv * (TempB - TempA)
    
    return EnergyChange
   
# Question 7
# Define function to calculate Net Internal Energy

def findNetIntEnergy(u1, u2, u3, u4):
    totalIntEnergy = u1 + u2 + u3 + u4
    
    return totalIntEnergy

# Question 8
# Define function to calculate efficiency

def findEfficiency (Cv, Cp, TempA, TempB, TempC, TempD):
    Efficiency = (((Cv*(TempB-TempA))+(Cp*(TempC- TempB))-(Cv*(TempD- TempC))+(Cp*(TempA-TempD)))/(Cv*(TempB-TempA)+(Cp*(TempC-TempB))))
    
    return Efficiency

#----------------------------Main Program-------------------------------------#

# Find and print out all the temperature values

print("\nQuestion 1")

tempA = round(findTemp(p0, alpha0), 2)
print("Temperature A: {} K".format(tempA))

tempB = round(findTemp(2 * p0, alpha0), 2)
print("Temperature B: {} K".format(tempB))

tempC = round(findTemp(2 * p0, 2 * alpha0), 2)
print("Temperature C: {} K".format(tempC))

tempD = round(findTemp(p0, 2 * alpha0), 2)
print("Temperature D: {} K".format(tempD))

# Get work

print("\nQuestion 2")

workAB = round(get_Work_Isochoric(), 2)
print("Work from A to B: {} J/kg".format(workAB))

workBC = round(get_Work_Isobaric(2 * p0, alpha0, 2 * alpha0), 2)
print("Work from B to C: {} J/kg".format(workBC))

workCD = round(get_Work_Isochoric(), 2)
print("Work from C to D: {} J/kg".format(workCD))

workDA = round(get_Work_Isobaric(p0, 2 * alpha0, alpha0), 2)
print("Work from D to A: {} J/kg".format(workDA))

# Get net work
print("Problem 7")


print("\nQuestion 3")
netWork = round(Total_Work(workAB, workBC, workCD, workDA), 2)
print("Net Work: {} J/kg".format(netWork))

# Get heat

print("\nQuestion 4")

HeatAB = round(findHeat1(Cv, tempB, tempA), 2)
print("Heat from A to B: {} J/kg".format(HeatAB))

HeatBC = round(findHeat2(Cp, tempC, tempB), 2)
print("Heat from B to C: {} J/kg".format(HeatBC))

HeatCD = round(findHeat1(Cv, tempD, tempC), 2)
print("Heat from C to D: {} J/kg".format(HeatCD))

HeatDA = round(findHeat2(Cp, tempA, tempD), 2)
print("Heat from D to A: {} J/kg".format(HeatDA))

# Get net heat

print("\nQuestion 5")

HeatNet = round(NetHeat(HeatAB, HeatBC, HeatCD, HeatDA), 2)
print("Net Heat: {} J/kg".format(HeatNet))

# Get internal energy

print("\nQuestion 6")

EnergyAB = round(InternalEnergy(tempA, tempB), 2)
print("Change in Internal Energy from A to B: {} J/kg".format(EnergyAB))

EnergyBC = round(InternalEnergy(tempB, tempC), 2)
print("Change in Internal Energy from B to C: {} J/kg".format(EnergyBC))

EnergyCD = round(InternalEnergy(tempC, tempD), 2)
print("Change in Internal Energy from C to D: {} J/kg".format(EnergyCD))

EnergyDA = round(InternalEnergy(tempD, tempA), 2)
print("Change in Internal Energy from D to A: {} J/kg".format(EnergyDA))

# Get net internal energy

print("\nQuestion 7")

NetIntEnergy = round(findNetIntEnergy(EnergyAB, EnergyBC, EnergyCD, EnergyDA), 2)
print("Net Internal Energy: {} J/kg".format(NetIntEnergy)) 

# Get efficiency

print("\nQuestion 8")

Efficiency = round(findEfficiency (Cv, Cp, tempA, tempB, tempC, tempD), 2)
print("Efficiency: {}".format(Efficiency))


print(" /\../\\")
print("('o..o')")
print("   =*=   ")
print("(\.||./)~~**")