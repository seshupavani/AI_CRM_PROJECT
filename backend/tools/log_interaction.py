import json
from database import SessionLocal
from models.interaction_model import Interaction

def log_interaction(summary_json):

    db=SessionLocal()

    data=json.loads(summary_json)

    interaction=Interaction(

        hcp_name=data.get("hcp_name"),

        topics=data.get("topics"),

        materials_shared=data.get("materials_shared"),

        samples_distributed=data.get("samples_distributed"),

        sentiment=data.get("sentiment"),

        outcomes=data.get("outcomes"),

        follow_up=data.get("follow_up")
    )

    db.add(interaction)

    db.commit()

    db.refresh(interaction)

    return interaction