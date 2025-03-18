# Large Language Models for Password Security Research

## Table of Contents
- [Purpose](#purpose)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Project](#running-the-project)
- [Datasets](#datasets)
- [Models](#models)
- [Results](#results)

## Purpose

This project explores the application of large language models in password security research. It uses Gemma, a powerful language model, to:

1. Generate realistic password variations based on existing password datasets
2. Predict and analyze password patterns to understand common user tendencies
3. Evaluate password security by identifying predictable patterns

The insights gained from this project can help:
- Improve password security policies
- Develop better password strength metrics
- Understand how attackers might exploit password patterns
- Create more effective password generation guidelines

## Getting Started

### Prerequisites

1. **LM Studio Setup**
   - Download and install LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/)
   - Download the Gemma-3b-12b-it model (approximately 7.33GB)
   - Launch LM Studio and load the Gemma model
   - Start the local server in LM Studio (should run on `localhost:1234`)

2. **Install UV**

- macOS/Linux
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
- Windows
   ```bash
   # On Windows.
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

### Running the Project
1. Clone this repository
2. Install dependencies:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Run the main script:
   ```bash
   uv run python main.py
   ```

## Datasets
- https://www.skullsecurity.org/wiki/Passwords
- https://github.com/yuqian5/PasswordCollection

## Models
- Gemma-3-12b-it ~ 7.33GB

## Results

The generated passwords are stored in the `generations/` directory. Each file in this directory is a text file (`.txt`) containing passwords generated with specific parameters:

- Files are named according to the dataset and temperature used (e.g., `000webhost_t=0.1_passwords.txt`)
- Different temperature values (0.1, 0.5, 1.0) affect the randomness of the generated passwords
  - Lower temperatures (0.1) produce more conservative, pattern-following passwords
  - Higher temperatures (1.0) generate more diverse and unique passwords
  
To analyze the results:
- Examine the generated password files to identify patterns
- Compare passwords across different temperature settings to understand how randomness affects generation
- Perform frequency analysis on character usage and password structures
- Evaluate the diversity and strength of generated passwords against the original dataset
