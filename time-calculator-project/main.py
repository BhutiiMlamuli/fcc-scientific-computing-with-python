def add_time(start, duration, starting_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM':
        start_hour = start_hour + 12 if start_hour != 12 else 12
    else:  # AM
        start_hour = 0 if start_hour == 12 else start_hour
    
    # Add minutes
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    final_minute = total_minutes % 60
    
    # Add hours
    total_hours = start_hour + duration_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'
    
    # Format time string
    time_string = f"{final_hour}:{final_minute:02d} {final_period}"
    
    # Handle day of week if provided
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if starting_day:
        # Find the index of the starting day
        start_day_index = days.index(starting_day.capitalize())
        # Calculate the new day index
        new_day_index = (start_day_index + days_later) % 7
        new_day = days[new_day_index]
        time_string += f", {new_day}"
    
    # Add day information
    if days_later == 1:
        time_string += " (next day)"
    elif days_later > 1:
        time_string += f" ({days_later} days later)"
    
    return time_string