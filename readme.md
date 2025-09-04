# Gemini AI Job Description Q&A

This app uses Google Gemini AI to answer questions about a job description provided in a text file. It leverages text embeddings to retrieve relevant context and generates answers using Gemini's generative model.

## Features

- Loads a job description from `job.txt`
- Splits the text into manageable chunks for embedding
- Uses Google Gemini API for text embeddings and content generation
- Retrieves the most relevant chunks based on user queries
- Interactive Streamlit interface for Q&A

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [numpy](https://numpy.org/)

## Setup

1. Clone this repository or copy the files to your project directory.
2. Install dependencies:
    ```sh
    pip install streamlit google-generativeai numpy
    ```
3. Add your Google Gemini API key to the `GOOGLE_API_KEY` variable in [`gemini-ap.py`](d:/Python/pythonclass/AI/gemini/gemini-ap.py).
4. Ensure your job description is in [`job.txt`](d:/Python/pythonclass/AI/gemini/job.txt).

## Usage

Run the Streamlit app:

```sh
streamlit run gemini-ap.py
```

Enter your query in the chat input to get answers based on the job description.

## Files

- [`gemini-ap.py`](d:/Python/pythonclass/AI/gemini/gemini-ap.py): Main application code.
- [`job.txt`](d:/Python/pythonclass/AI/gemini/job.txt): Job description used for context.

## License

This project is for educational purposes.