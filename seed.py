from app import app
from models import db, User, Feedback

db.drop_all()
db.create_all()

jonny = User.register(username='jon123', password='testing',
                      email='jonbon@jon.com', first_name='Jonny', last_name='Kim')
test = User.register(username='test123', password='testing23',
                     email='test@t.com', first_name='tester', last_name='1')
megan = User.register(username='megan1', password='test123',
                      email='m@mc.com', first_name='Megan', last_name='Choi')

db.session.add_all([jonny, test, megan])
db.session.commit()
