# ==============================
# frontend/src/App.js (React Boilerplate)
# ==============================


import React from 'react';
import ChatBox from './components/chatBox';
import Upload from './components/Upload';
import './styles.css';


function App() {
return (
<div className="app-container">
<h1>AI Document Q&A Chatbot</h1>
<Upload />
<ChatBox />
</div>
);
}


export default App;