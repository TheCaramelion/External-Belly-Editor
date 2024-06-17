from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QListWidget, QPushButton, QGroupBox, QHBoxLayout
)
from constants.controls_options import MODE_ADDONS_OPTIONS, MODE_OPTIONS, ITEM_MODE_OPTIONS

class ControlsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Name
        self.name_label = QLabel('Name:')
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.mode_label = QLabel('Mode:')
        self.layout.addWidget(self.mode_label)

        self.mode_combobox = QComboBox()
        self.mode_combobox.addItems(MODE_OPTIONS)
        self.layout.addWidget(self.mode_combobox)

        # Item Mode
        self.item_mode_label = QLabel('Item Mode:')
        self.layout.addWidget(self.item_mode_label)

        self.item_mode_combobox = QComboBox()
        self.item_mode_combobox.addItems(ITEM_MODE_OPTIONS)
        self.layout.addWidget(self.item_mode_combobox)

        # Mode Addons
        self.mode_addons_groupbox = QGroupBox('Mode Addons')
        self.mode_addons_layout = QVBoxLayout()

        self.mode_addons_label = QLabel('Select Mode Addon:')
        self.mode_addons_layout.addWidget(self.mode_addons_label)

        self.mode_addons_combobox = QComboBox()
        self.mode_addons_combobox.addItems(MODE_ADDONS_OPTIONS)
        self.mode_addons_layout.addWidget(self.mode_addons_combobox)

        # Button row for Add and Remove Mode Addon
        button_layout = QHBoxLayout()
        self.add_mode_addon_button = QPushButton('Add Mode Addon')
        button_layout.addWidget(self.add_mode_addon_button, 1)

        self.remove_mode_addon_button = QPushButton('Remove Mode Addon')
        button_layout.addWidget(self.remove_mode_addon_button, 1)

        self.mode_addons_layout.addLayout(button_layout)

        self.addon_list_widget = QListWidget()
        self.mode_addons_layout.addWidget(self.addon_list_widget)

        self.mode_addons_groupbox.setLayout(self.mode_addons_layout)
        self.layout.addWidget(self.mode_addons_groupbox)

        self.setLayout(self.layout)

        self.add_mode_addon_button.clicked.connect(self.on_add_mode_addon_clicked)
        self.remove_mode_addon_button.clicked.connect(self.on_remove_mode_addon_clicked)

        # Remove already added addons from the mode_addons_combobox
        self.update_mode_addons_index([])

    def set_belly_data(self, belly_data):
        self.name_input.setText(belly_data.get('name', ''))
        self.mode_combobox.setCurrentText(belly_data.get('mode', ''))
        self.item_mode_combobox.setCurrentText(belly_data.get('item_mode', ''))
        self.load_addons(belly_data.get('addons', []))
        self.update_mode_addons_index(belly_data.get('addons', []))

    def get_belly_data(self):
        belly_data = {
            'name': self.name_input.text(),
            'mode': self.mode_combobox.currentText(),
            'item_mode': self.item_mode_combobox.currentText(),
            'addons': self.get_addons()
        }
        return belly_data

    def clear_fields(self):
        self.name_input.clear()
        self.mode_combobox.setCurrentIndex(0)
        self.item_mode_combobox.setCurrentIndex(0)
        self.addon_list_widget.clear()
        self.update_mode_addons_index([])

    def load_addons(self, addons):
        self.addon_list_widget.clear()
        for addon in addons:
            self.addon_list_widget.addItem(addon)
            # Remove addon from mode_addons_combobox if it exists
            if addon in MODE_ADDONS_OPTIONS:
                self.mode_addons_combobox.removeItem(self.mode_addons_combobox.findText(addon))

    def on_add_mode_addon_clicked(self):
        selected_addon = self.mode_addons_combobox.currentText()
        if selected_addon and selected_addon not in self.get_addons():
            self.addon_list_widget.addItem(selected_addon)
            self.mode_addons_combobox.removeItem(self.mode_addons_combobox.findText(selected_addon))

    def on_remove_mode_addon_clicked(self):
        selected_items = self.addon_list_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                addon_text = item.text()
                self.addon_list_widget.takeItem(self.addon_list_widget.row(item))
                self.mode_addons_combobox.addItem(addon_text)

    def get_addons(self):
        addons = []
        for index in range(self.addon_list_widget.count()):
            addon = self.addon_list_widget.item(index).text()
            addons.append(addon)
        return addons

    def update_mode_addons_index(self, selected_addons):
        self.mode_addons_combobox.clear()
        available_addons = [addon for addon in MODE_ADDONS_OPTIONS if addon not in selected_addons]
        self.mode_addons_combobox.addItems(available_addons)
