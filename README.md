# text-utils

**Text Utils** is a Django-based web application designed to analyze and manipulate text. It provides a simple interface for users to perform operations like removing punctuation, capitalizing text, and counting characters.

## Features

Based on the application logic and interface, the following features are available:

  * **Remove Punctuation**: Strips all punctuation characters (e.g., `!`, `$`, `.`, `?`) from the input text.
  * **UPPERCASE**: Converts the entire input text to capital letters.
  * **Character Count**: Calculates and displays the total number of characters in the text.
  * **Dark Mode UI**: The interface is built with Bootstrap 5 and features a modern dark theme.

## Prerequisites

  * Python 3.x
  * Django 4.2.4

## Installation and Setup

Follow these steps to run the project locally:

1.  **Clone the repository** (if you haven't already):

    ```bash
    git clone https://github.com/greatwhite9/text-utils
    ```

2.  **Navigate to the project directory**:
    Move into the folder containing `manage.py`.

    ```bash
    cd textutil
    ```

3.  **Install Dependencies**:
    Ensure you have Django installed.

    ```bash
    pip install django
    ```

4.  **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

5.  **Access the Application**:
    Open your web browser and go to:
    `http://127.0.0.1:8000/`

## Usage

1.  Enter your text in the large text area on the homepage.
2.  Use the toggle switches to select the operation you want to perform:
      * *Remove Punctuation*
      * *UPPERCASE*
      * *Count the Characters*
3.  Click the **Analyse** button.
4.  The processed text or result will be displayed on the next page.

> **Note:** The current logic prioritizes operations in the order listed above. If multiple options are selected, only the first valid operation in the chain (Remove Punctuation \> Capitalize \> Count) will be executed and displayed.

## Project Structure

  * `manage.py`: Django's command-line utility.
  * `textutil/`: Main project package.
      * `views.py`: Contains the logic for processing text (`removepunc`, `captialise`, `charcounter`).
      * `urls.py`: URL routing for the `index` and `analyse` views.
      * `settings.py`: Project configuration.
  * `templates/`: HTML templates.
      * `index.html`: The main input form with Bootstrap styling.
      * `analyse.html`: The results display page.

## Technologies Used

  * **Python** (Backend Logic)
  * **Django** (Web Framework)
  * **HTML/CSS** (Frontend Structure)
  * **Bootstrap 5.3.3** (Styling and Responsive Design)
