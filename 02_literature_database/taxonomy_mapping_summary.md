# Literature Database Taxonomy & Selection Mapping

This document details the categorization and mapping of the **N = 128** synthesized papers included in the systematic review:
**"Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges"** (*Discover Artificial Intelligence*, Springer Nature).

---

## 1. Architectural Distribution (N = 128 Total)

* **CNN-Based Descriptors & Feature Representation:** **32 Papers** (Early deep baselines, fine-tuning, pooling strategies like R-MAC/GeM).
* **Vision Transformers & Attention-Based Models:** **28 Papers** (ViT, Swin, DeiT, prompt tuning, spatial attention).
* **Multimodal Vision-Language & Foundation Models:** **34 Papers** (CLIP, BLIP, BLIP-2, Florence, Flamingo, Cross-modal alignment).
* **Lightweight & Resource-Efficient Edge Models:** **18 Papers** (MobileNet, EfficientNet, MobileViT, Swin-Tiny).
* **Scalable Indexing & ANN Search Pipelines:** **16 Papers** (HNSW graphs, Product Quantization, Vector Databases, FAISS/Milvus).

---

## 2. Quantitative Comparison Subset (N = 68)

Out of the $N = 128$ synthesized papers, **$N = 68$ papers** explicitly evaluate standardized quantitative metrics ($mAP$, $Recall@k$, $nDCG$, $Precision@k$) on benchmark datasets (e.g., Oxford/Paris, ImageNet, MS-COCO, LAION) and are directly incorporated into the comparative analysis tables in Sections 6 and 7 of the manuscript.
