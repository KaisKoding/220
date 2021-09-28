def main():
    # ask how many roads were surveyed
    global, avg_cars
    roads = eval(input(" How many roads were surveyed?: "))

    # Overall cars traveled across roads/ days
    overall_cars = 0

    # ask user how many days
    for d in range(0, roads):
        days = eval(input(" How many days was road surveyed?: "))

        # ask user how many cars traveled in certain day
        sum_of_cars = 0

        for c in range(0, days):
            cars = eval(input(" How many cars traveled on day?: "))

            # get the sum of cars
            sum_of_cars = sum_of_cars + cars

            # average the sum of cars
            avg_cars = sum_of_cars / days

        print("Road average vehicles per day: ", avg_cars)

    # Average cars across all roads/ days
    total_avg_cars = overall_cars / roads

    print("Total number of vehicles traveled on roads: ", overall_cars)

    print("Average number of vehicles per road:", round(total_avg_cars, 2))


main()
