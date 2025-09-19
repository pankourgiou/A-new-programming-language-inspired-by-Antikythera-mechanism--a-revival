#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Antikythera Mechanism Interpreter
---------------------------------
A celestial programming language with astronomical glyphs.
"""

import sys, os, random, time

class AntikytheraMechanismInterpreter:
    def __init__(self):
        self.symbols = {}

    def run_line(self, line: str):
        line = line.strip()
        if not line or line.startswith("✶"):  # comment
            return

        # ☉ Sun → variable assignment
        if line.startswith("☉"):
            parts = line[1:].split("=", 1)
            if len(parts) == 2:
                var = parts[0].strip()
                expr = parts[1].strip()
                self.symbols[var] = self.evaluate(expr)
            else:
                print("Syntax error in ☉ assignment.")

        # ♀ Venus → string assignment
        elif line.startswith("♀"):
            parts = line[1:].split("=", 1)
            if len(parts) == 2:
                var = parts[0].strip()
                expr = parts[1].strip().strip('"')
                self.symbols[var] = expr
            else:
                print("Syntax error in ♀ assignment.")

        # ☽ Moon → print
        elif line.startswith("☽"):
            expr = line[1:].strip()
            print(self.evaluate(expr))

        # ☿ Mercury → input
        elif line.startswith("☿"):
            var = line[1:].strip()
            self.symbols[var] = input(f"{var}> ")

        # ♅ Uranus → random number
        elif line.startswith("♅"):
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                return random.randint(0, int(parts[1]))
            return "[Error: invalid ♅ usage]"

        # ♆ Neptune → sleep
        elif line.startswith("♆"):
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                time.sleep(int(parts[1]))
            else:
                print("[Error: invalid ♆ usage]")

        # ♃ Jupiter → loop
        elif line.startswith("♃"):
            head, body = line.split("{", 1)
            body = body.rsplit("}", 1)[0].strip()
            count = int(head[1:].strip())
            for _ in range(count):
                self.run_line(body)

        # ♂ Mars → conditional
        elif line.startswith("♂"):
            head, body = line.split("{", 1)
            body = body.rsplit("}", 1)[0].strip()
            condition = head[1:].strip()
            if self.evaluate(condition):
                self.run_line(body)

        # ☿ help (if typed literally)
        elif line == "☿":
            self.show_help()

        # ♄ Saturn → exit
        elif line.startswith("♄"):
            sys.exit(0)

        else:
            print(f"Unknown cosmic glyph sequence: {line}")

    def evaluate(self, expr: str):
        try:
            for var, val in self.symbols.items():
                expr = expr.replace(var, f'"{val}"' if isinstance(val, str) else str(val))
            return eval(expr, {"str": str, "random": random}, {})
        except Exception as e:
            return f"[Error: {e}]"

    def run_file(self, filename: str):
        if not filename.endswith(".antikythera_mechanism"):
            print("Error: file must end with .antikythera_mechanism")
            return
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            return

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                self.run_line(line)

    def show_help(self):
        print("""
Antikythera Mechanism Language
==============================
☉ var = expr     → Assign variable
♀ var = "text"   → Assign string
☽ expr           → Print expression
☿ var            → Input from user
♃ n { code }     → Repeat code n times
♂ condition { c }→ If condition true, run code
♅ n              → Random number 0–n
♆ n              → Sleep for n seconds
♄                → Exit
✶ comment        → Comment
""")

# --- REPL ---
def repl():
    print("Antikythera Mechanism REPL (symbols: ☉ ☽ ♀ ☿ ♃ ♂ ♅ ♆ ♄ ✶)")
    interp = AntikytheraMechanismInterpreter()
    while True:
        try:
            line = input("⚙︎ > ")
            interp.run_line(line)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting REPL.")
            break

# --- Entry ---
if __name__ == "__main__":
    interpreter = AntikytheraMechanismInterpreter()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        repl()
