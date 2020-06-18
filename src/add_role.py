from app import db, user_data_store
from user.models import User, Role

user_data_store.create_user(
    first_name="Сергей",
    last_name="Кайнов",
    email="Sergej_kajnov@mail.ru",
    password="21121987",
)

user_data_store.create_role(
    naem="admin",
    description="admin",
)

db.session.commit()

user = User.query.first()
role = Role.query.first()

user_data_store.add_role_to_user(user, role)

db.session.commit()

