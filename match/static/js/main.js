const submitBtn = document.querySelector('#submit-btn')

submitBtn.addEventListener(('click'), (e) => {
    e.preventDefault()
    console.log('hello')
    // Collect user inputs
    // var experience = document.getElementById("experience").value;
    // var skills = document.getElementById("skills").value;
    // var age = document.getElementById("age").value;
    // var qualifications = document.getElementById("qualifications").value;
    // var salary = document.getElementById("salary").value;
    // var role = document.getElementById("role").value;
    // var country = document.getElementById("country").value;

    // Send data to the server for processing
    fetch('http://127.0.0.1:8000/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
        body: new URLSearchParams({ 
            // experience: experience, 
            // skills: skills, 
            // age: age,
            // qualifications: qualifications,
            // salary: salary,
            // role: role,
            // country: country,
            skills: 'hello world'
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display result to the user
        console.log(data)
    })
    .catch(error => console.error('Error:', error));})
