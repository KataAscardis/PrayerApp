from website import db

class GenericController:
    def __init__(self, session=db.session):
        self._session = session