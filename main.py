from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

session_local = sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


# Create API
@app.post("/todos/")
def create_todo(title:str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message": "Todo created successfully",
        "data": todo
    }

# Read API
@app.get("/todos/")
def  get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return {
        "message": "Todos retrieved successfully",
        "data": todos
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail=f"Todo with id {todo_id} not found"
        )
    return {
        "message": "Todo retrieved successfully",
        "data": todo
    }