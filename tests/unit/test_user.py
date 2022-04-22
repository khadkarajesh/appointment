from db.models.user import User


def test_should_save_user(db):
    user = User()
    user.id = 1
    user.username = "rajesh"
    user.password = "password"
    user.confirmed = True

    db.session.add(user)
    db.session.commit()

    saved_user = User.query.get(user.id)
    assert saved_user.id == user.id
    assert saved_user.username == "rajesh"


def test_should_make_request(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200
    assert response.json == {"version": "v1"}
