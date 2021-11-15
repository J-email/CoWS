# ALL DATA IN METRIC UNLESS SPECIFIED
import random
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

volumeB = [0.153, 1.00700, 2.00600, 3.15600, 4.47500, 5.98100, 7.68300, 9.60100, 11.73500, 14.09200, 16.73300, 19.72800, 23.14400, 26.973000]
areaB = [31.20, 37.10, 42.90, 49.20, 56.40, 64.10, 72.20, 81.10, 89.30, 99.30, 112.30, 128.40, 144.80, 160.70]
heightB = [900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225]
model = np.poly1d(np.polyfit(volumeB, heightB, 3))


def volume_to_area(volume):
    return -0.01162 * volume ** 2 + 5.062 * volume + 32.6


def volume_to_elevation(volume):
    return 0.01242 * volume ** 3 - 0.8166 * volume ** 2 + 25.08 * volume + 900.6


def population(year):
    return startPopulation * (1.03 ** (year - startYear))


def coloradoRiver(year):
    if currentYear < 2001:
        return 12
    return 9 * (0.97 ** (currentYear - 2001))


def lasVegasWash(year):
    return 0.7


def virginRiver(year):
    return 0.3


def SNWA(year):
    return 0.45 * population(year) / startPopulation


def hooverDam(year):
    if volume_to_elevation(currentVolume) < 1000:
        return 9
    return 9.4


def inflow(year):
    return coloradoRiver(year) + lasVegasWash(year) + virginRiver(year)


def outflow(year):
    return hooverDam(year) + SNWA(year)


def evaporation(year):
    return 65615.8 * volume_to_area(lastVolume) / 1000000


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    step = 1/2048
    startYear = 1980
    startPopulation = 2772000
    endYear = 2020
    currentYear = startYear
    currentVolume = 24
    lastVolume = currentVolume
    # prfloat(population(2000))
    x, y, z, u = [], [], [], []
    for i in range(1980, 2022):
        z.append(i)
    u = [1201.572, 1200.94, 1199.958, 1210.452, 1207.838, 1207.21, 1203.94, 1208.608, 1209.64, 1198.822, 1188.626, 1178.496, 1178.814, 1190.058, 1187.23, 1180.646, 1193.016, 1198.242, 1213.408, 1210.822, 1211.166, 1193.33, 1171.276, 1150.758, 1136.776, 1142.93, 1137.444, 1124.254, 1113.34, 1105.758, 1099.238, 1095.512, 1127.992, 1116.864, 1100.082, 1083.592, 1079.646, 1086.114, 1085.662, 1087.878, 1095.45, 1082.08]
    while currentYear < endYear:
        currentYear += step
        deltaYear = currentYear - startYear
        lastVolume = currentVolume
        currentVolume += step * (inflow(currentYear) - outflow(currentYear) - evaporation(currentYear))
        x.append(currentYear)
        y.append(volume_to_elevation(currentVolume))
        if currentVolume == 0:
            break
    plt.plot(x, y)
    plt.plot(z, u)
    for i in range(len(x)):
        print(str(x[i]) + " " + str(y[i]))
    plt.show()
    print(model)
