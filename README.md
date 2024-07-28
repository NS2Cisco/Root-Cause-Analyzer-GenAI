
# Root Cause Analyzer Application

## Overview

Welcome to the Root Cause Analyzer Application repository! This project leverages the power of generative AI and modular programming to provide a comprehensive solution for performing root cause analysis. The application allows users to analyze problems, identify root causes, and suggest actionable solutions to prevent recurrence.

## Features

- **Modular Programming:** The application is designed using modular programming principles, ensuring flexibility and ease of maintenance.
- **Generative AI:** Utilizes advanced AI models to enhance the accuracy and efficiency of root cause analysis.
- **User-Friendly Interface:** Simple and intuitive interface for seamless user experience.
- **Comprehensive Analysis Tools:** Includes various RCA techniques such as 5 Whys, Fishbone Diagram, and more.
- **Solution Suggestion Engine:** Generates alternative solutions based on identified root causes.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/root-cause-analyzer.git
   cd root-cause-analyzer
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Navigate to the app directory:**
   ```sh
   cd app
   ```

2. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

3. **Open the application:**
   - The application will open in your default web browser. If not, navigate to `http://localhost:8501` in your browser.

## Usage

1. **Upload Document:**
   - Upload the document describing the problem or incident.
   
2. **Perform Root Cause Analysis:**
   - Use the provided tools to identify root causes of the problem.
   
3. **Generate Solutions:**
   - Get suggestions for alternative solutions based on the analysis.
   
4. **Review and Implement:**
   - Review the suggested solutions and implement the most suitable ones.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thank you to the open-source community for providing invaluable resources and tools.
- Special thanks to the developers and contributors who have made this project possible.
