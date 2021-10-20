from datetime import datetime, timezone

from ..extensions import db


class DateMixin(object):
    create_date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    update_date = db.Column(db.DateTime(timezone=True), onupdate=datetime.utcnow)
    remove_date = db.Column(db.DateTime(timezone=True))
