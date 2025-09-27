import React, { useState } from 'react';


function ChatBox() {
const [messages, setMessages] = useState([]);
const [input, setInput] = useState("");


const sendMessage = () => {
if (input.trim() === "") return;
setMessages([...messages, { sender: "user", text: input }]);
setInput("");
};


return (
<div className="chat-container">
<div className="messages">
{messages.map((msg, idx) => (
<div key={idx} className={msg.sender}>{msg.text}</div>
))}
</div>
<input
type="text"
value={input}
onChange={(e) => setInput(e.target.value)}
placeholder="Ask a question..."
/>
<button onClick={sendMessage}>Send</button>
</div>
);
}


export default ChatBox;