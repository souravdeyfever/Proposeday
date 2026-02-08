import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Valentine Proposal 💖", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .main { padding: 0 !important; }
        .block-container { padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  width: 100%;
  height: 100%;
  text-align: center;
  font-family: 'Arial';
  background: linear-gradient(135deg, #ffe6f2 0%, #ffcceb 100%);
  overflow: hidden;
}

.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  color: #ff3366;
  font-size: 60px;
  margin-bottom: 50px;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

button {
  font-size: 32px;
  padding: 20px 50px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  margin: 20px 30px;
  transition: transform 0.2s;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

button:hover {
  transform: scale(1.1);
}

#yes {
  background: linear-gradient(135deg, #ff3366, #ff1744);
  color: white;
  font-weight: bold;
}

#no {
  background: #666;
  color: white;
  position: fixed;
}

#result {
  color: #ff3366;
  font-size: 48px;
  margin-top: 50px;
  font-weight: bold;
}

.footer {
  position: fixed;
  bottom: 20px;
  right: 25px;
  font-size: 25px;
  color: #ff3366;
}

.footer a {
  color: #ff3366;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.3s;
}

.footer a:hover {
  opacity: 0.7;
  text-decoration: underline;
}

</style>
</head>

<body>

<div class="container">
  <h1>💖 Will you be my Valentine? 💖</h1>
  
  <div style="display: flex; justify-content: center; align-items: center;">
    <button id="yes" onclick="sayYes()">YES 💕</button>
    <button id="no" onmouseover="runAway()">NO 😒</button>
  </div>

  <h2 id="result"></h2>
</div>

<div class="footer">
  Created by <a href="https://sites.google.com/view/souravdey" target="_blank">@sourav</a>
</div>

<audio id="bgm" autoplay loop>
  <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
</audio>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<script>
function sayYes(){
  document.getElementById("result").innerHTML = "Yay! I knew it! 🥰💐";
  confetti({shapes:['heart'], particleCount:200, spread:180, duration:3000});
}

function runAway(){
  var noBtn = document.getElementById("no");

  var x = Math.random() * (window.innerWidth - 200);
  var y = Math.random() * (window.innerHeight - 200);

  noBtn.style.left = x + "px";
  noBtn.style.top = y + "px";

  confetti({shapes:['heart'], particleCount:20, spread:120});
}
</script>

</body>
</html>
"""

components.html(html_code, height=1200, scrolling=False)
