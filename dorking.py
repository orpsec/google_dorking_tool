import sys
import webbrowser
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

# Google Dork listesi dosya yolu (BURAYI OTOMATİK OKUYOR)
DORK_FILE_PATH = "/home/kali/Desktop/other/Google+Dorking+Örnekleri.txt"

class GoogleDorkApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Dork Scanner")
        self.setGeometry(100, 100, 400, 300)

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Google logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("google_logo.png")  # Google logosunu buraya ekleyin
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.logo_label)

        # Dork listesi
        self.dork_label = QLabel("Dork Listesi:", self)
        self.layout.addWidget(self.dork_label)

        self.dork_combo = QComboBox(self)
        self.layout.addWidget(self.dork_combo)

        # Site girişi
        self.site_label = QLabel("Site (Örn: example.com, boş bırakıp genel arama yapabilirsin):", self)
        self.layout.addWidget(self.site_label)

        self.site_input = QLineEdit(self)
        self.layout.addWidget(self.site_input)

        # Arama butonu
        self.search_button = QPushButton("Ara", self)
        self.search_button.clicked.connect(self.perform_search)
        self.layout.addWidget(self.search_button)

        # Dork listesini yükle
        self.load_dorks()

    def load_dorks(self):
        """ Dosyadan dork listesini okur ve combo box'a ekler. """
        if not os.path.isfile(DORK_FILE_PATH):
            QMessageBox.critical(self, "Hata", f"'{DORK_FILE_PATH}' bulunamadı! Lütfen dosyanın yolunu kontrol edin.")
            return
        
        try:
            with open(DORK_FILE_PATH, "r", encoding="utf-8") as file:
                dorks = [line.strip() for line in file.readlines() if line.strip()]
                self.dork_combo.addItems(dorks)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Dosya okunurken bir sorun oluştu -> {e}")

    def perform_search(self):
        """ Seçilen dork ve site ile Google araması yapar. """
        selected_dork = self.dork_combo.currentText()
        site = self.site_input.text().strip()

        if site:
            search_url = f"https://www.google.com/search?q=site:{site} {selected_dork}"
        else:
            search_url = f"https://www.google.com/search?q={selected_dork}"
        
        webbrowser.open(search_url)

def main():
    app = QApplication(sys.argv)
    window = GoogleDorkApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()