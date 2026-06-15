# OrangeHRM UI Automation Framework - Playwright (python)

## Overview

This repository contains a UI automation testing framework built with **Python, Playwright, and pytest**, targeting the OrangeHRM demo application.

The project was developed during an intensive QA Automation training focused on building real-world automation skills and understanding how professional QA frameworks are designed, structured, and maintained.

It combines both practical automation implementation and QA engineering principles, including scalable test design, maintainability, and quality-focused development practices.

---

## What This Project Demonstrates

- Designing scalable and maintainable automation frameworks  
- Implementing Page Object Model (POM)  
- Applying Object-Oriented Programming (OOP) principles  
- Building UI automation tests using Playwright + pytest  
- API request handling and validation concepts  
- Test data lifecycle management (Faker)  
- Advanced locator strategies in Playwright  
- Debugging, tracing, and Allure Reports  
- Parallel test execution  
- CI/CD integration using GitHub Actions  
- Code quality enforcement (Pylint)  
- AI-assisted workflows for optimization  

---

## Tech Stack

- Python  
- Playwright  
- Pytest  
- Faker  
- Allure Reports  
- GitHub Actions  
- Pylint  
- UV Package Manager  

---

## Installation & Setup

### 1. Install uv (if not installed)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```
# via pip
pip install uv
```
2. Setup project
```
uv sync
```
3. Install Playwright browsers
```
uv run playwright install
```
4. Run tests
```
uv run pytest
```

## Conclusion

This project represents my hands-on experience in building a scalable UI automation framework using modern QA tools and practices. It helped me strengthen my understanding of test automation design, software quality principles, and real-world QA workflows.
uv run pytest
