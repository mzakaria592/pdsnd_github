import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Inputs#
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city: ")
    while city.lower() not in ["chicago", "new york city", "washington"]:
        print("\nInvalid city")
        city = input("Please enter the name of the city: ")

    # get user input for month (all, january, february, ... , june)
    month = input("Enter the month: ")
    while month.lower() not in ["all", "january", "february", "march", "april", "may", "june"]:
        print("\nInvalid")
        month = input("Please enter month: ")
    if month.lower() == "all":
        print("\nAll months are selected")
    else:
        print("\n{} is selected".format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day: ")
    while day.lower() not in ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
        print("\nInvalid")
        day = input("Please enter day: ")
    if day.lower() == "all":
        print("\nAll days are selected")
    else:
        print("\n{} is selected".format(day.title()))

    print('-'*40)
    return city, month, day
#1#
"""__________________________________________________________________________________________________"""

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name(locale='English')
    df['day'] = df['Start Time'].dt.weekday_name
    
    #Filtering months#
    if month.lower() in ["january", "february", "march", "april", "may", "june"]:
        df = df[df['month']==month.title()]
    
    #Filtering days#
    if day.lower() in ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
        df = df[df['day']==day.title()]
    
    return df
#2#
"""__________________________________________________________________________________________________"""

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    try:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month_name(locale='English')
        df['day'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour
    
        # display the most common month
        months = df['month'].value_counts()
        print("The most common month is ", str(months[[0]]))

        # display the most common day of week
        days = df['day'].value_counts()
        print("The most common day is ", str(days[[0]]))

        # display the most common start hour
        print("The most common hour is ", str(df['hour'].mode()[0]))
    
    except:
        print("No data found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#3#
"""__________________________________________________________________________________________________"""

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city.lower()])

    try:
        # display most commonly used start station
        start_stations = df['Start Station'].value_counts()
        print("The most common Start Station is ", str(start_stations[[0]]))

        # display most commonly used end station
        end_stations = df['End Station'].value_counts()
        print("The most common End Station is ", str(end_stations[[0]]))
    
        # display most frequent combination of start station and end station trip
        df["Combined Stations"] = df['Start Station'] + df['End Station']
        combined_station = df["Combined Stations"].value_counts()
        print("The most combination of start station and end station is: ", str(combined_station[[0]]))
    
    except:
        print("No data found")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#4#
"""__________________________________________________________________________________________________"""

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city.lower()])

    try:
        # display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print("The total travel time is ", str(total_travel_time))

        # display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print("The mean travel time is ", str(mean_travel_time))
    
    except:
        print("No data found")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#5#
"""__________________________________________________________________________________________________"""

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_count = df['User Type'].value_counts()
        print("User type count:\n", str(user_count))

        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Gender count:\n", str(gender_count))

        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        birth_year_count = df['Birth Year'].value_counts()
        print("The earliest year of birth is ", str(earliest_year))
        print("The most recent year of birth is ", str(most_recent_year))
        print("The most common year of birth is ", str(birth_year_count[[0]]))
    
    except:
        print("No data found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#6#
"""__________________________________________________________________________________________________"""

#Running program#
while True:
    city, month, day = get_filters()
    df = load_data(city, month, day)

    show_results = input("Enter the number of rows you want to show:\n (If you want to show all results, enter all)\n")    
    try:
        show_results = int(show_results)
    except:
        print("")
    while True:
        try:
            show_results = int(show_results)
        except:
            print("...")
        if type(show_results) is int:
            print(df.head(show_results))
            break
        elif show_results.lower() == "all":
            print(df)
            break
        else:
            print("Invalid")
            show_results = input("Enter the number of rows you want to show:\n (If you want to show all results, enter all)\n")

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break
