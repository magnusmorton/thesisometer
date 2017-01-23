
function drawGraph(data) {
    var labels = [];
    var graph_data = [];
    data.forEach(function (el) {
        console.log(el);
        labels.push(el.username);
        graph_data.push(el.counts);
    });
    for (var i=0; i < graph_data.length; i++) {
       graph_data[i] = MG.convert.date(graph_data[i], "date");
    }

    MG.data_graphic({
        title: "Thesis Progress",
        data:graph_data,
        target: '#chart',
        width: 800,
        height: 600,
        right: 100,
        x_accessor: "date",
        y_accessor: "count",
        missing_text: "No data",
        show_missing_background: true,
        legend: labels
    });


}

var xhr = new XMLHttpRequest();
xhr.open('GET', 'graphs/api/users/');
xhr.responseType = "json";
xhr.onload = function() {
    if (xhr.status == 200) {
        console.log(xhr.response);
        drawGraph(xhr.response);
    } else {
        console.error("XHR error: " + xhr.status);
    }
};
xhr.send();
