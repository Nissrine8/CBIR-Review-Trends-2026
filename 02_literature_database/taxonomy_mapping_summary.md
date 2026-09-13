# Literature Database Taxonomy & Selection Mapping

This document details the categorization and mapping of the **N = 128** synthesized papers included in the systematic review:
**"Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges"** (*Discover Artificial Intelligence*, Springer Nature).

---

## 1. Architectural Distribution (N = 128 Total Synthesized Papers)

* **CNN-Based Descriptors & Feature Representation:** **32 Papers**
  * *Focus:* Early deep baselines, fine-tuning strategies, global/local pooling mechanisms (R-MAC, GeM, SPoC), and spatial attention refinement.
* **Vision Transformers & Attention-Based Models:** **28 Papers**
  * *Focus:* Global context modeling via ViT, Swin Transformer, DeiT, prompt tuning, and hybrid CNN-Transformer backbones.
* **Multimodal Vision-Language & Foundation Models:** **34 Papers**
  * *Focus:* Contrastive pre-training (CLIP, ALIGN), generative alignment (BLIP, BLIP-2, xGen-MM/BLIP-3, Florence-2), cross-modal projection, and Visual RAG pipelines.
* **Lightweight & Resource-Efficient Edge Models:** **18 Papers**
  * *Focus:* Edge deployment, MobileNet, EfficientNet, MobileViT, Swin-Tiny, model quantization, and knowledge distillation.
* **Scalable Indexing & ANN Search Pipelines:** **16 Papers**
  * *Focus:* Approximate Nearest Neighbor (ANN) search, HNSW graph indexing, Product Quantization (PQ), and vector database integrations (FAISS, ScaNN, Milvus).

---

## 2. Quantitative Comparison Subset (N = 66)

Out of the $N = 128$ synthesized papers, **$N = 66$ papers** explicitly evaluate standardized quantitative metrics ($mAP$, $Recall@k$, $nDCG$, $Precision@k$) on public benchmark datasets (e.g., ROxford/RParis, ImageNet, MS-COCO, LAION) and are directly incorporated into the comparative state-of-the-art tables in Sections 6 and 7 of the manuscript.
