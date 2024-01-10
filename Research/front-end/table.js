var myArray = [
    {'name': 'John', 'age': 31, 'birthday': '1980-01-01'},
    {'name': 'Mary', 'age': 25, 'birthday': '1986-01-01'},
    {'name': 'Peter', 'age': 21, 'birthday': '1990-01-01'},
    {'name': 'Ann', 'age': 23, 'birthday': '1988-01-01'},
    {'name': 'Steve', 'age': 19, 'birthday': '1992-01-01'}
];

buildTable(myArray);

function buildTable(data){
    var table = document.querySelector('tbody');	

    for (var i = 0; i < data.length; i++){
        var row = `<tr>
                        <td>${data[i].name}</td>
                        <td>${data[i].age}</td>
                        <td>${data[i].birthday}</td>
                  </tr>`
        table.innerHTML += row
    }
}


