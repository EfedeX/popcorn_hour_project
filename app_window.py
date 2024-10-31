from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap
import requests
from app_ui import Ui_MainWindow

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
        self.ui.comment_button.clicked.connect(self.handle_comment)
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

        try:
            image_data = requests.get(movie["image_url"]).content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.ui.image.setPixmap(pixmap)
        except Exception:
            self.ui.image.setPixmap(QPixmap())

        self.ui.movie_title.setText(movie["title"])
        self.ui.movie_director.setText(f"Director: {movie['director']['name']}")
        self.ui.average_rating.setText(f"Average: {movie['average_rating']:.1f} ★")
        self.update_user_rating(movie["id"])

    def handle_upload(self):
        if self.user_type != "moderator":
            QMessageBox.warning(self, "Warning", "Only moderators can upload images")
            return

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select Movie Image",
            "",
            "Image Files (*.png *.jpg *.jpeg)"
        )

        if file_name:
            # Aquí implementaría la lógica para subir la imagen
            # junto con la información de la película
            pass

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

    def handle_comment(self):
        comment, ok = QInputDialog.getText(self, "Add Comment", "Enter your comment:")
        if ok and comment:
            item = QListWidgetItem(comment)
            self.ui.conversation_list.addItem(item)
