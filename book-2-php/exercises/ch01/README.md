# Chapter 1 Exercises

## Exercise A: Greeting API

Create `src/routes/greet.php` with a `GET /api/greet` endpoint that:

1. Reads a `name` query parameter (default: "Stranger")
2. Determines the time of day based on the server's current hour
3. Returns JSON with `greeting` and `time_of_day` fields

### Time of Day Rules

- 5:00 - 11:59 = "morning"
- 12:00 - 16:59 = "afternoon"
- 17:00 - 20:59 = "evening"
- 21:00 - 4:59 = "night"

### Expected Output

```bash
curl "http://localhost:7145/api/greet?name=Sarah"
# {"greeting":"Welcome, Sarah!","time_of_day":"afternoon"}

curl "http://localhost:7145/api/greet"
# {"greeting":"Welcome, Stranger!","time_of_day":"afternoon"}
```

## Exercise B: Product List Page

Create a page at `GET /store` that displays a product catalog using Frond templates.

### Requirements

1. At least 5 products, each with: name, category, price, featured (boolean)
2. Featured products visually highlighted
3. Show total count and featured count
4. Use template inheritance (layout + page)
5. Include tina4.css and frond.js

### Files to Create

- `src/routes/store.php` -- route handler
- `src/templates/store-layout.html` -- base layout
- `src/templates/store.html` -- product list page

### Starter Data

```php
$products = [
    ["name" => "Espresso Machine", "category" => "Kitchen", "price" => 299.99, "featured" => true],
    ["name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "featured" => false],
    ["name" => "Standing Desk", "category" => "Office", "price" => 549.99, "featured" => true],
    ["name" => "Noise-Canceling Headphones", "category" => "Electronics", "price" => 199.99, "featured" => true],
    ["name" => "Water Bottle", "category" => "Fitness", "price" => 24.99, "featured" => false]
];
```
