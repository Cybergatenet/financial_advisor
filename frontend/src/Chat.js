import React, { useState } from 'react';
import { Container, Paper, TextField, Button, List, ListItem, ListItemText, Box } from '@mui/material';
import { sendChat } from './api';

function Chat() {
  const [message, setMessage] = useState('');
  const [conversation, setConversation] = useState([]);

  const handleSend = async () => {
    if (!message.trim()) return;
    const userMsg = { role: 'user', text: message };
    setConversation([...conversation, userMsg]);
    try {
      const res = await sendChat(message);
      const botMsg = { role: 'bot', text: res.data.reply };
      setConversation(prev => [...prev, botMsg]);
    } catch (err) {
      console.error(err);
      setConversation(prev => [...prev, { role: 'bot', text: 'Sorry, I encountered an error.' }]);
    }
    setMessage('');
  };

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Paper sx={{ p: 3, height: '70vh', display: 'flex', flexDirection: 'column' }}>
        <Typography variant="h4" gutterBottom>Financial Chatbot</Typography>
        <Box sx={{ flexGrow: 1, overflow: 'auto', mb: 2 }}>
          <List>
            {conversation.map((msg, idx) => (
              <ListItem key={idx} sx={{ justifyContent: msg.role === 'user' ? 'flex-end' : 'flex-start' }}>
                <Paper sx={{ p: 1, bgcolor: msg.role === 'user' ? '#e3f2fd' : '#f5f5f5' }}>
                  <ListItemText primary={msg.text} />
                </Paper>
              </ListItem>
            ))}
          </List>
        </Box>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField fullWidth value={message} onChange={(e) => setMessage(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleSend()} />
          <Button variant="contained" onClick={handleSend}>Send</Button>
        </Box>
      </Paper>
    </Container>
  );
}

export default Chat;