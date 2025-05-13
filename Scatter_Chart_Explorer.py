# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "plotly.express",
#     "plotly==6.0.1",
#     "duckdb==1.2.1",
#     "sqlglot==26.11.1",
#     "pyarrow==19.0.1",
#     "polars==1.27.1",
#     "pandas==2.2.3",
# ]
# ///

import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""<h1> <center> Scatter Chart Explorer </h1> </center>""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    return pd, px


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    <h2> Introduction </h2> 
    <p> This notebook explores the ability of using plotly scatter charts as a visual searchable table. Where, you could brush, or select a certain part of the scatter chart, and get that particular section of the table used to make the chart.  </p> 
    <p> In this notebook we'll:</p>
    <ul>
        <li> import a csv file using SQL </li>
        <li> Create a separate table out of the main table</li> 
        <li> Create a scatter chart for the customized table</li> 
        <li> Build a path for creating visualizations like pie charts and bar charts based on selected scatter points</li>
    </ul>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##Data""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM 'prescribed-drug-spending.csv'
        LIMIT 6;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##Extract Data of Interest""")
    return


@app.cell
def _(mo):
    DF = mo.sql(
        f"""
        SELECT Calender_Year, Jurisdiction, Drug_Spending_Lowest_Income_Quantile, Number_of_Beneficiaries_from_the_Highest_Income_Quantiles
        FROM 'prescribed-drug-spending.csv'
        WHERE Calender_Year = '2023'
        """
    )
    return (DF,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ##Create Scatter Chart 
    <p> Because marimo allows for seeamless switching between SQL and Python cells, we can use Python libraries to visualize the products of our queries. We named the SQL cell to DF, so we could reference it as a dataframe for the scatter chart.</p>
    """
    )
    return


@app.cell
def _(DF, mo, px):
    Spending_Scatter = px.scatter(DF,'Jurisdiction','Drug_Spending_Lowest_Income_Quantile', title = 'Scatter Chart of Drug Spending in Lowest Income Quintile by Jurisdiction')
    Spending_Scatter = mo.ui.plotly(Spending_Scatter)
    Spending_Scatter
    return (Spending_Scatter,)


@app.cell
def _(Spending_Scatter, pd):
    Selected_Data = pd.DataFrame(Spending_Scatter.value)
    return (Selected_Data,)


@app.cell
def _(Selected_Data, mo, px):
    mo.hstack([
              px.pie(Selected_Data,'Jurisdiction','Drug_Spending_Lowest_Income_Quantile', title = 'Pie Chart of Drug Spending within Lowest Income Quintile'),
              px.bar(Selected_Data,'Jurisdiction','Drug_Spending_Lowest_Income_Quantile', title = 'Bar Chart of Drug Spending within Lowest Income Quintile')
    ]
    ).center()

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""<p> In order to get the corresponding pie and bar charts, we'll need to select some points by dragging the cursor over the data points of interest. </p>""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ##Conclusion
    <p> In this notebook, we: </p>
    <ul>
        <li> imported a csv file using SQL </li>
        <li> Created a separate table out of the main table</li> 
        <li> Created a scatter chart for the customized table</li> 
        <li> Built a path for creating visualizations like pie charts and bar charts based on selected scatter points</li>
    </ul>
    """
    )
    return


if __name__ == "__main__":
    app.run()
