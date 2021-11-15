# ALL DATA IN METRIC UNLESS SPECIFIED
import random

from matplotlib import pyplot as plt


def volume_to_area(volume):
    return 4 * volume + 50


def area_to_volume(area):
    return (area - 50) / 4


def population(year):
    return startPopulation * (1.03 ** (year - startYear))


def coloradoRiver(year):
    if currentYear <= 2001:
        return 22
    return 15 * (0.999 ** (currentYear - 2001))


def lasVegasWash(year):
    return 0.7


def SNWA(year):
    return 0.45 * population(year) / 2772000


def hooverDam(year):
    return 9.6


def inflow(year):
    return coloradoRiver(year) + lasVegasWash(year)


def outflow(year):
    return hooverDam(year) + SNWA(year)


def evaporation(year):
    return 65615.8 * volume_to_area(lastVolume) / 1000000


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    step = 1/2048
    startYear = 1980
    startPopulation = 2772000
    endYear = 2050
    currentYear = startYear
    currentVolume = 34
    lastVolume = currentVolume
    # prfloat(population(2000))
    x, y, z, u = [], [], [], []
    for i in range(1980, 2022):
        z.append(i)
    u = [1201.572, 1200.94, 1199.958, 1210.452, 1207.838, 1207.21, 1203.94, 1208.608, 1209.64, 1198.822, 1188.626, 1178.496, 1178.814, 1190.058, 1187.23, 1180.646, 1193.016, 1198.242, 1213.408, 1210.822, 1211.166, 1193.33, 1171.276, 1150.758, 1136.776, 1142.93, 1137.444, 1124.254, 1113.34, 1105.758, 1099.238, 1095.512, 1127.992, 1116.864, 1100.082, 1083.592, 1079.646, 1086.114, 1085.662, 1087.878, 1095.45, 1082.08]
    for i in range(len(u)):
        u[i] = area_to_volume(u[i]) - 255
    while currentYear < endYear:
        currentYear += step
        deltaYear = currentYear - startYear
        lastVolume = currentVolume
        currentVolume += step * (inflow(currentYear) - outflow(currentYear) - evaporation(currentYear))
        x.append(currentYear)
        y.append(currentVolume)
    plt.plot(x, y)
    plt.plot(z, u)
    for i in range(len(x)):
        print(str(x[i]) + " " + str(y[i]))
    plt.show()
