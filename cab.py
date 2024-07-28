import streamlit as st
import pandas as pd
import numpy as np

# Simulating cab data for demonstration purposes
def get_cab_availability(pickup_location):
    # For demonstration, let's randomly generate the number of available cabs
    return np.random.randint(1, 20)

def main():
    st.set_page_config(page_title='Cab Booking App', page_icon='🚖', layout='wide')

    # Header section
    st.title('🚖 Welcome to the Cab Booking App')
    st.markdown("### Your reliable ride, just a click away.")

    # Cab availability check
    st.markdown("## Check Cab Availability")
    pickup_location_avail = st.text_input('Enter your current location', placeholder='Enter your location')
    
    if st.button('Check Availability'):
        if pickup_location_avail:
            available_cabs = get_cab_availability(pickup_location_avail)
            st.info(f'{available_cabs} cabs available near {pickup_location_avail}.')
        else:
            st.warning('Please enter a location to check cab availability.')

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

        submit_button = st.form_submit_button(label='Book Now')

    # Booking Confirmation
    if submit_button:
        if name and pickup_location and destination:
            st.success(f'Thank you {name}, your cab is booked from {pickup_location} to {destination} at {booking_time}.')
            st.balloons()
        else:
            st.error('Please fill in all the details to book a cab.')

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Cab Booking App. All rights reserved.")

if __name__ == '__main__':
    main()
