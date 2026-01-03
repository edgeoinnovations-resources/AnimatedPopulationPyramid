"""
Animated Population Pyramid Dashboard
UN World Population Prospects 2024 (1950-2030)

Built with Streamlit + Plotly Express
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Population Pyramid",
    page_icon="📊",
    layout="wide"
)

# =============================================================================
# Phase 1: Data Loading with Caching
# =============================================================================

@st.cache_data
def load_data():
    """Load and preprocess the population data."""
    df = pd.read_csv(
        "unpopulation_dataportal_20251230141141.csv",
        encoding="utf-8-sig",
        usecols=[
            "Location", "Iso3", "Time", "Sex", "SexId",
            "AgeStart", "Age", "Value"
        ],
        dtype={
            "Location": "category",
            "Sex": "category",
            "Age": "category",
            "Time": "int16",
            "SexId": "int8",
            "AgeStart": "int8",
            "Value": "float64"
        }
    )
    return df


@st.cache_data
def preprocess_for_pyramid(df):
    """
    Filter and transform data for population pyramid visualization.
    - Remove 'Both sexes' (keep only Male/Female)
    - Create Population_Plot column (negative for Males)
    - Sort by Time and AgeStart
    """
    # Filter: Keep only Male (SexId=1) and Female (SexId=2)
    df_pyramid = df[df["SexId"].isin([1, 2])].copy()

    # Transform: Negative values for Males (left side of pyramid)
    df_pyramid["Population_Plot"] = df_pyramid.apply(
        lambda row: -row["Value"] if row["Sex"] == "Male" else row["Value"],
        axis=1
    )

    # Sort by Time and AgeStart for proper animation order
    df_pyramid = df_pyramid.sort_values(["Time", "AgeStart"]).reset_index(drop=True)

    # Create ordered categorical for Age to ensure proper Y-axis ordering
    age_order = [
        "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
        "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
        "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+"
    ]
    df_pyramid["Age"] = pd.Categorical(
        df_pyramid["Age"], categories=age_order, ordered=True
    )

    return df_pyramid


@st.cache_data
def get_locations(df):
    """Get sorted list of unique locations."""
    return sorted(df["Location"].unique())


# =============================================================================
# Phase 2: Animated Pyramid Chart
# =============================================================================

def format_tick_label(value):
    """Format a population value as a readable string (always positive)."""
    abs_val = abs(value)
    if abs_val >= 1e9:
        return f"{abs_val/1e9:.1f}B"
    elif abs_val >= 1e6:
        return f"{abs_val/1e6:.1f}M"
    elif abs_val >= 1e3:
        return f"{abs_val/1e3:.0f}K"
    else:
        return f"{abs_val:.0f}"


def plot_pyramid(filtered_df, location_name):
    """
    Create an animated population pyramid using Plotly Express.
    """
    # Calculate max population for fixed axis range
    max_pop = filtered_df["Value"].max() * 1.1

    # Create the animated bar chart
    fig = px.bar(
        filtered_df,
        y="Age",
        x="Population_Plot",
        color="Sex",
        orientation="h",
        animation_frame="Time",
        color_discrete_map={"Male": "#3498db", "Female": "#e74c3c"},
        labels={"Population_Plot": "Population", "Age": "Age Group"},
        category_orders={"Sex": ["Male", "Female"]}
    )

    # Generate tick values and labels (positive numbers on both sides)
    # Create 9 evenly spaced ticks from -max_pop to +max_pop
    tick_vals = np.linspace(-max_pop, max_pop, 9)
    tick_labels = [format_tick_label(v) for v in tick_vals]

    # Update layout
    fig.update_layout(
        title=dict(
            text=f"Population Pyramid: {location_name}",
            font=dict(size=24),
            x=0.5,
            y=0.98,
            yanchor="top"
        ),
        margin=dict(t=100),
        xaxis=dict(
            range=[-max_pop, max_pop],
            title="← Male          Population          Female →",
            tickmode="array",
            tickvals=tick_vals.tolist(),
            ticktext=tick_labels
        ),
        yaxis=dict(
            title="Age Group",
            categoryorder="array",
            categoryarray=[
                "0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34",
                "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69",
                "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+"
            ]
        ),
        legend=dict(
            title=None,
            orientation="h",
            yanchor="bottom",
            y=1.0,
            xanchor="center",
            x=0.5
        ),
        height=700,
        bargap=0.1,
        # Animation settings
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                y=0,
                x=0.1,
                xanchor="right",
                yanchor="top",
                buttons=[
                    dict(
                        label="▶ Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 200, "redraw": True},
                                "fromcurrent": True,
                                "transition": {"duration": 100}
                            }
                        ]
                    ),
                    dict(
                        label="⏸ Pause",
                        method="animate",
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0}
                            }
                        ]
                    )
                ]
            )
        ],
        sliders=[
            dict(
                active=0,
                yanchor="top",
                xanchor="left",
                currentvalue=dict(
                    font=dict(size=16),
                    prefix="Year: ",
                    visible=True,
                    xanchor="center"
                ),
                transition=dict(duration=100),
                pad=dict(b=10, t=50),
                len=0.9,
                x=0.1,
                y=0
            )
        ]
    )

    return fig


def format_population(value):
    """Format population number for display."""
    if value >= 1e9:
        return f"{value/1e9:.2f}B"
    elif value >= 1e6:
        return f"{value/1e6:.2f}M"
    elif value >= 1e3:
        return f"{value/1e3:.1f}K"
    else:
        return f"{value:.0f}"


# =============================================================================
# Phase 3: Streamlit Interface
# =============================================================================

def main():
    # Title
    st.title("🌍 Animated Population Pyramid")
    st.markdown("**UN World Population Prospects 2024** | Data: 1950-2030")

    # Load data
    with st.spinner("Loading population data..."):
        df = load_data()
        df_pyramid = preprocess_for_pyramid(df)
        locations = get_locations(df_pyramid)

    # Sidebar controls
    st.sidebar.header("Controls")

    # Location selector with search
    selected_location = st.sidebar.selectbox(
        "Select Country/Region",
        options=locations,
        index=locations.index("World") if "World" in locations else 0,
        help="Choose a country or region to display"
    )

    # Year selector for metrics
    years = sorted(df_pyramid["Time"].unique())
    selected_year = st.sidebar.select_slider(
        "Select Year for Statistics",
        options=years,
        value=2024
    )

    # Filter data for selected location
    location_data = df_pyramid[df_pyramid["Location"] == selected_location]

    if location_data.empty:
        st.error(f"No data available for {selected_location}")
        return

    # Display metrics for selected year
    year_data = location_data[location_data["Time"] == selected_year]

    col1, col2, col3, col4 = st.columns(4)

    total_pop = year_data["Value"].sum()
    male_pop = year_data[year_data["Sex"] == "Male"]["Value"].sum()
    female_pop = year_data[year_data["Sex"] == "Female"]["Value"].sum()
    sex_ratio = (male_pop / female_pop * 100) if female_pop > 0 else 0

    with col1:
        st.metric("Total Population", format_population(total_pop))
    with col2:
        st.metric("Male Population", format_population(male_pop))
    with col3:
        st.metric("Female Population", format_population(female_pop))
    with col4:
        st.metric("Sex Ratio (M/F)", f"{sex_ratio:.1f}%")

    # Display the animated pyramid
    st.markdown("---")
    fig = plot_pyramid(location_data, selected_location)
    st.plotly_chart(fig, use_container_width=True)

    # Additional info
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.markdown(
        """
        This dashboard visualizes population pyramids
        using UN World Population Prospects 2024 data.

        **Features:**
        - 📊 81 years of data (1950-2030)
        - 🌍 314 countries & regions
        - 👥 21 age groups
        - ▶️ Animated playback

        **How to use:**
        1. Select a location from the dropdown
        2. Click **Play** to animate through years
        3. Use the slider to jump to specific years
        """
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        "*Data source: United Nations Population Division*"
    )


if __name__ == "__main__":
    main()
