
var graph_params = {
        title: "Thesis Progress",
        target: '#chart',
        width: 1000,
        height: 600,
        right: 100,
        x_accessor: "date",
        y_accessor: "count",
        missing_text: "No data",
        show_missing_background: true
};

function drawGraph(data) {
    var labels = [];
    var graph_data = [];
    data.forEach(function (el) {
        labels.push(el.username);
        graph_data.push(el.counts);
    });
    for (var i=0; i < graph_data.length; i++) {
       graph_data[i] = MG.convert.date(graph_data[i], "date");
    }
    graph_params.data = graph_data;
    graph_params.legend = labels;
    delete graph_params.xax_format;

    MG.data_graphic(graph_params);


}

function rangeChangedHandler(event) {
    console.log(this.value);
    fetchDataAndDraw(this.value);
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("foo");
    document.querySelectorAll('input[name="range"]').forEach(function(el) {
        console.log(el);
        el.onchange=rangeChangedHandler;
    });
    fetchDataAndDraw("all");

}, false);

function fetchDataAndDraw(range) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'graphs/api/users/?date_range=' + range);
    xhr.responseType = "json";
    xhr.onload = function () {
        if (xhr.status == 200) {
            console.log(xhr.response);
            drawGraph(xhr.response);
        } else {
            console.error("XHR error: " + xhr.status);
        }
    };
    xhr.send();
}