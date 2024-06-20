from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit, QCheckBox, QScrollArea, QGroupBox, QPushButton, QGridLayout
)
from .message_window import MessageWindow

class ExamineWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)

class DescriptionsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        content_widget = QWidget(self.scroll_area)
        self.scroll_area.setWidget(content_widget)

        self.layout = QVBoxLayout(content_widget)

        # Main Description Section
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
        
        # Toggle Switch
        self.toggle_switch = QCheckBox('Show All Messages', self)
        self.toggle_switch.toggled.connect(self.toggle_options)
        self.layout.addWidget(self.toggle_switch)

        # Examine Messages Group
        self.examine_messages_groupbox = QGroupBox('Examine Messages')
        self.examine_messages_layout = QGridLayout(self.examine_messages_groupbox)

        self.examine_messages_text = 'Examine Messages (When full)'
        self.examine_messages_btn = QPushButton(self.examine_messages_text, self)
        self.examine_messages_btn.clicked.connect(lambda: self.open_messages_window(self.examine_messages_text, self.examine_messages))
        self.examine_messages_layout.addWidget(self.examine_messages_btn, 0, 0, 1, 1)

        self.examine_messages_absorbed_text = 'Examine Messages (With absorbed victim)'
        self.examine_messages_absorbed_btn = QPushButton(self.examine_messages_absorbed_text, self)
        self.examine_messages_absorbed_btn.clicked.connect(lambda: self.open_messages_window(self.examine_messages_absorbed_text, self.absorbed_examine_messages))
        self.examine_messages_layout.addWidget(self.examine_messages_absorbed_btn, 0, 1, 1, 1)

        self.layout.addWidget(self.examine_messages_groupbox)
        
        # Struggle Messages Group
        self.struggle_messages_groupbox = QGroupBox('Struggle Messages')
        self.struggle_messages_layout = QGridLayout(self.struggle_messages_groupbox)
        
        self.struggle_messages_outside_text = 'Struggle Messages (Outside)'
        self.struggle_messages_outside_btn = QPushButton(self.struggle_messages_outside_text, self)
        self.struggle_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_outside_text, self.struggle_messages_outside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_outside_btn, 0, 0, 1, 1)
        
        self.struggle_messages_inside_text = 'Struggle Messages (Inside)'
        self.struggle_messages_inside_btn = QPushButton(self.struggle_messages_inside_text, self)
        self.struggle_messages_inside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_inside_text, self.struggle_messages_inside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_inside_btn, 0, 1, 1, 1)
        
        self.struggle_messages_absorbed_outside_text = 'Absorbed Struggle Messages (Outside)'
        self.struggle_messages_absorbed_outside_btn = QPushButton(self.struggle_messages_absorbed_outside_text, self)
        self.struggle_messages_absorbed_outside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_absorbed_outside_text, self.struggle_messages_outside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_absorbed_outside_btn, 1, 0, 1, 1)
        
        self.struggle_messages_absorbed_inside_text = 'Absorbed Struggle Messages (Inside)'
        self.struggle_messages_absorbed_inside_btn = QPushButton(self.struggle_messages_absorbed_inside_text, self)
        self.struggle_messages_absorbed_inside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_absorbed_inside_text, self.struggle_messages_inside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_absorbed_inside_btn, 1, 1, 1, 1)

        self.layout.addWidget(self.struggle_messages_groupbox)
        
        # Escape Messages Group
        self.escape_messages_groupbox = QGroupBox('Escape Messages')
        self.escape_messages_layout = QGridLayout(self.escape_messages_groupbox)

        self.escape_attempt_messages_prey_text = 'Escape Attempt Messages (To prey)'
        self.escape_attempt_messages_prey_btn = QPushButton(self.escape_attempt_messages_prey_text, self)
        self.escape_attempt_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_messages_prey_text, self.escape_attempt_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_attempt_messages_prey_btn, 0, 0, 1, 1)
        
        self.escape_attempt_messages_owner_text = 'Escape Attempt Messages (To you)'
        self.escape_attempt_messages_owner_btn = QPushButton(self.escape_attempt_messages_owner_text, self)
        self.escape_attempt_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_messages_owner_text, self.escape_attempt_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_attempt_messages_owner_btn, 0, 1, 1, 1)
        
        self.escape_messages_prey_text = 'Escape Messages (To prey)'
        self.escape_messages_prey_btn = QPushButton(self.escape_messages_prey_text, self)
        self.escape_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_prey_text, self.escape_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_messages_prey_btn, 1, 0, 1, 1)

        self.escape_messages_owner_text = 'Escape Messages (To you)'
        self.escape_messages_owner_btn = QPushButton(self.escape_messages_owner_text, self)
        self.escape_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_owner_text, self.escape_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_messages_owner_btn, 1, 1, 1, 1)
        
        self.escape_messages_outside_text = "Escape Messages (Outside)"
        self.escape_messages_outside_btn = QPushButton(self.escape_messages_outside_text, self)
        self.escape_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_outside_text, self.escape_messages_outside))
        self.escape_messages_layout.addWidget(self.escape_messages_outside_btn, 1, 2, 1, 1)
        
        self.escape_item_messages_prey_text = 'Item Escape Messages (To prey)'
        self.escape_item_messages_prey_btn = QPushButton(self.escape_item_messages_prey_text, self)
        self.escape_item_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_prey_text, self.escape_item_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_item_messages_prey_btn, 2, 0, 1, 1)
        
        self.escape_item_messages_owner_text = 'Item Escape Messages (To you)'
        self.escape_item_messages_owner_btn = QPushButton(self.escape_item_messages_owner_text, self)
        self.escape_item_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_owner_text, self.escape_item_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_item_messages_owner_btn, 2, 1, 1, 1)
        
        self.escape_item_messages_outside_text = 'Item Escape Messages (Outside)'
        self.escape_item_messages_outside_btn = QPushButton(self.escape_item_messages_outside_text, self)
        self.escape_item_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_outside_text, self.escape_item_messages_outside))
        self.escape_messages_layout.addWidget(self.escape_item_messages_outside_btn, 2, 2, 1, 1)
        
        self.escape_fail_messages_prey_text = 'Escape Fail Messages (To prey)'
        self.escape_fail_messages_prey_btn = QPushButton(self.escape_fail_messages_prey_text, self)
        self.escape_fail_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_messages_prey_text, self.escape_fail_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_fail_messages_prey_btn, 3, 0, 1, 1)
        
        self.escape_fail_messages_owner_text = 'Escape Fail Messages (To you)'
        self.escape_fail_messages_owner_btn = QPushButton(self.escape_fail_messages_owner_text, self)
        self.escape_fail_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_messages_owner_text, self.escape_fail_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_fail_messages_owner_btn, 3, 1, 1, 1)
        
        self.escape_attempt_absorbed_messages_prey_text = 'Absorbed Escape Messages (To prey)'
        self.escape_attempt_absorbed_messages_prey_btn = QPushButton(self.escape_attempt_absorbed_messages_prey_text, self)
        self.escape_attempt_absorbed_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_absorbed_messages_prey_text, self.escape_attempt_absorbed_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_attempt_absorbed_messages_prey_btn, 4, 0, 1, 1)
        
        self.escape_attempt_absorbed_messages_owner_text = 'Absorbed Escape Messages (To you)'
        self.escape_attempt_absorbed_messages_owner_btn = QPushButton(self.escape_attempt_absorbed_messages_owner_text, self)
        self.escape_attempt_absorbed_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_absorbed_messages_owner_text, self.escape_attempt_absorbed_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_attempt_absorbed_messages_owner_btn, 4, 1, 1, 1)
        
        self.escape_fail_absorbed_messages_prey_text = 'Absorbed Escape Fail Messages (To prey)'
        self.escape_fail_absorbed_messages_prey_btn = QPushButton(self.escape_fail_absorbed_messages_prey_text, self)
        self.escape_fail_absorbed_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_absorbed_messages_prey_text, self.escape_fail_absorbed_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_fail_absorbed_messages_prey_btn, 5, 0, 1, 1)
        
        self.escape_fail_absorbed_messages_owner_text = 'Absorbed Escape Fail Messages (To you)'
        self.escape_fail_absorbed_messages_owner_btn = QPushButton(self.escape_fail_absorbed_messages_owner_text, self)
        self.escape_fail_absorbed_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_absorbed_messages_owner_text, self.escape_fail_absorbed_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_fail_absorbed_messages_owner_btn, 5, 1, 1, 1)

        
        self.layout.addWidget(self.escape_messages_groupbox)
        
        # Additional Options (hidden initially)
        self.additional_options_layout = QVBoxLayout()
        self.additional_options_layout.setContentsMargins(20, 0, 0, 0)
        self.layout.addLayout(self.additional_options_layout)

        # Stretch to push content to the top
        self.layout.addStretch(1)

        content_widget.setLayout(self.layout)

        # Main layout for the tab
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        # Hide additional options initially
        self.toggle_options(False)

        # Examine messages
        self.examine_messages = []
        self.absorbed_examine_messages = []
        
        # Struggle messages
        self.struggle_messages_outside = []
        self.struggle_messages_inside = []
        self.absorbed_struggle_messages_outside = []
        self.absorbed_struggle_messages_inside = []
        
        # Escape messages
        self.escape_attempt_messages_owner = []
        self.escape_attempt_messages_prey = []
        self.escape_messages_owner = []
        self.escape_messages_prey = []
        self.escape_messages_outside = []
        self.escape_item_messages_owner = []
        self.escape_item_messages_prey = []
        self.escape_item_messages_outside = []
        self.escape_fail_messages_owner = []
        self.escape_fail_messages_prey = []
        self.escape_attempt_absorbed_messages_owner = []
        self.escape_attempt_absorbed_messages_prey = []
        self.escape_absorbed_messages_owner = []
        self.escape_absorbed_messages_prey = []
        self.escape_absorbed_messages_outside = []
        self.escape_fail_absorbed_messages_owner = []
        self.escape_fail_absorbed_messages_prey = []
        

    def toggle_options(self, checked):
        for i in range(self.additional_options_layout.count()):
            widget = self.additional_options_layout.itemAt(i).widget()
            if widget:
                widget.setVisible(checked)

    def set_description_data(self, belly_data):
        self.description_text_edit.setPlainText(belly_data.get('desc', ''))
        self.absorbed_desc_text_edit.setPlainText(belly_data.get('absorbed_desc', ''))
        self.vore_verb_input.setText(belly_data.get('vore_verb', ''))
        self.vore_release_input.setText(belly_data.get('release_verb', ''))
        
        # Examine
        self.examine_messages = belly_data.get('examine_messages', [])
        self.absorbed_examine_messages = belly_data.get('examine_messages_absorbed', [])
        
        # Struggle
        self.struggle_messages_outside = belly_data.get('struggle_messages_outside', [])
        self.struggle_messages_inside = belly_data.get('struggle_messages_inside', [])
        self.absorbed_struggle_messages_outside = belly_data.get('absorbed_struggle_messages_outside', [])
        self.absorbed_struggle_messages_inside = belly_data.get('absorbed_struggle_messages_inside', [])
        
        # Escape
        self.escape_attempt_messages_owner = belly_data.get('escape_attempt_messages_owner', [])
        self.escape_attempt_messages_prey = belly_data.get('escape_attempt_messages_prey', [])
        self.escape_messages_owner = belly_data.get('escape_messages_owner', [])
        self.escape_messages_prey = belly_data.get('escape_messages_prey', [])
        self.escape_messages_outside = belly_data.get('escape_messages_outside', [])
        self.escape_item_messages_owner = belly_data.get('escape_item_messages_owner', [])
        self.escape_item_messages_prey = belly_data.get('escape_item_messages_prey', [])
        self.escape_item_messages_outside = belly_data.get('escape_item_messages_outside', [])
        self.escape_fail_messages_owner = belly_data.get('escape_fail_messages_owner', [])
        self.escape_fail_messages_prey = belly_data.get('escape_fail_messages_prey', [])
        self.escape_fail_messages_outside = belly_data.get('escape_fail_messages_outside', [])
        self.escape_absorbed_messages_owner = belly_data.get('escape_absorbed_messages_owner', [])
        self.escape_absorbed_messages_prey = belly_data.get('escape_absorbed_messages_prey', [])
        self.escape_absorbed_messages_outside = belly_data.get('escape_absorbed_messages_outside', [])
        self.escape_fail_absorbed_messages_owner = belly_data.get('escape_failed_absorbed_messages_owner', [])
        self.escape_fail_absorbed_messages_prey = belly_data.get('escape_failed_absorbed_messages_prey', [])

    def get_description_data(self):
        belly_data = {
            'desc': self.description_text_edit.toPlainText(),
            'absorbed_desc': self.absorbed_desc_text_edit.toPlainText(),
            'vore_verb': self.vore_verb_input.text(),
            'release_verb': self.vore_release_input.text(),
            'examine_messages': self.examine_messages,
            'examine_messages_absorbed': self.absorbed_examine_messages,
            'struggle_messages_outside': self.struggle_messages_outside,
            'struggle_messages_inside': self.struggle_messages_inside,
            'absorbed_struggle_messages_outside': self.absorbed_struggle_messages_outside,
            'absorbed_struggle_messages_inside': self.absorbed_struggle_messages_inside,
            'escape_attempt_messages_owner': self.escape_attempt_messages_owner,
            'escape_attempt_messages_prey': self.escape_attempt_messages_prey,
            'escape_attempt_absorbed_messages_owner': self.escape_attempt_absorbed_messages_owner,
            'escape_attempt_absorbed_messages_prey': self.escape_attempt_absorbed_messages_prey,
            'escape_absorbed_messages_owner': self.escape_absorbed_messages_owner,
            'escape_absorbed_messages_prey': self.escape_absorbed_messages_prey,
            'escape_absorbed_messages_outside': self.escape_absorbed_messages_outside,
            'escape_fail_absorbed_messages_owner': self.escape_fail_absorbed_messages_owner,
            'escape_fail_absorbed_messages_prey': self.escape_fail_absorbed_messages_prey
        }
        return belly_data

    def open_messages_window(self, title, messages):
        if messages:
            self.examine_window = MessageWindow(title, messages)
            self.examine_window.save_btn.clicked.connect(lambda: self.save_messages(messages))
            self.examine_window.show()

    def save_messages(self, messages):
        edited_messages = self.examine_window.get_edited_messages()
        if edited_messages is not None:
            if messages is self.examine_messages:
                self.examine_messages = edited_messages
            elif messages is self.absorbed_examine_messages:
                self.absorbed_examine_messages = edited_messages
            elif messages is self.struggle_messages_outside:
                self.struggle_messages_outside = edited_messages
            elif messages is self.struggle_messages_inside:
                self.struggle_messages_inside = edited_messages
            elif messages is self.absorbed_struggle_messages_outside:
                self.absorbed_struggle_messages_outside = edited_messages
            elif messages is self.absorbed_struggle_messages_inside:
                self.absorbed_struggle_messages_inside = edited_messages
        self.examine_window.close()
