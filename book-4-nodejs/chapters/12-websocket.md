# Chapter 12: Real-time with WebSocket

## 1. The Refresh Button Problem

Your project management app needs live updates. Someone moves a card from "In Progress" to "Done." Everyone else should see it. Now. Not after a refresh.

WebSocket establishes a persistent, bi-directional connection between the browser and the server. Data flows both ways. No polling. No refresh.

Tina4 treats WebSocket the same way it treats routing. Define a WebSocket handler the same way you define an HTTP route.

---

## 2. What WebSocket Is

HTTP is a conversation that ends. Request. Response. Connection closes. WebSocket is an open line. Persistent. Bi-directional. Low overhead. Real-time.

---

## 3. Router.websocket() -- WebSocket as a Route

```typescript
import { Router } from "tina4-nodejs";

Router.websocket("/ws/echo", async (connection, event, data) => {
    if (event === "message") {
        connection.send(`Echo: ${data}`);
    }
});
```

```bash
tina4 serve
```

```
  Tina4 Node.js v3.0.0
  HTTP server running at http://0.0.0.0:7148
  WebSocket server running at ws://0.0.0.0:7148
```

---

## 4. Connection Events

```typescript
import { Router } from "tina4-nodejs";

Router.websocket("/ws/chat", async (connection, event, data) => {
    switch (event) {
        case "open":
            console.log(`[Chat] New connection: ${connection.id}`);
            connection.send(JSON.stringify({
                type: "system",
                message: "Welcome to the chat!",
                your_id: connection.id
            }));
            break;

        case "message":
            const message = JSON.parse(data);
            console.log(`[Chat] ${connection.id}: ${message.text ?? data}`);
            connection.send(JSON.stringify({
                type: "message",
                from: connection.id,
                text: message.text ?? data,
                timestamp: new Date().toISOString()
            }));
            break;

        case "close":
            console.log(`[Chat] Disconnected: ${connection.id}`);
            break;
    }
});
```

---

## 5. Sending to a Single Client

```typescript
connection.send(JSON.stringify({ type: "pong", timestamp: new Date().toISOString() }));
```

---

## 6. Broadcasting to All Clients

```typescript
Router.websocket("/ws/announcements", async (connection, event, data) => {
    if (event === "open") {
        connection.broadcast(JSON.stringify({
            type: "system",
            message: "A new user joined",
            online_count: connection.connectionCount()
        }));
    }

    if (event === "message") {
        const message = JSON.parse(data);
        connection.broadcast(JSON.stringify({
            type: "announcement",
            from: connection.id,
            text: message.text ?? "",
            timestamp: new Date().toISOString()
        }));
    }

    if (event === "close") {
        connection.broadcast(JSON.stringify({
            type: "system",
            message: "A user left",
            online_count: connection.connectionCount()
        }));
    }
});
```

### Broadcast Excluding Sender

```typescript
connection.broadcast(JSON.stringify({ type: "message", text: message.text }), true);
```

---

## 7. Path-Scoped Isolation

```typescript
Router.websocket("/ws/chat/{room}", async (connection, event, data) => {
    const room = connection.params.room;

    if (event === "open") {
        connection.broadcast(JSON.stringify({
            type: "system",
            message: `Someone joined room ${room}`,
            room,
            online: connection.connectionCount()
        }));
    }

    if (event === "message") {
        const message = JSON.parse(data);
        connection.broadcast(JSON.stringify({
            type: "message",
            room,
            from: message.username ?? "Anonymous",
            text: message.text ?? "",
            timestamp: new Date().toISOString()
        }));
    }
});
```

Connect to different rooms:

```
ws://localhost:7148/ws/chat/general
ws://localhost:7148/ws/chat/dev-team
```

A broadcast in `/ws/chat/general` reaches only clients on that path. The rooms are walls.

---

## 8. Live Chat with Typing Indicators

```typescript
import { Router } from "tina4-nodejs";

const chatUsers: Record<string, { id: string; username: string; room: string }> = {};

Router.websocket("/ws/livechat/{room}", async (connection, event, data) => {
    const room = connection.params.room;

    if (event === "open") {
        chatUsers[connection.id] = { id: connection.id, username: "Anonymous", room };

        connection.send(JSON.stringify({
            type: "welcome",
            message: `Connected to room: ${room}`,
            your_id: connection.id,
            online: connection.connectionCount()
        }));
    }

    if (event === "message") {
        const message = JSON.parse(data);
        const type = message.type ?? "message";

        if (type === "set-username") {
            const oldName = chatUsers[connection.id].username;
            chatUsers[connection.id].username = message.username;
            connection.broadcast(JSON.stringify({
                type: "system",
                message: `${oldName} is now known as ${message.username}`
            }));
        }

        if (type === "message") {
            const username = chatUsers[connection.id].username;
            connection.broadcast(JSON.stringify({
                type: "message",
                from: username,
                text: message.text ?? "",
                timestamp: new Date().toISOString()
            }));
        }

        if (type === "typing") {
            connection.broadcast(JSON.stringify({
                type: "typing",
                username: chatUsers[connection.id].username
            }), true);
        }
    }

    if (event === "close") {
        const username = chatUsers[connection.id]?.username ?? "Unknown";
        delete chatUsers[connection.id];

        connection.broadcast(JSON.stringify({
            type: "system",
            message: `${username} left the chat`,
            online: connection.connectionCount()
        }));
    }
});
```

