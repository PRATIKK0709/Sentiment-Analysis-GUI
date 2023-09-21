import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QFont
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalysisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sentiment Analysis Tool")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.text_entry = QTextEdit(self)
        self.analyze_button = QPushButton("Analyze Sentiment", self)
        self.clear_button = QPushButton("Clear Text", self)
        self.result_label = QLabel(self)
        self.score_label = QLabel(self)

        # Set font styles
        font = QFont()
        font.setPointSize(14)
        self.result_label.setFont(font)
        self.score_label.setFont(font)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_entry)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.analyze_button)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.result_label)
        layout.addWidget(self.score_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to functions
        self.analyze_button.clicked.connect(self.analyze_sentiment)
        self.clear_button.clicked.connect(self.clear_text)

    def analyze_sentiment(self):
        text = self.text_entry.toPlainText()
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(text)

        compound_score = sentiment_scores['compound']
        sentiment_label = self.get_sentiment_label(compound_score)

        self.result_label.setText(f"Sentiment: {sentiment_label}")
        self.score_label.setText(f"Compound Score: {compound_score:.2f}")

    def clear_text(self):
        self.text_entry.clear()
        self.result_label.clear()
        self.score_label.clear()

    def get_sentiment_label(self, compound_score):
        if compound_score >= 0.05:
            return "Positive"
        elif compound_score <= -0.05:
            return "Negative"
        else:
            return "Neutral"

def main():
    app = QApplication(sys.argv)
    window = SentimentAnalysisApp()
    
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

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
