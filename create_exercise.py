from flask import Flask
from models import db, Exercise
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    # Créer un nouvel exercice à trous
    exercise = Exercise(
        title="Exercice à trous - Nombres décimaux",
        exercise_type="fill_in_blanks",
        teacher_id=1,
        content=json.dumps({
            "sentences": [
                "Dans 3,45 le chiffre des dixièmes est ___",
                "Dans 3,45 le chiffre des centièmes est ___",
                "3,45 = ___ unités et 45 centièmes",
                "3,45 = ___ dixièmes",
                "3,45 = ___ centièmes"
            ],
            "words": ["4", "5", "3", "34,5", "345"]
        })
    )
    
    db.session.add(exercise)
    db.session.commit()
    
    print(f"Exercice créé avec l'ID: {exercise.id}")
    print("\nContenu:")
    print(json.dumps(exercise.get_content(), indent=2))
