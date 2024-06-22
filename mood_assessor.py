import datetime
import os

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Function to write the integer to the file
def write_integer(date,integer):
    file_path = os.path.join('data', 'mood_diary.txt')
    with open(file_path, 'a') as file:
        file.write(f"{date} {integer}\n")

# Function to read the entries from the file
def read_mood_file():
    file_path = os.path.join('data', 'mood_diary.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    return []

#Function to check if a day's mood has already entered 
def check(date):
    entries = read_mood_file()
    for entry in entries:
        if entry.startswith(date):
            return True
    return False

#Function to print out the result
def result_print():
    entries = read_mood_file()
    if len(entries) < 7:
        return
    recent_entries = [int(entry.split()[1]) for entry in entries[-7:]]
    happy_days = recent_entries.count(2)
    sad_days = recent_entries.count(-1)
    apathetic_days = recent_entries.count(0)
    
    if happy_days >= 5:
        diagnosis = "manic"
    elif sad_days >= 4:
        diagnosis = "depressive"
    elif apathetic_days >= 6:
        diagnosis = "schizoid"
    else:
        average_mood = round(sum(recent_entries) / 7)
        diagnosis_map = {2: "happy", 1: "relaxed", 0: "apathetic", -1: "sad", -2: "angry"}
        diagnosis = diagnosis_map[average_mood]
    print(f"Your diagnosis: {diagnosis}!")

#Main function here
def assess_mood():
    date_today = datetime.date.today() # get the date today as a date object
    date_today = str(date_today) # convert it to a string
    for run in range (1,8):
        if check(date_today):
            print('Sorry, you have already entered your mood today.')
            return
        flag = True
        while flag:
            mood = input(f'enter your mood day{run}:').strip().lower()
            if mood in ['happy', 'relaxed', 'apathetic', 'sad', 'angry']:
                flag = False
            else:
                print('invalid mood enter again')
        if mood == 'happy':
            write_integer(date_today,2)
        elif mood =='relaxed':
            write_integer(date_today,1)
        elif mood == 'apathetic':
            write_integer(date_today,0)
        elif mood == 'sad':
            write_integer(date_today,-1)
        elif mood == 'angry':
            write_integer(date_today,-2)
        result_print()
        
      






