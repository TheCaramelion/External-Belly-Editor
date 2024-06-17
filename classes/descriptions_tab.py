from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit
)

class DescriptionsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.description_label = QLabel('Description:')
        self.layout.addWidget(self.description_label)

        self.description_text_edit = QTextEdit()
        self.layout.addWidget(self.description_text_edit)

        self.absorbed_desc_label = QLabel('Description (Absorbed):')
        self.layout.addWidget(self.absorbed_desc_label)

        self.absorbed_desc_text_edit = QTextEdit()
        self.layout.addWidget(self.absorbed_desc_text_edit)

        self.vore_verb_label = QLabel('Vore Verb:')
        self.layout.addWidget(self.vore_verb_label)

        self.vore_verb_input = QLineEdit()
        self.layout.addWidget(self.vore_verb_input)
        
        self.vore_release_label = QLabel('Release Verb:')
        self.layout.addWidget(self.vore_release_label)
        
        self.vore_release_input = QLineEdit()
        self.layout.addWidget(self.vore_release_input)

        self.setLayout(self.layout)

    def set_description_data(self, belly_data):
        self.description_text_edit.setPlainText(belly_data.get('desc', ''))
        self.absorbed_desc_text_edit.setPlainText(belly_data.get('absorbed_desc', ''))
        self.vore_verb_input.setText(belly_data.get('vore_verb', ''))
        self.vore_release_input.setText(belly_data.get('release_verb', ''))

    def get_description_data(self):
        belly_data = {
            'desc': self.description_text_edit.toPlainText(),
            'absorbed_desc': self.absorbed_desc_text_edit.toPlainText(),
            'vore_verb': self.vore_verb_input.text(),
            'release_verb': self.vore_release_input.text()
        }
        return belly_data