---

## 9. Live Notifications via HTTP

```typescript
Router.post("/api/orders/{orderId:int}/ship", async (req, res) => {
    const orderId = req.params.orderId;
    const userId = req.body.user_id ?? 0;

    Router.pushToWebSocket(`/ws/notifications/${userId}`, JSON.stringify({
        type: "notification",
        title: "Order Shipped",
        message: `Your order #${orderId} has been shipped!`,
        timestamp: new Date().toISOString()
    }));

    return res.json({ message: "Order shipped, user notified" });
});
```

---

## 10. Connecting from JavaScript

```html
<script src="/js/frond.js"></script>
<script>
    const ws = frond.ws("/ws/chat/general");

    ws.on("open", function () {
        console.log("Connected");
    });

    ws.on("message", function (data) {
        const message = JSON.parse(data);
        console.log("Received:", message);
    });

    function sendMessage(text) {
        ws.send(JSON.stringify({ type: "message", text }));
    }
</script>
```

### Auto-Reconnect

```javascript
const ws = frond.ws("/ws/notifications/42", {
    reconnect: true,
    reconnectInterval: 3000,
    maxReconnectAttempts: 10
});
```

---

## 11. Exercise: Build a Real-Time Chat Room

Build a WebSocket chat at `/ws/room/{roomName}` with usernames, join/leave messages, and an HTML page at `GET /room/{roomName}`.

---

## 12. Solution

Create `src/routes/chat-room.ts`:

```typescript
import { Router } from "tina4-nodejs";

const roomUsers: Record<string, string> = {};

Router.websocket("/ws/room/{roomName}", async (connection, event, data) => {
    const room = connection.params.roomName;
    const key = `${room}:${connection.id}`;

    if (event === "open") {
        roomUsers[key] = "Anonymous";
        connection.send(JSON.stringify({ type: "system", message: `Welcome to room: ${room}`, online: connection.connectionCount() }));
        connection.broadcast(JSON.stringify({ type: "system", message: "A new user joined", online: connection.connectionCount() }), true);
    }

    if (event === "message") {
        const msg = JSON.parse(data);

        if (msg.type === "set-name") {
            const oldName = roomUsers[key];
            roomUsers[key] = msg.name ?? "Anonymous";
            connection.broadcast(JSON.stringify({ type: "system", message: `${oldName} changed their name to ${roomUsers[key]}` }));
        }

        if (msg.type === "chat") {
            connection.broadcast(JSON.stringify({ type: "chat", from: roomUsers[key], text: msg.text ?? "", timestamp: new Date().toTimeString().substring(0, 8) }));
        }
    }

    if (event === "close") {
        const username = roomUsers[key] ?? "Anonymous";
        delete roomUsers[key];
        connection.broadcast(JSON.stringify({ type: "system", message: `${username} left the room`, online: connection.connectionCount() }));
    }
});

Router.get("/room/{roomName}", async (req, res) => {
    return res.html("room.html", { room: req.params.roomName });
});
```

---

## 13. Gotchas

### 1. WebSocket Needs a Persistent Server

**Fix:** Use `tina4 serve` or `npx tsx app.ts`. Configure Nginx for WebSocket proxying.

### 2. Messages Are Strings, Not Objects

**Fix:** Always `JSON.parse(data)` on receive, `JSON.stringify()` on send.

### 3. Connection Count Is Per-Path

**Fix:** By design. Each path is an isolated group.

### 4. Broadcasting Does Not Scale Across Servers

**Fix:** Use Redis pub/sub to relay messages across server instances.

### 5. Large Messages Cause Disconnects

**Fix:** Keep messages under 64KB. Use HTTP for bulk data.

### 6. Memory Leak from Tracking Users

**Fix:** Always clean up in the `close` handler.

### 7. No Authentication on WebSocket

**Fix:** Pass token as query parameter and validate in the `open` handler.
