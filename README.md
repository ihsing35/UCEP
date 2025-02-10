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

#### 3.1 Main Program File `run.py`
This is the core file of the program, containing the main logic and simulation process of the model. Its specific functions are as follows:
- **Parameter Reading**: Reads the initial parameters of the model from the `model_parameters.csv` file, including the start year, initial population, initial GDP per capita, etc.
- **Scenario Setting**: Defines three scenarios (Base Scenario, Low - Carbon Scenario, and Zero - Carbon Scenario) and reads the parameter adjustment information for each scenario from the corresponding CSV files.
- **Simulation Calculation**: Based on the read parameters, the program simulates the city's population, GDP, energy consumption, and carbon dioxide emissions year by year. It also adjusts the parameters every five years according to the scenario parameters.
- **Result Visualization**: Uses the `matplotlib` library to plot the carbon dioxide emission trends under the three scenarios as a line chart, facilitating users to intuitively compare the emission differences under different scenarios.
- **Output Results**:
        - **CSV Output**: If `output_csv` is set to `1`, it saves the simulation results to `carbon_emission_results.csv`.
        - **Image Generation**: If `output_image` is set to `1`, it uses `matplotlib` to generate a line chart showing the carbon emission trends under different scenarios and saves it as `carbon_emission_results.png` in the `static` directory.
        - **Web Display**: If `output_web` is set to `1`, it starts a Flask application and renders the `results.html` template to display the results on a web page.

#### 3.2 Model Parameter File (`model_parameters.csv`)
This file stores the initial parameters of the model. Each row contains the following fields:
| Field Name | Meaning | Example Value |
| ---- | ---- | ---- |
| `start_year` | The start year of the simulation | 2020 |
| `initial_population` | The urban population at the start year | 1000000 |
| `initial_gdp_per_capita` | The GDP per capita at the start year | 50000 |
| `initial_energy_intensity` | The energy intensity (energy consumption per unit of GDP) at the start year | 0.5 |
| `initial_fossil_fuel_ratio` | The proportion of fossil fuels at the start year | 0.8 |
| `initial_co2_emission` | The cumulative carbon dioxide emissions at the start year | 0 |
| `population_growth_rate` | The population growth rate | 0.01 |
| `gdp_growth_rate` | The GDP growth rate | 0.03 |
| `energy_intensity_decrease_rate` | The decreasing rate of energy intensity | 0.02 |
| `fossil_fuel_decrease_rate` | The decreasing rate of the proportion of fossil fuels | 0.01 |
| `carbon_emission_factor` | The carbon emission factor of fossil fuels | 2.5 |

#### 3.3 Scenario Parameter Files
- **Base Scenario File (`base_scenario.csv`)**
- **Low - Carbon Scenario File (`low_carbon_scenario.csv`)**
- **Zero - Carbon Scenario File (`zero_carbon_scenario.csv`)**

These three files store the parameter adjustment information for each five - year period under the three scenarios respectively. Each row contains the following fields:
| Field Name | Meaning | Example Value |
| ---- | ---- | ---- |
| `year` | The specific year for parameter adjustment | 2025 |
| `population_growth_rate_factor` | The adjustment coefficient for the population growth rate | 0.95 |
| `gdp_growth_rate_factor` | The adjustment coefficient for the GDP growth rate | 0.98 |
| `energy_intensity_decrease_rate_factor` | The adjustment coefficient for the decreasing rate of energy intensity | 1.05 |
| `fossil_fuel_decrease_rate_factor` | The adjustment coefficient for the decreasing rate of the proportion of fossil fuels | 1.05 |


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
