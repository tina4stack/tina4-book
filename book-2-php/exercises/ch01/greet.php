<?php
// Exercise A: Greeting API
// Place this file at src/routes/greet.php in your Tina4 project
//
// TODO: Create a GET /api/greet endpoint that:
// 1. Reads query parameter "name" (default "Stranger")
// 2. Calculates time_of_day from the current hour
// 3. Returns JSON with "greeting" and "time_of_day"

use Tina4Router;

Router::get("/api/greet", function ($request, $response) {
    // Your code here
    // Hints:
    //   $request->params["name"] to get query parameters
    //   date("G") returns the hour in 24-hour format (0-23)
    //   $response->json([...]) to return JSON

    return $response->json(["error" => "Not implemented yet"]);
});
