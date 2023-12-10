import random

# List of random facts about the Earth
earth_facts = [
    "Earth is the third planet from the sun.",
    "The Earth is approximately 4.5 billion years old.",
    "The highest point on Earth is Mount Everest.",
    "The Earth's atmosphere is composed mostly of nitrogen and oxygen.",
    "The Earth's rotation is gradually slowing.",
    "The Earth is the only known planet to support life.",
    "Earth is not a perfect sphere; it is slightly flattened at the poles.",
    "70% of the Earth's surface is covered with water.",
    "The Earth orbits the sun at an average speed of 67,000 mph (107,000 km/h)."
]

# List of random facts about underwater life
underwater_facts = [
    "The Great Barrier Reef is the largest coral reef system on Earth.",
    "The Mariana Trench is the deepest part of the world's oceans.",
    "The blue whale is the largest animal on Earth, and it's found in the ocean.",
    "Coral reefs are often called the 'rainforests of the sea' due to their biodiversity.",
    "The ocean contains about 97% of Earth's water.",
    "The anglerfish uses a bioluminescent lure to attract prey in the dark depths.",
    "Seahorses are unique as the male carries and gives birth to the babies.",
    "The ocean is home to a diverse range of marine life, from microscopic plankton to massive whales.",
    "Some species of jellyfish are biologically immortal."
]

def generate_random_fact():
    # Randomly select whether to generate an Earth fact or an underwater life fact
    category = random.choice(["earth", "underwater"])
    
    if category == "earth":
        return random.choice(earth_facts)
    else:
        return random.choice(underwater_facts)


