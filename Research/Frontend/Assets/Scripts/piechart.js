const ctx = document.getElementById('pieChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'pie',

    data: {
        labels: ['React', 'Angular', 'Vue'],
        datasets: [{
            label: 'Front-end Frameworks',
            data: [10, 7, 3],
            backgroundColor: [
                'red',
                'yellow',
                'pink'
            ],

            // border:
            // borderColor: [
            //     'rgba(255, 99, 132, 1)',
            //     'rgba(0, 255, 0, 1)',
            //     'rgba(0, 0, 255, 1)'
            // ],
        }]
    },

    options: {
        title: {   
            display: true,
            text: 'Front-end Frameworks'
        }, 

        Response: true,

        data: {
            display: true,
            position: 'bottom'
        }
    }
});