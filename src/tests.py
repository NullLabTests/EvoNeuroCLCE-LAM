import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from seed import evolve_loop, clce_to_logic, lam_exec, generator

def test_clce_mutation_llm():
    result = clce_to_logic("Test seed")
    assert len(result) > 10

def test_evolve_loop_growth():
    G = evolve_loop("Start seed", iterations=3)
    assert len(G.nodes) == 3
    assert G.number_of_edges() == 3
    assert all('score' in G.nodes[n] for n in G.nodes)

def test_lam_exec():
    roots = lam_exec()
    assert len(roots) == 4

def test_persistence():
    G = evolve_loop("Persist seed", iterations=2)
    pickle.dump(G, open('test.pkl', 'wb'))
    loaded = pickle.load(open('test.pkl', 'rb'))
    assert len(loaded.nodes) == 2

# Run: pytest src/tests.py -v
