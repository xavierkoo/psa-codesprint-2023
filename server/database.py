from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
import models
from seed import seed_db


db_config = {
    "host": "bts_db",
    "user": "bts_user",
    "password": "bts_password",
    "port": 3306,
    "database": "bts_db_mysql",
}


def create_database_if_not_exists(db_persist=False):
    """
    The function `create_database_if_not_exists` creates a database if it does not exist, and optionally
    persists the database if specified.

    :param db_persist: The `db_persist` parameter is a boolean flag that determines whether the database
    should be persisted or not. If `db_persist` is set to `True`, the database will be created if it
    doesn't exist and the connection will be established using that database. If `db_persist`, defaults
    to False (optional)
    :return: If `db_persist` is `True`, the function will return after executing the `CREATE DATABASE IF
    NOT EXISTS` and `USE` statements. If `db_persist` is `False`, the function will return after
    executing the `DROP DATABASE IF EXISTS`, `CREATE DATABASE IF NOT EXISTS`, and `USE` statements.
    """

    try:
        connection = pymysql.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

        with connection.cursor() as cursor:
            if db_persist:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
                cursor.execute(f"USE {db_config['database']}")
                return

            else:
                cursor.execute(f"DROP DATABASE IF EXISTS {db_config['database']}")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']}")
                cursor.execute(f"USE {db_config['database']}")

    except pymysql.MySQLError as e:
        print(f"Error creating or using database: {e}")
    finally:
        connection.close()


def init_db(db_persist=False):
    """
    The function `init_db` initializes a database by creating a new database if it doesn't exist,
    setting up the engine and session, and optionally returning the engine and session objects.
    
    :param db_persist: The `db_persist` parameter is a boolean flag that determines whether the database
    connection should be persistent or not. If `db_persist` is set to `True`, the function will return
    the engine and session objects without creating or seeding the database. If `db_persist` is set to,
    defaults to False (optional)
    :return: The function `init_db` returns either the `engine` and `SessionLocal` objects if
    `db_persist` is `True`, or it returns the `engine`, `SessionLocal`, and `session` objects if
    `db_persist` is `False`.
    """
    # Connects to the database and drop/create new database
    create_database_if_not_exists(db_persist)

    # Sets up the engine and session
    URL_DB = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    engine = create_engine(URL_DB)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    if db_persist:
        return engine, SessionLocal
    else:
        models.Base.metadata.create_all(bind=engine)
        session = SessionLocal()
        seed_db(session)

    return engine, SessionLocal


def get_session():
    """
    The function `get_session` creates a database connection engine and yields a session object for
    interacting with the database.
    """

    # Connects to the database and create engine
    URL_DB = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    engine = create_engine(URL_DB, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    return session


def get_db():
    """
    The function `get_db()` returns a database session and ensures that it is closed properly after use.
    """

    db = get_session()
    return db