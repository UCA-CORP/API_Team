from sqlmodel import Field, SQLModel, create_engine, Session, select


class Chat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    race: str
    age: int | None = None

class Arme(SQLModel, table=True):
    id: int | None=Field(default=None, primary_key=True)
    type:str


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True) 
#echo = true : It will make the engine print all the SQL statements it executes, which can help you understand what's happening.


def create_db_and_tables():
    SQLModel.metadata.create_all(engine) #create database and tables

def create_cats():
    chat1 = Chat(name="Kovou", race="x", age=9)
    chat2 = Chat(name="Cacato", race="europeen", age=10)
    with Session(engine) as session:
        session.add(chat1)
        session.add(chat2)
        session.commit()

def create_weapons():
    knife = Arme(type="Knife")
    sword = Arme(type="Sword")

    session = Session(engine)
    session.add(knife)
    session.add(sword)
    session.commit()
    session.close()


# with Session(engine) as session:
#     statement = select(Chat).where(Chat.name == "Kovou")
#     chat = session.exec(statement).first()
#     print(chat)


if __name__ == "__main__":
    create_db_and_tables()
    # create_cats() #ajoute systematiquement les données (pas de check de doublons dans le code)
    # create_weapons() #ajoute systematiquement les données (pas de check de doublons dans le code)