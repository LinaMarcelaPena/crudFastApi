from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Reviewer(Base):

    __tablename__ = "reviewer"

    rev_id = Column(Integer, primary_key=True, index=True)
    rev_name = Column(String)
    