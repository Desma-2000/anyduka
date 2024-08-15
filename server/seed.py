from faker import Faker
from app import app
from models import db, Product

fake = Faker()

with app.app_context():
    for _ in range(5):  # Loop to create 5 fake products
        product = Product(  # Assuming your model is named `Product`
            title=fake.word(),  # Assuming `title` is the correct field name
            price=round(fake.random_number(digits=5), 2),
            image_url=fake.image_url(),  # Generate a fake image URL
        )
        db.session.add(product)
    db.session.commit()

    print("Seeding complete!")
