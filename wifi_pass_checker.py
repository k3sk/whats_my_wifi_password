# downloading the Subprocess module needed for the project
import subprocess

# This here is getting the list of all Wi-Fi profiles (registerd wifi you had typed in)
command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [profile.split(":")[1][1:-1] for profile in command_output if "All User Profile" in profile]

# Looking at each profiles and find what the password is.
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    password = [result.split(":")[1][1:-1] for result in results if "Key Content" in result]

    # Printing the profile name and password
    try:
        print(f"{profile:<30}|  {password[0]:<}")  # Using f-strings for better readability
    except IndexError:
        print(f"{profile:<30}|  {'':<}")  # Handle empty passwords which were incorrect

# Waitin for user input to prevent the console from closing
input("")