import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QWidget, QStatusBar
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import action
import speech_to_text


class AIAssistant(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties (Reduced size)
        self.setWindowTitle("AI Assistant")
        self.setFixedSize(500, 650)
        self.setStyleSheet("background-color: #203A43; color: white;")

        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Main container widget
        container = QWidget()
        self.setCentralWidget(container)
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignTop)

        # Main Frame (AI Assistant Label and Image)
        main_frame = QFrame()
        main_frame.setStyleSheet("background-color: #2C5364; border: 2px solid white; border-radius: 10px;")
        main_layout = QVBoxLayout(main_frame)

        # Text Label
        label = QLabel("🌟 AI Assistant 🌟")
        label.setFont(QFont("Trebuchet MS", 16, QFont.Bold))  # Adjusted font size
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #FFFFFF; padding: 10px;")
        main_layout.addWidget(label)

        # Image
        image_label = QLabel()
        pixmap = QPixmap("image/assistant.png").scaled(100, 100, Qt.KeepAspectRatio)  # Scaled image
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_label)

        layout.addWidget(main_frame)

        # Text Area
        self.text_area = QTextEdit()
        self.text_area.setFont(QFont("Courier", 11))  # Slightly smaller font size
        self.text_area.setStyleSheet("background-color: #0F2027; color: #A9CCE3; border-radius: 10px; padding: 5px;")
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Entry Widget (Input Field)
        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Type your command here or specify a city for weather...")
        self.entry.setAlignment(Qt.AlignCenter)
        self.entry.setStyleSheet("background-color: #FFFFFF; color: black; padding: 5px; border-radius: 10px;")
        layout.addWidget(self.entry)

        # Buttons
        button_layout = QHBoxLayout()

        self.ask_button = QPushButton("🎙 Voice Input")
        self.ask_button.setStyleSheet("""
            QPushButton {
                background-color: #3A6073; 
                color: white; 
                border-radius: 10px; 
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #1E3C50;
            }
        """)
        self.ask_button.clicked.connect(self.ask)
        button_layout.addWidget(self.ask_button)

        self.send_button = QPushButton("📤 Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #3A6073; 
                color: white; 
                border-radius: 10px; 
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #1E3C50;
            }
        """)
        self.send_button.clicked.connect(self.user_send)
        button_layout.addWidget(self.send_button)

        self.delete_button = QPushButton("❌ Clear")
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #3A6073; 
                color: white; 
                border-radius: 10px; 
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #1E3C50;
            }
        """)
        self.delete_button.clicked.connect(self.delete_text)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)

    def user_send(self):
        send = self.entry.text()
        if not send.strip():
            self.status_bar.showMessage("Input cannot be empty!", 3000)
            return

        bot_response = action.Action(send)
        self.text_area.append(f"Me --> {send}\n")
        if bot_response:
            self.text_area.append(f"Bot <-- {bot_response}\n")
        if bot_response == "ok sir":
            self.close()

    def ask(self):
        self.status_bar.showMessage("Listening...", 2000)
        ask_val = speech_to_text.speech_to_text()
        if not ask_val:
            self.status_bar.showMessage("Failed to recognize speech!", 3000)
            return

        bot_response = action.Action(ask_val)
        self.text_area.append(f"Me --> {ask_val}\n")
        if bot_response:
            self.text_area.append(f"Bot <-- {bot_response}\n")
        if bot_response == "ok sir":
            self.close()

    def delete_text(self):
        self.text_area.clear()
        self.status_bar.showMessage("Chat cleared!", 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AIAssistant()
    window.show()
    sys.exit(app.exec())
