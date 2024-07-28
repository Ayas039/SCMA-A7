import streamlit as st

def main():
    st.set_page_config(page_title='Cab Booking App', page_icon='🚖', layout='wide')

    # Header section
    st.title('🚖 Welcome to the Cab Booking App')
    st.markdown("### Your reliable ride, just a click away.")

    # User Input Section
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

        # Submission Button
        submit_button = st.form_submit_button(label='Book Now')

    # Booking Confirmation
    if submit_button:
        st.success(f'Thank you {name}, your cab is booked from {pickup_location} to {destination} at {booking_time}.')
        st.balloons()

    # Footer
    st.markdown("---")
    st.markdown("© 2024 Cab Booking App. All rights reserved.")

if __name__ == '__main__':
    main()
