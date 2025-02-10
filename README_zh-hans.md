### 1. 概述
该模型用于预测一个城市的碳排放。它运用系统动力学模型，对不同情景（包括基准情景、低碳情景和零碳情景）下的城市二氧化碳排放量进行预测。该系统从 CSV 文件中读取参数数据，开展模拟运算，并能以三种形式输出结果：将数据保存为 CSV 文件、生成排放趋势图像，以及在网页上展示结果。用户可通过修改 `model_parameters.csv` 文件来调整输出形式。

### 2. 文件结构
```plaintext
carbon_emission_prediction/
│
├── run.py
├── templates/
│   └── results.html
├── static/
│   └── carbon_emission_results.png （如果启用则会生成）
├── model_parameters.csv
├── base_scenario.csv
├── low_carbon_scenario.csv
├── zero_carbon_scenario.csv
├── carbon_emission_results.csv （如果启用则会生成）
```

### 3. 关键文件及其功能

#### 3.1 主程序文件 `run.py`
这是程序的核心文件，包含了模型的主要逻辑和模拟过程。其具体功能如下：
- **参数读取**：从 `model_parameters.csv` 文件中读取模型的初始参数，包括起始年份、初始人口、初始人均国内生产总值等。
- **场景设置**：定义三种场景（基本场景、低碳场景和零碳场景），并从相应的CSV文件中读取每个场景的参数调整信息。
- **模拟计算**：根据读取的参数，程序逐年模拟城市的人口、国内生产总值、能源消耗和二氧化碳排放量。并且，它会根据场景参数每五年调整一次参数。
- **结果可视化**：使用 `matplotlib` 库将三种场景下的二氧化碳排放趋势绘制成折线图，方便用户直观地比较不同场景下的排放差异。
- **输出结果**：
    - **CSV输出**：如果 `output_csv` 设置为 `1`，则将模拟结果保存到 `carbon_emission_results.csv` 中。
    - **图像生成**：如果 `output_image` 设置为 `1`，则使用 `matplotlib` 生成一个显示不同场景下碳排放趋势的折线图，并将其保存为 `carbon_emission_results.png` 到 `static` 目录中。
    - **网页显示**：如果 `output_web` 设置为 `1`，则启动一个Flask应用程序并渲染 `results.html` 模板，以便在网页上显示结果。

#### 3.2 模型参数文件（`model_parameters.csv`）
该文件存储了模型的初始参数。每行包含以下字段：
| 字段名称 | 含义 | 示例值 |
| ---- | ---- | ---- |
| `start_year` | 模拟的起始年份 | 2020 |
| `initial_population` | 起始年份的城市人口 | 1000000 |
| `initial_gdp_per_capita` | 起始年份的人均国内生产总值 | 50000 |
| `initial_energy_intensity` | 起始年份的能源强度（单位国内生产总值的能源消耗） | 0.5 |
| `initial_fossil_fuel_ratio` | 起始年份的化石燃料比例 | 0.8 |
| `initial_co2_emission` | 起始年份的累计二氧化碳排放量 | 0 |
| `population_growth_rate` | 人口增长率 | 0.01 |
| `gdp_growth_rate` | 国内生产总值增长率 | 0.03 |
| `energy_intensity_decrease_rate` | 能源强度下降率 | 0.02 |
| `fossil_fuel_decrease_rate` | 化石燃料比例下降率 | 0.01 |
| `carbon_emission_factor` | 化石燃料的碳排放因子 | 2.5 |

#### 3.3 场景参数文件
- **基本场景文件（`base_scenario.csv`）**
- **低碳场景文件（`low_carbon_scenario.csv`）**
- **零碳场景文件（`zero_carbon_scenario.csv`）**

这三个文件分别存储了三种场景下每五年的参数调整信息。每行包含以下字段：
| 字段名称 | 含义 | 示例值 |
| ---- | ---- | ---- |
| `year` | 参数调整的具体年份 | 2025 |
| `population_growth_rate_factor` | 人口增长率的调整系数 | 0.95 |
| `gdp_growth_rate_factor` | 国内生产总值增长率的调整系数 | 0.98 |
| `energy_intensity_decrease_rate_factor` | 能源强度下降率的调整系数 | 1.05 |
| `fossil_fuel_decrease_rate_factor` | 化石燃料比例下降率的调整系数 | 1.05 |


### 4. 使用方法
1. **环境设置**：确保你已经安装了Python，以及所需的库，如 `Flask`、`numpy` 和 `matplotlib`。你可以使用以下命令进行安装：
```bash
pip install flask numpy matplotlib
```
2. **配置参数**：根据你的需求修改 `model_parameters.csv` 文件，以设置初始参数和输出形式。
3. **运行程序**：在终端中执行 `run.py` 脚本：
```bash
python run.py
```
4. **查看结果**：
    - **CSV结果**：如果 `output_csv` 设置为 `1`，你可以在 `carbon_emission_results.csv` 文件中找到模拟结果。
    - **图像结果**：如果 `output_image` 设置为 `1`，生成的图像将保存为 `carbon_emission_results.png` 到 `static` 目录中。
    - **网页结果**：如果 `output_web` 设置为 `1`，打开网页浏览器并访问 `http://127.0.0.1:5000/` 以查看显示不同场景下碳排放趋势的动态图表。

### 5. 注意事项
- 确保CSV文件（`model_parameters.csv`、`base_scenario.csv` 等）存在于正确的目录中，并且格式正确。
- 如果你遇到任何问题，请检查控制台输出的错误信息，以帮助排查问题。
