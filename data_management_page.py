import streamlit as st
from streamlit_extras.colored_header import colored_header

def show_data_management_page(db_manager):
    """Display the data management page"""
    colored_header(
        label="Data Management",
        description="Manage and export water usage data",
        color_name="blue-70"
    )
    
    try:
        df = db_manager.get_data()
        if not df.empty:
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📥 Download Data as CSV",
                data=csv,
                file_name="water_data_export.csv",
                mime="text/csv",
            )
            
            if st.button("Clear All Data"):
                if db_manager.clear_data():
                    st.success("All data has been cleared!")
                    st.experimental_rerun()
                else:
                    st.error("Failed to clear data")
        else:
            st.info("No data available yet.")
    except Exception as e:
        st.error(f"Error in data management: {e}")
