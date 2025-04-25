function showPopup() {
	alert("Please say a number only.");
	startListening(); //Called after alert
};

function startListening() {
	const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

	if (!SpeechRecognition) {
		alert("Speech recognition not supported in this browser.");
		return;
	}

	const recognition = new SpeechRecognition();
	recognition.lang = 'en-US';
	recognition.start();

	recognition.onresult = function (event) {
		let transcript = event.results[0][0].transcript.toLowerCase().trim();
		console.log("Transcript:", transcript);
		transcript = transcript.replace(/[.,!?]/g, '');

		//We need to add these conversions because the microphone is not interpretting numbers below 10 as numbers.
		const wordToNumber = {
			"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
		};
		
		let number = parseInt(transcript);

		if (isNaN(number)) {
			//Try hearing a matching number word
			const words = transcript.split(" ");
			for (let word of words) {
				if (wordToNumber.hasOwnProperty(word)) {
					number = wordToNumber[word];
					break;
				}
			}
		}
		if (!isNaN(number)) {
			document.getElementById("dog_age").value = number;
		}
		else {
			alert("Please say only a whole number.");
			document.getElementById("dog_age").value = '';
		}
		
	};

	recognition.onerror = function (event) {
		alert("Error: " + event.error);
	};
	
}

//Clear button will show only when the text is displayed, then disappears with the text once it is clicked
function clearResult() {
	const resultContainer = document.getElementById("result-container");
	if (resultContainer) {
		resultContainer.style.display = "none";
	}
}