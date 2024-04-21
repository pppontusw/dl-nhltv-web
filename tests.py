from datetime import datetime
import unittest
from app import create_app, db
from app.models import DbGame
from config import Config


def push_games():
    games = [
        # TODO
    ]
    for idx, game in enumerate(games):
        new_game = DbGame(
            # TODO
        )
        db.session.add(new_game)
        db.session.commit()


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "very-secret"


class MainViewCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_view(self):
        rsp = self.test_client.get("/")
        self.assertEqual(rsp.status, "200 OK")
        self.assertTrue(
            '<a class="hidden ajaxurl" id="ajaxurl" href="/ajax">/ajax</a>'
            in rsp.get_data(as_text=True)
        )

if __name__ == "__main__":
    unittest.main(verbosity=1)

