import tensorflow as tf
import tensorflow_privacy
from tensorflow_privacy.privacy.analysis import compute_dp_sgd_privacy

def create_private_optimizer(learning_rate, l2_norm_clip, noise_multiplier, num_microbatches):
    """
    Kreira Differentially Private Optimizer.
    Ovo garantuje da model nece 'zapamtiti' podatke pojedinacnih korisnika.
    """
    optimizer = tensorflow_privacy.DPKerasSGDOptimizer(
        l2_norm_clip=l2_norm_clip,
        noise_multiplier=noise_multiplier,
        num_microbatches=num_microbatches,
        learning_rate=learning_rate
    )
    return optimizer

def calculate_privacy_budget(n, batch_size, epochs, noise_multiplier):
    """
    Izracunava Epsilon (Privacy Budget) - kljucna metrika za AIGP audit.
    n: Ukupan broj primera u datasetu
    """
    epsilon, _ = compute_dp_sgd_privacy.compute_dp_sgd_privacy(
        n=n, 
        batch_size=batch_size, 
        noise_multiplier=noise_multiplier, 
        epochs=epochs, 
        delta=1e-5
    )
    return epsilon

if __name__ == "__main__":
    print("--- Differential Privacy Setup ---")
    # Primer proracuna budzeta privatnosti
    eps = calculate_privacy_budget(n=60000, batch_size=250, epochs=3, noise_multiplier=1.1)
    print(f"Privacy Guarantee (Epsilon): {eps:.2f}")
