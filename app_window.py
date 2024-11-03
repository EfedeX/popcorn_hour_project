from PySide6.QtWidgets import (QMainWindow, QFileDialog, QMessageBox, QLineEdit,
                              QDialog, QVBoxLayout, QLabel, QDateEdit, QDialogButtonBox)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QDate
import requests
from app_ui import Ui_MainWindow


class MovieUploadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Upload Movie")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Title
        layout.addWidget(QLabel("Title:"))
        self.title_input = QLineEdit()
        layout.addWidget(self.title_input)

        # Description
        layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        layout.addWidget(self.description_input)

        # Release Date
        layout.addWidget(QLabel("Release Date:"))
        self.release_date_input = QDateEdit()
        self.release_date_input.setCalendarPopup(True)
        self.release_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.release_date_input)

        # Genre
        layout.addWidget(QLabel("Genre:"))
        self.genre_input = QLineEdit()
        layout.addWidget(self.genre_input)

        # Director Name
        layout.addWidget(QLabel("Director Name:"))
        self.director_name_input = QLineEdit()
        layout.addWidget(self.director_name_input)

        # Director Birth Date
        layout.addWidget(QLabel("Director Birth Date:"))
        self.director_birth_date_input = QDateEdit()
        self.director_birth_date_input.setCalendarPopup(True)
        layout.addWidget(self.director_birth_date_input)

        # OK and Cancel buttons
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_movie_data(self):
        return {
            "title": self.title_input.text(),
            "description": self.description_input.text(),
            "release_date": self.release_date_input.date().toString("yyyy-MM-dd"),
            "genre": self.genre_input.text(),
            "director": {
                "name": self.director_name_input.text(),
                "born_at": self.director_birth_date_input.date().toString("yyyy-MM-dd"),
            }
        }

class MainWindow(QMainWindow):
    def __init__(self, token=None, user_type=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.token = token
        self.user_type = user_type
        self.current_movie_index = 0
        self.movies = []
        self.setup_upload_button()
        self.ui.upload_button.clicked.connect(self.handle_upload)
        self.ui.previous_button.clicked.connect(self.show_previous_movie)
        self.ui.next_button.clicked.connect(self.show_next_movie)
        for i, star in enumerate(self.ui.rating_stars):
            star.clicked.connect(lambda checked, rating=i+1: self.handle_rating(rating))
        self.load_movies()

    def setup_upload_button(self):
        if self.user_type != "moderator":
            self.ui.upload_button.setEnabled(False)
            self.ui.upload_button.setToolTip("Only moderators can upload images")

    def load_movies(self):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get("http://localhost:8000/movies", headers=headers)
            if response.status_code == 200:
                self.movies = response.json()
                if self.movies:
                    self.show_current_movie()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load movies: {str(e)}")

    def show_current_movie(self):
        if not self.movies:
            return

        movie = self.movies[self.current_movie_index]
        self.ui.movie_title.setText(movie["title"])
        self.ui.movie_director.setText(f"Director: {movie['director']['name']}")
        self.ui.average_rating.setText(f"Average: {movie['average_rating']:.1f} ★")
        # self.update_user_rating(movie["id"])
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            movie_id = movie["id"]
            image_response = requests.get(f"http://localhost:8000/images/movie/{movie_id}", headers=headers)

            if image_response.status_code == 200:
                image_data = image_response.content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                self.ui.image.setPixmap(pixmap)
            else:
                self.ui.image.setPixmap(QPixmap())
        except Exception:
            self.ui.image.setPixmap(QPixmap())

    def handle_upload(self):
        if self.user_type != "moderator":
            QMessageBox.warning(self, "Warning", "Only moderators can upload images")
            return

        dialog = MovieUploadDialog(self)
        if dialog.exec() != QDialog.Accepted:
            return

        movie_data = dialog.get_movie_data()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Movie Image",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )

        if file_name:
            try:
                headers = {"Authorization": f"Bearer {self.token}"}
                movie_response = requests.post(
                    "http://localhost:8000/movies",
                    json=movie_data,
                    headers=headers
                )

                if movie_response.status_code != 200:
                    raise Exception("Failed to create movie")

                movie_id = movie_response.json().get("id")

                # uploading image
                with open(file_name, 'rb') as f:
                    files = {'image': ('image.jpg', f, 'image/jpeg')}
                    data = {
                        'movie_id': int(movie_id)
                    }
                    response = requests.post(
                        "http://localhost:8000/images",
                        files=files,
                        data=data,
                        headers=headers
                    )
                if response.status_code == 200:
                    QMessageBox.information(self,
                                            "Success",
                                            "Movie and image uploaded successfully!"
                    )
                    self.load_movies()
                else:
                    raise Exception("Failed to upload image")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to upload: {str(e)}")

    def handle_rating(self, rating):
        if not self.movies:
            return

        movie_id = self.movies[self.current_movie_index]["id"]
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.post(
                f"http://localhost:8000/movies/{movie_id}/rate",
                json={"score": rating},
                headers=headers
            )
            if response.status_code == 200:
                self.load_movies()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to submit rating: {str(e)}")

    def show_previous_movie(self):
        if self.movies and self.current_movie_index > 0:
            self.current_movie_index -= 1
            self.show_current_movie()

    def show_next_movie(self):
        if self.movies and self.current_movie_index < len(self.movies) - 1:
            self.current_movie_index += 1
            self.show_current_movie()

    def update_user_rating(self, movie_id):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(
                f"http://localhost:8000/movies/{movie_id}/user-rating",
                headers=headers
            )
            if response.status_code == 200:
                rating = response.json()["rating"]
                for i, star in enumerate(self.ui.rating_stars):
                    star.setChecked(i < rating)
        except Exception:
            pass
