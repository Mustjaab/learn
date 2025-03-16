import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo 
    import plotly.express as px
    return mo, px


@app.cell
def _(mo):
    mo.md(r"""#Loading CSVs with DuckDB""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        <p> I remember when I first learnt about DuckDB, it was a gamechanger - I used to load the data I wanted to work on to a database software like MS SQL Server, and then build a bridge to an IDE with the language I wanted to use like Python, or R; it was quite the hassle. DuckDB changed my whole world - now I could just import the data file into the IDE, or notebook, make a duckdb connection, and there we go! But then, I realized I didn't even need the step of first importing the file using python. I could just query the csv file directly using SQL through a DuckDB connection.</p> 

        ##Introduction
        <p> I found this dataset on the evolution of AI research by disclipine from OECD, and it piqued my interest. I feel like publications in natural language processing drastically jumped in the mid 2010s, and I'm excited to find out if that's the case. </p>
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""##Load the CSV""")
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        SELECT * 
        FROM "AI_Research_Data.csv"
        LIMIT 5;
        """
    )
    return


@app.cell
def _(mo):
    Discipline_Analysis = mo.sql(
        f"""
        CREATE TABLE Domain_Analysis AS
            SELECT Year, Concept, publications FROM "AI_Research_Data.csv"
        """
    )
    return Discipline_Analysis, Domain_Analysis


@app.cell
def _(Domain_Analysis, mo):
    Analysis = mo.sql(
        f"""
        SELECT * 
        FROM Domain_Analysis
        GROUP BY Concept, Year, publications
        ORDER BY Year
        """
    )
    return (Analysis,)


@app.cell
def _(Analysis, px):
    px.line(Analysis,x=0,y=2,color=1) 
    return


@app.cell
def _(Domain_Analysis, mo):
    _df = mo.sql(
        f"""
        SELECT Year, Concept, publications, AVG(publications)
        FROM Domain_Analysis
        WHERE Year >= 2020
        AND Concept = 'Natural language processing'
        GROUP BY Year,Concept,publications
        ORDER BY Year
        """
    )
    return


if __name__ == "__main__":
    app.run()
