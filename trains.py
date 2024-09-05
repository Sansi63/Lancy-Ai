from lansy import *
import requests

def get_train_details(train_type, source_station, destination_station):
    url = "https://trains.p.rapidapi.com/v1/railways/trains/india"
    
    # Modify payload based on the train type provided by the user
    payload = { "search": train_type }
    
    headers = {
        "x-rapidapi-key": "c97d49d091msh20e539d1aad2a81p13ba7fjsn0df2a07e0880",
        "x-rapidapi-host": "trains.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    # Make API request
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Return the train data
    else:
        return None

def process_train_data(train_data, source_station, destination_station):
    if train_data:
        found_trains = []
        for train in train_data:
            if train['train_from'] == source_station and train['train_to']== destination_station:
                train_name = train.get('name', 'Unknown Train')
                train_number = train.get('train_num', 'Unknown Number')
                departure_time = train['data'].get('departTime', 'Unknown Time')
                arrival_time = train['data'].get('arriveTime', 'Unknown Time')
                running_days = train['data'].get('days', {})
                available_classes = ", ".join(train['data'].get('classes', []))
                
                # Add matched train to the list
                found_trains.append({
                    "train_name": train_name,
                    "train_number": train_number,
                    "departure_time": departure_time,
                    "arrival_time": arrival_time,
                    "running_days": running_days,
                    "available_classes": available_classes
                })

        if found_trains:
            speak("Here are the available trains:")
            for train in found_trains:
                # Output the train details
                speak(f"Train Name: {train['train_name']}")
                speak(f"Train Number: {train['train_number']}")
                speak(f"Departure Time: {train['departure_time']}")
                speak(f"Arrival Time: {train['arrival_time']}")
                speak(f"Available Classes: {train['available_classes']}")
                speak(f"Running Days: {', '.join([f'{day}: {status}' for day, status in train['running_days'].items()])}")
                # Print details to console for debugging
                print(f"Train Name: {train['train_name']}")
                print(f"Train Number: {train['train_number']}")
                print(f"Departure Time: {train['departure_time']}")
                print(f"Arrival Time: {train['arrival_time']}")
                print(f"Available Classes: {train['available_classes']}")
                print(f"Running Days: {train['running_days']}")
        else:
            speak(f"Sorry, no trains found from {source_station} to {destination_station}.")
            print("No matching trains found.")
    else:
        speak("Sorry, I couldn't retrieve any train details at the moment.")
        print("No train data found or API request failed.")

if __name__ == "__main__":
    speak("Please tell me the type of train, for example, Shatabdi or Rajdhani.")
    train_type = takecommand()

    speak("Please tell me the source station.")
    source_station = takecommand().upper()

    speak("Please tell me the destination station.")
    destination_station = takecommand().upper()

    # Fetch train details based on the input
    train_data = get_train_details(train_type, source_station, destination_station)
    # train_data = get_train_details("Shatabdi", "HWH", "RNC")
    
    # Process and announce train details
    process_train_data(train_data, source_station, destination_station)
    # process_train_data(train_data, "HWH", "RNC")
