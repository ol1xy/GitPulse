# GitPulse
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue) ![Tests](https://img.shields.io/badge/tests-25%20passed-success) ![UI](https://img.shields.io/badge/UI-Streamlit-FF4B4B) ![License](https://img.shields.io/badge/license-GPL-green)

**GitPulse** is a web-based FOSS (Free and Open-Source Software) Health Dashboard. It helps junior developers and open-source contributors analyze GitHub repositories to see how active, healthy, and beginner-friendly a community is before they decide to contribute.

##   Live Demo
The application is officially live and publicly accessible! Try it now without any installation:
**[gitpulse.streamlit.app](https://gitpulse.streamlit.app/)**

*(No GitHub token or setup required for the web version)*


## The Problem We Solve
Finding a welcoming open-source project can be a pain point for new developers. Some repositories look popular but have dead issue trackers, while others lack basic community guidelines. **GitPulse** takes a GitHub URL, fetches live data using the GitHub REST API, and generates a human-readable "Health Report."

## Features (Current & Planned)
- [x] **API Integration:** Secure connection to GitHub REST API using fine-grained tokens.
- [x] **Smart URL Parsing:** Automatically extracts `owner/repo` from any valid/messy GitHub link.
- [x] **Activity Logic:** Calculates days since the last push to identify abandoned projects.
- [x] **Community Scoring:** A weighted algorithm that checks for `README`, `LICENSE`, `CONTRIBUTING`, and `CODE_OF_CONDUCT`.
- [x] **Engagement Rate:** Calculates the Forks-to-Stars ratio to distinguish true engagement from "vanity metrics".
- [x] **Automated Tests:** 100% test coverage for logic and parsing using `pytest` and mock side-effects.
- [x] **Web UI:** Interactive frontend built with Streamlit.

## Tech Stack
*   **Backend & Logic:** Python 3, `requests`
*   **Security:** `python-dotenv` (for API token management)
*   **Frontend:** [Streamlit](https://streamlit.io/)
*   **Testing:** `pytest`, `unittest`

## How the Scoring Works
We don't just display raw data. Our backend calculates specific statuses:
*   **Activity:** Projects inactive for >365 days are marked as `critical` (abandoned).
*   **Community:** `CONTRIBUTING.md` gives the highest score (30 pts), because it is the most vital file for FOSS newcomers.
*   **Engagement:** If the Forks-to-Stars ratio is below 5%, it raises a red flag (users bookmark the project, but rarely write code for it). 

## Project Structure
```text
GitPulse/
├── src/                 # Main source code (The "Brain" of GitPulse)
│   ├── api.py           # GitHub REST API interaction logic
│   ├── logic.py         # Scoring algorithm and health metrics
│   └── parser.py        # URL validation and string parsing
├── tests/               # Automated test suite (100% logic coverage)
│   ├── test_API.py      # Mocks for API responses
│   ├── test_logic.py    # Unit tests for scoring heuristics
│   └── test_parser.py   # Parameterized tests for URL parsing
├── docs                 # Project documentation and visual architecture
│   └── sequence_diagram.drawio  # Visual UML sequence diagram (Draw.io)
├── CONTRIBUTING.md      # Guidelines for new contributors
├── LICENSE              # MIT License
├── Makefile             # Project automation (make test, make run)
├── README.md            # Project overview and documentation
├── requirements.txt     # List of external dependencies
└── app.py               # Main streamlit app
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
Add your GitHub personal access token to the `.env` file in the root directory to avoid rate limits:
```text
GITHUB_TOKEN=your_fine_grained_token_here
```
*(Note: Never commit your `.env` file to GitHub! It is already included in our `.gitignore`).*

**5. Run the application**
```bash
streamlit run app.py
```

## Contributing
Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the [GNU License](LICENSE).
