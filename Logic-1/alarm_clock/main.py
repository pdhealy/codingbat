# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

# Version 1 (My Attempt)
def alarm_clock(day, vacation):
  if vacation:
    if 1 <= day <= 5:
      return "10:00"
    else:
      return "off"
  else:
    if 1 <= day <= 5:
      return "7:00"
    else:
      return "10:00"

# Version 2 (Optimized)
def alarm_clock(day, vacation):
  if vacation:
    return "10:00" if 1 <= day <= 5 else "off"
  else:
    return "7:00" if 1 <= day <= 5 else "10:00"

if __name__ == "__main__":
    # Example test cases
    print(alarm_clock(1, False))  # Output: '7:00'
    print(alarm_clock(5, False))  # Output: '7:00'
    print(alarm_clock(0, False))  # Output: '10:00'
    print(alarm_clock(6, False))  # Output: '10:00'
    print(alarm_clock(0, True))   # Output: 'off'
    print(alarm_clock(6, True))   # Output: 'off'
    print(alarm_clock(1, True))   # Output: '10:00'
    print(alarm_clock(3, True))   # Output: '10:00'
    print(alarm_clock(5, True))   # Output: '10:00'
