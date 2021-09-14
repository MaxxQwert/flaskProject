from app import app

app.config.update(
    DEBUG=False,
)


if __name__ == "__main__":
    app.run(debug=False)