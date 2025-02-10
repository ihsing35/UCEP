# Program Name: Urban Carbon Emission Prediction
# Developer: ihsing35
# Date: 2025-02-10 15:30:00
# Description: This program uses a system dynamics model to predict urban carbon dioxide emissions
#              under different scenarios (Base Scenario, Low - Carbon Scenario, Zero - Carbon Scenario).
#              It reads parameter data from CSV files, and the output forms can be adjusted by the user
#              through the model_parameters.csv file.

import numpy as np
import matplotlib.pyplot as plt
import csv
from flask import Flask, render_template
import os

app = Flask(__name__)

# Define scenarios and corresponding parameter adjustment files
scenarios = {
    "Base Scenario": "base_scenario.csv",
    "Low - Carbon Scenario": "low_carbon_scenario.csv",
    "Zero - Carbon Scenario": "zero_carbon_scenario.csv"
}

# Read the initial model parameter file
try:
    with open('model_parameters.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            start_year = int(row['start_year'])
            initial_population = float(row['initial_population'])
            initial_gdp_per_capita = float(row['initial_gdp_per_capita'])
            initial_energy_intensity = float(row['initial_energy_intensity'])
            initial_fossil_fuel_ratio = float(row['initial_fossil_fuel_ratio'])
            initial_co2_emission = float(row['initial_co2_emission'])
            population_growth_rate = float(row['population_growth_rate'])
            gdp_growth_rate = float(row['gdp_growth_rate'])
            energy_intensity_decrease_rate = float(row['energy_intensity_decrease_rate'])
            fossil_fuel_decrease_rate = float(row['fossil_fuel_decrease_rate'])
            carbon_emission_factor = float(row['carbon_emission_factor'])
            output_csv = int(row['output_csv'])
            output_image = int(row['output_image'])
            output_web = int(row['output_web'])
except FileNotFoundError:
    print("The model parameter file 'model_parameters.csv' was not found. Using default values.")
    # Default values
    start_year = 2020
    initial_population = 1000000
    initial_gdp_per_capita = 50000
    initial_energy_intensity = 0.5
    initial_fossil_fuel_ratio = 0.8
    initial_co2_emission = 0
    population_growth_rate = 0.01
    gdp_growth_rate = 0.03
    energy_intensity_decrease_rate = 0.02
    fossil_fuel_decrease_rate = 0.01
    carbon_emission_factor = 2.5
    output_csv = 1
    output_image = 1
    output_web = 1

# Simulation time settings
time_steps = 30  # Number of simulation time steps (years)
dt = 1  # Time step (years)

# Initialize a dictionary to store carbon dioxide emission results under different scenarios
co2_emissions = {scenario: np.zeros(time_steps) for scenario in scenarios}
years = np.arange(start_year, start_year + time_steps)

# Loop through each scenario
for scenario, file_name in scenarios.items():
    # Reset parameters to initial values
    current_population_growth_rate = population_growth_rate
    current_gdp_growth_rate = gdp_growth_rate
    current_energy_intensity_decrease_rate = energy_intensity_decrease_rate
    current_fossil_fuel_decrease_rate = fossil_fuel_decrease_rate
    current_population = initial_population
    current_gdp_per_capita = initial_gdp_per_capita
    current_energy_intensity = initial_energy_intensity
    current_fossil_fuel_ratio = initial_fossil_fuel_ratio
    current_co2_emission = initial_co2_emission

    # Read the parameter adjustment file
    adjustment_factors = {}
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                year = int(row['year'])
                pop_factor = float(row['population_growth_rate_factor'])
                gdp_factor = float(row['gdp_growth_rate_factor'])
                energy_factor = float(row['energy_intensity_decrease_rate_factor'])
                fossil_factor = float(row['fossil_fuel_decrease_rate_factor'])
                adjustment_factors[year] = [pop_factor, gdp_factor, energy_factor, fossil_factor]
    except FileNotFoundError:
        print(f"The parameter adjustment file '{file_name}' was not found. Skipping the simulation for the {scenario} scenario.")
        continue

    # Simulation calculation
    for t in range(time_steps):
        current_year = start_year + t
        if current_year in adjustment_factors:
            pop_factor, gdp_factor, energy_factor, fossil_factor = adjustment_factors[current_year]
            current_population_growth_rate *= pop_factor
            current_gdp_growth_rate *= gdp_factor
            current_energy_intensity_decrease_rate *= energy_factor
            current_fossil_fuel_decrease_rate *= fossil_factor

        # Update the population
        current_population = current_population * (1 + current_population_growth_rate * dt)

        # Update the GDP per capita
        current_gdp_per_capita = current_gdp_per_capita * (1 + current_gdp_growth_rate * dt)

        # Update the energy intensity
        current_energy_intensity = current_energy_intensity * (1 - current_energy_intensity_decrease_rate * dt)

        # Update the proportion of fossil fuels
        current_fossil_fuel_ratio = current_fossil_fuel_ratio * (1 - current_fossil_fuel_decrease_rate * dt)

        # Calculate the current - year GDP
        gdp = current_population * current_gdp_per_capita

        # Calculate the energy consumption
        energy_consumption = gdp * current_energy_intensity

        # Calculate the fossil fuel consumption
        fossil_fuel_consumption = energy_consumption * current_fossil_fuel_ratio

        # Calculate the current - year carbon dioxide emissions
        annual_co2_emission = fossil_fuel_consumption * carbon_emission_factor

        # Update the cumulative carbon dioxide emissions
        current_co2_emission = current_co2_emission + annual_co2_emission * dt

        # Store the carbon dioxide emissions at this time step for the current scenario
        co2_emissions[scenario][t] = current_co2_emission

# Output the result data to a CSV file if enabled
if output_csv:
    output_file = 'carbon_emission_results.csv'
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Year'] + list(scenarios.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for i in range(time_steps):
            row = {'Year': years[i]}
            for scenario in scenarios.keys():
                row[scenario] = co2_emissions[scenario][i]
            writer.writerow(row)

    print(f"Result data has been successfully written to {output_file}.")

# Generate and save the image if enabled
if output_image:
    plt.figure(figsize=(12, 8))
    for scenario, emissions in co2_emissions.items():
        plt.plot(years, emissions, label=scenario)
    plt.xlabel('Year')
    plt.ylabel('CO2 Emission (tons)')
    plt.title('City CO2 Emission Prediction under Different Scenarios')
    plt.legend()
    plt.grid(True)

    static_folder = app.static_folder
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)
    image_file = 'carbon_emission_results.png'
    image_path = os.path.join(static_folder, image_file)
    plt.savefig(image_path)
    print(f"Result image has been successfully saved to {image_path}.")

# Start the Flask application and show the web interface if enabled
if output_web:
    @app.route('/')
    def show_results():
        data = []
        if output_csv:
            with open(output_file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        scenario_keys = list(scenarios.keys())
        return render_template('results.html', data=data, scenarios=scenario_keys, years=years.tolist())

    if __name__ == '__main__':
        app.run(debug=True)