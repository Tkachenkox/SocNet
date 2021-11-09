from datetime import datetime, timezone

from ..extensions import db


class BaseMixin(object):
    create_date = db.Column(db.DateTime(timezone=True),  default=datetime.utcnow, nullable=False)
    remove_date = db.Column(db.DateTime(timezone=True))
