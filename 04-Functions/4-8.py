def time_string(hour,minute,format):
    if format not in [12, 24]:
        return "Invalid format!"
    if hour < 0 or hour > 23 and minute < 0 or minute > 59:
        return "Invalid time!"
    if format == '24':
        return f"{hour:02}:{minute:02}"
    else: 
        period = 'AM' if hour < 12 else 'PM'
        hour12 = hour % 12
        hour12 = hour12 if hour12 != 0 else 12  
        return f"{hour12}:{minute:02} {period}"

hour = int(input("Input hour (0-23): "))
minute = int(input("Input minutes (0-59): "))
format = int(input("Input format (12/24): "))
time = time_string(hour,minute,format)
print (time)