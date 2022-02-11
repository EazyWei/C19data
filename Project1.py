"""
202210.CAP4630.10979 Project 1 - Python Basics
Intro to AI - Liu
This python program reads data from a csv file and provides the user with a main menu
User may print reports, sort by name using quicksort, sort by case fatality rate using mergesort
Find and print a state using binary search if sorted by name and linear search otherwise
Print a Spearman's p correlation matrix containing state COVID data
Program handles invalid inputs and loops until user exits
Author: Jonathan Shih
Version: 2/11/2022
Email: N01447401@unf.edu
"""

# contains States
database = []
# to determine whether binary or linear search is used
name_sorted = False


# State class
class State:
    """
    State class creates an object representing a real-life US state
    containing attributes related to census info and COVID data
    """
    def __init__(self, name, cap, region, seats, pop, cases, deaths, rates, income, crime):
        self.name = name
        self.cap = cap
        self.region = region
        self.seats = seats
        self.pop = pop
        self.cases = cases
        self.deaths = deaths
        self.rates = (float(rates)/100)
        self.income = income
        self.crime = crime
        self.cfr = (float(deaths)/float(cases))
        self.case_rate = (float(cases)/float(pop))*100000
        self.death_rate = (float(deaths)/float(pop))*100000

    def get_cfr(self):
        format_cfr = "{:.6f}".format(self.cfr)
        return str(format_cfr)

    def set_cfr(self, cfr):
        self.cfr = cfr

    def get_case_rate(self):
        format_case_rate = "{:.2f}".format(self.case_rate)
        return str(format_case_rate)

    def set_case_rate(self, case_rate):
        self.case_rate = case_rate

    def get_death_rate(self):
        format_death_rate = "{:.2f}".format(self.death_rate)
        return  str(format_death_rate)

    def set_death_rate(self, death_rate):
        self.death_rate = death_rate

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cap(self):
        return self.cap

    def set_cap(self, cap):
        self.cap = cap

    def get_region(self):
        return self.region

    def set_region(self, region):
        self.region = region

    def get_seats(self):
        return self.seats

    def set_seats(self, seats):
        self.seats = seats

    def get_pop(self):
        return self.pop

    def set_pop(self, pop):
        self.pop = pop

    def get_cases(self):
        return self.cases

    def set_cases(self, cases):
        self.cases = cases

    def get_deaths(self):
        return self.deaths

    def set_deaths(self, deaths):
        self.deaths = deaths

    def get_rates(self):
        format_rate = "{:.3f}".format(self.rates)
        return str(format_rate)

    # FVR
    def set_rates(self, rates):
        self.rates = rates

    def get_income(self):
        return self.income

    def set_income(self, income):
        self.income = income

    def get_crime(self):
        return self.crime

    def set_crime(self, crime):
        self.crime = crime

    def __gt__(self, other):
        x = self.name
        y = other.name
        if x > y:
            return True

    def __str__(self):
        return State.__str__(self) + str(self.name) + str(self.mhi) + str(self.crime) + str(self.cfr) + str(self.cases)\
               + str(self.death_rate) + str(self.rates)


def readfile():
    """
    Opens states.csv file, reads and inputs data into State objects and appends to the database
    """
    with open('states.csv') as states:
        global database
        reader = states.readlines()
        # states.close()
        for item in reader[1:]:
            # print(item)
            data = item.split(",")
            database.append(State(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                                  data[9].rstrip("\n")))
        print("\nThere were " + str(len(database)) + " state records read from States.csv.\n")


def state_report():
    """
    Prints entire State database with formatting specified by the project
    """
    global database
    print("Name".ljust(20)+"MHI".ljust(10)+"VCR".ljust(10)+"CFR".ljust(12)+"Case Rate".ljust(15)+"Death Rate".ljust(15)
          + "FVR".ljust(15))
    print("------------------------------------------------------------------------------------------")
    for State in database:
        print("".join(State.get_name().ljust(20))+"".join(State.get_income().ljust(10))+
              "".join(State.get_crime().ljust(10))+"".join(State.get_cfr().ljust(12))+
              "".join(State.get_case_rate().ljust(15))+"".join(State.get_death_rate().ljust(15))+
              "".join(State.get_rates().ljust(15)))
    # print("\n")


def partition(array, start, end):
    """
    Supports Quicksort method by providing sorting
    :param array: array to be sorted
    :param start: first index
    :param end: last index
    :return: pointer for dividing the array
    """
    i = (start - 1)
    pivot = array[end].get_name()

    for j in range(start, end):
        if array[j].get_name() <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]
    return i+1


def quicksort(array, start, end):
    """
    Standard quicksort algorithm
    :param array: to be sorted
    :param start: first index
    :param end: last index
    """
    if start < end:
        p = partition(array, start, end)

        quicksort(array, start, p-1)
        quicksort(array, p+1, end)


def sort_by_name():
    """
    Calls quicksort to sort the database by State name
    Sets name_sorted to True for Binary Searching by State name
    """
    global database
    quicksort(database, 0, len(database)-1)
    global name_sorted
    name_sorted = True
    print("List is sorted by name")


def binary_search(arr, left, r, x):
    """
    Binary search algorithm for searching a State by name when sorted by name
    :param arr: array to search
    :param left: left sub-array
    :param x: right sub-array
    :return: -1 if not found
    """
    if left > r:
        return -1
    else:
        mid = (left + r)//2
        if arr[mid].name == x:
            return mid
        elif arr[mid].name > x:
            return binary_search(arr, left, mid-1, x)
        elif arr[mid].name < x:
            return binary_search(arr, mid+1, r, x)
        else:
            return -1


