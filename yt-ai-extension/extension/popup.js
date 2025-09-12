document.getElementById("askBtn").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const videoUrl = tab.url;
  const question = document.getElementById("question").value;

  document.getElementById("answer").innerText = "🔄 Asking...";

  try {
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        video_url: videoUrl,
        question: question
      })
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer || "❌ No answer received.";
  } catch (err) {
    console.error("Error:", err);
    document.getElementById("answer").innerText = "❌ Failed to connect to backend.";
  }
});
