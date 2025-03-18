# Purpose

This project explores the application of large language models in password security research. It uses Gemma, a powerful language model, to:

1. Generate realistic password variations based on existing password datasets
2. Predict and analyze password patterns to understand common user tendencies
3. Evaluate password security by identifying predictable patterns

The insights gained from this project can help:
- Improve password security policies
- Develop better password strength metrics
- Understand how attackers might exploit password patterns
- Create more effective password generation guidelines

# Getting Started

## Prerequisites

1. **LM Studio Setup**
   - Download and install LM Studio from [https://lmstudio.ai/](https://lmstudio.ai/)
   - Download the Gemma-3b-12b-it model (approximately 7.33GB)
   - Launch LM Studio and load the Gemma model
   - Start the local server in LM Studio (should run on `localhost:1234`)

2. **Install UV**
   ```bash
   pipx install uv
   ```

## Running the Project
1. Clone this repository
2. Install dependencies:
   ```bash
   uv pip install -r pyproject.toml
   ```
3. Run the main script:
   ```bash
   uv run python main.py
   ```

# Datasets
- https://www.skullsecurity.org/wiki/Passwords
- https://github.com/yuqian5/PasswordCollection

# Models
- Gemma-3-12b-it ~ 7.33GB

# Results
