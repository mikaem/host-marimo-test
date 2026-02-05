import marimo

__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        r"""
        # Welcome to Marimo!
        
        This is an example marimo notebook that demonstrates basic functionality.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Interactive Slider
        
        Try moving the slider below:
        """
    )
    return


@app.cell
def __(mo):
    slider = mo.ui.slider(0, 100, value=50, label="Value:")
    slider
    return slider,


@app.cell
def __(mo, slider):
    mo.md(f"The slider value is: **{slider.value}**")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Simple Calculation
        
        Let's do some basic math:
        """
    )
    return


@app.cell
def __():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def __(np, plt):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.set_title('Sine Wave')
    ax.grid(True, alpha=0.3)
    plt.close()
    fig
    return ax, fig, x, y


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Data Table Example
        
        Here's a simple data table:
        """
    )
    return


@app.cell
def __(mo, np):
    import pandas as pd
    
    data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': np.random.randint(60, 100, 4)
    })
    
    mo.ui.table(data)
    return data, pd


if __name__ == "__main__":
    app.run()
