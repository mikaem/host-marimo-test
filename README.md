# host-marimo-test

This repository demonstrates how to host [marimo](https://marimo.io) notebooks on GitHub Pages. The setup automatically converts marimo Python files to HTML and deploys them to GitHub Pages.

## 📁 Repository Structure

- `notebooks/` - Contains marimo notebook files (`.py` format)
- `.github/workflows/deploy-notebooks.yml` - GitHub Actions workflow for automatic deployment
- `requirements.txt` - Python dependencies

## 🚀 How It Works

1. **Main Branch**: Store your marimo notebooks as Python files in the `notebooks/` directory
2. **Automatic Conversion**: On every push to `main`, GitHub Actions converts notebooks to HTML
3. **GitHub Pages**: The HTML files are automatically deployed to the `gh-pages` branch and served via GitHub Pages

## 📝 Adding New Notebooks

1. Create your marimo notebook (e.g., using `marimo edit notebook_name.py`)
2. Save it in the `notebooks/` directory
3. Commit and push to the `main` branch
4. The workflow will automatically convert and deploy it

## 🛠️ Local Development

### Prerequisites

```bash
pip install -r requirements.txt
```



### Running Notebooks Locally

```bash
# Edit a notebook
marimo edit notebooks/example.py

# Run a notebook
marimo run notebooks/example.py

# Export to HTML manually
marimo export html notebooks/example.py -o output.html
```

## 🌐 Viewing Your Notebooks

After the workflow runs successfully, your notebooks will be available at:
```
https://[username].github.io/[repository-name]/
```

For this repository:
```
https://mikaem.github.io/host-marimo-test/
```

## ⚙️ Setup Instructions

### First Time Setup

1. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Under "Source", select the `gh-pages` branch
   - Click Save

2. **Workflow Permissions**:
   - Go to Settings → Actions → General
   - Scroll to "Workflow permissions"
   - Select "Read and write permissions"
   - Save

3. **Push your first notebook** to the `main` branch, and the workflow will run automatically

## 📦 Dependencies

- **marimo**: Interactive Python notebooks
- **numpy**: Numerical computing
- **matplotlib**: Plotting library
- **pandas**: Data manipulation

## 🔧 Customization

### Adding More Dependencies

Edit `requirements.txt` to add more Python packages needed by your notebooks.

### Modifying the Workflow

Edit `.github/workflows/deploy-notebooks.yml` to customize:
- Python version
- Branch triggers
- Deployment settings
- Output styling

### Styling the Index Page

The workflow creates an `index.html` that lists all notebooks. You can customize the styling in the workflow file under "Create index.html" step.

## 📚 Resources

- [marimo Documentation](https://docs.marimo.io)
- [marimo GitHub](https://github.com/marimo-team/marimo)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## 📄 License

See [LICENSE](LICENSE) file for details.
