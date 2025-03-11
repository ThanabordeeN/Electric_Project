import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards

def show_dashboard_page(db_manager):
    """Display the analytics dashboard page"""
    colored_header(
        label="Water Management Dashboard",
        description="Analytics and reporting for water consumption",
        color_name="blue-70"
    )
    
    try:
        df = db_manager.get_data()
        if not df.empty:
            # Dashboard Tabs with larger text
            tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Charts", "📋 Detailed Data"])
            
            with tab1:
                show_overview_tab(df)
            
            with tab2:
                show_charts_tab(df)

            with tab3:
                show_detailed_data_tab(df)
        else:
            st.info("ℹ️ No data available yet. Please add data using the Form page.")
    except Exception as e:
        st.error(f"❌ Error loading dashboard: {e}")

def show_overview_tab(df):
    """Display the overview tab with key metrics"""
    st.markdown('<p class="section-header">Key Metrics</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Houses", len(df['House Number'].unique()))
    with col2:
        st.metric("Total Water Usage", f"{df['Water Meter'].sum():.2f} m³")
    with col3:
        st.metric("Average Usage", f"{df['Water Meter'].mean():.2f} m³")
    
    # Apply metric styling
    style_metric_cards()
    
    st.markdown('<p class="section-header">Financial Summary</p>', unsafe_allow_html=True)
    fin_col1, fin_col2 = st.columns(2)
    with fin_col1:
        st.metric("Total Revenue", f"{df['Price'].sum():.2f} Bath")
    with fin_col2:
        st.metric("Average Bill", f"{df['Price'].mean():.2f} Bath")
    
    # Recent entries
    st.markdown('<p class="section-header">Recent Entries</p>', unsafe_allow_html=True)
    recent = df.sort_values('Date', ascending=False).head(5)
    st.dataframe(recent[['House Number', 'Water Meter', 'Price', 'Date']], 
                 use_container_width=True, height=200)

def show_charts_tab(df):
    """Display the charts tab with visualizations"""
    st.markdown('<p class="section-header">Visualization</p>', unsafe_allow_html=True)
    
    chart_type = st.selectbox("Select Chart Type", 
                             ["Bar Charts", "Pie Chart", "Line Chart"])
    
    if chart_type == "Bar Charts":
        fig = px.bar(
            df.groupby('House Number')['Water Meter'].sum().reset_index(),
            x='House Number',
            y='Water Meter',
            title="Water Usage by House",
            labels={'Water Meter': 'Water Usage (m³)'},
            color='Water Meter',
            height=500,
            color_continuous_scale="blues"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        fig2 = px.bar(
            df.groupby('House Number')['Price'].sum().reset_index(),
            x='House Number',
            y='Price',
            title="Revenue by House",
            labels={'Price': 'Amount (Bath)'},
            color='Price',
            height=500,
            color_continuous_scale="greens"
        )
        st.plotly_chart(fig2, use_container_width=True)
        
    elif chart_type == "Pie Chart":
        fig = px.pie(
            df, 
            values='Water Meter', 
            names='House Number', 
            title="Water Usage Distribution",
            hole=.3,
            height=600,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_traces(textinfo='percent+label', textfont_size=14)
        st.plotly_chart(fig, use_container_width=True)
        
    else:  # Line Chart
        if 'Date' in df.columns:
            time_df = df.copy()
            time_df['Date'] = pd.to_datetime(time_df['Date']).dt.date
            time_data = time_df.groupby(['Date', 'House Number'])['Water Meter'].sum().reset_index()
            
            fig = px.line(
                time_data,
                x='Date',
                y='Water Meter',
                color='House Number',
                title="Water Usage Over Time",
                labels={'Water Meter': 'Usage (m³)'},
                height=500,
                markers=True
            )
            st.plotly_chart(fig, use_container_width=True)

def show_detailed_data_tab(df):
    """Display the detailed data tab with search and filters"""
    st.markdown('<p class="section-header">Data Explorer</p>', unsafe_allow_html=True)
    
    search_col, filter_col = st.columns([1, 2])
    with search_col:
        search = st.text_input("🔍 Search by House Number", placeholder="Enter house number")
    with filter_col:
        if df['Date'].min().date() and df['Date'].max().date():
            date_range = st.date_input("Filter by date range", 
                                    value=(df['Date'].min().date(), df['Date'].max().date()),
                                    max_value=datetime.datetime.now().date())
        else:
            today = datetime.datetime.now().date()
            date_range = st.date_input("Filter by date range", 
                                    value=(today, today),
                                    max_value=today)
    
    if search:
        filtered_df = df[df['House Number'].str.contains(search, case=False)]
    else:
        filtered_df = df
        
    if len(date_range) == 2:
        start_date, end_date = date_range
        mask = (filtered_df['Date'].dt.date >= start_date) & (filtered_df['Date'].dt.date <= end_date)
        filtered_df = filtered_df.loc[mask]
    
    st.dataframe(
        filtered_df.sort_values('Date', ascending=False).style.highlight_max(axis=0),
        use_container_width=True,
        height=400
    )
    
    # Add export functionality
    if not filtered_df.empty:
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Download Data as CSV",
            data=csv,
            file_name="water_data_export.csv",
            mime="text/csv",
        )
