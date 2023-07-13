# Rewriter

## Description

Rewriter is a web application that allows users to rewrite articles.It uses chatgpt. It utilizes Flask as the backend framework and Vite as the frontend build tool. With Rewriter, users can input an article, and the application will generate alternative versions of the article by rephrasing sentences and replacing words while preserving the overall meaning.

## Features

- **Article Rewriting**: Users can input an article and generate alternative versions by applying various rewriting techniques.
- **Sentence Rephrasing**: Rewriter can rephrase sentences using different sentence structures and synonyms.
- **Word Replacement**: The application can replace words with similar alternatives to create varied versions of the original article.
- **Preservation of Meaning**: Rewriter ensures that the rewritten articles maintain the overall meaning of the original text.
- **Flask Backend**: The application utilizes Flask, a Python web framework, to handle the backend logic and serve the API endpoints.
- **Vite Frontend**: Vite, a frontend build tool for modern web development, is used to build and bundle the frontend components of the application.

## Installation

1. Make sure you have python installed.

1. Clone the repository: `git clone https://github.com/Hasnain190/rewriter.git` (You must also install git for this command to work.Otherwise just download it)

1. Navigate to the project directory: `cd rewriter`
1. Create a virtual environment (optional): `python -m virtualenv venv`
1. Activate the virtual environment (optional):
   - For Windows: `venv\Scripts\activate`
   - For Unix/Linux: `source venv/bin/activate`
1. Install the dependencies: `pip install -r requirements.txt`
1. Install Node.js and npm if you haven't already.
1. Navigate to the `frontend` directory: `cd frontend`
1. Install the frontend dependencies: `npm install`

## Configuration

1. Open the `.env` file and modify the configuration values if needed.

## Usage

1. Make sure you are in the project root directory.
2. Activate the virtual environment if you created one (see installation step 4).
3. Start the Flask backend server: `flask run`
4. In a separate terminal, navigate to the `frontend` directory.
5. Start the Vite frontend development server: `npm run dev`
6. Open your browser and visit `http://localhost:3000` to access the Rewriter application.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/rewriter`.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request detailing your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The development of Rewriter was inspired by the need for an article rewriting tool and the power of Flask and Vite in web development. We would like to thank the open-source community for their valuable contributions and the creators of Flask and Vite for their amazing frameworks.
