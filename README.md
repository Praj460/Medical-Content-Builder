# Medical Content Builder

A Streamlit application that leverages Google Gemini (Gemini-2.0-Flash) and SentenceTransformer embeddings to generate concise, referenced medical content and validate it against authoritative sources.

## Features

* **Interactive Q\&A**: Users can input medical questions and receive AI-generated answers.
* **Reference Extraction**: Automatically extracts URLs from the AI response.
* **Content Similarity Scoring**: Computes similarity scores between the generated answer and the fetched content of each reference URL using MiniLM embeddings.
* **Most Relevant Source Identification**: Highlights which reference URL the AI answer most closely matches.
* **Regeneration with References**: Regenerates content by combining all fetched reference contents and prompting the LLM to synthesize a consolidated answer.

## Requirements

* Python 3.8+
* [Streamlit](https://streamlit.io/)
* [google-generativeai](https://pypi.org/project/google-generativeai/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [sentence-transformers](https://www.sbert.net/)

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/medical-content-builder.git
   cd medical-content-builder
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables**

   * Create a `.env` file in the project root:

     ```env
     GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
     ```
   * Replace `YOUR_GOOGLE_GEMINI_API_KEY` with your actual API key.

2. **Load the `.env` file**

   * The app uses `python-dotenv` to load environment variables automatically.

## Usage

1. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

2. **Interact via Web UI**

   * Open the provided local URL (usually `http://localhost:8501`).
   * Enter your medical question in the input box.
   * Click **Ask the question** to view:

     * The AI-generated answer.
     * Extracted reference URLs.
     * Similarity scores and the most relevant source.

## Code Structure

* `app.py`
  Main Streamlit application with:

  * API configuration and initialization
  * User interface layout
  * Functions:

    * `get_gemini_response(question)`: Prompts Gemini-2.0-Flash for answers with structured references.
    * `extract_urls(text)`: Uses regex to find URLs in text.
    * `fetch_url_content(url)`: (Placeholder) Simulates fetching page content.
    * `calculate_similarity(text1, text2)`: Computes cosine similarity with `all-MiniLM-L6-v2`.

* `.env`
  Environment file storing sensitive API credentials.

* `requirements.txt`
  Lists required Python packages.

## Customization

* **Actual URL Fetching**: Replace `fetch_url_content` placeholder with real HTTP requests (e.g., using `requests` or `aiohttp`).
* **Model Variants**: Swap out `gemini-2.0-flash` for other Gemini models if available.
* **Advanced Scoring**: Adjust or extend similarity metrics (e.g., incorporate readability or domain-specific scoring).

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Developed by Prajwal Anand*
