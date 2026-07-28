import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
              
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Also asks whether they want to filter by month, day, both or not at all.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
        (str) day - name of the day of week to filter by, or "all"
    """
    print("Hello! Let's explore some US bikeshare data!")

    while True:
        city = input(
            "\nWhich city would you like to explore?\n"
            "Enter: chicago, new york city, or washington\n> "
        ).lower()

        if city in CITY_DATA:
            print(f"\nYou selected: {city.title()}")
            break
        else:
            print(f'\nSorry! "{city}" is not a valid city. Please try again.')
            print("Please choose from: chicago, new york city, or washington\n")

    while True:
        filter_type = input(
            "\nWould you like to filter by month, day, both, or not at all?\n> "
        ).lower()

        if filter_type in ['month', 'day', 'both', 'not at all']:
            break
        else:
            print("Invalid choice. Please enter: month, day, both, or not at all.")

    if filter_type == 'month':
        while True:
            month = input("Enter month: ").lower()
            if month in MONTH_DATA:
                day = 'all'
                break
            else:
                print("Invalid month. Please try again.")

    elif filter_type == 'day':
        while True:
            day = input("Enter day: ").lower()
            if day in DAY_DATA:
                month = 'all'
                break
            else:
                print("Invalid day. Please try again.")

    elif filter_type == 'both':
        while True:
            month = input("Enter month: ").lower()
            if month in MONTH_DATA:
                break
            else:
                print("Invalid month. Please try again.")

        while True:
            day = input("Enter day: ").lower()
            if day in DAY_DATA:
                break
            else:
                print("Invalid day. Please try again.")

    else:
        month = 'all'
        day = 'all'

    print(f"\nYou will now explore data for: {city.title()}")
    print(f"Loading file: {CITY_DATA[city]}")
    print('-' * 40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Returns the filtered data.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
   
    if month !='all':
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1
         df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel including the most common month, day of week."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print(f'Most Common Month: {months[common_month - 1]}')

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most Common Day: {common_day}')

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f'Most Common Start Hour: {common_hour}')
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most Common Start Station: {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most Common End Station: {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Start to End'].mode()[0]
    print(f'Most Common Trip: {common_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total Travel Time: {total_travel_time}')
    
   
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Average Travel Time: {mean_travel_time}')
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:')
    print(user_types)
    
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Counts:')
        print(gender_counts)
    else:
        print('\nGender data not available for this city.')

    # TO DO: Display counts of gender
  

    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print(f'\nEarliest Birth Year: {earliest_birth_year}')

        most_recent_birth_year = df['Birth Year'].max()
        print(f'Most Recent Birth Year: {most_recent_birth_year}')

        most_common_birth_year = df['Birth Year'].mode()[0]
        print(f'Most Common Birth Year: {most_common_birth_year}')
    else:
        print('\nBirth year data not available for this city.')
          
    # TO DO: Display earliest, most recent, and most common year of birth
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        show_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
        
        start_loc = 0
        while show_data =='yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            show_data = input('\nWould you like to view the next 5 rows? Enter yes or no.\n').lower()
            
      
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
