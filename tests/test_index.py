def test_index_status(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_index_title(test_client):
    response = test_client.get('/')
    assert 'PyDev Reactions' in response

