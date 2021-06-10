from app import db
from datetime import datetime as dt

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    tax = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=dt.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'tax': self.tax,
            'date_created': self.date_created
        }
        return data

    def from_dict(self, data):
        for attr in ['name', 'description', 'price']:
            if attr in data:
                setattr(self, attr, data[attr])
        self.tax = round(self.price * .06, 2)
        
        
    def __repr__(self):
        return f'<Product: {self.name} @{self.price}>'
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.ForeignKey('product.id'), nullable=False)
    date_added = db.Column(db.DateTime, default=dt.utcnow)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        from app.blueprints.authentication.models import User
        return f'<Cart: {User.quert.get(self.user_id).email}: {Product.query.get(self.product_id).name}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.ForeignKey('product.id'), nullable=False)
    date_filled = db.Column(db.DateTime, default=dt.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
