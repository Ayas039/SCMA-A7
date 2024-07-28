import streamlit as st
import pandas as pd
import numpy as np

# Function to simulate cab availability and pricing
def get_cab_data():
    # For demonstration, generate random availability and pricing data
    return {
        'Cab Type': ['SUV', 'Sedan', 'Mini'],
        'Availability': [np.random.randint(1, 10), np.random.randint(1, 15), np.random.randint(1, 20)],
        'Price (₹)': ['2000 - 3000', '1500 - 2000', '1000 - 1500']
    }

# Set up the app
def main():
    st.set_page_config(page_title='Easy Go', page_icon='🚖', layout='wide')

    # Header section
    st.title('🚖 Easy Go')
    st.markdown("### Book Your Ride Easily with Easy Go")
    
    st.markdown("---")

    # Live dashboard for cab availability and pricing
    st.markdown("## Live Dashboard: Cab Availability and Pricing")
    
    # Display data
    cab_data = get_cab_data()
    df = pd.DataFrame(cab_data)

    st.write("### Current Cab Availability and Pricing")
    st.dataframe(df, height=200)

    if st.button('Refresh Data'):
        # Update data manually
        cab_data = get_cab_data()
        df = pd.DataFrame(cab_data)
        st.dataframe(df, height=200)
    
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
    st.markdown("© 2024 Easy Go. All rights reserved.")

if __name__ == '__main__':
    main()
