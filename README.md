# 🤝TrustTalk 

TrustTalk is a two-bot system designed for **anonymous communication on Telegram**. It enables people to ask questions, share thoughts, or send confessions safely without revealing their identity.

This project was created to make anonymous interaction more accessible, structured, and transparent by using **two specialized bots** that work together:

1. **Confess Bot** – Handles anonymous submissions from users.
2. **Helper Bot** – Acts as an admin/moderator tool, forwarding anonymous messages and ensuring the flow stays secure and organized.

Together, these bots allow users to send confessions while giving admins the ability to receive, moderate, and respond in a controlled way.

---

## 🔍 Why Two Bots?

Instead of packing everything into a single bot, the system was designed with **separation of roles** for clarity and reliability:

* **Confess Bot**

  * Collects user confessions/questions.
  * Ensures messages remain anonymous.
  * Passes messages securely to the Helper Bot.

* **Helper Bot**

  * Receives confessions from the Confess Bot.
  * Handles responses and moderation.
  * Connects with a Telegram channel/group where messages can be shared publicly (if required).

This separation ensures better **security**, **scalability**, and **simplified management** of anonymous interactions.

---

## ⚙️ How It Works (Flow)

1. A user opens **Confess Bot** and submits a message anonymously.
2. The message is securely transferred to **Helper Bot**.
3. **Helper Bot**:

   * Stores/forwards the confession to a connected channel or group.
   * Lets admins review and reply if necessary.
4. The user never knows the admin identity, and the admin never sees the user identity — maintaining **full anonymity**.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trusttalk.git
cd trusttalk
```

### 2. Create Two Telegram Bots

* Go to [@BotFather](https://t.me/botfather).
* Create two bots:

  1. **Confess Bot** → For users.
  2. **Helper Bot** → For admins/moderation.
* Save both bot tokens.

### 3. Configure Environment

Create a `.env` file in the project root:

```env
CONFESS_BOT_TOKEN=your_confess_bot_token
HELPER_BOT_TOKEN=your_helper_bot_token
CHANNEL_ID=@your_channel_or_group_id
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Both Bots

Since both bots must run **at the same time**, open two terminals:

**Terminal 1 (Confess Bot):**

```bash
python confess_bot.py
```

**Terminal 2 (Helper Bot):**

```bash
python helper_bot.py
```

✅ Now both bots are connected. When a user sends a message to **Confess Bot**, it will flow through to **Helper Bot** and then to your channel/group.

---

## 🛠️ Tech Stack

* **Python**
* **Aiogram** (Telegram Bot Framework)
* **SQLite / SQLAlchemy** (for data storage, if enabled)

---

## 🌟 Future Plans

* Add reply functionality so admins can send anonymous responses back to users.
* Dashboard for monitoring anonymous interactions.
* Multi-language support.


