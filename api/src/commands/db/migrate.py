from app.infrastractures.database import engine
from app.config.schema import Base

def exec(*args, **kwargs):
  Base.metadata.create_all(engine)

