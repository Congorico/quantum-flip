# quantum-flip

A Python implementation of the classic Quantum Coin Flip paradox. 
It demonstrates the power of quantum superposition and quantum strategies over classical ones.

          How it Works
The game follows the Meyer-Penny Flip paradox:
1. The coin starts in the state |0> (Heads).
2. The Quantum Computer applies a Hadamard Gate (H), putting the coin into a superposition.
3. The Human player chooses to flip (X Gate) or fake-flip (I Gate). 
Because the coin is in superposition, the classical move has no real effect on the probabilities.
4. The Quantum Computer applies another Hadamard Gate (H), interference brings the state back to |0> with 100% probability.
5. The final measurement is always 
Heads, meaning the Quantum Computer wins every single time.

## Technologies Used
* Python 3
* Qiskit / Custom Quantum Logic
