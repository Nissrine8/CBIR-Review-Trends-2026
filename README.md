Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges

Reference & Citation

If you find this review or the curated resources helpful for your research, please cite our work as follows:

    Baarab, N., & Chaouki, B. E. L. K. (2026). Deep Learning-Based Content-Based Image Retrieval: A Review of Trends, Multimodal Fusion, and Open Challenges. *Discover Artificial Intelligence* (Springer Nature)

> **Permanent Archival Snapshot:** [https://doi.org/10.5281/zenodo.19520870](https://doi.org/10.5281/zenodo.19520870)

About
This repository serves as an open-access technical resource, reproducible toolkit, and curated directory for our systematic review paper. Representing a **primary auxiliary contribution** of the study, this living repository provides researchers and practitioners with structured literature categorizations, dataset taxonomies, PRISMA search logs, and baseline evaluation utilities.

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

Maintenance Schedule & Community Contributions

To ensure this repository remains an active, living resource for the computer vision community:

    Update Frequency: Maintained and updated quarterly through 2028.

    Scope of Updates: Incorporating emerging vision-language models, visual RAG benchmarks, lightweight edge architectures, and novel metric learning strategies.

    Community Pull Requests: We actively welcome contributions! If you would like to submit new benchmark results, suggest recently published high-impact papers, or refine taxonomy entries, please submit a Pull Request or open an Issue following the repository guidelines.

Technical Dependencies & Recommended Environment

To execute the baseline metric calculation scripts ($mAP$, $Recall@k$) and implement the models discussed in the review, the following setup is recommended:

    Language: Python 3.8+

    Deep Learning Frameworks: PyTorch 1.10+ or TensorFlow 2.0+

    Core Libraries:
       transformers (Hugging Face): Vision Transformers (ViT) and CLIP implementations.
       opencv-python: Image preprocessing and baseline feature extraction.
       scipy / numpy: Vector distance computations and similarity ranking.
       faiss-cpu / faiss-gpu / ScaNN: Large-scale vector indexing and similarity search.
       
Standard Benchmark Datasets Analyzed

The review analyzes several key datasets used for training and evaluating modern CBIR systems:

| Dataset | Domain/Type | Scale | Primary Evaluation Focus |
| :--- | :--- | :--- | :--- |
| **ImageNet** | Object Classification | 1.2M+ Images | Transfer Learning & Backbones |
| **MS-COCO** | Object Detection / Captioning | 330k Images | Multimodal Retrieval & Captioning |
| **LAION-400M** | Multimodal (Image-Text) | 400M Pairs | Vision-Language Pre-training |
| **Oxford/Paris** | Landmark Retrieval | Curated subsets | Fine-Grained Instance Search |

Ethics, Bias & Fairness Protocols

In alignment with the transparency goals of Discover Artificial Intelligence, this repository emphasizes responsible deployment, bias auditing, and interpretability in multimodal retrieval systems. We provide references to fairness-aware evaluation metrics and explainable AI (XAI) frameworks (e.g., Grad-CAM) used to inspect feature attribution and retrieval decisions.

Contact & Institutional Affiliation

Nissrine Baarab 

ESDS laboratory, National School of Applied Sciences (ENSA)

Ibn Zohr University, Agadir, Morocco 

Email: nissrine.baarab@edu.uiz.ac.ma
