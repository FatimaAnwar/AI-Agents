from database.repository import CookingRepository


def test_save_and_get_recipe(tmp_path):

    db_file = tmp_path / "test.db"

    repository = CookingRepository(str(db_file))

    repository.save_recipe(
        request_id="123",
        recipe_name="Chicken Biryani",
        ingredients=["Chicken", "Rice"],
        instructions="Cook the chicken and rice."
    )

    recipe = repository.get_recipe("123")

    assert recipe is not None
    assert recipe["recipe_name"] == "Chicken Biryani"
    assert recipe["ingredients"] == ["Chicken", "Rice"]