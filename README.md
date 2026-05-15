# GitPulse


**GitPulse** is a web-based FOSS (Free and Open-Source Software) Health Dashboard. It helps junior developers and open-source contributors analyze GitHub repositories to see how active, healthy, and beginner-friendly a community is before they decide to contribute.

## The Problem We Solve
Finding a welcoming open-source project can be a pain point for new developers. Some repositories look popular but have dead issue trackers, while others lack basic community guidelines. **GitPulse** takes a GitHub URL, fetches live data using the GitHub REST API, and generates a human-readable "Health Report."

## Features (Current & Planned)
- [x] **API Integration:** Secure connection to GitHub REST API using fine-grained tokens.
- [ ] **Smart URL Parsing:** Automatically extracts `owner/repo` from any valid GitHub link.
- [ ] **Vitals Check:** Analyzes stars, forks, and the number of open issues.
- [ ] **Community Standards:** Checks for the existence of `README.md`, `LICENSE`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md`.
- [ ] **Activity Scoring:** Checks the date of the last commit to identify dormant/abandoned projects.
- [ ] **Web UI:** Interactive and beautiful frontend built with Streamlit.

## Tech Stack
*   **Backend & Logic:** Python 3, `requests`
*   **Security:** `python-dotenv` (for API token management)
*   **Frontend:** [Streamlit](https://streamlit.io/) *(coming soon)*
*   **Testing:** `pytest` (for URL parsing and API fetching tests)

## Project Structure
```text
GitPulse/
├── docs/                # Documentation and project domain info
├── src/                 # Main application source code
├── tests/               # Automated tests (e.g., test_API.py)
├── .env                 # Secret API tokens (Ignored by Git)
├── .gitignore           # Files to be ignored by version control
├── Makefile             # Terminal command shortcuts
├── README.md            # Project description
├── requirements.txt     # Python dependencies
└── setup.py             # Package configuration
```

## Local Setup & Installation

To run GitPulse locally on your machine, follow these steps:

**1. Clone the repository**
```bash
git clone https://github.com/ol1xy/GitPulse.git
cd GitPulse
```

**2. Set up a virtual environment**
```bash
make shell
```

**3. Install dependencies**
```bash
make install-dep
make install
```

**4. Set up your Environment Variables**
Create a `.env` file in the root directory (if it doesn't exist) and add your GitHub Personal Access Token to avoid rate limits:
```text
GITHUB_TOKEN=your_fine_grained_token_here
```
*(Note: Never commit your `.env` file to GitHub! It is already included in our `.gitignore`).*

**5. Run the application** *(Streamlit integration in progress)*
```bash
# Currently testing backend API:
python tests/test_API.py
```

## Roadmap (Sprint Plan)
- **day 1:** Setup repo, API fetching, and URL parsing logic + Unit tests.
- **day 2:** Implement scoring logic, English text generation, and Streamlit Web UI.
- **day 3:** Deploy to Streamlit Community Cloud and prepare case studies for the pitch.

## Contributing
Contributions, issues, and feature requests are welcome! Since this project is actively developed as a university assignment, please reach out via Issues before opening a Pull Request.

## License
This project is licensed under the [GNU License](LICENSE).
