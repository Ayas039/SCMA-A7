import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulating cab availability and pricing data
def get_cab_availability(pickup_location):
    # Generate random availability data for demonstration
    return {
        'SUV': np.random.randint(1, 10),
        'Sedan': np.random.randint(1, 15),
        'Mini': np.random.randint(1, 20)
    }

def get_cab_prices():
    # Fixed prices for demonstration purposes
    return {
        'SUV': 20,  # Price per km
        'Sedan': 15,  # Price per km
        'Mini': 10  # Price per km
    }

def main():
    st.set_page_config(page_title='Cab Booking App', page_icon='🚖', layout='wide')

    # Header section
    st.title('🚖 Welcome to the Cab Booking App')
    st.markdown("### Your reliable ride, just a click away.")
    
    st.markdown("---")

    # Cab availability check
    st.markdown("## Check Cab Availability and Prices")
    pickup_location_avail = st.text_input('Enter your current location', placeholder='Enter your location')
    
    if st.button('Check Availability'):
        if pickup_location_avail:
            available_cabs = get_cab_availability(pickup_location_avail)
            cab_prices = get_cab_prices()
            
            st.markdown(f"**Cabs available near {pickup_location_avail}:**")
            for cab_type, availability in available_cabs.items():
                st.write(f"{cab_type}: {availability} available, ₹{cab_prices[cab_type]} per km")
            
            # Data visualization: Pie chart for cab availability
            st.markdown("### Cab Availability Distribution")
            fig, ax = plt.subplots()
            ax.pie(available_cabs.values(), labels=available_cabs.keys(), autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        else:
            st.warning('Please enter a location to check cab availability and prices.')

    st.markdown("---")

    # Booking form
    st.markdown("## Book Your Cab")
    with st.form(key='booking_form'):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Name', placeholder='Enter your full name')
            email = st.text_input('Email', placeholder='Enter your email')
            phone = st.text_input('Phone', placeholder='Enter your phone number')

        with col2:
            pickup_location = st.text_input('Pickup Location', placeholder='Enter your pickup location')
            destination = st.text_input('Destination', placeholder='Enter your destination')
            booking_time = st.time_input('Booking Time')

            cab_type = st.selectbox('Select Cab Type', ['SUV', 'Sedan', 'Mini'])

        submit_button = st.form_submit_button(label='Book Now')

    # Booking Confirmation
    if submit_button:
        if name and pickup_location and destination:
            st.success(f'Thank you {name}, your {cab_type} cab is booked from {pickup_location} to {destination} at {booking_time}.')
            st.balloons()
        else:
            st.error('Please fill in all the details to book a cab.')

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Cab Booking App. All rights reserved.")

if __name__ == '__main__':
    main()
