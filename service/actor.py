from models.actor import Actor as ActorMoldel
from schemas.actor import Actor as Actor

class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorMoldel:
        result = self.db.query(ActorMoldel).all()
        return result

    # traer la lista de generos por el titulo
    def get_actors_first_name(self, first: str):
        result = self.db.query(ActorMoldel).filter(
            ActorMoldel.actor_first_name == first.capitalize()).all()
        return result
    # Traer la lista de peliculas por id

    def get_actors_for_id(self, id: int):
        result = self.db.query(ActorMoldel).filter(ActorMoldel.id == id).all()
        return result

    def get_actors_for_last_name(self, last: str):
        result = self.db.query(ActorMoldel).filter(
            ActorMoldel.actor_last_name == last.capitalize()).all()
        return result

    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        actor_first_name = actor.actor_first_name.capitalize() ,
        actor_last_name = actor.actor_last_name.capitalize(),
        actor_gender = actor.actor_gender.upper(),    
        )
        self.db.add(new_actor)
        self.db.commit()
        return

    def update_actor(self,id:int, actor: Actor):
        act = self.db.query(ActorMoldel).filter(ActorMoldel.id == id).first()
        act.actor_first_name = actor.actor_first_name.capitalize()
        act.actor_last_name = actor.actor_last_name.capitalize()
        act.actor_gender = actor.actor_gender.upper()
        self.db.commit()
        return

    def delete_actor(self, id: int):
        self.db.query(ActorMoldel).filter(ActorMoldel.id == id).delete()
        self.db.commit()
        return