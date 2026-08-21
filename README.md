CBIR-Review-Trends-2026
Reference

If you find this review or the curated resources helpful for your research, please cite our work as follows:

    Baarab, N., & Chaouki, B. E. L. K. (2026). Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges. *Discover Artificial Intelligence* (Springer Nature)

About

This repository serves as a technical resource and curated directory for the review paper: "Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges".

As a comprehensive survey, this work traces the evolution of Content-Based Image Retrieval (CBIR) from traditional handcrafted descriptors to state-of-the-art deep learning architectures . The repository catalogs the transition toward multimodal fusion and foundation models, providing researchers with a centralized guide to the benchmarks, search logs, and models discussed in the manuscript.
Key Research Areas Covered:

    Feature Learning: Transition from handcrafted features (LBP, Gabor) to hierarchical CNN representations.

    Semantic Gap Reduction: Strategies using attention mechanisms, knowledge graphs, and relevance feedback.

    Vision Transformers (ViT): Analysis of global dependency capturing using ViT, Swin, and DeiT.

    Multimodal Retrieval: Integration of Vision-Language models like CLIP, BLIP, and Florence .

    Open Challenges: Scalability, data scarcity, interpretability, and the rise of Omni-modal systems.

Repository Structure & Resources

```text

CBIR-Review-Trends-2026/
├── 01_prisma_methodology/      <-- PRISMA search logs & screening criteria
├── 02_literature_database/     <-- Structured catalog of reviewed literature (.csv / .json)
├── 03_benchmarks_and_metrics/  <-- Dataset taxonomies & baseline evaluation scripts
└── 04_maintenance_and_updates/ <-- Quarterly literature addition logs.
```

Maintenance & Update Schedule

To ensure this resource remains valuable to the computer vision community:

    Update Frequency: Quarterly updates scheduled through 2027.

    Scope of Updates: Incorporating emerging vision-language foundation models, visual RAG benchmarks, lightweight edge architectures, and novel metric learning strategies.

Dependencies and Requirements

To implement the deep learning models and CBIR techniques discussed in the review, the following technical environment and libraries are recommended:
Environment

    Language: Python 3.8+

    Deep Learning Frameworks: PyTorch 1.10+ or TensorFlow 2.0+

Core Libraries

    Transformers (Hugging Face): For Vision Transformer (ViT) and CLIP implementations.

    OpenCV: For image preprocessing and traditional feature extraction.

    SciPy / NumPy: For vector distance calculations and similarity metrics.
    
    FAISS / ScaNN: For large-scale efficient vector indexing and similarity search.

Benchmark Datasets

The review analyzes several key datasets used for training and evaluating modern CBIR systems:

| Dataset | Type | Scale |
| :--- | :--- | :--- |
| **ImageNet** | Object Classification | 1.2M+ Images |
| **MS-COCO** | Object Detection / Captioning | 330k Images |
| **LAION-400M** | Multimodal (Image-Text) | 400M Pairs |
| **Oxford/Paris** | Landmark Retrieval | Curated subsets |

Ethics and Fairness

In alignment with the transparency goals of The Visual Computer, this repository emphasizes the importance of bias detection and interpretability in multimodal models. We provide references to bias-aware evaluation protocols and explainable AI (XAI) tools like Grad-CAM used to verify retrieval logic.

Contact

Nissrine Baarab ESDS laboratory, National School of Applied Sciences (ENSA)

Ibn Zohr University, Agadir, Morocco 

nissrine.baarab@edu.uiz.ac.ma
