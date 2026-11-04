from flask import Flask, render_template,  request
app = Flask(__name__)

# FoodFinder restaurants in Marikina City
# Budget values are estimates for demonstration.
# Ratings and review counts are listing snapshots and may change.

restaurants = [
    {
        "name": "Cafe Lidia",
        "location": "Calumpang, Marikina City",
        "type": "Pizza",
        "budget": 300,
        "rating": 4.1,
        "reviews": 173,
        "map": "https://www.google.com/maps/search/?api=1&query=Cafe+Lidia+Marikina"
    },
    {
        "name": "Pan de Amerikana",
        "location": "Concepcion Dos, Marikina City",
        "type": "Filipino",
        "budget": 200,
        "rating": 4.0,
        "reviews": 33,
        "map": "https://www.google.com/maps/search/?api=1&query=Pan+de+Amerikana+Marikina"
    },
    {
        "name": "Eat Fresh",
        "location": "General Ordonez Street, Marikina City",
        "type": "Fast Food",
        "budget": 200,
        "rating": 4.4,
        "reviews": 886,
        "map": "https://www.google.com/maps/search/?api=1&query=Eat+Fresh+Marikina"
    },
    {
        "name": "Qizia Cafe",
        "location": "Katipunan Extension, Marikina City",
        "type": "Cafe",
        "budget": 250,
        "rating": 4.0,
        "reviews": 62,
        "map": "https://www.google.com/maps/search/?api=1&query=Qizia+Cafe+Marikina"
    },
    {
        "name": "Pares House",
        "location": "Marikina City",
        "type": "Filipino",
        "budget": 150,
        "rating": 4.5,
        "reviews": 523,
        "map": "https://www.google.com/maps/search/?api=1&query=Pares+House+Marikina"
    },
    {
        "name": "Ramen Kuroda",
        "location": "SM City Marikina",
        "type": "Fast Food",
        "budget": 300,
        "rating": 4.5,
        "reviews": 328,
        "map": "https://www.google.com/maps/search/?api=1&query=Ramen+Kuroda+SM+Marikina"
    }
]


@app.route("/")
def home():
    location = request.args.get("location", "").strip()
    food_type = request.args.get("food_type", "").strip()
    budget = request.args.get("budget", "").strip()
    min_rating = request.args.get("min_rating", "").strip()

    filtered = restaurants.copy()

    # Search only within Marikina restaurant data.
    if location:
        filtered = [
            r for r in filtered
            if location.lower() in r["location"].lower()
            or location.lower() in r["name"].lower()
        ]

    # Filter by food type.
    if food_type:
        filtered = [
            r for r in filtered
            if r["type"] == food_type
        ]

    # Filter by maximum budget.
    if budget:
        try:
            max_budget = float(budget)
            filtered = [
                r for r in filtered
                if r["budget"] <= max_budget
            ]
        except ValueError:
            pass

    # Filter by minimum rating.
    if min_rating:
        try:
            minimum_rating = float(min_rating)
            filtered = [
                r for r in filtered
                if r["rating"] >= minimum_rating
            ]
        except ValueError:
            pass

    return render_template(
        "index.html",
        restaurants=filtered,
        location=location,
        food_type=food_type,
        budget=budget,
        min_rating=min_rating
    )


if __name__ == "main":
    app.run(debug=True)
