<?php

/*
 * Copyright (c) 2026 Code Infinity
 * SPDX-License-Identifier: MPL-2.0
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

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
