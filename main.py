# ALL DATA IN METRIC UNLESS SPECIFIED

def elevation_to_volume(elevation):
    volume = input("elevation: " + str(elevation) + "\n" + "volume: ")
    return int(volume)


def area_to_volume(area):
    volume = input("area: " + str(area) + "\n" + "volume: ")
    return int(volume)


def volume_to_elevation(volume):
    elevation = input("volume: " + str(volume) + "\n" + "elevation: ")
    return int(elevation)


def volume_to_area(volume):
    area = input("volume: " + str(volume) + "\n" + "area: ")
    return int(area)


def elevation_to_area(elevation):
    return int(volume_to_area(elevation_to_volume(elevation)))


def area_to_elevation(area):
    return int(volume_to_elevation(area_to_volume(area)))


def population(year):
    if year == 2021:
        return 2772000
    if year > 2021:
        return 1.03 * population(year - 1)
    return 0.97 * population(year + 1)


def coloradoRiver(year):
    return 15


def lasVegasWash(year):
    return 1 * population(year) / 2772000


def SNWA(year):
    return 2 * population(year) / 2772000


def hooverDam(year):
    return 0

def inflow(year):
    return coloradoRiver(year) + lasVegasWash(year)


def outflow(year):
    return hooverDam(year) + SNWA(year)


def evaporation(year):
    65.6158 * volume_to_area(lastVolume)
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startYear = 2020
    startVolume = 100
    endYear = 2050
    currentYear = startYear
    currentVolume = 25
    lastVolume = currentVolume
    # print(population(2000))
    for i in range(startYear, endYear):
        lastVolume = currentVolume
        currentVolume = inflow(i) - outflow(i) - evaporation(i)
        print(str(i) + "    " + str(currentVolume))


