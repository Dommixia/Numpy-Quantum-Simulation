import numpy as np

# Qubits
zero = np.array([1,0], dtype = complex)
one = np.array([0,1], dtype = complex)

#Multi Qubits
q00 = np.kron(zero, zero)
q01 = np.kron(zero, one)
q10 = np.kron(one, zero)
q11 = np.kron(one, one)

#identity Matrix
I = np.eye(2, dtype = complex)

#Gates
H_gate = np.array([[1,1], [1,-1]], dtype = complex)/np.sqrt(2)
X = np.array([[0,1], [1,0]], dtype = complex)
Y = np.array([[0,-1j], [1j, 0]], dtype = complex)
Z = np.array([[1,0], [0, -1]], dtype = complex)
CNOT = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1],
                  [0, 0, 1, 0]], dtype=complex)

#Matrix Multiplication
def applyGate(gate, state):
    return gate @ state

def measure(state):
    prob = np.abs(state)**2
    outcome = np.random.choice(len(state), p = prob)
    return outcome

#Multi Qubit Gates via Tensor Products
def applyQubit0(gate, state):
    f_gate = np.kron(gate, I)
    return f_gate @ state
def applyQubit1(gate, state):
    f_gate = np.kron(I, gate)
    return f_gate @ state
def applyCNOT(state):
    return CNOT @ state

hq0 = np.kron(H_gate, I)
state = hq0 @q00

bell_state = applyCNOT(state)
print(bell_state)