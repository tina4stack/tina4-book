<?php
// Chapter 1 Solution: Exercise B - Product List Route
// Place this file at src/routes/store.php in your Tina4 project

use Tina4\Route;

Route::get("/store", function ($request, $response) {
    $products = [
        ["name" => "Espresso Machine", "category" => "Kitchen", "price" => 299.99, "featured" => true],
        ["name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "featured" => false],
        ["name" => "Standing Desk", "category" => "Office", "price" => 549.99, "featured" => true],
        ["name" => "Noise-Canceling Headphones", "category" => "Electronics", "price" => 199.99, "featured" => true],
        ["name" => "Water Bottle", "category" => "Fitness", "price" => 24.99, "featured" => false]
    ];

    $featuredCount = count(array_filter($products, fn($p) => $p["featured"]));

    return $response->render("store.html", [
        "products" => $products,
        "featured_count" => $featuredCount
    ]);
});
