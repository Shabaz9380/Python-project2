# Python-projects-this repo has small python projects that i did in my college days
## 1st Project
# System Resource Monitor

This Python script provides a tool for monitoring system resource utilization (CPU, memory, and disk) and generating real-time visualizations and email alerts. It's designed to help users track system performance, identify potential bottlenecks, and receive notifications when resource usage exceeds predefined thresholds.

## Features

* **Resource Monitoring:** Continuously monitors CPU utilization, memory usage, and disk usage using the `psutil` library.
* **Data Logging:** Records resource utilization data to a CSV file (`resource_utilization.csv` by default) for historical analysis.
* **Real-time Visualization:** Displays a live-updating graph of resource usage using `matplotlib`, providing a visual representation of system performance over time.
* **Email Alerts:** Sends email notifications when CPU, memory, or disk usage exceeds user-defined thresholds.
* **Configurable Thresholds:** Allows users to customize the thresholds for triggering email alerts.
* **Summary Statistics:** Calculates and prints average resource utilization after the monitoring process completes.

## Requirements

* Python 3.x
* `psutil` library: For system information retrieval.
* `csv` library: For working with CSV files (built-in to Python).
* `matplotlib` library: For plotting.
* `matplotlib.animation`: For creating animated plots.
* `smtplib` library: For sending emails (built-in to Python).
* `email.mime` library: For creating email messages (built-in to Python).

## Installation

1.  **Install Python:** Ensure you have Python 3.x installed on your system.
2.  **Install Dependencies:** Install the required Python libraries using pip:

    ```bash
    pip install psutil matplotlib
    ```

## Usage

1.  **Clone the Repository:** (If you are using version control)
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Configure Settings (Optional):**
    * Open the script (`your_script_name.py`) in a text editor.
    * Modify the following variables in the `if __name__ == "__main__":` block to customize the monitoring:
        * `interval`: Monitoring interval in seconds (default: 5).
        * `duration`: Total monitoring duration in seconds (default: 60).
        * `output_file`: Path to the CSV output file (default: `resource_utilization.csv`).
        * `email_address`: Your email address to receive alerts. **(Important: See Security Note Below)**
        * `thresholds`: A dictionary to customize resource usage thresholds (default: `{'cpu': 80, 'memory': 85, 'disk': 90}`).

3.  **Run the Script:**
    ```bash
    python your_script_name.py
    ```

4.  **View Results:**
    * The script will display a live graph of resource utilization.
    * Resource usage data will be saved to the specified CSV file.
    * Email alerts will be sent to the configured email address if thresholds are exceeded.
    * Average resource utilization statistics will be printed to the console after monitoring is complete.

## Function Details

* **`monitor_resources(interval, duration, output_file, email_address, thresholds)`:**
    * This is the main function that performs the resource monitoring.
    * It takes the monitoring interval, duration, output file path, email address, and resource usage thresholds as input.
    * It collects resource data, logs it to a CSV file, generates the live graph, and sends email alerts.

* **`send_alert(email_address, message)`:**
    * This function sends an email alert to the specified email address with the provided message.
    * It uses the `smtplib` library to connect to an SMTP server (in this case, `smtp.gmail.com`).

## Security Note (Important!)

* **Email Credentials:** The current script includes placeholders for email credentials (in the `send_alert` function). **It is extremely important that you do NOT hardcode your actual email address and password directly into the script, especially if you plan to share or distribute it.**
* **Recommended Security Practices:**
    * **Environment Variables:** Store your email address and password as environment variables on your system. Modify the `send_alert` function to retrieve these values from the environment variables. This is the most secure approach.
    * **Configuration Files:** If you are not familiar with environment variables, you can use a separate configuration file (e.g., `.env` file) to store your credentials. Add this file to your `.gitignore` to prevent it from being committed to version control.
    * **Never Commit Secrets:** Never, under any circumstances, commit your email address and password to a public repository like GitHub. This could compromise your email account security.

## Disclaimer

This script is provided as-is and may require modifications to suit specific system configurations or monitoring needs. Use it responsibly and at your own risk.

## Contributing

If you are interested in this project you can do any small contibution to this project.




## 2nd Project
# CROPER: Your Agricultural Advice Chatbot

## Overview

CROPER is a simple, interactive chatbot designed to provide basic advice related to crop cultivation in India. By understanding your queries about specific crops, CROPER aims to offer relevant information based on its knowledge base.

## Features

* **Intent Recognition:** Identifies the user's intent related to specific crops (e.g., soybean, sugarcane, cotton).
* **Basic Crop Advice:** Provides pre-defined information regarding the cultivation of supported crops in India, including suitable regions.
* **Simple Natural Language Interaction:** Allows users to ask questions in natural language.
* **Exit Command:** Users can type 'exit' to end the conversation.

## Getting Started

1.  **Prerequisites:**
    * Python 3.x
    * NLTK (Natural Language Toolkit)
    * NumPy
    * scikit-learn

    You can install these libraries using pip:
    ```bash
    pip install nltk numpy scikit-learn
    ```
    You also need to download the WordNet lemmatizer data for NLTK. Run the following in a Python interpreter:
    ```python
    import nltk
    nltk.download('wordnet')
    ```

2.  **Running the Chatbot:**
    1.  Save the provided Python code as a `.py` file (e.g., `croper.py`).
    2.  Open your terminal or command prompt.
    3.  Navigate to the directory where you saved the file.
    4.  Run the script using:
        ```bash
        python croper.py
        ```
    5.  The chatbot will start, and you can begin asking questions.

## Usage

Once the chatbot is running, you can type questions related to soybean, sugarcane, or cotton cultivation in India. For example:
You: How to grow soybean in India?
CROPER: For successful soybean cultivation in India, ensure warm weather and adequate rainfall, particularly in regions like Uttar Pradesh, Maharashtra, and Karnataka.

You: Tell me about cotton production.
CROPER: Optimize cotton production in India by choosing suitable regions like Gujarat, Maharashtra, and Andhra Pradesh, known for their favorable conditions.

You: exit
CROPER: BOSS if you need any assistance regarding any crops in future, feel free to reach out.
Have A Nice Day BOSS. BYE


If the chatbot doesn't understand your intent or finds no relevant information, it will respond with a default message.

## Data

The chatbot's knowledge is currently based on a small, predefined corpus of sentences and a limited set of intents. To improve its accuracy and coverage, the `corpus` and `intents` dictionaries in the code would need to be expanded with more comprehensive information.

## Limitations

* **Limited Knowledge Base:** The chatbot's understanding is restricted to the information provided in the `corpus` and `intents`.
* **Basic Intent Recognition:** The intent recognition relies on keyword matching and a simple Naive Bayes classifier. It may not accurately identify complex or nuanced queries.
* **Simple Response Generation:** The chatbot retrieves the most similar sentence from its corpus as a response. It does not generate new, contextually rich answers.
* **No Context Handling:** The chatbot does not maintain context between turns in the conversation. Each query is treated independently.

## Future Enhancements

* Expand the `corpus` with more detailed information about various crops, cultivation practices, pest control, etc.
* Increase the number of supported `intents` and associated keywords.
* Implement more sophisticated Natural Language Understanding (NLU) techniques for better intent recognition (e.g., using more advanced NLP models).
* Develop a more dynamic response generation mechanism.
* Incorporate context management to handle follow-up questions.
* Integrate with external agricultural databases or APIs for real-time and comprehensive information.

## Alert - This is just trial project that i wanted to try (just to learn the concepts). It might improve in the upcoming future.
