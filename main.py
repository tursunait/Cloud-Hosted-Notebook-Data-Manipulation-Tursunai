"""
Main cli or app entry point
"""

# importing packages
import pandas as pd

from mylib.lib import (
    load_dataset,
    calculate_mean,
    calculate_median,
    calculate_std_dev,
    build_graph,
    build_graph2,
)


# loading the data
def load_df(filepath):
    df = load_dataset(filepath)
    return df


# Generate statistics
def gen_stat(df, analysis_col):
    mean = calculate_mean(df, analysis_col)
    median = calculate_median(df, analysis_col)
    std_dev = calculate_std_dev(df, analysis_col)
    # Creating a DataFrame for the markdown table
    stats_dict = {
        "Statistic": ["Mean", "Median", "Standard Deviation"],
        "Value": [mean, median, std_dev],
    }
    stats_df = pd.DataFrame(stats_dict)
    return stats_df


# generating graphs
def gen_graphs(
    df,
    x_col,
    y_col,
    plot_title,
    xlabel,
    ylabel,
    x2_col,
    y2_col,
    graph2_title,
    jupyter_render=False,
):
    build_graph(
        df,
        x_col,
        y_col,
        plot_title,
        xlabel,
        ylabel,
        color="lightgray",
        jupyter_render=jupyter_render,
    )
    # Distribution of material types
    build_graph2(df, x2_col, y2_col, graph2_title, jupyter_render=jupyter_render)


def save_to_md():
    # Write the markdown table to a file
    describe_df = gen_stat(df, analysis_col)
    markdown_table = describe_df.to_markdown()
    gen_graphs(
        df,
        x_col,
        y_col,
        plot_title,
        xlabel,
        ylabel,
        x2_col,
        y2_col,
        graph2_title,
        jupyter_render=False,
    )
    with open("MTA.md", "w") as file:
        file.write("Describe:\n")
        file.write(markdown_table)
        file.write("\n\n")
        file.write("![MTA_bar1](bar.png)\n")
        file.write("\n\n")
        file.write("![MTA_bar2](bar2.png)")


# Parameters for the analysis
filepath = "MTA_NYCT_Stat.csv"
analysis_col = "Total Incoming Calls"
x_col = "Month of Year"
y_col = "Total Incoming Calls"
plot_title = "MTA_Seasonality"
xlabel = "Month of Year"
ylabel = "Total Incoming Calls"
x2_col = "Year"
y2_col = "Social Media Customer Satisfaction Score"
graph2_title = "Social Media Customer Satisfaction Score"
# Loading the data
df = load_df(filepath)
# Call generate_statistics
gen_stat(df, analysis_col)
# Call generate graphs
gen_graphs(
    df,
    x_col,
    y_col,
    plot_title,
    xlabel,
    ylabel,
    x2_col,
    y2_col,
    graph2_title,
    jupyter_render=False,
)
# Saving it to markdown
save_to_md()
