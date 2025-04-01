# README

## Project Overview
This project utilizes Google Gemini for AI-powered data analysis. It enables users to perform exploratory data analysis (EDA), filter data by timeline, ask questions about the dataset, and visualize insights through interactive charts using Streamlit.

## Features
- Load and analyze datasets directly in code.
- Handle missing values and perform type conversions.
- Filter data based on timeline.
- Interactive visualizations.
- AI-powered insights using Google Gemini.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the Streamlit application using:
```sh
streamlit run Gemini.py
```

## Dependencies
Below are the main dependencies required for this project:
- `streamlit`
- `pandas`
- `chardet`
- `plotly`
- `google-generativeai`
- `python-dotenv`
- `langchain-core`
- `langchain-google-genai`
- `statsmodels`
- `scikit-learn`

These are listed in `requirements.txt` for installation.

## License
This project is licensed under the MIT License.

