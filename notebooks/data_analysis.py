import marimo


__generated_with = "0.9.30"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, np, pd, plt


@app.cell
def __(mo):
    mo.md(
        r"""
        # Data Analysis Example
        
        This notebook demonstrates data analysis capabilities with marimo.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Generate Sample Data
        
        Let's create a sample dataset for analysis:
        """
    )
    return


@app.cell
def __(np, pd):
    # Generate sample data
    np.random.seed(42)
    n_samples = 100
    
    data = pd.DataFrame({
        'x': np.linspace(0, 10, n_samples),
        'y': 2 * np.linspace(0, 10, n_samples) + np.random.normal(0, 1, n_samples),
        'category': np.random.choice(['A', 'B', 'C'], n_samples),
        'value': np.random.uniform(10, 100, n_samples)
    })
    
    data
    return data, n_samples


@app.cell
def __(data, mo):
    mo.md(
        f"""
        ## Dataset Statistics
        
        - **Total samples**: {len(data)}
        - **Mean value**: {data['value'].mean():.2f}
        - **Std deviation**: {data['value'].std():.2f}
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Visualization
        
        Let's visualize the relationship between x and y:
        """
    )
    return


@app.cell
def __(data, plt):
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Scatter plot
    ax1.scatter(data['x'], data['y'], alpha=0.6, c='steelblue', edgecolors='navy')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Scatter Plot: X vs Y')
    ax1.grid(True, alpha=0.3)
    
    # Histogram
    ax2.hist(data['value'], bins=20, color='coral', edgecolor='darkred', alpha=0.7)
    ax2.set_xlabel('Value')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Distribution of Values')
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.close()
    fig1
    return ax1, ax2, fig1


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Category Analysis
        
        Let's analyze the data by category:
        """
    )
    return


@app.cell
def __(data, mo):
    category_stats = data.groupby('category')['value'].agg(['count', 'mean', 'std'])
    mo.ui.table(category_stats)
    return category_stats,


@app.cell
def __(data, plt):
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    
    categories = data.groupby('category')['value'].mean().sort_values()
    categories.plot(kind='barh', ax=ax3, color='skyblue', edgecolor='navy')
    
    ax3.set_xlabel('Mean Value')
    ax3.set_ylabel('Category')
    ax3.set_title('Average Value by Category')
    ax3.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.close()
    fig2
    return ax3, categories, fig2


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Interactive Filtering
        
        Use the slider to filter data based on value:
        """
    )
    return


@app.cell
def __(data, mo):
    threshold = mo.ui.slider(
        start=data['value'].min(),
        stop=data['value'].max(),
        value=data['value'].mean(),
        label="Value threshold:",
        show_value=True
    )
    threshold
    return threshold,


@app.cell
def __(data, mo, threshold):
    filtered_data = data[data['value'] >= threshold.value]
    mo.md(
        f"""
        **Filtered dataset**: {len(filtered_data)} samples with value >= {threshold.value:.2f}
        """
    )
    return filtered_data,


@app.cell
def __(filtered_data, mo):
    mo.ui.table(filtered_data.head(10))
    return


if __name__ == "__main__":
    app.run()
