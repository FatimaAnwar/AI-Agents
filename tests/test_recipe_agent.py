def test_recipe_request_is_not_empty():
    request = "Give me a chicken biryani recipe"

    assert request
    assert "recipe" in request.lower()