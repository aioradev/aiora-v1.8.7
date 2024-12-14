# examples/basic_research_simulation.py
from aiora.core import AioraResearchModel

def main():
    # Initialize the Aiora Research Model
    aiora = AioraResearchModel()
    
    # Generate hypotheses across different domains
    quantum_hypothesis = aiora.generate_research_hypothesis("quantum_physics")
    math_hypothesis = aiora.generate_research_hypothesis("theoretical_mathematics")
    
    # Print generated hypotheses
    print("Quantum Physics Hypothesis:", quantum_hypothesis)
    print("Mathematics Hypothesis:", math_hypothesis)
    
    # Simulate research progression
    progression = aiora.simulate_research_progression(50)
    
    # Save research state
    aiora.save_research_state()

if __name__ == "__main__":
    main()
