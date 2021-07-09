const ws = new WebSocket('ws://localhost/ws/msg')

ws.onmessage = function(e){
    const data = JSON.parse(e.data);
    listMsg(data.name,data.date,data.view);
};

function listMsg(nam,date,view){
    var data_list = document.getElementById("data_box")
    var data = document.createElement("p");

    msg = nam + " update its views to " + view + " at " + date;
    data.innerHTML = msg;
    data_list.appendChild(data);
    data_list.scrollTop = data_list.scrollHeight;

}; 