import numpy as np
import matplotlib.pyplot as plt

MAR23QUAD = np.array(
    [[-30.535,1.254,4.326],
     [-34.432,2.631,4.234],
     [-49.812,11.371,3.015],
     [-37.084,5.012,3.727],
     [-42.904,10.62,3.235],
     [-30.965,0.779,4.444],
     [-41.432,8.158,3.681],
     [-40.698,7.546,3.647]])

LastUpdate = "Mar 23, 2023 22:00"

def getBestCaliAll():
    """Returns the current best calibration availble for all sensors.
    
    Returns: A two dimensional array containing the coefficients of the polynomial calibrations"""
    return MAR23QUAD

def getBestCali(sensor):
    """Returns the current best calibration availble for a specific sensor.
    
    Params:
    -sensor: int between 0 and 7, inclusive
    Returns: An array containg the coefficients for the specified sensor, indexed by power"""
    return getBestCaliAll()[sensor]

def caliVoltage(sensor,voltage):
    if voltage < 0: raise ValueError("Input voltage outside of range")
    elif voltage > 5: raise ValueError("Input voltage outside of range")
    coef = getBestCali(sensor)
    result = 0
    for n in range(len(coef)):
        result += coef[n]*(np.power(voltage,n))
    return result

def loadAllCaliPtsAsObjects():
    """returns a mess... probably don't use this unless you're the author and wrapping useful functions."""
    ptsData = np.load("MpembaCaliPts.npy",allow_pickle=True)
    return ptsData

def loadAllCaliPtsForSensorAsPoints(sensor):
    """Returns a list of all calibration points for a specified sensor as tuples of (voltage,temperature)"""
    return loadAllCaliPtsAsObjects()[sensor]
def loadAllCaliPtsForSensor(sensor):
    """Returns a list of all calibration points for a specified sensor as tuples of (voltage,temperature)"""
    return loadAllCaliPtsAsObjects()[sensor]

def loadAllCaliPtsForSensorAsTwoLists(sensor):
    """Returns a list of two lists, the first item containing the voltages, and the second containing the temperatures"""
    return np.transpose(loadAllCaliPtsForSensorAsPoints(sensor))

def plotAllCaliPtsForSensor(sensor):
    data = loadAllCaliPtsForSensorAsTwoLists(sensor)
    return plt.plot(data[0],data[1],"o")

def convertVoltagesToTemps(sensor,voltages):
    result = []
    for voltage in voltages:
        result.append(caliVoltage(sensor,voltage))
    return result

def cVtT(s,vs):
    return convertVoltagesToTemps(s,vs)
    
#Rerouting Functions
def getCali(sensor): return getBestCali(sensor)
def getCaliAll(): return getBestCaliAll()
def getLastUpdate(): return LastUpdate

if __name__ == '__main__':
    testvoltages = [4,3.6,2]
    print(len(testvoltages))
    print(convertVoltagesToTemps(1,testvoltages))