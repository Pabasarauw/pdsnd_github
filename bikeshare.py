import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = CITY_DATA.keys()
    while True:
        city=input('\nOut of Chicago, New york city, Washington, which city you would like to explore?')
        if city.lower() not in cities:
            print('\nPlease choose one of Chicago, New york city or Washington')
        else:
            city.lower() in cities
            print('\nYou have chosen:{}'.format(city.title()))
            break         
                

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month=input('\nWhich month [january, february, march, april, may, june or all] you would like to explore?')
        if month.lower() not in months:
            print('\nPlease choose a valid month from january to june or all')
        else:
                  month.lower() in months
                  print('\nYou have chosen:{}'.format(month.title()))
                  break
                
                          
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while True:
        day=input('\nWhich day of the week (sunday, monday, tuesday, wednesday, thursday, friday, saturday or all) you would like to explore?')
        if day.lower() not in days:
            print('\nPlease choose a valid day from sunday, monday, tuesday, wednesday, thursday, friday, saturday or all')
        else:
                  day.lower() in days
                  print('\nYou have chosen:{}'.format(day.title()))
                  break
    
    print('-'*40)
    return city, month, day


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
    # convert the Start Time column to datetime#
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns#
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month#
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int#
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe#
        df = df[df['month'] == month]
        
    # filter by day#
    if day.lower() != 'all':
        # filter by day to create the new dataframe#
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)
    

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', most_common_day)
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # dispaly how many start and end stations are there
    number_of_start_stations = df['Start Station'].value_counts().count()
    number_of_end_stations = df['End Station'].value_counts().count()
    print('Number of start and end stations:', 'Start stations =', number_of_start_stations, ' , ', 'End stations =',  number_of_end_stations)
    
    # TO DO: display most commonly used start station
    most_commonly_used_start_station =df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', most_commonly_used_start_station)
    

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', most_commonly_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_stations = (df['Start Station'] + "to" + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip:', most_frequent_start_end_stations) 
    
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round((df['Trip Duration'].sum())/(60*60))
    print('Total travel time:', total_travel_time,'hours')


    # TO DO: display mean travel time
    mean_travel_time = round((df['Trip Duration'].mean())/60)
    print('Mean travel time:', mean_travel_time,'minutes')
    
    # Highest trip duration is between which stations
    Highest_trip_duration = df.loc[df['Trip Duration'].idxmax()]
    print ('Highest trip duration is between:', Highest_trip_duration['Start Station'] + ' to ' + Highest_trip_duration['End Station'] ) 

    #Lowest trip duration is between which stations
    lowest_trip_duration = df.loc[df['Trip Duration'].idxmin()]
    print ('Lowest trip duration is between:', lowest_trip_duration['Start Station'] + ' to ' + lowest_trip_duration['End Station'] ) 
    
    # median of the trip duration
    x = np.array(df['Trip Duration'])
    median_trip_duration = (np.median(x))/60
    print('Median of trip duration:', np.around(median_trip_duration, decimals=2), 'minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Bikeshare user types:')
    print(user_types)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender distribution of Bikeshare users:') 
        print(gender_counts)

    # Display female prefered station
    if "Gender" in df.columns:
        female_prefered_start_station = df.loc[df['Gender'] == 'Female', ['Start Station']]
        female_prefered_end_station = df.loc[df['Gender'] == 'Female', ['End Station']]
        print ('\nStations popular with female users:') 
        print('Start -', (female_prefered_start_station['Start Station'].value_counts().idxmax()))
        print('End -',(female_prefered_end_station['End Station'].value_counts().idxmax()))                              
                                         
   # Display male prefered station
    if "Gender" in df.columns:
        male_prefered_start_station = df.loc[df['Gender'] == 'Male', ['Start Station']]
        male_prefered_end_station = df.loc[df['Gender'] == 'Male', ['End Station']]
        print ('\nStations popular with male users:') 
        print('Start -', (male_prefered_start_station['Start Station'].value_counts().idxmax()))
        print('End -',(male_prefered_end_station['End Station'].value_counts().idxmax()))    


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].max()
        most_recent_birth_year = df['Birth Year'].min()
        common_year_of_birth = df['Birth Year'].mode()[0]
        print('\nThe year the oldest user was born:', earliest_birth_year)
        print('\nThe year the youngest user was born:', most_recent_birth_year)
        print('\nThe year most users were born:', common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Displays raw Bikeshare data"""
    print('\nDisplay raw data...\n')
    start_time = time.time()
    
    head = 0
    tail = 5
    
    while True:
        raw = input(('\nWould you like to view 5 or more lines of Bikeshare raw data? Enter yes or no.\n'))
        if raw.lower() != 'yes':
           break
        else:
            print(df[df.columns[0:-1]].iloc[head:tail])
            head +=5
            tail +=5 
   
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        


if __name__ == "__main__":
	main()
