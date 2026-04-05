import { useState } from "react";

interface Props {
  onAnswer: (answer: string) => void;
}

function QueryBox({ onAnswer }: Props) {
  const [query, setQuery] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query }),
    });
    const claudeResponse = await response.json();
    console.log("Querying:", query);
    console.log(claudeResponse);
    onAnswer(claudeResponse.message);
  }

  return (
    <div className="card">
      <div className="card-heading">
        <span className="card-heading-icon">💬</span>
        Ask a Question
      </div>
      <form onSubmit={handleSubmit}>
        <textarea
          className="query-textarea"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question about your documents..."
          rows={4}
        />
        <button className="btn" type="submit" disabled={query.trim() === ""}>
          Ask
        </button>
      </form>
    </div>
  );
}

export default QueryBox;
