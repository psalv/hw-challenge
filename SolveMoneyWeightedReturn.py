


def loadData():
    """
    Loads data from a standardized .csv datafile.

    :return: an array of arrays of the form [ [input, current market value], [..], ... ]
    """
    file = open("test.csv")
    results = []
    first = True
    for line in file:
        if line != "" and not first:
            line = line.rstrip().split(",")

            if len(line) == 3:

                results.append([float(line[1]), float(line[2])])
        first = False
    return results



def visit(currentNode, count, metric, data):
    """
    Determines if the given metric produces the intended end value in the inputted number of steps.

    :param currentNode: the value of our current position in the search
    :param count: our current position in the search
    :param metric: the possible MWR value
    :param data: the .csv file data array
    :return: true if we reach the end value in the allotted number of steps,
                false otherwise (we reach allotted steps without the reaching the end value)
    """

    count += 1

    currentNode *= 1 + metric

    if abs(currentNode - data[-1][-1]) < 0.01 and count == len(data) - 1:
        return True

    if count >= len(data) - 1:
        return False

    else:
        return visit(currentNode + data[count][0], count, metric, data)



def BFcheckPercentages():
    """Uses a BF algorithm to iteratively check the """

    data = loadData()

    toContinue = True

    metric = 0.001

    print(data)

    while(toContinue):

        print("\nCurrent MWR estimate: ", round(metric * 100, 3), "%")

        if visit(data[0][0], 0, metric, data):
            print("\n\nFound value, MWR: ", round(metric * 100, 3), "%")
            return round(metric * 100, 3)

        else:
            metric += 0.001

        if metric > 1:
            print("Did not find value.")
            return -1



BFcheckPercentages()

