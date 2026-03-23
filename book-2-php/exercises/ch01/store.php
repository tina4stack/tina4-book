<?php
// Exercise B: Product List Page
// Place this file at src/routes/store.php in your Tina4 project
//
// TODO: Create a GET /store endpoint that:
// 1. Defines an array of 5+ products (name, category, price, featured)
// 2. Counts featured products
// 3. Renders the store.html template with the data

use Tina4Router;

Router::get("/store", function ($request, $response) {
    $products = [
        ["name" => "Espresso Machine", "category" => "Kitchen", "price" => 299.99, "featured" => true],
        ["name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "featured" => false],
        ["name" => "Standing Desk", "category" => "Office", "price" => 549.99, "featured" => true],
        ["name" => "Noise-Canceling Headphones", "category" => "Electronics", "price" => 199.99, "featured" => true],
        ["name" => "Water Bottle", "category" => "Fitness", "price" => 24.99, "featured" => false]
    ];

    // TODO: Count featured products
    // TODO: Render the store.html template with products and featured_count

    return $response->json(["error" => "Not implemented yet"]);
});
