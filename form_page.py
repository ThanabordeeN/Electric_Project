import streamlit as st
import datetime
import time
from streamlit_extras.colored_header import colored_header

def show_form_page(db_manager, unit_per_price):
    """Display the data entry form page"""
    colored_header(
        label="Data Entry Form",
        description="Enter water meter readings for each house",
        color_name="blue-70"
    )
    
    with st.form(key='water_form'):
        col1, col2 = st.columns(2)
        with col1:
            house_number = st.text_input('House Number', placeholder="e.g. H-123")
        with col2:
            water_meter = st.number_input('Water Meter Reading (m³)', 
                                         min_value=0.0, step=0.1, 
                                         format="%.1f")
        
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        submit_col1, submit_col2 = st.columns([1, 3])
        with submit_col1:
            submit = st.form_submit_button('Save Data', use_container_width=True)
        
        if submit:
            if not house_number:
                st.error('⚠️ Please enter a house number')
            else:
                with st.spinner('Saving data...'):
                    try:
                        price = water_meter * unit_per_price
                        success = db_manager.add_reading(house_number, water_meter, current_date, price)
                        
                        time.sleep(0.5)  # Small delay for better UX
                        if success:
                            st.success('✅ Data successfully added!')
                        else:
                            st.error('❌ Failed to add data')
                    except Exception as e:
                        st.error(f'❌ An error occurred: {e}')
