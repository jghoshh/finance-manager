document.addEventListener('DOMContentLoaded', function getData(){

    let title = null;
    let graphHolder = document.querySelector('#graphHolder');
    const dateCode = window.location.href.slice(-5);

    if (dateCode === "L0007"){
        title = "Last 7 days";
      }
      else if (dateCode === "1YEAR"){
          title = "Last Year";
      }
      else if (dateCode === "6MTHS"){
        title = "Last 6 Months";
    }
    else if (dateCode === "3MTHS"){
        title = "Last 3 Months";
    }

    fetch(`/dev-expense-summary/${dateCode}`)
    .then(res => res.json())
    .then(res => {
        const [labels, data] = [Object.keys(res), Object.values(res)];
        getChart(labels, data, title);
    })

});

function getChart(labels, data, title) {

    const ctx = document.getElementById('summary-chart');
    const isAllZero = data.every(item => item === 0);

    if (isAllZero){
        const nothingTxt = document.createElement('h2');
        nothingTxt.innerHTML = "No expenses to summarize.";
        graphHolder.appendChild(nothingTxt);
    }
  
    else if (title !== null) {
      new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: labels,
            datasets: [{
              data: data,
              borderWidth: 1,
              backgroundColor: [
                  "#4BC0C0",
                  "#FF6384",
                  "#36A2EB",
                  "#FFCD56",
                  "#FF9F40",
              ]
            }]
          },
          options: {
              color: '#ffff',
          }
        });
      }
    }
