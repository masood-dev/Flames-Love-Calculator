document.addEventListener('DOMContentLoaded', () => {
    const flamesForm = document.getElementById('flamesForm');
    if (flamesForm) {
        const resultContainer = document.getElementById('result');
        const resultTitle = document.getElementById('resultTitle');
        const resultMessage = document.getElementById('resultMessage');
        const resetBtn = document.getElementById('resetBtn');
        const calcBtn = document.getElementById('calcBtn');

        flamesForm.addEventListener('submit', async (e) => {
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
                    showFlamesResult(data.result, data.message);
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
            flamesForm.classList.remove('hidden');
            flamesForm.reset();
            document.getElementById('name1').focus();
        });

        function showFlamesResult(result, message) {
            resultTitle.textContent = result;
            resultMessage.textContent = message;

            resultContainer.classList.remove('hidden');

            // Scroll to result if needed (on mobile)
            resultContainer.scrollIntoView({ behavior: 'smooth' });
        }
    }

    const zodiacForm = document.getElementById('zodiacForm');
    if (zodiacForm) {
        const zodiacResult = document.getElementById('zodiacResult');
        const zodiacBtn = document.getElementById('zodiacBtn');
        const zodiacReset = document.getElementById('zodiacReset');
        const swapSigns = document.getElementById('swapSigns');
        const sign1Field = document.getElementById('sign1');
        const sign2Field = document.getElementById('sign2');
        const sign1Label = document.getElementById('sign1Label');
        const sign2Label = document.getElementById('sign2Label');
        const zodiacScore = document.getElementById('zodiacScore');
        const zodiacVibe = document.getElementById('zodiacVibe');
        const zodiacInsight = document.getElementById('zodiacInsight');
        const scoreCircle = document.getElementById('scoreCircle');

        zodiacForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const originalBtnText = zodiacBtn.querySelector('span').innerText;
            zodiacBtn.querySelector('span').innerText = 'Reading Stars...';
            zodiacBtn.disabled = true;

            try {
                const response = await fetch('/zodiac-check', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        sign1: sign1Field.value,
                        sign2: sign2Field.value
                    }),
                });

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();

                setTimeout(() => {
                    showZodiacResult(data);
                    zodiacBtn.querySelector('span').innerText = originalBtnText;
                    zodiacBtn.disabled = false;
                }, 700);
            } catch (error) {
                console.error('Error:', error);
                alert('Something went wrong. Please try again.');
                zodiacBtn.querySelector('span').innerText = originalBtnText;
                zodiacBtn.disabled = false;
            }
        });

        swapSigns.addEventListener('click', () => {
            const currentSign1 = sign1Field.value;
            sign1Field.value = sign2Field.value;
            sign2Field.value = currentSign1;
        });

        zodiacReset.addEventListener('click', () => {
            zodiacResult.classList.add('hidden');
            zodiacForm.classList.remove('hidden');
            zodiacForm.reset();
            sign1Field.focus();
        });

        function showZodiacResult(data) {
            sign1Label.textContent = `${data.sign1} · ${data.element1}`;
            sign2Label.textContent = `${data.sign2} · ${data.element2}`;
            zodiacScore.textContent = `${data.score}%`;
            zodiacVibe.textContent = data.vibe;
            zodiacInsight.textContent = data.insight;
            scoreCircle.style.setProperty('--score', data.score);

            zodiacResult.classList.remove('hidden');
            zodiacResult.scrollIntoView({ behavior: 'smooth' });
        }
    }
});
