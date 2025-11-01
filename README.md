# My Chess Engine

Welcome to My Chess Engine! This is a super smart chess program that you can run on your computer. It can play chess against you, and it can even learn to get better over time by playing against itself!

## How It Works (for a 13-Year-Old!)

Imagine our chess engine has two parts: a **Calculator** and a **Learner**.

*   **The Calculator** 🧠: This part is like a super-fast thinker. It can look at the chessboard and calculate millions of possible moves in just a few seconds. It's really good at seeing many steps into the future, so it can find the best possible move to make. We built this using a clever technique called **NegaMax**.

*   **The Learner** 📚: This part is like the engine's brain. It has a special "neural network" that learns what a good or bad position looks like. At first, it doesn't know much about chess, but it learns by playing thousands of games against itself and seeing what moves lead to a win. Over time, it gets smarter and smarter, and it teaches the Calculator what to look for.

So, the **Calculator** finds the moves, and the **Learner** tells it which moves are the smartest. Together, they make a really strong chess player!

## Getting Started: How to Use the Engine

Ready to play? Here’s how you can get everything set up.

### Step 1: Download the Code

First, you need to get the code for the engine onto your computer. If you have `git` installed, you can open a terminal and type:

```bash
git clone <repository_url>
cd my-chess-engine
```

If you don't have `git`, you can download the code as a ZIP file and unzip it.

### Step 2: Install the Brain Food (Dependencies)

Our engine needs some special tools to work. You can install them easily using a tool called `pip`. In your terminal, type this command:

```bash
pip install -r requirements.txt
```

This will install `python-chess` (for the chess rules) and `PyTorch` (for the engine's brain).

### Step 3: Play a Game!

You can't play against the engine in the terminal. Instead, you need a special program called a **chess GUI**. A great free one is called **Arena**.

1.  **Download Arena** (it's free!).
2.  Open Arena and go to **Engines > Install New Engine**.
3.  Find the `main.py` file in the code you downloaded. Arena will ask you to configure the engine. Make sure it knows to use `python` to run it.
4.  Once the engine is loaded, you can start a new game and play against it!

When you want to play, run this command in your terminal:

```bash
python main.py play
```

This tells the engine it's time to play chess!

## How to Train the Engine (Make It Smarter!)

This is the really cool part. You can train the engine to become a better player. It's a two-step process: first, you let it play against itself to gather experience, and then you use that experience to train its brain.

### Step 1: Generate Game Data

First, we need the engine to play a bunch of games against itself. This is how it learns. To do this, run the following command in your terminal:

```bash
python main.py generate
```

This will make the engine play 10 games against itself and save all the moves to a file called `game_data.json`. You can make it play more games if you want, like this:

```bash
python main.py generate --num-games 50
```

The more games it plays, the smarter it will get!

### Step 2: Train the Brain

Now that we have some game data, we can use it to train the engine's brain. Run this command:

```bash
python main.py train
```

This will take the `game_data.json` file and use it to teach the neural network. You'll see some output in the terminal that shows the training progress. After it's done, it will save the new, smarter brain to a file called `model.pth`.

The next time you play against the engine, it will use its new brain and be a little bit better at chess! You can repeat these steps as many times as you want to keep making the engine smarter.
