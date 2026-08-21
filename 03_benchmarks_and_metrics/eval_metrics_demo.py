"""
CBIR Baseline Evaluation Metrics Script
----------------------------------------
This script provides standard reference implementations for evaluating Content-Based
Image Retrieval (CBIR) systems using Mean Average Precision (mAP) and Recall@k.
Companion resource for: "Deep Learning-Based Content-Based Image Retrieval: A Review 
of Trends, Multimodal Fusion, and Open Challenges" (Discover Artificial Intelligence).
"""

import numpy as np

def calculate_ap(retrieved_ids, ground_truth_ids):
    """
    Computes Average Precision (AP) for a single query ranking.
    
    Parameters:
        retrieved_ids (list): Ranked list of retrieved item IDs.
        ground_truth_ids (set): Set of relevant ground truth item IDs.
        
    Returns:
        float: Average Precision score for the query.
    """
    hits = 0
    sum_precisions = 0.0
    
    for i, item_id in enumerate(retrieved_ids):
        if item_id in ground_truth_ids:
            hits += 1
            precision_at_i = hits / (i + 1)
            sum_precisions += precision_at_i
            
    if len(ground_truth_ids) == 0:
        return 0.0
        
    return sum_precisions / len(ground_truth_ids)

def calculate_recall_at_k(retrieved_ids, ground_truth_ids, k=10):
    """
    Computes Recall@k for a query ranking.
    
    Parameters:
        retrieved_ids (list): Ranked list of retrieved item IDs.
        ground_truth_ids (set): Set of relevant ground truth item IDs.
        k (int): Cutoff rank k.
        
    Returns:
        float: Recall@k score.
    """
    top_k_retrieved = set(retrieved_ids[:k])
    relevant_hits = top_k_retrieved.intersection(ground_truth_ids)
    
    if len(ground_truth_ids) == 0:
        return 0.0
        
    return len(relevant_hits) / len(ground_truth_ids)

if __name__ == "__main__":
    # Example verification test case
    retrieved_items = [101, 203, 104, 501, 102, 305, 105]
    ground_truth_items = {101, 102, 105}
    
    ap_score = calculate_ap(retrieved_items, ground_truth_items)
    recall_at_5 = calculate_recall_at_k(retrieved_items, ground_truth_items, k=5)
    
    print(f"Sample AP: {ap_score:.4f}")
    print(f"Sample Recall@5: {recall_at_5:.4f}")
