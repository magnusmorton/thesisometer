
function drawGraph(data) {
    counts = data[0].counts;
    MG.convert.date(counts, "date");

    MG.data_graphic({
        title: "Thesis Progress",
        data:counts,
        target: '#chart',
        width: 600,
        height: 400,
        right: 40,
        x_accessor: "date",
        y_accessor: "count"
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
