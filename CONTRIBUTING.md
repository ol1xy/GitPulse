# Contributing to GitPulse

First off, thank you for considering contributing to GitPulse! 

## How can you contribute?

### 1. Reporting Bugs
If you find a bug (e.g., the URL parser crashes on a specific link format), please open an Issue. Describe the expected behavior and the actual behavior.

### 2. Suggesting Enhancements
Want to add a new metric to our Scoring Logic? Open an issue and explain why this metric is important for open-source health.

### 3. Submitting Pull Requests
1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'feat: add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request.

## Development Setup
Before submitting a PR, ensure that all tests pass:
```bash
make test-pytest
```
*Note: We use `pytest` with mocked API responses. You do not need an active internet connection to run the tests.*