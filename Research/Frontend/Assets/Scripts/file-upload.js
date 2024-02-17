document.addEventListener("DOMContentLoaded", function() {
    const sliders = document.querySelectorAll('.slider');
    const values = document.querySelectorAll('.value');
    const submitButton = document.querySelector('.submit')
    const errorMessage = document.getElementById('form-error-message');
    
    sliders.forEach((slider, index) => {
        slider.addEventListener('input', function() {

            // Calculate the remaining sum
            const currentSum = Array.from(sliders).reduce((sum, s, i) => (i !== index ? sum + parseInt(s.value, 10): sum), 0);

            // Update the max values of all sliders to ensure the total sum is 100
            const remainingMax = 100 - currentSum;
            sliders.forEach(s => (s.max = remainingMax));

            // Update the displayed value
            values[index].textContent = this.value;

            // Prevent the user from sliding the sliders beyond their updated maximum values
            // if (parseInt(this.value) > remainingMax) {
            //     this.value = remainingMax;
            //     values[index].textContent = remainingMax;
            // }

            if (currentSum === 100) {
                submitButton.disabled = false;
                errorMessage.textContent = "";
            } else {
                submitButton.disabled = true;
                errorMessage.textContent = "The sum should be 100"
            }
        });
    });
});