# Peppi Advanced Recipes

This directory contains advanced Jupyter notebook tutorials for the [Peppi](https://github.com/NASA-PDS/peppi) library, which provides programmatic access to NASA's Planetary Data System (PDS).

## About These Notebooks

These notebooks demonstrate advanced data analysis and workflow patterns using Peppi. They are designed for users who are comfortable with the basics of Peppi and want to explore more sophisticated use cases.

## Notebooks

### Recipe 13: Compare Data Coverage Across Multiple Targets
**File:** `recipe-13-compare-target-coverage.ipynb`

Compare data availability across different planetary bodies. Learn how to:
- Query multiple targets programmatically
- Aggregate results for analysis
- Create comparison DataFrames and visualizations

### Recipe 14: Build a Data Timeline
**File:** `recipe-14-build-data-timeline.ipynb`

Analyze when data was collected over time. Learn how to:
- Extract and parse temporal metadata
- Group data by time periods (year, month, day)
- Visualize data collection timelines
- Identify data gaps and mission phases

### Recipe 15: Find Overlapping Observations
**File:** `recipe-15-overlapping-observations.ipynb`

Find products from different instruments that observed the same target simultaneously. Learn how to:
- Use temporal windows for coordinated observations
- Group results by instrument
- Identify multi-instrument campaigns

### Recipe 16: Create a Custom Data Report
**File:** `recipe-16-custom-data-report.ipynb`

Generate formatted reports about PDS data. Learn how to:
- Extract and format metadata programmatically
- Create reusable report templates
- Output to various formats (text, HTML, etc.)

### Recipe 17: Work with OSIRIS-REx Specialized Products
**File:** `recipe-17-orex-products.ipynb`

Use mission-specific product classes. Learn how to:
- Access specialized product classes (OrexProducts)
- Leverage mission-specific functionality
- Apply standard filters to specialized products

### Recipe 18: Handle Large Result Sets Efficiently
**File:** `recipe-18-large-result-sets.ipynb`

Process thousands of products without memory issues. Learn how to:
- Use field filtering for efficiency
- Implement batch processing
- Manage pagination manually when needed

### Recipe 19: Fuzzy Search Across Multiple Terms
**File:** `recipe-19-fuzzy-search.ipynb`

Leverage fuzzy search to handle typos and uncertain names. Learn how to:
- Use typo-tolerant search
- Handle spelling variations
- Search across targets and spacecraft with uncertain names

### Recipe 20: Build a Reusable Search Function
**File:** `recipe-20-reusable-search-function.ipynb`

Create flexible, reusable search functions. Learn how to:
- Design parameterized search functions
- Handle optional filters elegantly
- Build a library of custom search patterns

## Prerequisites

- Python 3.13 or newer
- Peppi library: `pip install pds.peppi`
- JupyterLab or Jupyter Notebook
- Basic familiarity with Peppi (see [Getting Started Guide](https://nasa-pds.github.io/peppi/getting_started.html))

## Installation

```bash
# Install dependencies
pip install pds.peppi jupyterlab pandas matplotlib

# Start JupyterLab
jupyter lab
```

## Usage

1. Start JupyterLab in this directory
2. Open any notebook
3. Run cells sequentially
4. Modify examples for your own use cases

## Related Resources

- [Peppi Documentation](https://nasa-pds.github.io/peppi/)
- [Peppi GitHub Repository](https://github.com/NASA-PDS/peppi)
- [PDS Search API Documentation](https://nasa-pds.github.io/pds-api/)
- [PDS Data Portal](https://pds.nasa.gov/)

## Contributing

Have a recipe idea? Found an issue? Contributions are welcome!

- Report issues: [NASA-PDS/search-api-notebook/issues](https://github.com/NASA-PDS/search-api-notebook/issues)
- Contribute recipes: Submit a PR with your notebook

## License

Copyright © 2025, California Institute of Technology ("Caltech").
U.S. Government sponsorship acknowledged.

Licensed under the Apache License, Version 2.0. See [LICENSE.md](../../LICENSE.md) for details.
