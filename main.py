import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QFileDialog
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
        self.load_dict_button = QPushButton("Load Custom Dictionary", self)
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
        button_layout.addWidget(self.load_dict_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.result_label)
        layout.addWidget(self.score_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to functions
        self.analyze_button.clicked.connect(self.analyze_sentiment)
        self.clear_button.clicked.connect(self.clear_text)
        self.load_dict_button.clicked.connect(self.load_custom_sentiment_dictionary)

        # Create the sentiment analyzer
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self):
        text = self.text_entry.toPlainText()
        sentiment_scores = self.analyzer.polarity_scores(text)

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

    def load_custom_sentiment_dictionary(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Load Custom Sentiment Dictionary", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            self.analyzer.lexicon.update(self.load_custom_lexicon(file_path))
            self.analyze_sentiment()

    def load_custom_lexicon(self, file_path):
        custom_lexicon = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    word, score = parts
                    custom_lexicon[word] = float(score)
                else:
                    print(f"Ignoring line: {line} (Format: word<TAB>score)")
        return custom_lexicon

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
