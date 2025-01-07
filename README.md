# Dynamic-Route-Optimization-and-Emission-Reduction-System
1) Have to Obtain API keys:
TomTom API Key: For geospatial features.
AQICN API Token: For air quality data.
2) Backend Development : 
Fetch Route Details
1)Implement a function to get route from google map.
2)Fetch route distance, duration, and step-by-step directions.
3)Error handling must be taken care 
Fetch Air Quality Data
Use AQICN API to retrieve air quality index  for the starting location.
3) Streamlit Frontend Development
Create a user interface:
a) Input Fields: Collect start location, destination, and vehicle type.
b) Button: Trigger the optimization process.
Display results:
1) Route details: Distance, duration, and steps.
2) Estimated emissions: Show calculated emissions based on the input.
3)Air quality: Display AQI and dominant pollutant.
4) Integration
Combine backend functions into a cohesive flow triggered by the "Get Optimized Route" button.
Handle missing data gracefully with appropriate error messages.
5) Testing
Test with different inputs:
1) Valid start and end locations.
2) Invalid or incomplete inputs.
3) Test air quality API with various cities.
