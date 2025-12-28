# Animated Population Pyramid

An interactive, animated population pyramid dashboard built with **Streamlit** and **Plotly Express**, visualizing UN World Population Prospects 2024 data (1990-2030).

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Animated playback** through 41 years (1990-2030)
- **314 countries and regions** to explore
- **21 age groups** (0-4 through 100+)
- **Interactive controls**: Play/Pause, year slider, country selector
- **Live metrics**: Total population, male/female breakdown, sex ratio

## Screenshot

```
         Population Pyramid: Japan

     Male ←              → Female
100+  ▌                        ▐
95-99 ▌                        ▐
90-94 ██                      ██
85-89 ████                  ████
80-84 ██████              ██████
  ... ████████          ████████
 0-4  ██████              ██████
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/edgeoinnovations-resources/AnimatedPopulationPyramid.git
   cd AnimatedPopulationPyramid
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the data from the [UN Population Data Portal](https://population.un.org/dataportal/):
   - **Indicator**: Population by 5-year age groups and sex
   - **Sex**: Male, Female, Both sexes
   - **Age**: All 5-year age groups
   - **Time**: 1990-2030
   - **Variant**: Median
   - **Location**: All countries

   Save the CSV file in the project directory.

4. Update the filename in `app.py` (line ~30) to match your downloaded file.

## Usage

```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501`

## Data Source

**United Nations, Department of Economic and Social Affairs, Population Division (2024).**
World Population Prospects 2024, Online Edition.

https://population.un.org/dataportal/

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Pandas** | Data loading and preprocessing |
| **NumPy** | Numerical operations |
| **Plotly Express** | Animated visualization |
| **Streamlit** | Web dashboard framework |

## License

MIT License - feel free to use and modify for your own projects.
