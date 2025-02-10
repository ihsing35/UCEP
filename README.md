# Urban Carbon Emission Prediction Model

### 1.  Overview
This model is an urban carbon emission prediction system. It uses a system dynamics model to forecast urban carbon dioxide emissions under different scenarios, including the Base Scenario, Low - Carbon Scenario, and Zero - Carbon Scenario. The system reads parameter data from CSV files, conducts simulations, and can output results in three forms: saving data to a CSV file, generating an image of the emission trend, and displaying the results on a web page. Users can adjust the output forms by modifying the `model_parameters.csv` file.

### 2. File Structure
```plaintext
carbon_emission_prediction/
│
├── run.py
├── templates/
│   └── results.html
├── static/
│   └── carbon_emission_results.png (generated if enabled)
├── model_parameters.csv
├── base_scenario.csv
├── low_carbon_scenario.csv
├── zero_carbon_scenario.csv
├── carbon_emission_results.csv (generated if enabled)
```

### 3. Key Files and Their Functions

#### 3.1 `run.py`
- **Function**: This is the main Python script that implements the carbon emission prediction model. It reads parameter data from CSV files, runs simulations for different scenarios, and controls the output forms based on the settings in `model_parameters.csv`.
- **Steps**:
    1. **Read Initial Parameters**: Reads initial model parameters from `model_parameters.csv`, including starting year, initial population, GDP per capita, etc., as well as the settings for output forms (`output_csv`, `output_image`, `output_web`).
    2. **Scenario Simulation**: Loops through different scenarios (Base, Low - Carbon, Zero - Carbon), reads scenario - specific parameter adjustment files, and conducts simulation calculations for each time step.
    3. **Output Results**:
        - **CSV Output**: If `output_csv` is set to `1`, it saves the simulation results to `carbon_emission_results.csv`.
        - **Image Generation**: If `output_image` is set to `1`, it uses `matplotlib` to generate a line chart showing the carbon emission trends under different scenarios and saves it as `carbon_emission_results.png` in the `static` directory.
        - **Web Display**: If `output_web` is set to `1`, it starts a Flask application and renders the `results.html` template to display the results on a web page.

#### 3.2 `templates/results.html`
- **Function**: This is an HTML template used to display the carbon emission prediction results on a web page. It uses the ECharts library to generate a dynamic line chart showing the carbon emission trends under different scenarios.
- **Key Components**:
    - **CSS Styling**: Defines the layout and style of the web page, including the font, background color, and chart container style.
    - **ECharts Integration**: Imports the ECharts library from a CDN and uses JavaScript to initialize an ECharts instance. It then configures the chart options, such as the title, axes, and series data, and displays the chart in the `co2Chart` container.

#### 3.3 `model_parameters.csv`
- **Function**: Stores the initial parameters for the carbon emission prediction model and the settings for output forms.
- **Sample Content**:
```plaintext
start_year,initial_population,initial_gdp_per_capita,initial_energy_intensity,initial_fossil_fuel_ratio,initial_co2_emission,population_growth_rate,gdp_growth_rate,energy_intensity_decrease_rate,fossil_fuel_decrease_rate,carbon_emission_factor,output_csv,output_image,output_web
2020,1000000,50000,0.5,0.8,0,0.01,0.03,0.02,0.01,2.5,1,1,1
```
- **Field Explanation**:
    - `start_year`: The starting year of the simulation.
    - `initial_population`: The initial population of the city.
    - `initial_gdp_per_capita`: The initial GDP per capita.
    - `initial_energy_intensity`: The initial energy intensity.
    - `initial_fossil_fuel_ratio`: The initial proportion of fossil fuels in energy consumption.
    - `initial_co2_emission`: The initial carbon dioxide emission.
    - `population_growth_rate`: The population growth rate.
    - `gdp_growth_rate`: The GDP growth rate.
    - `energy_intensity_decrease_rate`: The rate of decrease in energy intensity.
    - `fossil_fuel_decrease_rate`: The rate of decrease in the proportion of fossil fuels.
    - `carbon_emission_factor`: The carbon emission factor.
    - `output_csv`: Whether to output the results to a CSV file (`1` for yes, `0` for no).
    - `output_image`: Whether to generate an image of the emission trend (`1` for yes, `0` for no).
    - `output_web`: Whether to display the results on a web page (`1` for yes, `0` for no).

#### 3.4 `base_scenario.csv`, `low_carbon_scenario.csv`, `zero_carbon_scenario.csv`
- **Function**: These files store the parameter adjustment factors for different scenarios at specific years. For example, they can adjust the population growth rate, GDP growth rate, etc., in different scenarios to simulate different development paths.

### 4. How to Use
1. **Environment Setup**: Make sure you have Python installed, along with the required libraries such as `Flask`, `numpy`, and `matplotlib`. You can install them using the following command:
```bash
pip install flask numpy matplotlib
```
2. **Configure Parameters**: Modify the `model_parameters.csv` file according to your needs to set the initial parameters and output forms.
3. **Run the Program**: Execute the `app.py` script in the terminal:
```bash
python app.py
```
4. **View Results**:
    - **CSV Results**: If `output_csv` is set to `1`, you can find the simulation results in the `carbon_emission_results.csv` file.
    - **Image Results**: If `output_image` is set to `1`, the generated image will be saved as `carbon_emission_results.png` in the `static` directory.
    - **Web Results**: If `output_web` is set to `1`, open a web browser and visit `http://127.0.0.1:5000/` to view the dynamic chart showing the carbon emission trends under different scenarios.

### 5. Notes
- Make sure the CSV files (`model_parameters.csv`, `base_scenario.csv`, etc.) exist in the correct directory and have the correct format.
- If you encounter any issues, check the console output for error messages to help troubleshoot the problem.
