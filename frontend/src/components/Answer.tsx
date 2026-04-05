interface Props {
  answer: string
}

function Answer({ answer }: Props) {
  if (!answer) return null

  return (
    <div className="card">
      <div className="card-heading">
        <span className="card-heading-icon">✨</span>
        Answer
      </div>
      <p className="answer-text">{answer}</p>
    </div>
  )
}

export default Answer
