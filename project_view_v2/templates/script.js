const ws = new WebSocket('ws://localhost/ws/msg')

ws.onmessage = function(e){
    const data = JSON.parse(e.data)
}