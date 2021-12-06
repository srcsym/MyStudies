import requests
import json

my_solution="srcsymmysolution"
flights_url="https://api.skypicker.com/flights?flyFrom=VIE&to=JFK&v=3&partner=" + my_solution
check_url="https://booking-api.skypicker.com/api/v0.1/check_flights?v=2&bnum=0&pnum=1&currency=USD&adults=1&children=0&infants=0&affily=" + my_solution

flights_response=requests.get(flights_url)

if(flights_response.ok):

    flights_data=json.loads(flights_response.content)
    for item in flights_data["data"]:
        check_full_url=check_url +"&booking_token=" + item["booking_token"]
        check_full_response=requests.get(check_full_url)

        if(check_full_response.ok):
            check_full_data=json.loads(check_full_response.content)

            if (check_full_data["flights_to_check"]==False and check_full_data["flights_checked"]==True and check_full_data["flights_invalid"]==False):
                for item in check_full_data["flights"]:
                    print(item["id"])


        else:
            print("Bad request!!!")


else:
    print("Bad request!!!")