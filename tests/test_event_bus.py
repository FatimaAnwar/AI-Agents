def test_recipe_event_has_correct_type():
    event = {
        "type": "recipe.generated",
        "data": {
            "recipe": "Chicken Biryani"
        }
    }

    assert event["type"] == "recipe.generated"
    assert "recipe" in event["data"]