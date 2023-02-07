from models.reviewer import Reviewer as ReviewerModels
from schemas.reviewer import Reviewer

class ReviewerService():

    def __init__(self, db) -> None:
        self.db = db

    def get_reviewer(self):
        result = self.db.query(ReviewerModels).all()
        return result

    # traer la lista de revisores por el nombre
    def get_reviewer_for_name(self, name: str):
        result = self.db.query(ReviewerModels).filter(
            ReviewerModels.rev_name == name.capitalize()).all()
        return result
    # Traer la lista de revisores por id

    def get_reviewer_for_id(self, id: int):
        result = self.db.query(ReviewerModels).filter(ReviewerModels.rev_id== id).all()
        return result


    def create_reviewer(self, reviewer: ReviewerModels):
        new_reviewer = ReviewerModels(
            rev_name=reviewer.rev_name
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return

    def update_reviewer(self,id:int, data:Reviewer):
        revie = self.db.query(ReviewerModels).filter(ReviewerModels.rev_id == id).first()
        revie.rev_name = data.rev_name
        self.db.commit()
        return

    def delete_reviewer(self, id: int):
        self.db.query(ReviewerModels).filter(ReviewerModels.rev_id == id).delete()
        self.db.commit()
        return
