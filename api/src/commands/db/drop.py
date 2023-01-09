from app.infrastractures.database import engine
from app.config.schema import Base

def exec(*args, **kwargs):
  Base.metadata.drop_all(engine)

