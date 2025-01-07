import requests
import streamlit as st
import folium
import polyline


TOMTOM_API_KEY = "jcNH1tB2wZaitYTTj6ezvTn9KqZTOTxk"
AQICN_API_TOKEN = "b5709c74b9bd962ebd27e7eb8f2cf999aa2e72e8"

def get_tomtom_route(start, end):
    try:
        url = f"https://api.tomtom.com/routing/1/calculateRoute/{start}:{end}/json"
        params = {
            "key": TOMTOM_API_KEY,
            "routeType": "fastest",
            "traffic": "true"
        }
        response = requests.get(url, params=params)
        
        # Debugging: print the response content
        print(f"API Response: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if "routes" in data:
                route = data["routes"][0]["summary"]
                
                polyline_points = data["routes"][0]["legs"][0]["points"]
                decoded_polyline = polyline.decode(polyline_points)
                return {
                    "distance": route["lengthInMeters"] / 1000,  
                    "duration": route["travelTimeInSeconds"] / 60,  
                    "polyline": decoded_polyline,  
                }
        return None
    except Exception as e:
        print(f"Error fetching route: {e}")
        return None

def calculate_emissions(distance_km, vehicle_type):
    emission_factors = {"gasoline": 2.31, "diesel": 2.68, "electric": 0.0}
    return distance_km * emission_factors.get(vehicle_type, 2.31)

def main():
    st.title("Dynamic Route Optimization and Emission Reduction")
    st.header("Find the most efficient route and minimize your carbon footprint!")

    start = st.text_input("Enter starting location (latitude,longitude):")
    end = st.text_input("Enter destination (latitude,longitude):")
    vehicle_type = st.selectbox("Select vehicle type:", ["gasoline", "diesel", "electric"])

    def parse_location(location):
        try:
            lat, lon = location.split(",")
            lat = float(lat)
            lon = float(lon)
            return lat, lon
        except ValueError:
            return None  

 
    if st.button("Get Optimized Route"):
        if start and end:
            start_coords = parse_location(start)
            end_coords = parse_location(end)

            if start_coords and end_coords:
                
                route = get_tomtom_route(start, end)
                if route:
                    st.subheader("Route Details")
                    st.write(f"Distance: {route['distance']} km")
                    st.write(f"Estimated Duration: {route['duration']} minutes")

                    
                    emissions = calculate_emissions(route["distance"], vehicle_type)
                    st.write(f"Estimated Emissions: {emissions:.2f} kg CO2")

                    
                    my_map = folium.Map(location=start_coords, zoom_start=12)

                    
                    folium.Marker(start_coords, popup="Start").add_to(my_map)
                    folium.Marker(end_coords, popup="End").add_to(my_map)

                    
                    folium.PolyLine(locations=route["polyline"], color="blue", weight=2.5, opacity=1).add_to(my_map)

                   
                    st.write("### Route Map:")
                    st.components.v1.html(my_map.repr_html(), height=600)
                else:
                    st.error("Could not fetch route. Please check your input locations.")
            else:
                st.error("Invalid input format. Please provide coordinates in the form 'latitude,longitude'.")
        else:
            st.error("Please provide both starting location and destination.")

if _name_ == "_main_":
    main()
