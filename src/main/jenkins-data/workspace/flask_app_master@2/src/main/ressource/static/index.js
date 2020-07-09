// document.getElementById('date').innerHTML = new Date().toDateString();
// document.getElementById('getMethod').innerHTML = generatePage();
document.getElementById("getMethod").addEventListener("click", generatePage);
// document.getElementById("putMethod").addEventListener("click", closeWindowUpdate)

function getData(url) {
    var myInit = {
        method: 'GET'
    };
    return fetch(url, myInit)
        .then(async (response) => {
            var mountains = response.json()
            console.log('mountains:', mountains)
            return mountains
        }).then((value) => {
            return value;
        })
}

function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data) {
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTable(table, data) {
    for (let element of data) {
        let row = table.insertRow();
        for (key in element) {
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text);
        }
    }
}
function generatePage() {
    document.getElementById("myTable").innerHTML = ""
    document.getElementById('popupbox').style.top = "-3000px"
    document.getElementById('popupUpdate').style.top = "-3000px"
    document.getElementById('popupDel').style.top = "-3000px" 
    document.getElementById('popupBounding').style.top = "-3000px"
    url = 'http://127.0.0.1:5000/readAllTable'
    getData(url).then((value) => {
        let table = document.querySelector("table");
        let headers = Object.keys(value[0]);
        let data = value;
        generateTableHead(table, headers);
        generateTable(table, data);
    })
}

function openWindow() {
    document.getElementById("myTable").innerHTML = ""
    document.getElementById('popupbox').style.top = "30%"
    document.getElementById('popupUpdate').style.top = "-3000px" 
    document.getElementById('popupDel').style.top = "-3000px"
    document.getElementById('popupBounding').style.top = "-3000px"  




}

function closeWindow(){
    document.getElementById('popupbox').style.top = "-3000px"  
}


function openWindowToUpdate(){
    document.getElementById("myTable").innerHTML = ""
    document.getElementById('popupbox').style.top = "-3000px"
    document.getElementById('popupDel').style.top = "-3000px"
    document.getElementById('popupBounding').style.top = "-3000px"  
    document.getElementById('popupUpdate').style.top = "30%"
}

function closeWindowUpdate(){
    document.getElementById('popupUpdate').style.top = "-3000px"  
}

function openWindowToDel(){
    document.getElementById("myTable").innerHTML = ""
    document.getElementById('popupbox').style.top = "-3000px"
    document.getElementById('popupUpdate').style.top = "-3000px"
    document.getElementById('popupBounding').style.top = "-3000px"  
    document.getElementById('popupDel').style.top = "30%"
}

function closeWindowDel(){
    document.getElementById('popupDel').style.top = "-3000px"  
}

function openWindowBounding(){
    document.getElementById("myTable").innerHTML = ""
    document.getElementById('popupbox').style.top = "-3000px"
    document.getElementById('popupUpdate').style.top = "-3000px"
    document.getElementById('popupDel').style.top = "-3000px"  
    document.getElementById('popupBounding').style.top = "30%"
}

function closeWindowBounding(){
    document.getElementById('popupBounding').style.top = "-3000px"  
}
var boundingValues = new Object();
boundingValues.minLat = 0
boundingValues.minLon = 0
boundingValues.maxLat = 0
boundingValues.maxLon = 0
var postValues = new Object();
postValues.lat = 0
postValues.lon = 0
postValues.altitude = 0
postValues.name = 0
var UpdateValues = new Object();
UpdateValues.id = ''
UpdateValues.lat = 0
UpdateValues.lon = 0
UpdateValues.altitude = 0
UpdateValues.name = 0
var deleteValues = new Object();
deleteValues.id = 0

function sendDataToApi() {
    if(document.getElementById('popupBounding').style.top == "30%") {
        boundingValues.minLat = document.getElementById("min_lat").value
        boundingValues.minLon = document.getElementById("min_lon").value
        boundingValues.maxLat = document.getElementById("max_lat").value
        boundingValues.maxLon = document.getElementById("max_lon").value
        let url = new URL('http://127.0.0.1:5000/readAllTable')
        url.search = new URLSearchParams({
            minLat:boundingValues.minLat,
            minLon:boundingValues.minLon,
            maxLat:boundingValues.maxLat,
            maxLon:boundingValues.maxLon
        })
        if (boundingValues.minLat == '' && boundingValues.minLon == '' && boundingValues.maxLat == '' && boundingValues.maxLon == '') {
            alert('please fill ALL fields')
        }
        else {
            getData(url).then((value) => {
                if (value.length) {
                    document.getElementById('popupBounding').style.top = "-3000px"
                    let table = document.querySelector("table");
                    let headers = Object.keys(value[0]);
                    let data = value;
                    generateTableHead(table, headers);
                    generateTable(table, data);
                } 
                else {
                    document.getElementById('popupBounding').style.top = "-3000px" 
                    alert("There is no data!")
                }
            })
        }
    }

    else if (document.getElementById('popupUpdate').style.top == "30%") {

        var UpdateValuesWithoutNull = new Object();
         if (document.getElementById("identForUpdate").value.length) UpdateValuesWithoutNull.id= document.getElementById("identForUpdate").value 
        if (document.getElementById("latForUpdate").value) UpdateValuesWithoutNull.lat = document.getElementById("latForUpdate").value 
        if (document.getElementById("lonForUpdate").value) UpdateValuesWithoutNull.lon = document.getElementById("lonForUpdate").value 
        if (document.getElementById("altForUpdate").value) UpdateValuesWithoutNull.altitude = document.getElementById("altForUpdate").value 
        if (document.getElementById("nameForUpdate").value) UpdateValuesWithoutNull.name = document.getElementById("nameForUpdate").value 

    
        let url = 'http://127.0.0.1:5000/readAllTable'
        let newInit = {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(UpdateValuesWithoutNull)
        };
        console.log('newInit:', newInit)
        return fetch(url, newInit)
        .then(response => {
            status = response.status 
            texteError = response.statusText
            res = response.text()
            .then((res) => {
                status == 200 ? alert(res) : alert("Erreur " + status + ": " + texteError)
                
                return res
            })
        })
        
    
    }
    else if (document.getElementById('popupbox').style.top == "30%") {
        var postValuesWithoutNull = new Object();
        postValuesWithoutNull.lat = document.getElementById("latForPost").value 
        postValuesWithoutNull.lon = document.getElementById("lonForPost").value 
        postValuesWithoutNull.altitude = document.getElementById("altForPost").value 
        postValuesWithoutNull.name = document.getElementById("nameForPost").value 


        let url = 'http://127.0.0.1:5000/readAllTable'
        let newInit = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(postValuesWithoutNull)
        };
        console.log('postValuesWithoutNull:', postValuesWithoutNull)
        return fetch(url, newInit)
        .then(response => {
            status = response.status 
            texteError = response.statusText
            res = response.text()
            .then((res) => {
                status == 200 ? alert(res) : alert("Erreur " + status + ": " + texteError)
                return res
            })
        })
    }
    else if (document.getElementById('popupDel').style.top == "30%") {
        deleteValues.id = document.getElementById("identForDel").value
        let url = 'http://127.0.0.1:5000/readAllTable'
        let newInit = {
            method: 'DELETE',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(deleteValues),
        };
        console.log('newInit:', newInit)
        return fetch(url, newInit)
        .then(response => {
            status = response.status 
            texteError = response.statusText
            res = response.text()
            // alert("Erreur " + response.status + ": " + response.statusText)
            .then((res) => {
                status == 200 ? alert(res) : alert("Erreur " + status + ": " + texteError)
                return res
            })
        })
    }
}


// generatePage()
