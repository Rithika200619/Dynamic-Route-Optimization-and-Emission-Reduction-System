# Dynamic-Route-Optimization-and-Emission-Reduction-System
### OUR WORKFLOW
#### Obtain API Keys:
- **TomTom API Key**: For geospatial features.
- **AQICN API Token**: For air quality data.

#### Backend Development:
- **Fetch Route Details**:
  - Implement a function to get the route from Google Maps.
  - Retrieve route distance, duration, and step-by-step directions.
  - Ensure proper error handling.
  
- **Fetch Air Quality Data**:
  - Use the AQICN API to retrieve the air quality index for the starting location.

#### Streamlit Frontend Development:
- **Create a User Interface**:
  - Input Fields: Collect start location, destination, and vehicle type.
  - Button: Trigger the optimization process.
  
- **Display Results**:
  - Route details: Distance, duration, and steps.
  - Estimated emissions: Show calculated emissions based on input.
  - Air quality: Display AQI and dominant pollutant.

#### Integration:
- Combine backend functions into a cohesive flow triggered by the "Get Optimized Route" button.
- Handle missing data gracefully with appropriate error messages.

#### Testing:
- Test with different inputs:
  - Valid start and end locations.
  - Invalid or incomplete inputs.
  - Test air quality API with various cities.

### Our Current Work:
We are in the process of integrating the Google Maps API for enhanced route visualization. However, since the Google Maps API key is currently available only through paid plans, we are exploring alternative solutions to achieve this functionality within a free or cost-effective framework. Updates to the program with this improved feature set will be available soon.

**Current Date and time**: Tuesday, January 07, 2025, 6 PM IST
