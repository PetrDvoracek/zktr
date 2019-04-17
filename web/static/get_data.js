var url = "https://jsonplaceholder.typicode.com/posts"

function get_data(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        var data = JSON.parse(xhttp.responseText)
        return data;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

