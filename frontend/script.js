let data = null;
let index = 0;
let showingAnswer = false;

const title = document.getElementById("title");
const question = document.getElementById("question");
const answer = document.getElementById("answer");
const statusText = document.getElementById("status");

const pdfInput = document.getElementById("pdfInput");
const generateButton = document.getElementById("generate");
const flipButton = document.getElementById("flip");
const nextButton = document.getElementById("next");
const prevButton = document.getElementById("prev");

function showCard() {
  title.textContent = data.title;
  question.textContent = data.flashcards[index].question;
  answer.textContent = data.flashcards[index].answer;
  answer.style.display = "none";
  showingAnswer = false;
}

async function generateFlashcards() {
  const file = pdfInput.files[0];

  if (!file) {
    statusText.textContent = "Please select a PDF first";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  statusText.textContent = "Generating flashcards...";
  question.textContent = "Please wait";
  answer.textContent = "";
  title.textContent = "AI Study Partner";

  try {
    const response = await fetch("http://127.0.0.1:8000/generate-flashcards", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();

    if (result.error) {
      statusText.textContent = result.error;
      question.textContent = "Could not generate flashcards";
      answer.textContent = "";
      return;
    }

    data = result;
    index = 0;
    statusText.textContent = "Flashcards generated";
    showCard();
  } catch (error) {
    statusText.textContent = "Could not connect to backend";
    question.textContent = "Request failed";
    answer.textContent = "";
  }
}

generateButton.addEventListener("click", generateFlashcards);

flipButton.addEventListener("click", () => {
  if (!data) return;

  showingAnswer = !showingAnswer;
  answer.style.display = showingAnswer ? "block" : "none";
});

nextButton.addEventListener("click", () => {
  if (!data) return;

  index = (index + 1) % data.flashcards.length;
  showCard();
});

prevButton.addEventListener("click", () => {
  if (!data) return;

  index = (index - 1 + data.flashcards.length) % data.flashcards.length;
  showCard();
});
