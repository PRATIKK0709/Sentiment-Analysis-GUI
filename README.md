# Sentiment-Analysis-GUI

# Sentiment Analysis Tool

![GitHub repo size](https://img.shields.io/github/repo-size/SysketSK/Sentiment-Analysis-GUI)
![GitHub stars](https://img.shields.io/github/stars/SysketSK/Sentiment-Analysis-GUI?style=social)


A simple PyQt5-based GUI application for sentiment analysis using the VADER sentiment analysis tool.

## Table of Contents


- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)



## Installation

1. Clone the repository:
```
   git clone https://github.com/SysketSK/Sentiment-Analysis-GUI.git
   cd Sentiment-Analysis-GUI
```
2. Install the required dependencies:
```
   pip install PyQt5 vaderSentiment
   pip install vaderSentiment
```

## Usage

1) Run the application

```
python sentiment_analysis_app.py
```
2) Enter the text you want to analyze in the text entry field.

3) Click the "Analyze Sentiment" button to see the sentiment analysis results.

4) Use the "Clear Text" button to clear the input and results.

## Customization

You can customize the application's appearance by modifying the CSS styles in the sentiment_analysis_app.py file.
```
# Apply custom style
app.setStyleSheet("""
    QMainWindow {
        background-color: #f0f0f0;
    }
    QTextEdit {
        background-color: #ffffff;
        font-size: 16px;
    }
    QPushButton {
        background-color: #0080FF;
        color: #ffffff;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #0055CC;
    }
    QLabel {
        font-size: 20px;
    }
""")
```

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository. <br>
Create a new branch for your feature or bug fix.<br>
Make your changes and commit them.<br>
Push your changes to your fork.<br>
Create a pull request, describing your changes in detail and explaining why they are needed.
