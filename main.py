from website import create_app, create_database
from flask import Flask

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
