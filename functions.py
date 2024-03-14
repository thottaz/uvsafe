def get_advice(postcode):

    if postcode == '3000':
        location = 'Melbourne City'
        UVLevel = 5
        cloth = "Sun glasses, wide-brimmed hat, lightweight cloth"
    elif postcode == '3008':
        location = 'Docklands'
        UVLevel = 6
        cloth = "Sun glasses, lightweight cloth"
    else:
        return "No such place, Please enter again"

    return f"Your location is %s, the UV level is %s, the recommend cloths are %s." %(location, UVLevel, cloth)

def call_openweather_api():
    # Call the OpenWeather API
    # ...
    # Return the response
    return {
        'temperature': 25,
        'description': 'Sunny',
        'humidity': 50,
        'wind_speed': 10
    }