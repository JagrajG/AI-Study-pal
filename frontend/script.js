const title = document.getElementById("title");
const question = document.getElementById("question");
const answer = document.getElementById("answer");
const flipButton = document.getElementById("flip");
const nextButton = document.getElementById("next");
const prevButton = document.getElementById("prev");

const data = {
  title: "Astronomy Concepts",
  flashcards: [
    {
      question: "What is redshift?",
      answer:
        "Redshift happens when light from an object is stretched as it moves away from us.",
    },
    {
      question: "What is the main sequence?",
      answer:
        "The main sequence is where stars fuse hydrogen into helium in their cores.",
    },
  ],
};

let index = 0;
let showingAnswer = false;

function showCard() {
  title.textContent = data.title;
  question.textContent = data.flashcards[index].question;
  answer.textContent = data.flashcards[index].answer;
  answer.style.display = "none";
  showingAnswer = false;
}

flipButton.addEventListener("click", () => {
  showingAnswer = !showingAnswer;
  answer.style.display = showingAnswer ? "block" : "none";
});

nextButton.addEventListener("click", () => {
  index = (index + 1) % data.flashcards.length;
  showCard();
});

prevButton.addEventListener("click", () => {
  index = (index - 1 + data.flashcards.length) % data.flashcards.length;
  showCard();
});

showCard();
