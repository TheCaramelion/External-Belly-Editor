from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class MessageWindow(QWidget):
    def __init__(self, title, messages):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)

        self.messages = messages if messages else [""]  # Ensure messages is never empty
        self.edited_messages = self.messages[:]
        self.title = title

        self.layout = QVBoxLayout(self)

        self.examine_label = QLabel(f'{title}:', self)
        self.layout.addWidget(self.examine_label)

        self.examine_text_edit = QTextEdit(self)
        self.examine_text_edit.setPlainText("\n".join(self.messages))
        self.layout.addWidget(self.examine_text_edit)

        # Save button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.clicked.connect(self.save_messages)
        
        # Cancel button
        self.cancel_btn = QPushButton('Cancel', self)
        self.cancel_btn.clicked.connect(self.close)

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.cancel_btn)
        self.layout.addLayout(button_layout)

        self.setLayout(self.layout)

    def save_messages(self):
        edited_text = self.examine_text_edit.toPlainText()
        self.edited_messages = edited_text.splitlines()
        self.messages = self.edited_messages[:]
        self.close()

    def get_edited_messages(self):
        return self.edited_messages
