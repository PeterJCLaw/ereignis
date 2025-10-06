from __future__ import annotations

import unittest

from starlette.testclient import TestClient

from ereignis.server import app


class AppTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()

        test_client = TestClient(app)
        self.session = test_client.__enter__()
        self.url_for = app.url_path_for

    def tearDown(self) -> None:
        self.session.__exit__(None, None, None)
        super().tearDown()

    def test_app(self) -> None:
        response = self.session.post(
            self.url_for("graphql"),
            json={
                "query": r"""
                    query TestQuery($events: [Event]) {
                        events(events: $events)
                    }
                """,
            },
        )
        self.assertEqual(200, response.status_code, response.text)
