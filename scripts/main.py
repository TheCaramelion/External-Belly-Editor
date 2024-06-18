import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFileDialog, QMessageBox, QLabel, QListWidget,
    QListWidgetItem, QTabWidget, QGroupBox, QTextEdit, QMainWindow, QAction, qApp
)
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from classes.controls_tab import ControlsTab
from classes.descriptions_tab import DescriptionsTab
from classes.sounds_tab import SoundsTab
from classes.visuals_tab import VisualsTab
from classes.interactions_tab import InteractionsTab
from classes.liquids_tab import LiquidsTab

class VRDBEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.belly_data_buffer = []
        self.current_file_data = None
        self.current_file_path = None

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('External Belly Editor')
        
        self.create_menu()
        self.create_layout()

    def create_menu(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('&File')
        
        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open Bellies')
        open_action.triggered.connect(self.load_vrdb)
        file_menu.addAction(open_action)

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save Bellies')
        save_action.triggered.connect(self.save_vrdb)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu('&Help')
        github_action = QAction('&GitHub', self)
        github_action.setStatusTip('Visit GitHub Repository')
        github_action.triggered.connect(self.open_github_repo)
        help_menu.addAction(github_action)

    def create_layout(self):
        self.layout = QVBoxLayout()

        # Create a title label (hidden initially)
        self.title_label = QLabel('File Title', self)
        self.title_label.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.title_label.setVisible(False)
        self.layout.addWidget(self.title_label)

        # Create a horizontal layout for the belly list and tabs
        self.horizontal_layout = QHBoxLayout()

        # Left side: Belly List
        self.left_group_box = QGroupBox('Belly List', self)
        self.left_layout = QVBoxLayout(self.left_group_box)

        self.belly_list = QListWidget()
        self.belly_list.setMaximumWidth(150)  # Adjusted width
        self.belly_list.itemSelectionChanged.connect(self.on_belly_selected)
        self.left_layout.addWidget(self.belly_list)

        self.load_button = QPushButton('Load Bellies', self)
        self.load_button.clicked.connect(self.load_vrdb)
        self.left_layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save Bellies', self)
        self.save_button.clicked.connect(self.save_vrdb)
        self.save_button.setEnabled(False)  # Initially disabled
        self.left_layout.addWidget(self.save_button)

        self.horizontal_layout.addWidget(self.left_group_box)

        # Right side: Tab Widget
        self.right_tab_widget = QTabWidget()
        self.right_tab_widget.setMinimumWidth(600)  # Adjusted minimum width

        # JSON tab
        self.json_tab = QWidget()
        self.json_layout = QVBoxLayout(self.json_tab)
        self.json_scroll_area = QTextEdit()
        self.json_scroll_area.setReadOnly(True)
        self.json_layout.addWidget(self.json_scroll_area)
        self.right_tab_widget.addTab(self.json_tab, 'JSON')

        # Controls tab
        self.controls_tab = ControlsTab()
        self.right_tab_widget.addTab(self.controls_tab, 'Controls')

        # Descriptions tab
        self.descriptions_tab = DescriptionsTab()
        self.right_tab_widget.addTab(self.descriptions_tab, 'Descriptions')

        # Sounds tab
        self.sounds_tab = SoundsTab()
        self.right_tab_widget.addTab(self.sounds_tab, 'Sounds')

        # Visuals tab
        self.visuals_tab = VisualsTab()
        self.right_tab_widget.addTab(self.visuals_tab, 'Visuals')

        # Interactions tab
        self.interactions_tab = InteractionsTab()
        self.right_tab_widget.addTab(self.interactions_tab, 'Interactions')

        # Liquids tab
        self.liquids_tab = LiquidsTab()
        self.right_tab_widget.addTab(self.liquids_tab, 'Liquids')

        self.horizontal_layout.addWidget(self.right_tab_widget)
        self.layout.addLayout(self.horizontal_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def load_vrdb(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("VRDB files (*.vrdb)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getOpenFileName(self, "Open VRDB File", "", "VRDB files (*.vrdb)")

        if file_path:
            try:
                # Set the title label text
                title = os.path.basename(file_path)
                title = title.split('_')[0]
                self.title_label.setText(title)
                self.title_label.setVisible(True)

                with open(file_path, 'r', encoding='utf-8') as f:
                    self.current_file_path = file_path
                    self.current_file_data = json.load(f)
                    self.belly_data_buffer = self.current_file_data.copy()
                    self.display_bellies(self.belly_data_buffer)
                    
                    if self.belly_list.count() > 0:
                        self.belly_list.setCurrentRow(0)
                    
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to load VRDB file:\n{str(e)}')

    def display_bellies(self, data):
        self.belly_list.clear()
        for index, belly in enumerate(data):
            belly_name = belly.get('name', f'Belly {index + 1}')
            item = QListWidgetItem(belly_name)
            item.belly_data = belly
            self.belly_list.addItem(item)

    def on_belly_selected(self):
        selected_items = self.belly_list.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            belly_data = selected_item.belly_data
            self.json_scroll_area.setPlainText(json.dumps(belly_data, indent=4))
            self.json_scroll_area.setReadOnly(False)
            self.save_button.setEnabled(True)

            # Update tabs with the selected belly data
            self.controls_tab.set_belly_data(belly_data)
            self.descriptions_tab.set_description_data(belly_data)

    def update_belly_data_from_tabs(self):
        selected_items = self.belly_list.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            belly_data = selected_item.belly_data

            belly_data.update(self.controls_tab.get_belly_data())
            belly_data.update(self.descriptions_tab.get_description_data())

            for i, item in enumerate(self.belly_data_buffer):
                if item.get('name') == belly_data.get('name'):
                    self.belly_data_buffer[i] = belly_data
                    break
            else:
                self.belly_data_buffer.append(belly_data)

            self.json_scroll_area.setPlainText(json.dumps(belly_data, indent=4))
            
            self.refresh_belly_list()

    def refresh_belly_list(self):
        self.belly_list.clear()
        for belly in self.belly_data_buffer:
            belly_name = belly.get('name', 'Unnamed Belly')
            item = QListWidgetItem(belly_name)
            item.belly_data = belly
            self.belly_list.addItem(item)

    def save_vrdb(self):
        if not self.current_file_path:
            QMessageBox.critical(self, 'Error', 'Current file path is not set')
            return

        self.update_belly_data_from_tabs() 

        try:
            with open(self.current_file_path, 'w', encoding='utf-8') as f:
                json.dump(self.belly_data_buffer, f, indent=4)
                QMessageBox.information(self, 'Success', 'Bellies saved successfully.')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to save bellies:\n{str(e)}')
            
    def open_github_repo(self):
        url = 'https://github.com/TheCaramelion/External-Belly-Editor'
        QDesktopServices.openUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = VRDBEditor()
    editor.show()
    sys.exit(app.exec_())
