document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('flamesForm');
    const resultContainer = document.getElementById('result');
    const resultTitle = document.getElementById('resultTitle');
    const resultMessage = document.getElementById('resultMessage');
    const resetBtn = document.getElementById('resetBtn');
    const calcBtn = document.getElementById('calcBtn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Button loading state
        const originalBtnText = calcBtn.querySelector('span').innerText;
        calcBtn.querySelector('span').innerText = 'Calculating...';
        calcBtn.disabled = true;

        const name1 = document.getElementById('name1').value;
        const name2 = document.getElementById('name2').value;

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name1, name2 }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            // Simulate a small delay for suspense
            setTimeout(() => {
                showResult(data.result, data.message);
                calcBtn.querySelector('span').innerText = originalBtnText;
                calcBtn.disabled = false;
            }, 800);

        } catch (error) {
            console.error('Error:', error);
            alert('Something went wrong. Please try again.');
            calcBtn.querySelector('span').innerText = originalBtnText;
            calcBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        resultContainer.classList.add('hidden');
        form.classList.remove('hidden'); // Ensure form is visible if we hid it
        form.reset();
        document.getElementById('name1').focus();
    });

    function showResult(result, message) {
        resultTitle.textContent = result;
        resultMessage.textContent = message;

        resultContainer.classList.remove('hidden');

        // Scroll to result if needed (on mobile)
        resultContainer.scrollIntoView({ behavior: 'smooth' });
    }
});
