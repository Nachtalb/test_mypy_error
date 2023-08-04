import reflex as rx


class TestmypyerrorConfig(rx.Config):
    pass


config = TestmypyerrorConfig(
    app_name="test_mypy_error",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)
