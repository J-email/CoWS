# ALL DATA IN METRIC UNLESS SPECIFIED

def elevation_to_volume(elevation):
    volume = input("elevation: " + str(elevation) + "\n" + "volume: ")
    return volume


def area_to_volume(area):
    volume = input("area: " + str(area) + "\n" + "volume: ")
    return volume


def volume_to_elevation(volume):
    elevation = input("volume: " + str(volume) + "\n" + "elevation: ")
    return elevation


def volume_to_area(volume):
    area = input("volume: " + str(volume) + "\n" + "area: ")
    return area


def elevation_to_area(elevation):
    return volume_to_area(elevation_to_volume(elevation))


def area_to_elevation(area):
    return volume_to_elevation(area_to_volume(area))

def population(year):
    return 0

def coloradoRiver(year):
    return 0

def lasVegasWash(year):
    return 0

def SNWA(year):
    return 0

def hooverDam(year):
    return 0

def inflow(year):
    return 0

def outflow(year):
    return 0

def evaporation(year):
    return 0

def
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startYear = 2020
    startVolume = 100
    endYear = 2050
    currentYear = startYear

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
