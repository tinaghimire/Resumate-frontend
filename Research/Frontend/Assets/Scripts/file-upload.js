document.addEventListener("DOMContentLoaded", function() {
    // Get the slider and value span elements
    const slider1 = document.getElementById('education');
    const slider2 = document.getElementById('skills');
    const slider3 = document.getElementById('experience');
    const slider4 = document.getElementById('language'); 
    const sliderValue1 = document.getElementById('value1');
    const sliderValue2 = document.getElementById('value2');
    const sliderValue3 = document.getElementById('value3');
    const sliderValue4 = document.getElementById('value4');
    const errorMessage = document.getElementById('error-message');
    const submitButton = document.getElementById('submit');


    // Function to update the value display
    // Function to update the value display for each slider
    function updateSliderValue(slider, sliderValue) {
        // Get the current value of the slider
        const value = slider.value;
        // Update the value displayed in the HTML
        sliderValue.textContent = value;
    }

    // Function to calculate the sum of slider values
    function calculateSum() {
        const sum = parseInt(slider1.value) + parseInt(slider2.value) + parseInt(slider3.value) + parseInt(slider4.value);
        return sum;
    }

    // Function to check if sum is equal to 100
    function checkSum() {
        const sum = calculateSum();
        if (sum === 100) {
            errorMessage.textContent = "";
            const url = "http://127.0.0.1:5500/Project/Research/Frontend/login.html";
            console.log("Form submitted!");
            window.location.href = url;
        } else {
            errorMessage.textContent = "The sum of values must be 100";
        }
    }

    // Add event listeners to each slider for input event
    slider1.addEventListener('input', function() {
        // When the slider value changes, call the updateSliderValue function
        updateSliderValue(slider1, sliderValue1);
    });

    slider2.addEventListener('input', function() {
        updateSliderValue(slider2, sliderValue2);
    });

    slider3.addEventListener('input', function() {
        updateSliderValue(slider3, sliderValue3);
    });

    slider4.addEventListener('input', function() {
        updateSliderValue(slider4, sliderValue4);
    });

    // Call the updateSliderValue function initially to display the default values
    updateSliderValue(slider1, sliderValue1);
    updateSliderValue(slider2, sliderValue2);
    updateSliderValue(slider3, sliderValue3);
    updateSliderValue(slider4, sliderValue4);

    // Add event listener to the submit button
    submitButton.addEventListener('click', function() {
        checkSum();
    });
});
