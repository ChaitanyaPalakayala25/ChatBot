css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: Cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.navitastech.com/assets/images/bg/bot.png" style="max-height: 30px; max-width: 30px; border-radius: 50%; object-fit: Cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.navitastech.com/assets/images/bg/emblem.png"style="max-height: 30px; max-width: 30px; border-radius: 50%; object-fit: Cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''