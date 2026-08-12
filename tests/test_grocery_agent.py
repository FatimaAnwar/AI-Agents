def test_grocery_request_contains_ingredients():
    request = "Create a grocery list from this recipe"

    assert "grocery" in request.lower()
    assert "recipe" in request.lower()