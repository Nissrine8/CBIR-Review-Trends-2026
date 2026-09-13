"""
CBIR Baseline Evaluation Metrics Script
----------------------------------------
This script provides standard reference implementations for evaluating Content-Based
Image Retrieval (CBIR) systems using Mean Average Precision (mAP) and Recall@k.

Companion resource for: "Deep Learning-Based Content-Based Image Retrieval: A Review 
of Trends, Multimodal Fusion, and Open Challenges" (Discover Artificial Intelligence).
"""

from typing import List, Set, Union
import numpy as np


def calculate_ap(retrieved_ids: List[Union[int, str]], ground_truth_ids: Union[Set[Union[int, str]], List[Union[int, str]]]) -> float:
    """
    Computes Average Precision (AP) for a single query ranking.

    Parameters:
        retrieved_ids (list): Ranked list of retrieved item IDs.
        ground_truth_ids (set or list): Set or list of relevant ground truth item IDs.

    Returns:
        float: Average Precision score for the query.
    """
    ground_truth_set = set(ground_truth_ids)
    if len(ground_truth_set) == 0:
        return 0.0

    hits = 0
    sum_precisions = 0.0

    for i, item_id in enumerate(retrieved_ids):
        if item_id in ground_truth_set:
            hits += 1
            precision_at_i = hits / (i + 1)
            sum_precisions += precision_at_i

    return sum_precisions / len(ground_truth_set)


def calculate_recall_at_k(retrieved_ids: List[Union[int, str]], ground_truth_ids: Union[Set[Union[int, str]], List[Union[int, str]]], k: int = 10) -> float:
    """
    Computes Recall@k for a query ranking.

    Parameters:
        retrieved_ids (list): Ranked list of retrieved item IDs.
        ground_truth_ids (set or list): Set or list of relevant ground truth item IDs.
        k (int): Cutoff rank k.

    Returns:
        float: Recall@k score.
    """
    ground_truth_set = set(ground_truth_ids)
    if len(ground_truth_set) == 0:
        return 0.0

    top_k_retrieved = set(retrieved_ids[:k])
    relevant_hits = top_k_retrieved.intersection(ground_truth_set)

    return len(relevant_hits) / len(ground_truth_set)


if __name__ == "__main__":
    # Example verification test case
    retrieved_items = [101, 203, 104, 501, 102, 305, 105]
    ground_truth_items = {101, 102, 105}

    ap_score = calculate_ap(retrieved_items, ground_truth_items)
    recall_at_5 = calculate_recall_at_k(retrieved_items, ground_truth_items, k=5)

    print(f"Sample AP: {ap_score:.4f}")
    print(f"Sample Recall@5: {recall_at_5:.4f}")
