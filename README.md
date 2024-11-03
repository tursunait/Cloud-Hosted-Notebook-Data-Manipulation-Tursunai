# Amazon Sales Data Analysis and Demand Forecasting
## Cloud-Hosted-Notebook-Data-Manipulation
### By Tursunai Turumbekova 

## Overview
This project provides an analysis of Amazon sales data, focusing on identifying top-selling items, understanding demand patterns influenced by fulfillment and courier performance, and forecasting future demand to optimize inventory and fulfillment planning. Using techniques in data exploration, demand trend analysis, and time series forecasting, this project aims to uncover insights that support better decision-making in product stocking and distribution.

## Project Objectives
1. **Define Top-Selling Items**: Identify items with consistently high sales or revenue to better understand what drives demand.
2. **Analyze Demand by Courier Status**: Examine how delivery performance impacts sales trends.
3. **Demand Forecasting**: Predict future demand for top-selling items using time series forecasting, particularly SARIMA, to inform inventory and fulfillment needs.

## Approach and Methodology

### **1. Data Exploration and Preparation**
   - **Data Loading and Cleaning**: Imported Amazon sales data containing 24 columns, including fields like `SKU`, `Category`, `Status`, `Fulfilment`, `Courier Status`, and financial details (`Qty`, `Amount`, `currency`).
   - **Data Summary**: Used `pandas` for data inspection and summary statistics to understand non-null counts, data types, and memory usage. Missing values were addressed, especially in key columns like `Courier Status` and `Amount`.

### **2. Identifying Top-Selling Items**
   - **Grouping Data**: Grouped data by `SKU`, `Category`, and `Style` to calculate total `Qty` (sales volume) and `Amount` (revenue).
   - **Defining Criteria**: Items in the top 10% by cumulative revenue or sales volume over a specified period were classified as "Top-Selling Items."
   - **Objective**: Recognize high-demand products to prioritize for forecasting and deeper analysis.
![Daily Completed Sales Volume and Unfulfilled Demand for Top-Selling Items](img/unfullfilled_demand.png)

### **3. Measuring Future Demand Trends by Courier Status**
   - **Impact Analysis**: Evaluated whether different courier statuses (e.g., delayed vs. on-time deliveries) influence future sales volumes.
   - **Monthly/Quarterly Demand Calculation**: Computed average monthly or quarterly sales volumes for each SKU, then compared trends based on courier status.
   - **Visualization**: Created line plots by fulfillment method to contrast demand trends for "Shipped," "Cancelled," and "Unshipped" statuses, helping to assess if certain fulfillment methods correlate with higher cancellations or reduced future demand.
![Daily Demand Trends by Fulfillment Method and Courier Status for Top-Selling Items](img/unfulfillment_by_method.png)

### **4. Demand Forecasting Using SARIMA**
   - **Forecasting Tool**: Leveraged SARIMA for time series forecasting to model future demand trends.
   - **Model Insights**: SARIMA forecasts indicate a potential seasonal dip, with demand gradually declining for top-selling items. A widening confidence interval suggests increased uncertainty in longer-term predictions.
   - **Inventory and Fulfillment Planning**: Forecasting results support proactive planning for high-demand periods and inventory adjustments, minimizing stockouts and improving customer satisfaction.
   - **Recommendation**: Regularly update the model with new data to refine predictions and respond to demand fluctuations.
![Demand Forecast for Top-Selling Items](img/forecast.png)
## Dependencies
Refer to `requirements.txt` for a list of packages required, including:
- **DevOps Tools**: `black`, `pytest`, `pytest-cov`, `nbval`
- **Analysis Tools**: `pandas`, `matplotlib`, `tabulate`
- **Ruff Linter**: `ruff`

Install all dependencies with:
```bash
make install
```

## Makefile Commands
The `Makefile` automates essential tasks, ensuring code quality and consistent data processing:

- **`make install`**: Installs all required packages.
- **`make test`**: Runs tests on IPython notebooks and code files.
- **`make format`**: Formats Python files using Black.
- **`make lint`**: Lints code with Ruff.
- **`make refactor`**: Combines formatting and linting for a clean codebase.
- **`make all`**: Executes the full pipeline (`install`, `lint`, `test`, `format`, and `deploy` if defined).

## CI/CD Pipeline
An automated CI/CD pipeline is configured to:

1. **Lint**: Enforces code style and quality.
2. **Format**: Ensures code consistency.
3. **Test**: Verifies functionality and accuracy of the code.
4. **Deploy**: (If applicable) Deploys the project.

## Project Structure
- `data/`: Contains raw and processed data files.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and modeling.
- `src/`: Core Python scripts for data processing, analysis, and modeling.
- `tests/`: Unit tests for code validation.
- `requirements.txt`: List of dependencies.
- `Makefile`: Command-line automation of project tasks.

## Future Enhancements
- **Integration of Prophet**: Expand demand forecasting by comparing SARIMA with Prophet, exploring Prophet's handling of seasonality and trends.
- **Model Optimization**: Enhance SARIMA model performance by tuning parameters based on demand patterns.
- **Real-time Data Feeds**: Incorporate real-time sales and courier data to update forecasts dynamically.

## License
This project is licensed under the [MIT License](LICENSE).