def name_search():
    """
    Support searching a State by name
    If sorted by name, calls binary search
    If not sorted by name, uses linear search
    """
    global name_sorted
    key = input("Please enter the name of a state to search: ")
    if name_sorted is True:
        print("List sorted by name. Binary search engaged...")
        index = binary_search(database, 0, len(database)-1, key)
        if index == -1:
            print("State not found.")
        else:
            print("Name: ".ljust(15) + database[index].get_name())
            print("MHI: ".ljust(15) + database[index].get_income())
            print("VCR: ".ljust(15) + database[index].get_crime())
            print("CFR: ".ljust(15) + database[index].get_cfr())
            print("Case Rate: ".ljust(15) + database[index].get_case_rate())
            print("Death Rate: ".ljust(15) + database[index].get_death_rate())
            print("FV Rate: ".ljust(15) + database[index].get_rates())

    else:
        print("List not sorted by name. Linear search engaged...")
        hit = 0
        for state in database:
            if state.get_name() == str(key):
                hit = 1
                print("Name: ".ljust(15) + state.get_name())
                print("MHI: ".ljust(15) + state.get_income())
                print("VCR: ".ljust(15) + state.get_crime())
                print("CFR: ".ljust(15) + state.get_cfr())
                print("Case Rate: ".ljust(15) + state.get_case_rate())
                print("Death Rate: ".ljust(15) + state.get_death_rate())
                print("FV Rate: ".ljust(15) + state.get_rates())
                break
        if hit == 0:
            print("State not found.")


def mergesort(arr):
    """
    Mergesort sorting algorithm used to sort database by Case Fatality Rate
    :param arr: array to be sorted
    :return: sorted array
    """
    global name_sorted
    name_sorted = False
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i].cfr < right[j].cfr:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


def sort_mhi(arr):
    """
    Sorts database by median household income
    :param arr: to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx].income > arr[j].income:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def sort_case_rate(arr):
    """
    Sorts database by case rate
    :param arr: to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx].case_rate > arr[j].case_rate:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def sort_crime_rate(arr):
    """
    Sorts database by crime rate
    :param arr: to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx].crime > arr[j].crime:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def sort_death_rate(arr):
    """
    Sorts database by death rate
    :param arr: to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx].death_rate > arr[j].death_rate:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def sort_fvr(arr):
    """
    Sorts database by fall vaccination rate
    :param arr: to be sorted
    :return: sorted array
    """
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx].rates > arr[j].rates:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def spearman_corr(X, Y):
    """
    Calculates Spearman's correlation between two lists
    :param X: First array
    :param Y: Second array
    :return: p correlation value
    """

    di = []
    n = len(X)
    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i].name == Y[j].name:
                d = i - j
                di.append(d)
                break
    # print(di)
    di_squared = [number ** 2 for number in di]
    total = sum(di_squared)
    p = float(1-((6*total)/(n*((n*n)-1))))
    #print(p)
    return p


def spearman_matrix():
    global name_sorted
    X = database
    Y = database.copy()
    a = spearman_corr(sort_case_rate(X), sort_mhi(Y))
    b = spearman_corr(sort_case_rate(X), sort_crime_rate(Y))
    c = spearman_corr(sort_case_rate(X), sort_fvr(Y))
    d = spearman_corr(sort_death_rate(X), sort_mhi(Y))
    e = spearman_corr(sort_death_rate(X), sort_crime_rate(Y))
    f = spearman_corr(sort_death_rate(X), sort_fvr(Y))
    name_sorted = False
    """
    Prints the matrix containing the Spearman's p Correlation data
    """
    print("----------------------------------------------------------")
    print("|            |      MHI     |     VCR     |     FVR      |")
    print("----------------------------------------------------------")
    print("| Case Rate  |  {:.7f}  |  {:.7f}  |  {:.7f}  |".format(a, b, c))
    print("----------------------------------------------------------")
    print("| Death Rate |  {:.7f}  |  {:.7f}  |  {:.7f}  |".format(d, e, f))
    print("----------------------------------------------------------")
    print()


def print_menu():
    """
    Prints the main menu to terminal
    """
    print(30 * "-", "MENU", 30 * "-")
    print("1. Print a state report")
    print("2. Sort by name")
    print("3. Sort by case fatality rate")
    print("4. Find and print a state from a given name")
    print("5. Print Spearman's rho matrix")
    print("6. Quit")
    print(67 * "-")


def main_menu():
    """
    Offers the main menu with several options for user
    Performs various functions 1-6 based on user input
    Loops continuously until manually exited by user
    Handles erroneous input
    """
    loop = True
    readfile()
    while loop:

        print_menu()
        choice = str(input("Enter your choice [1-6]: "))

        if choice == str(1):
            print("Option 1: state report\n")
            state_report()
        elif choice == str(2):
            print("Option 2: sort by name")
            sort_by_name()
        elif choice == str(3):
            print("Option 3: sort by case fatality rate")
            print("List is merge sorted by case fatality rate")
            mergesort(database)
        elif choice == str(4):
            print("Option 4: search by name")
            name_search()
        elif choice == str(5):
            global name_sorted
            print("Option 5: Spearman's rho matrix\n")
            spearman_matrix()
            # state_report()
        elif choice == str(6):
            print("Have a nice day!\n")
            loop = False
        else:
            input("Invalid input. Enter any key to try again.")


main_menu()






