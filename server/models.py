from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Define metadata before initializing SQLAlchemy
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)  # Corrected 'tittle' to 'title'
    price = db.Column(db.Float, nullable=False)  # Corrected 'float' to 'Float'
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return f"<Product(id={self.id}, title={self.title}, price={self.price}, image_url={self.image_url})>"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'image_url': self.image_url,
        }
