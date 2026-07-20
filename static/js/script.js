const chatWindow = document.getElementById('chatWindow');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const clearBtn = document.getElementById('clearBtn');

// auto-grow textarea
messageInput.addEventListener('input', () => {
  messageInput.style.height = 'auto';
  messageInput.style.height = Math.min(messageInput.scrollHeight, 140) + 'px';
});

// enter to send, shift+enter for newline
messageInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    chatForm.requestSubmit();
  }
});

function addMessage(text, role) {
  const msg = document.createElement('div');
  msg.className = `msg ${role}`;
  msg.innerHTML = `
    <div class="avatar">${role === 'user' ? 'You' : 'AT'}</div>
    <div class="bubble"></div>
  `;
  msg.querySelector('.bubble').textContent = text;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  return msg;
}

function addTyping() {
  const msg = document.createElement('div');
  msg.className = 'msg bot typing';
  msg.innerHTML = `
    <div class="avatar">AT</div>
    <div class="bubble"><span></span><span></span><span></span></div>
  `;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
  return msg;
}

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const text = messageInput.value.trim();
  if (!text) return;

  addMessage(text, 'user');
  messageInput.value = '';
  messageInput.style.height = 'auto';
  sendBtn.disabled = true;

  const typingEl = addTyping();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    if (!res.ok) throw new Error('Request failed');
    const data = await res.json();

    typingEl.remove();
    addMessage(data.reply, 'bot');
  } catch (err) {
    typingEl.remove();
    addMessage('Something went wrong. Please try again.', 'bot');
    console.error(err);
  } finally {
    sendBtn.disabled = false;
    messageInput.focus();
  }
});

clearBtn.addEventListener('click', async () => {
  if (!confirm('Clear the whole conversation?')) return;
  try {
    await fetch('/clear', { method: 'POST' });
  } catch (err) {
    console.error(err);
  }
  chatWindow.innerHTML = '';
  addMessage("Hi! I'm your AI Assist Tutor. Ask me anything and I'll break it down simply, with examples.", 'bot');
});