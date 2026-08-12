def test_nutrition_request_contains_nutrition():
    request = "Calculate calories and protein"

    assert "calories" in request.lower()
    assert "protein" in request.lower()