class ExamineWindow(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 400, 300)

class DescriptionsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        content_widget = QWidget(self.scroll_area)
        self.scroll_area.setWidget(content_widget)

        self.layout = QVBoxLayout(content_widget)

        # Toggle Switch
        self.toggle_switch = QCheckBox('Show More', self)
        self.toggle_switch.toggled.connect(self.toggle_options)
        self.layout.addWidget(self.toggle_switch)

        # Main Description Section
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

        # Examine Messages Group
        self.examine_messages_groupbox = QGroupBox('Examine Messages')
        self.examine_messages_layout = QGridLayout(self.examine_messages_groupbox)
        
        self.examine_messages_layout.addWidget(QLabel('When full'), 0, 0, 1, 1)
        self.examine_messages_layout.addWidget(QLabel('With absorbed victims'), 0, 1, 1, 1)

        self.examine_messages_text = 'Examine Messages'
        self.examine_messages_btn = QPushButton(self.examine_messages_text, self)
        self.examine_messages_btn.clicked.connect(lambda: self.open_messages_window(self.examine_messages_text, self.examine_messages))
        self.examine_messages_layout.addWidget(self.examine_messages_btn, 1, 0, 1, 1)

        self.examine_messages_absorbed_text = 'Examine Messages'
        self.examine_messages_absorbed_btn = QPushButton(self.examine_messages_absorbed_text, self)
        self.examine_messages_absorbed_btn.clicked.connect(lambda: self.open_messages_window(self.examine_messages_absorbed_text, self.absorbed_examine_messages))
        self.examine_messages_layout.addWidget(self.examine_messages_absorbed_btn, 1, 1, 1, 1)

        self.layout.addWidget(self.examine_messages_groupbox)
        
        # Struggle Messages Group
        self.struggle_messages_groupbox = QGroupBox('Struggle Messages')
        self.struggle_messages_layout = QGridLayout(self.struggle_messages_groupbox)
        
        self.struggle_messages_layout.addWidget(QLabel('Outside'), 0, 0, 1, 1)
        self.struggle_messages_layout.addWidget(QLabel('Inside'), 0, 1, 1, 1)
        
        self.struggle_messages_outside_text = 'Struggle Messages'
        self.struggle_messages_outside_btn = QPushButton(self.struggle_messages_outside_text, self)
        self.struggle_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_outside_text, self.struggle_messages_outside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_outside_btn, 1, 0, 1, 1)
        
        self.struggle_messages_inside_text = 'Struggle Messages'
        self.struggle_messages_inside_btn = QPushButton(self.struggle_messages_inside_text, self)
        self.struggle_messages_inside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_inside_text, self.struggle_messages_inside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_inside_btn, 1, 1, 1, 1)
        
        self.struggle_messages_absorbed_outside_text = 'Absorbed Struggle Messages'
        self.struggle_messages_absorbed_outside_btn = QPushButton(self.struggle_messages_absorbed_outside_text, self)
        self.struggle_messages_absorbed_outside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_absorbed_outside_text, self.struggle_messages_outside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_absorbed_outside_btn, 2, 0, 1, 1)
        
        self.struggle_messages_absorbed_inside_text = 'Absorbed Struggle Messages'
        self.struggle_messages_absorbed_inside_btn = QPushButton(self.struggle_messages_absorbed_inside_text, self)
        self.struggle_messages_absorbed_inside_btn.clicked.connect(lambda: self.open_messages_window(self.struggle_messages_absorbed_inside_text, self.struggle_messages_inside))
        self.struggle_messages_layout.addWidget(self.struggle_messages_absorbed_inside_btn, 2, 1, 1, 1)

        self.layout.addWidget(self.struggle_messages_groupbox)
        
        # Escape Messages Group
        self.escape_messages_groupbox = QGroupBox('Escape Messages')
        self.escape_messages_layout = QGridLayout(self.escape_messages_groupbox)
        
        self.escape_messages_layout.addWidget(QLabel('To prey'), 0, 0, 1, 1)
        self.escape_messages_layout.addWidget(QLabel('To you'), 0, 1, 1, 1)
        self.escape_messages_layout.addWidget(QLabel('Outside'), 0, 2, 1, 1)

        self.escape_attempt_messages_prey_text = 'Escape Attempt'
        self.escape_attempt_messages_prey_btn = QPushButton(self.escape_attempt_messages_prey_text, self)
        self.escape_attempt_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_messages_prey_text, self.escape_attempt_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_attempt_messages_prey_btn, 1, 0, 1, 1)
        
        self.escape_attempt_messages_owner_text = 'Escape Attempt Messages'
        self.escape_attempt_messages_owner_btn = QPushButton(self.escape_attempt_messages_owner_text, self)
        self.escape_attempt_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_messages_owner_text, self.escape_attempt_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_attempt_messages_owner_btn, 1, 1, 1, 1)
        
        self.escape_messages_prey_text = 'Escape Messages'
        self.escape_messages_prey_btn = QPushButton(self.escape_messages_prey_text, self)
        self.escape_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_prey_text, self.escape_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_messages_prey_btn, 2, 0, 1, 1)

        self.escape_messages_owner_text = 'Escape Messages'
        self.escape_messages_owner_btn = QPushButton(self.escape_messages_owner_text, self)
        self.escape_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_owner_text, self.escape_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_messages_owner_btn, 2, 1, 1, 1)
        
        self.escape_messages_outside_text = "Escape Messages"
        self.escape_messages_outside_btn = QPushButton(self.escape_messages_outside_text, self)
        self.escape_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.escape_messages_outside_text, self.escape_messages_outside))
        self.escape_messages_layout.addWidget(self.escape_messages_outside_btn, 2, 2, 1, 1)
        
        self.escape_item_messages_prey_text = 'Escape Item Messages'
        self.escape_item_messages_prey_btn = QPushButton(self.escape_item_messages_prey_text, self)
        self.escape_item_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_prey_text, self.escape_item_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_item_messages_prey_btn, 3, 0, 1, 1)
        
        self.escape_item_messages_owner_text = 'Escape Item Messages'
        self.escape_item_messages_owner_btn = QPushButton(self.escape_item_messages_owner_text, self)
        self.escape_item_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_owner_text, self.escape_item_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_item_messages_owner_btn, 3, 1, 1, 1)
        
        self.escape_item_messages_outside_text = 'Escape Item Messages'
        self.escape_item_messages_outside_btn = QPushButton(self.escape_item_messages_outside_text, self)
        self.escape_item_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.escape_item_messages_outside_text, self.escape_item_messages_outside))
        self.escape_messages_layout.addWidget(self.escape_item_messages_outside_btn, 3, 2, 1, 1)
        
        self.escape_fail_messages_prey_text = 'Escape Fail Messages'
        self.escape_fail_messages_prey_btn = QPushButton(self.escape_fail_messages_prey_text, self)
        self.escape_fail_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_messages_prey_text, self.escape_fail_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_fail_messages_prey_btn, 4, 0, 1, 1)
        
        self.escape_fail_messages_owner_text = 'Escape Fail Messages'
        self.escape_fail_messages_owner_btn = QPushButton(self.escape_fail_messages_owner_text, self)
        self.escape_fail_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_messages_owner_text, self.escape_fail_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_fail_messages_owner_btn, 4, 1, 1, 1)
        
        self.escape_attempt_absorbed_messages_prey_text = 'Absorbed Escape Attempt Messages'
        self.escape_attempt_absorbed_messages_prey_btn = QPushButton(self.escape_attempt_absorbed_messages_prey_text, self)
        self.escape_attempt_absorbed_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_absorbed_messages_prey_text, self.escape_attempt_absorbed_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_attempt_absorbed_messages_prey_btn, 5, 0, 1, 1)
        
        self.escape_attempt_absorbed_messages_owner_text = 'Absorbed Escape Attempt Messages'
        self.escape_attempt_absorbed_messages_owner_btn = QPushButton(self.escape_attempt_absorbed_messages_owner_text, self)
        self.escape_attempt_absorbed_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_attempt_absorbed_messages_owner_text, self.escape_attempt_absorbed_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_attempt_absorbed_messages_owner_btn, 5, 1, 1, 1)
        
        self.escape_absorbed_messages_prey_text = 'Absorbed Attempt Messages'
        self.escape_absorbed_messages_prey_btn = QPushButton( self.escape_absorbed_messages_prey_text, self)
        self.escape_absorbed_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_absorbed_messages_prey_text, self.escape_absorbed_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_absorbed_messages_prey_btn, 6, 0, 1, 1)
        
        self.escape_absorbed_messages_owner_text = 'Absorbed Attempt Messages'
        self.escape_absorbed_messages_owner_btn = QPushButton( self.escape_absorbed_messages_owner_text, self)
        self.escape_absorbed_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_absorbed_messages_owner_text, self.escape_absorbed_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_absorbed_messages_owner_btn, 6, 1, 1, 1)
        
        self.escape_absorbed_messages_outside_text = 'Absorbed Escape Attempt Messages'
        self.escape_absorbed_messages_outside_btn = QPushButton(self.escape_absorbed_messages_outside_text, self)
        self.escape_absorbed_messages_outside_btn.clicked.connect(lambda: self.open_messages_window(self.escape_absorbed_messages_outside_text, self.escape_absorbed_messages_outside))
        self.escape_messages_layout.addWidget(self.escape_absorbed_messages_outside_btn, 6, 2, 1, 1)
        
        self.escape_fail_absorbed_messages_prey_text = 'Absorbed Escape Fail Messages'
        self.escape_fail_absorbed_messages_prey_btn = QPushButton(self.escape_fail_absorbed_messages_prey_text, self)
        self.escape_fail_absorbed_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_absorbed_messages_prey_text, self.escape_fail_absorbed_messages_prey))
        self.escape_messages_layout.addWidget(self.escape_fail_absorbed_messages_prey_btn, 7, 0, 1, 1)
        
        self.escape_fail_absorbed_messages_owner_text = 'Absorbed Escape Fail Messages'
        self.escape_fail_absorbed_messages_owner_btn = QPushButton(self.escape_fail_absorbed_messages_owner_text, self)
        self.escape_fail_absorbed_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.escape_fail_absorbed_messages_owner_text, self.escape_fail_absorbed_messages_owner))
        self.escape_messages_layout.addWidget(self.escape_fail_absorbed_messages_owner_btn, 7, 1, 1, 1)
        
        self.layout.addWidget(self.escape_messages_groupbox)
        
        # Additional Options (hidden initially)
        self.additional_options_layout = QVBoxLayout()

        # Transfer Messages Group
        self.transfer_messages_groupbox = QGroupBox('Transfer Messages')
        self.transfer_messages_layout = QGridLayout(self.transfer_messages_groupbox)
        
        self.transfer_messages_layout.addWidget(QLabel('To prey'), 0, 0, 1, 1)
        self.transfer_messages_layout.addWidget(QLabel('To you'), 0, 1, 1, 1)

        self.primary_transfer_messages_prey_text = 'Primary Transfer Message'
        self.primary_transfer_messages_prey_btn = QPushButton(self.primary_transfer_messages_prey_text, self)
        self.primary_transfer_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.primary_transfer_messages_prey_text, self.primary_transfer_messages_prey))
        self.transfer_messages_layout.addWidget(self.primary_transfer_messages_prey_btn, 1, 0, 1, 1)
        
        self.primary_transfer_messages_owner_text = 'Primary Transfer Message'
        self.primary_transfer_messages_owner_btn = QPushButton(self.primary_transfer_messages_owner_text, self)
        self.primary_transfer_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.primary_transfer_messages_owner_text, self.primary_transfer_messages_owner))
        self.transfer_messages_layout.addWidget(self.primary_transfer_messages_owner_btn, 1, 1, 1, 1)
        
        self.secondary_transfer_messages_prey_text = 'Secondary Transfer Message'
        self.secondary_transfer_messages_prey_btn = QPushButton(self.secondary_transfer_messages_prey_text, self)
        self.secondary_transfer_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.secondary_transfer_messages_prey_text, self.secondary_transfer_messages_prey))
        self.transfer_messages_layout.addWidget(self.secondary_transfer_messages_prey_btn, 2, 0, 1, 1)
        
        self.secondary_transfer_messages_owner_text = 'Secondary Transfer Message'
        self.secondary_transfer_messages_owner_btn = QPushButton(self.secondary_transfer_messages_owner_text, self)
        self.secondary_transfer_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.secondary_transfer_messages_owner_text, self.secondary_transfer_messages_owner))
        self.transfer_messages_layout.addWidget(self.secondary_transfer_messages_owner_btn, 2, 1, 1, 1)
        
        self.primary_autotransfer_messages_prey_text = 'Primary Auto-Transfer Message'
        self.primary_autotransfer_messages_prey_btn = QPushButton(self.primary_autotransfer_messages_prey_text, self)
        self.primary_autotransfer_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.primary_autotransfer_messages_prey_text, self.primary_autotransfer_messages_prey))
        self.transfer_messages_layout.addWidget(self.primary_autotransfer_messages_prey_btn, 3, 0, 1, 1)
        
        self.primary_autotransfer_messages_owner_text = 'Primary Auto-Transfer Message'
        self.primary_autotransfer_messages_owner_btn = QPushButton(self.primary_autotransfer_messages_owner_text, self)
        self.primary_autotransfer_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.primary_autotransfer_messages_owner_text, self.primary_autotransfer_messages_owner))
        self.transfer_messages_layout.addWidget(self.primary_autotransfer_messages_owner_btn, 3, 1, 1, 1)
        
        self.secondary_autotransfer_messages_prey_text = 'Secondary Auto-Transfer Message'
        self.secondary_autotransfer_messages_prey_btn = QPushButton(self.secondary_autotransfer_messages_prey_text, self)
        self.secondary_autotransfer_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.secondary_autotransfer_messages_prey_text, self.secondary_autotransfer_messages_prey))
        self.transfer_messages_layout.addWidget(self.secondary_autotransfer_messages_prey_btn, 4, 0, 1, 1)
        
        self.secondary_autotransfer_messages_owner_text = 'Secondary Auto-Transfer Message'
        self.secondary_autotransfer_messages_owner_btn = QPushButton(self.secondary_autotransfer_messages_owner_text, self)
        self.secondary_autotransfer_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.secondary_autotransfer_messages_owner_text, self.secondary_autotransfer_messages_owner))
        self.transfer_messages_layout.addWidget(self.secondary_autotransfer_messages_owner_btn, 4, 1, 1, 1)
        
        self.additional_options_layout.addWidget(self.transfer_messages_groupbox)
        
        # Interaction Chance Messages
        self.interaction_messages_groupbox = QGroupBox('Interaction Chance Messages')
        self.interaction_messages_layout = QGridLayout(self.interaction_messages_groupbox)
        
        self.interaction_messages_layout.addWidget(QLabel('To prey'), 0, 0, 1, 1)
        self.interaction_messages_layout.addWidget(QLabel('To you'), 0, 1, 1, 1)
        
        self.digest_chance_messages_prey_text = 'Interaction Chance Digest Message'
        self.digest_chance_messages_prey_btn = QPushButton(self.digest_chance_messages_prey_text, self)
        self.digest_chance_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.digest_chance_messages_prey_text, self.digest_chance_messages_prey))
        self.interaction_messages_layout.addWidget(self.digest_chance_messages_prey_btn, 1, 0, 1, 1)
        
        self.digest_chance_messages_owner_text = 'Interaction Chance Digest Message'
        self.digest_chance_messages_owner_btn = QPushButton(self.digest_chance_messages_owner_text, self)
        self.digest_chance_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.digest_chance_messages_owner_text, self.digest_chance_messages_owner))
        self.interaction_messages_layout.addWidget(self.digest_chance_messages_owner_btn, 1, 1, 1, 1)
        
        self.absorb_chance_messages_prey_text = 'Interaction Chance Absorb Message'
        self.absorb_chance_messages_prey_btn = QPushButton(self.absorb_chance_messages_prey_text, self)
        self.absorb_chance_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.absorb_chance_messages_prey_text, self.absorb_chance_messages_prey))
        self.interaction_messages_layout.addWidget(self.absorb_chance_messages_prey_btn, 2, 0, 1, 1)
        
        self.absorb_chance_messages_owner_text = 'Interaction Chance Absorb Message'
        self.absorb_chance_messages_owner_btn = QPushButton(self.absorb_chance_messages_owner_text, self)
        self.absorb_chance_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.absorb_chance_messages_owner_text, self.absorb_chance_messages_owner))
        self.interaction_messages_layout.addWidget(self.absorb_chance_messages_owner_btn, 2, 1, 1, 1)
        
        self.additional_options_layout.addWidget(self.interaction_messages_groupbox)
        
        # Bellymode Messages
        self.bellymode_messages_groupbox = QGroupBox('Bellymode Messages')
        self.bellymode_messages_layout = QGridLayout(self.bellymode_messages_groupbox)
        
        self.bellymode_messages_layout.addWidget(QLabel('To prey'), 0, 0, 1, 1)
        self.bellymode_messages_layout.addWidget(QLabel('To you'), 0, 1, 1, 1)
        
        self.digest_messages_prey_text = 'Digest Message'
        self.digest_messages_prey_btn = QPushButton(self.digest_messages_prey_text, self)
        self.digest_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.digest_messages_prey_text, self.digest_messages_prey))
        self.bellymode_messages_layout.addWidget(self.digest_messages_prey_btn, 1, 0, 1, 1)
        
        self.digest_messages_owner_text = 'Digest Message'
        self.digest_messages_owner_btn = QPushButton(self.digest_messages_owner_text, self)
        self.digest_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.digest_messages_owner_text, self.digest_messages_owner))
        self.bellymode_messages_layout.addWidget(self.digest_messages_owner_btn, 1, 1, 1, 1)
        
        self.absorb_messages_prey_text = 'Absorb Message'
        self.absorb_messages_prey_btn = QPushButton(self.absorb_messages_prey_text, self)
        self.absorb_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.absorb_messages_prey_text, self.absorb_messages_prey))
        self.bellymode_messages_layout.addWidget(self.absorb_messages_prey_btn, 2, 0, 1, 1)
        
        self.absorb_messages_owner_text = 'Absorb Message'
        self.absorb_messages_owner_btn = QPushButton(self.absorb_messages_owner_text, self)
        self.absorb_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.absorb_messages_owner_text, self.absorb_messages_owner))
        self.bellymode_messages_layout.addWidget(self.absorb_messages_owner_btn, 2, 1, 1, 1)
        
        self.unabsorb_messages_prey_text = 'Unabsorb Message'
        self.unabsorb_messages_prey_btn = QPushButton(self.unabsorb_messages_prey_text, self)
        self.unabsorb_messages_prey_btn.clicked.connect(lambda: self.open_messages_window(self.unabsorb_messages_prey_text, self.unabsorb_messages_prey))
        self.bellymode_messages_layout.addWidget(self.unabsorb_messages_prey_btn, 3, 0, 1, 1)
        
        self.unabsorb_messages_owner_text = 'Unabsorb Message'
        self.unabsorb_messages_owner_btn = QPushButton(self.unabsorb_messages_owner_text, self)
        self.unabsorb_messages_owner_btn.clicked.connect(lambda: self.open_messages_window(self.unabsorb_messages_owner_text, self.unabsorb_messages_owner))
        self.bellymode_messages_layout.addWidget(self.unabsorb_messages_owner_btn, 3, 1, 1, 1)
        
        self.additional_options_layout.addWidget(self.bellymode_messages_groupbox)
        
        # Idle Messages
        self.idle_messages_groupbox = QGroupBox('Idle Messages')
        self.idle_messages_layout = QGridLayout(self.idle_messages_groupbox)
        
        self.emotes_hold_text = 'Hold'
        self.emotes_hold_btn = QPushButton(self.emotes_hold_text, self)
        self.emotes_hold_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_hold_text, self.emotes_hold))
        self.idle_messages_layout.addWidget(self.emotes_hold_btn, 0, 0, 1, 1)
        
        self.emotes_holdabsorbed_text = 'Hold Absorbed'
        self.emotes_holdabsorbed_btn = QPushButton(self.emotes_holdabsorbed_text, self)
        self.emotes_holdabsorbed_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_holdabsorbed_text, self.emotes_holdabsorbed))
        self.idle_messages_layout.addWidget(self.emotes_holdabsorbed_btn, 0, 1, 1, 1)
        
        self.emotes_digest_text = 'Digest'
        self.emotes_digest_btn = QPushButton(self.emotes_digest_text, self)
        self.emotes_digest_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_digest_text, self.emotes_digest))
        self.idle_messages_layout.addWidget(self.emotes_digest_btn, 0, 2, 1, 1)
        
        self.emotes_absorb_text = 'Absorb'
        self.emotes_absorb_btn = QPushButton(self.emotes_absorb_text, self)
        self.emotes_absorb_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_absorb_text, self.emotes_absorb))
        self.idle_messages_layout.addWidget(self.emotes_absorb_btn, 1, 0, 1, 1)
        
        self.emotes_unabsorb_text = 'Unabsorb'
        self.emotes_unabsorb_btn = QPushButton(self.emotes_unabsorb_text, self)
        self.emotes_unabsorb_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_unabsorb_text, self.emotes_unabsorb))
        self.idle_messages_layout.addWidget(self.emotes_unabsorb_btn, 1, 1, 1, 1)
        
        self.emotes_drain_text = 'Drain'
        self.emotes_drain_btn = QPushButton(self.emotes_drain_text, self)
        self.emotes_drain_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_drain_text, self.emotes_drain))
        self.idle_messages_layout.addWidget(self.emotes_drain_btn, 1, 2, 1, 1)
        
        self.emotes_heal_text = 'Heal'
        self.emotes_heal_btn = QPushButton(self.emotes_heal_text, self)
        self.emotes_heal_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_heal_text, self.emotes_heal))
        self.idle_messages_layout.addWidget(self.emotes_heal_btn, 2, 0, 1, 1)
        
        self.emotes_steal_text = 'Size Steal'
        self.emotes_steal_btn = QPushButton(self.emotes_steal_text, self)
        self.emotes_steal_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_steal_text, self.emotes_steal))
        self.idle_messages_layout.addWidget(self.emotes_steal_btn, 2, 1, 1, 1)
        
        self.emotes_shrink_text = 'Shrink'
        self.emotes_shrink_btn = QPushButton(self.emotes_shrink_text, self)
        self.emotes_shrink_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_shrink_text, self.emotes_shrink))
        self.idle_messages_layout.addWidget(self.emotes_shrink_btn, 2, 2, 1, 1)
        
        self.emotes_grow_text = 'Grow'
        self.emotes_grow_btn = QPushButton(self.emotes_grow_text, self)
        self.emotes_grow_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_grow_text, self.emotes_grow))
        self.idle_messages_layout.addWidget(self.emotes_grow_btn, 3, 0, 1, 1)
        
        self.emotes_egg_text = 'Ecanse In Egg'
        self.emotes_egg_btn = QPushButton(self.emotes_egg_text, self)
        self.emotes_egg_btn.clicked.connect(lambda: self.open_messages_window(self.emotes_egg_text, self.emotes_egg))
        self.idle_messages_layout.addWidget(self.emotes_egg_btn, 3, 1, 1, 1)
        
        self.additional_options_layout.addWidget(self.idle_messages_groupbox)

        # Stretch to push content to the top
        self.layout.addStretch(1)

        # Add the additional_options_layout to the main layout (self.layout)
        self.layout.addLayout(self.additional_options_layout)

        # Set the main layout for the content widget
        content_widget.setLayout(self.layout)

        # Main layout for the tab
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

        # Hide additional options initially
        self.toggle_options(False)

        # Examine messages
        self.examine_messages = []
        self.absorbed_examine_messages = []
        
        # Struggle messages
        self.struggle_messages_outside = []
        self.struggle_messages_inside = []
        self.absorbed_struggle_messages_outside = []
        self.absorbed_struggle_messages_inside = []
        
        # Escape messages
        self.escape_attempt_messages_owner = []
        self.escape_attempt_messages_prey = []
        self.escape_messages_owner = []
        self.escape_messages_prey = []
        self.escape_messages_outside = []
        self.escape_item_messages_owner = []
        self.escape_item_messages_prey = []
        self.escape_item_messages_outside = []
        self.escape_fail_messages_owner = []
        self.escape_fail_messages_prey = []
        self.escape_attempt_absorbed_messages_owner = []
        self.escape_attempt_absorbed_messages_prey = []
        self.escape_absorbed_messages_owner = []
        self.escape_absorbed_messages_prey = []
        self.escape_absorbed_messages_outside = []
        self.escape_fail_absorbed_messages_owner = []
        self.escape_fail_absorbed_messages_prey = []
        
        # Transfer messages
        self.primary_transfer_messages_owner = []
        self.primary_transfer_messages_prey = []
        self.secondary_transfer_messages_owner = []
        self.secondary_transfer_messages_prey = []
        self.primary_autotransfer_messages_owner = []
        self.primary_autotransfer_messages_prey = []
        self.secondary_autotransfer_messages_owner = []
        self.secondary_autotransfer_messages_prey = []
        
        # Interaction chance messages
        self.digest_chance_messages_owner = []
        self.digest_chance_messages_prey = []
        self.absorb_chance_messages_owner = []
        self.absorb_chance_messages_prey = []
        
        # Bellymode messages
        self.digest_messages_prey = []
        self.digest_messages_owner = []
        self.absorb_messages_prey = []
        self.absorb_messages_owner = []
        self.unabsorb_messages_prey = []
        self.unabsorb_messages_owner = []
        
        # Idle messages
        self.emotes_hold = []
        self.emotes_holdabsorbed = []
        self.emotes_digest = []
        self.emotes_absorb = []
        self.emotes_unabsorb = []
        self.emotes_drain = []
        self.emotes_heal = []
        self.emotes_steal = []
        self.emotes_shrink = []
        self.emotes_grow = []
        self.emotes_egg = []

    def toggle_options(self, checked):
        self.toggle_switch.setText('Show All Messages')

        for i in range(self.additional_options_layout.count()):
            widget = self.additional_options_layout.itemAt(i).widget()
            if widget:
                widget.setVisible(checked)

    def set_belly_data(self, belly_data):
        self.description_text_edit.setPlainText(belly_data.get('desc', ''))
        self.absorbed_desc_text_edit.setPlainText(belly_data.get('absorbed_desc', ''))
        self.vore_verb_input.setText(belly_data.get('vore_verb', ''))
        self.vore_release_input.setText(belly_data.get('release_verb', ''))
        
        # Examine
        self.examine_messages = belly_data.get('examine_messages', [])
        self.absorbed_examine_messages = belly_data.get('examine_messages_absorbed', [])
        
        # Struggle
        self.struggle_messages_outside = belly_data.get('struggle_messages_outside', [])
        self.struggle_messages_inside = belly_data.get('struggle_messages_inside', [])
        self.absorbed_struggle_messages_outside = belly_data.get('absorbed_struggle_messages_outside', [])
        self.absorbed_struggle_messages_inside = belly_data.get('absorbed_struggle_messages_inside', [])
        
        # Escape
        self.escape_attempt_messages_owner = belly_data.get('escape_attempt_messages_owner', [])
        self.escape_attempt_messages_prey = belly_data.get('escape_attempt_messages_prey', [])
        self.escape_messages_owner = belly_data.get('escape_messages_owner', [])
        self.escape_messages_prey = belly_data.get('escape_messages_prey', [])
        self.escape_messages_outside = belly_data.get('escape_messages_outside', [])
        self.escape_item_messages_owner = belly_data.get('escape_item_messages_owner', [])
        self.escape_item_messages_prey = belly_data.get('escape_item_messages_prey', [])
        self.escape_item_messages_outside = belly_data.get('escape_item_messages_outside', [])
        self.escape_attempt_absorbed_messages_owner = belly_data.get('escape_attempt_absorbed_messages_owner', [])
        self.escape_attempt_absorbed_messages_prey = belly_data.get('escape_attempt_absorbed_messages_prey', [])
        self.escape_attempt_absorbed_messages_outside = belly_data.get('escape_attempt_absorbed_messages_outside', [])
        self.escape_fail_messages_owner = belly_data.get('escape_fail_messages_owner', [])
        self.escape_fail_messages_prey = belly_data.get('escape_fail_messages_prey', [])
        self.escape_fail_messages_outside = belly_data.get('escape_fail_messages_outside', [])
        self.escape_absorbed_messages_owner = belly_data.get('escape_absorbed_messages_owner', [])
        self.escape_absorbed_messages_prey = belly_data.get('escape_absorbed_messages_prey', [])
        self.escape_absorbed_messages_outside = belly_data.get('escape_absorbed_messages_outside', [])
        self.escape_fail_absorbed_messages_owner = belly_data.get('escape_fail_absorbed_messages_owner', [])
        self.escape_fail_absorbed_messages_prey = belly_data.get('escape_fail_absorbed_messages_prey', [])
        
        # Transfer
        self.primary_transfer_messages_owner = belly_data.get('primary_transfer_messages_owner', [])
        self.primary_transfer_messages_prey = belly_data.get('primary_transfer_messages_prey', [])
        self.secondary_transfer_messages_owner = belly_data.get('secondary_transfer_messages_owner', [])
        self.secondary_transfer_messages_prey = belly_data.get('secondary_transfer_messages_prey', [])
        self.primary_autotransfer_messages_owner = belly_data.get('primary_autotransfer_messages_owner', [])
        self.primary_autotransfer_messages_prey = belly_data.get('primary_autotransfer_messages_prey', [])
        self.secondary_autotransfer_messages_owner = belly_data.get('secondary_autotransfer_messages_owner', [])
        self.secondary_autotransfer_messages_prey = belly_data.get('secondary_autotransfer_messages_prey', [])
        
        # Interaction Chance
        self.digest_chance_messages_owner = belly_data.get('digest_chance_messages_owner', [])
        self.digest_chance_messages_prey = belly_data.get('digest_chance_messages_owner', [])
        self.absorb_chance_messages_owner = belly_data.get('absorb_chance_messages_owner', [])
        self.absorb_chance_messages_prey = belly_data.get('absorb_chance_messages_owner', [])
        
        # Bellymode
        self.digest_messages_prey = belly_data.get('digest_messages_prey', [])
        self.digest_messages_owner = belly_data.get('digest_messages_owner', [])
        self.absorb_messages_prey = belly_data.get('absorb_messages_prey', [])
        self.absorb_messages_owner = belly_data.get('absorb_messages_owner', [])
        self.unabsorb_messages_prey = belly_data.get('unabsorb_messages_prey', [])
        self.unabsorb_messages_owner = belly_data.get('unabsorb_messages_owner', [])
        
        # Idle
        self.emotes_hold = belly_data.get('emotes_hold', [])
        self.emotes_holdabsorbed = belly_data.get('emotes_holdabsorbed', [])
        self.emotes_digest = belly_data.get('emotes_digest', [])
        self.emotes_absorb = belly_data.get('emotes_absorb', [])
        self.emotes_unabsorb = belly_data.get('emotes_unabsorb', [])
        self.emotes_drain = belly_data.get('emotes_drain', [])
        self.emotes_heal = belly_data.get('emotes_heal', [])
        self.emotes_steal = belly_data.get('emotes_steal', [])
        self.emotes_shrink = belly_data.get('emotes_shrink', [])
        self.emotes_grow = belly_data.get('emotes_grow', [])
        self.emotes_egg = belly_data.get('emotes_egg', [])

    def get_description_data(self):
        belly_data = {
            'desc': self.description_text_edit.toPlainText(),
            'absorbed_desc': self.absorbed_desc_text_edit.toPlainText(),
            'vore_verb': self.vore_verb_input.text(),
            'release_verb': self.vore_release_input.text(),
            'examine_messages': self.examine_messages,
            'examine_messages_absorbed': self.absorbed_examine_messages,
            # Struggle
            'struggle_messages_outside': self.struggle_messages_outside,
            'struggle_messages_inside': self.struggle_messages_inside,
            'absorbed_struggle_messages_outside': self.absorbed_struggle_messages_outside,
            'absorbed_struggle_messages_inside': self.absorbed_struggle_messages_inside,
            # Escape
            'escape_attempt_messages_owner': self.escape_attempt_messages_owner,
            'escape_attempt_messages_prey': self.escape_attempt_messages_prey,
            'escape_messages_owner': self.escape_messages_owner,
            'escape_messages_prey': self.escape_messages_prey,
            'escape_messages_outside': self.escape_messages_outside,
            'escape_item_messages_owner': self.escape_item_messages_owner,
            'escape_item_messages_prey': self.escape_item_messages_prey,
            'escape_item_messages_outside': self.escape_item_messages_outside,
            'escape_attempt_absorbed_messages_owner': self.escape_attempt_absorbed_messages_owner,
            'escape_attempt_absorbed_messages_prey': self.escape_attempt_absorbed_messages_prey,
            'escape_attempt_absorbed_messages_outside': self.escape_attempt_absorbed_messages_outside,
            'escape_fail_messages_owner': self.escape_fail_messages_owner,
            'escape_fail_messages_prey': self.escape_fail_messages_prey,
            'escape_fail_messages_outside': self.escape_fail_messages_outside,
            'escape_absorbed_messages_owner': self.escape_absorbed_messages_owner,
            'escape_absorbed_messages_prey': self.escape_absorbed_messages_prey,
            'escape_absorbed_messages_outside': self.escape_absorbed_messages_outside,
            'escape_fail_absorbed_messages_owner': self.escape_fail_absorbed_messages_owner,
            'escape_fail_absorbed_messages_prey': self.escape_fail_absorbed_messages_prey,
            # Transfer
            'primary_transfer_messages_owner': self.primary_transfer_messages_owner,
            'primary_transfer_messages_prey': self.primary_transfer_messages_prey,
            'secondary_transfer_messages_owner': self.secondary_transfer_messages_owner,
            'secondary_transfer_messages_prey': self.secondary_transfer_messages_prey,
            'primary_autotransfer_messages_owner': self.primary_autotransfer_messages_owner,
            'primary_autotransfer_messages_prey': self.primary_autotransfer_messages_prey,
            'secondary_autotransfer_messages_owner': self.secondary_autotransfer_messages_owner,
            'secondary_autotransfer_messages_prey': self.secondary_autotransfer_messages_prey,
            # Bellymode
            'digest_messages_prey': self.digest_messages_prey,
            'digest_messages_owner': self.digest_messages_owner,
            'absorb_messages_prey': self.absorb_messages_prey,
            'absorb_messages_owner': self.absorb_messages_owner,
            'unabsorb_messages_prey': self.unabsorb_messages_prey,
            'unabsorb_messages_owner': self.unabsorb_messages_owner,
            # Idle
            'emotes_hold': self.emotes_hold,
            'emotes_holdabsorbed': self.emotes_holdabsorbed,
            'emotes_digest': self.emotes_digest,
            'emotes_absorb': self.emotes_absorb,
            'emotes_unabsorb': self.emotes_unabsorb,
            'emotes_drain': self.emotes_drain,
            'emotes_heal': self.emotes_heal,
            'emotes_steal': self.emotes_steal,
            'emotes_shrink': self.emotes_shrink,
            'emotes_grow': self.emotes_grow,
            'emotes_egg': self.emotes_egg,
        }
        return belly_data

    def open_messages_window(self, title, messages):
        if messages:
            self.examine_window = MessageWindow(title, messages)
            self.examine_window.save_btn.clicked.connect(lambda: self.save_messages(messages))
            self.examine_window.show()

    def save_messages(self, messages):
        edited_messages = self.examine_window.get_edited_messages()
        if edited_messages is not None:
            if messages is self.examine_messages:
                self.examine_messages = edited_messages
            elif messages is self.absorbed_examine_messages:
                self.absorbed_examine_messages = edited_messages
            elif messages is self.struggle_messages_outside:
                self.struggle_messages_outside = edited_messages
            elif messages is self.struggle_messages_inside:
                self.struggle_messages_inside = edited_messages
            elif messages is self.absorbed_struggle_messages_outside:
                self.absorbed_struggle_messages_outside = edited_messages
            elif messages is self.absorbed_struggle_messages_inside:
                self.absorbed_struggle_messages_inside = edited_messages
            elif messages is self.escape_attempt_messages_owner:
                self.escape_attempt_messages_owner = edited_messages
            elif messages is self.escape_attempt_messages_prey:
                self.escape_attempt_messages_prey = edited_messages
            elif messages is self.escape_messages_owner:
                self.escape_messages_owner = edited_messages
            elif messages is self.escape_messages_prey:
                self.escape_messages_prey = edited_messages
            elif messages is self.escape_messages_outside:
                self.escape_messages_outside = edited_messages
            elif messages is self.escape_item_messages_owner:
                self.escape_item_messages_owner = edited_messages
            elif messages is self.escape_item_messages_prey:
                self.escape_item_messages_prey = edited_messages
            elif messages is self.escape_item_messages_outside:
                self.escape_item_messages_outside = edited_messages
            elif messages is self.escape_fail_messages_owner:
                self.escape_fail_messages_owner = edited_messages
            elif messages is self.escape_fail_messages_prey:
                self.escape_fail_messages_prey = edited_messages
            elif messages is self.escape_attempt_absorbed_messages_owner:
                self.escape_attempt_absorbed_messages_owner = edited_messages
            elif messages is self.escape_attempt_absorbed_messages_prey:
                self.escape_attempt_absorbed_messages_prey = edited_messages
            elif messages is self.escape_absorbed_messages_owner:
                self.escape_absorbed_messages_owner = edited_messages
            elif messages is self.escape_absorbed_messages_prey:
                self.escape_absorbed_messages_prey = edited_messages
            elif messages is self.escape_absorbed_messages_outside:
                self.escape_attempt_absorbed_messages_outside = edited_messages
            elif messages is self.escape_attempt_absorbed_messages_outside:
                self.escape_absorbed_messages_outside = edited_messages
            elif messages is self.escape_fail_absorbed_messages_owner:
                self.escape_fail_absorbed_messages_owner = edited_messages
            elif messages is self.escape_fail_absorbed_messages_prey:
                self.escape_fail_absorbed_messages_prey = edited_messages
            elif messages is self.primary_transfer_messages_owner:
                self.primary_transfer_messages_owner = edited_messages
            elif messages is self.primary_transfer_messages_prey:
                self.primary_transfer_messages_prey = edited_messages
            elif messages is self.secondary_transfer_messages_owner:
                self.secondary_transfer_messages_owner = edited_messages
            elif messages is self.secondary_transfer_messages_prey:
                self.secondary_transfer_messages_prey = edited_messages
            elif messages is self.primary_autotransfer_messages_owner:
                self.primary_autotransfer_messages_owner = edited_messages
            elif messages is self.primary_autotransfer_messages_prey:
                self.primary_autotransfer_messages_prey = edited_messages
            elif messages is self.secondary_autotransfer_messages_owner:
                self.secondary_autotransfer_messages_owner = edited_messages
            elif messages is self.secondary_autotransfer_messages_prey:
                self.secondary_autotransfer_messages_prey = edited_messages
            elif messages is self.digest_messages_prey:
                self.digest_messages_prey = edited_messages
            elif messages is self.digest_messages_owner:
                self.digest_messages_owner = edited_messages
            elif messages is self.absorb_messages_prey:
                self.absorb_messages_prey = edited_messages
            elif messages is self.absorb_messages_owner:
                self.absorb_messages_owner = edited_messages
            elif messages is self.unabsorb_messages_prey:
                self.unabsorb_messages_prey = edited_messages
            elif messages is self.unabsorb_messages_owner:
                self.unabsorb_messages_owner = edited_messages
            elif messages is self.emotes_hold:
                self.emotes_hold = edited_messages
            elif messages is self.emotes_holdabsorbed:
                self.emotes_holdabsorbed = edited_messages
            elif messages is self.emotes_digest:
                self.emotes_digest = edited_messages
            elif messages is self.emotes_absorb:
                self.emotes_absorb = edited_messages
            elif messages is self.emotes_unabsorb:
                self.emotes_unabsorb = edited_messages
            elif messages is self.emotes_drain:
                self.emotes_drain = edited_messages
            elif messages is self.emotes_heal:
                self.emotes_heal = edited_messages
            elif messages is self.emotes_steal:
                self.emotes_steal = edited_messages
            elif messages is self.emotes_shrink:
                self.emotes_shrink = edited_messages
            elif messages is self.emotes_grow:
                self.emotes_grow = edited_messages
            elif messages is self.emotes_egg:
                self.emotes_egg = edited_messages

        self.examine_window.close()

