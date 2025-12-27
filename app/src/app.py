import os
from flask import Flask, jsonify, request
from .extensions import db, migrate
from .models import User

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///local.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/hello")
    def hello():
        return "Hello from Flask!"

    @app.get("/users")
    def list_users():
        users = User.query.order_by(User.id).all()
        return jsonify([u.to_dict() for u in users])

    @app.post("/users")
    def create_user_endpoint():
        data = request.get_json(force=True)
        name = data.get("name")
        u = User(name=name)
        db.session.add(u)
        db.session.commit()
        return jsonify(u.to_dict()), 201

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
