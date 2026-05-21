console.log("Script loaded successfully!");
const form = document.getElementById("predictionForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    // Collect form data
    const data = {

        age: parseInt(document.getElementById("age").value),

        weight: parseFloat(document.getElementById("weight").value),

        height: parseFloat(document.getElementById("height").value),

        income_lpa: parseFloat(document.getElementById("income_lpa").value),

        smoker: document.getElementById("smoker").value === "true",

        city: document.getElementById("city").value,

        occupation: document.getElementById("occupation").value
    };
    console.log("Form data collected:", data);

    const resultDiv = document.getElementById("result");

    // Loading state
    resultDiv.innerHTML = `
        <div class="result-box">
            <h2>Processing Prediction...</h2>
        </div>
    `;

    try {

        const response = await fetch("/api/predict", { // for local development, use "http://localhost:8000/api/predict"

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)
        });
        console.log("API response received:", response);
        const result = await response.json();

        console.log(result);

        // Extract API response
        const prediction = result.response.predicted_premium;

        const confidence = result.response.confidence_scores;

        // Dynamic HTML rendering
        resultDiv.innerHTML = `

            <div class="result-box">

                <h2>Insurance Premium Prediction</h2>

                <p class="prediction-text">
                    ${prediction}
                </p>

                <div class="confidence-section">

                    <h3>Confidence Scores</h3>

                    <div class="score">
                        <span>High</span>
                        <span>${(confidence.High * 100).toFixed(1)}%</span>
                    </div>

                    <div class="progress-bar">
                        <div class="progress-fill"
                             style="width:${confidence.High * 100}%">
                        </div>
                    </div>

                    <div class="score">
                        <span>Medium</span>
                        <span>${(confidence.Medium * 100).toFixed(1)}%</span>
                    </div>

                    <div class="progress-bar">
                        <div class="progress-fill"
                             style="width:${confidence.Medium * 100}%">
                        </div>
                    </div>

                    <div class="score">
                        <span>Low</span>
                        <span>${(confidence.Low * 100).toFixed(1)}%</span>
                    </div>

                    <div class="progress-bar">
                        <div class="progress-fill"
                             style="width:${confidence.Low * 100}%">
                        </div>
                    </div>

                </div>

            </div>
        `;

    } catch (error) {

        console.error(error);

        resultDiv.innerHTML = `

            <div class="error-box">

                <h2>Error</h2>

                <p>
                    Unable to connect to FastAPI backend.
                </p>

            </div>
        `;
    }
});

console.log("Execution reached end of script.js");