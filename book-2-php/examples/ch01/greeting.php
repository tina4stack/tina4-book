<?php
// Chapter 1 Example: Basic Greeting Route
// Place this file at src/routes/greeting.php in your Tina4 project

use Tina4\Route;

// GET endpoint with a path parameter
Route::get("/api/greeting/{name}", function ($request, $response) {
    $name = $request->params["name"];
    return $response->json([
        "message" => "Hello, " . $name . "!",
        "timestamp" => date("c")
    ]);
});

// POST endpoint with a JSON body
Route::post("/api/greeting", function ($request, $response) {
    $name = $request->body["name"] ?? "World";
    $language = $request->body["language"] ?? "en";

    $greetings = [
        "en" => "Hello",
        "es" => "Hola",
        "fr" => "Bonjour",
        "de" => "Hallo",
        "ja" => "Konnichiwa"
    ];

    $greeting = $greetings[$language] ?? $greetings["en"];

    return $response->json([
        "message" => $greeting . ", " . $name . "!",
        "language" => $language
    ], 201);
});
