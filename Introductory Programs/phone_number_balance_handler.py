initial_balance = 98.6
user_name = input("Please Enter your Name: ")
phone_number = input("Please Enter your phone number: ")  # Keep as string to preserve formatting like leading 0s
call_minutes = float(input("Enter your call duration (minutes): "))
call_seconds = float(input("Enter your call duration (seconds): "))
cost_per_minute = 0.6

# Calculate total call duration in minutes
call_duration = call_minutes + (call_seconds / 60)

# Calculate total cost of the call
total_cost_of_call = call_duration * cost_per_minute

# Calculate remaining balance
remaining_balance = initial_balance - total_cost_of_call

# Final output using f-string for clean formatting
print(f"\nDear {user_name},")
print(f"NPR {total_cost_of_call:.2f} has been deducted from your account balance ({initial_balance} NPR) for a call of duration {call_duration:.2f} minutes.")
print(f"Your remaining balance is NPR {remaining_balance:.2f}.")
print(f"Phone number: {phone_number}")
print("\nPlease dial 6969 to subscribe to data packages.")
print("Thank you!")
print("Namaste dhogdiya, timro herai le mero dhadkan rokdiya ")
