import { useState } from 'react'
import FileUpload from './components/FileUpload'
import QueryBox from './components/QueryBox'
import Answer from './components/Answer'
import './App.css'

function App() {
  const [answer, setAnswer] = useState('')

  return (
    <div className="app">
      <header className="app-header">
        <div className="app-logo">🔍</div>
        <h1 className="app-title">DocQuery</h1>
        <p className="app-subtitle">Upload documents and ask questions about them.</p>
      </header>
      <FileUpload />
      <QueryBox onAnswer={setAnswer} />
      <Answer answer={answer} />
    </div>
  )
}

export default App
