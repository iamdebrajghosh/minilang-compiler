import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState(`let x = 5;\nlet y = x + 2;\nprint y;`);
  const [output, setOutput] = useState('');

  const compileCode = async () => {
    try {
      const response = await axios.post('https://github.com/yourusername/minilang-backend.git/', { code: input });
      setOutput(response.data.js_code);
    } catch (error) {
      setOutput('Error compiling code.');
    }
  };

  return (
    <div className="App">
      <h2>MiniLang Online Compiler</h2>
      <textarea
        rows={10}
        cols={60}
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <br />
      <button onClick={compileCode}>Compile</button>
      <h3>Output JavaScript Code:</h3>
      <pre>{output}</pre>
    </div>
  );
}

export default App;