
# 🦖 RaptorScript

**RaptorScript** is a beginner-friendly scripting language inspired by Python, Ruby, and JavaScript — built for simplicity, readability, and fun.

🚀 Perfect for learning programming or making tiny scripts with big claws.

---

## ✅ Features
- `say "..."` — print to screen
- `set x = ...` — assign variables
- `if ... { ... }` — conditionals
- `repeat ... { ... }` — loops
- `func name(args) { ... }` — define functions
- `name(args)` — call functions

---

## 🧪 Example Script: `example.rap`

```raptorscript
say "Welcome to RaptorScript!"

set name = "Peoplerep"
greet(name)

func greet(person) {
    say "Hello, " + person + "!"
}

repeat 3 {
    say "Roarrr!"
}

if name == "Peoplerep" {
    say "You are the commander."
} else {
    say "You are a guest."
}
```

---

## ▶️ How to Run

1. Install Python 3
2. Download this repo
3. In terminal, run:
```bash
python3 raptorscript.py example.rap
```

---

## 🛠 Roadmap
- [x] Basic interpreter
- [ ] Input support
- [ ] Arrays and objects
- [ ] Web playground
- [ ] RaptorScript Standard Library (RSL)

---

## 📜 License
MIT License — use it, share it, evolve it.
