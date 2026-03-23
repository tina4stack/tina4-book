<?php
// Chapter 1 Example: Template Rendering Route
// Place this file at src/routes/pages.php in your Tina4 project

use Tina4Router;

Router::get("/products", function ($request, $response) {
    $products = [
        [
            "name" => "Wireless Keyboard",
            "description" => "Ergonomic wireless keyboard with backlit keys.",
            "price" => 79.99,
            "in_stock" => true
        ],
        [
            "name" => "USB-C Hub",
            "description" => "7-port USB-C hub with HDMI, SD card reader, and Ethernet.",
            "price" => 49.99,
            "in_stock" => true
        ],
        [
            "name" => "Monitor Stand",
            "description" => "Adjustable aluminum monitor stand with cable management.",
            "price" => 129.99,
            "in_stock" => false
        ],
        [
            "name" => "Mechanical Mouse",
            "description" => "High-precision wireless mouse with 16,000 DPI sensor.",
            "price" => 59.99,
            "in_stock" => true
        ]
    ];

    return $response->render("products.html", ["products" => $products]);
});
