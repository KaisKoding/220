def main():
    # ask how many roads were surveyed
    global avg_cars, sum_of_cars
    roads = eval(input(" How many roads were surveyed?: "))

    # Overall cars traveled across roads/ days
    overall_cars = 0

    # ask user how many days
    for d in range(0, roads):
        days = eval(input(" How many days was road %s surveyed?: " % (d + 1)))

        sum_of_cars = 0

        # ask user how many cars traveled in certain day
        for c in range(0, days):
            cars = eval(input(" How many cars traveled on day %s?: " % (c + 1)))

            # get the sum of cars
            sum_of_cars = sum_of_cars + cars

            # average the sum of cars
            avg_cars = sum_of_cars / days

        # add into overall cars
        overall_cars = overall_cars + sum_of_cars

        print("Road %s average vehicles per day: " % (d + 1), avg_cars)

    # Average cars across all roads/ days
    total_avg_cars = overall_cars / roads

    print("Total number of vehicles traveled on roads: ", overall_cars)

    print("Average number of vehicles per road:", round(total_avg_cars, 2))


if __name__ == "__main__":
    main()