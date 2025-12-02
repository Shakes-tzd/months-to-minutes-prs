# PRS Submission Package

## From Months to Minutes: Evaluating an AI-Driven Approach to Systematic Reviews in Plastic Surgery

**Submitted to:** Plastic and Reconstructive Surgery

**Date:** December 2025

---

## Folder Structure

```
2025-11_prs_submission/
├── README.md                          # This file
├── Cover_Letter_Revision.md           # Cover letter (markdown)
├── Cover_Letter_Revision.docx         # Cover letter (Word)
├── manuscript/
│   ├── manuscript_2025-11_PRS_FINAL.docx  # Main manuscript
│   ├── manuscript_review.html         # HTML version for review
│   └── manuscript_review.pdf          # PDF version for review
├── tables/
│   ├── Table_1_Review_Characteristics.docx
│   ├── Table_2_Performance_Metrics.docx
│   ├── Table_3_False_Negatives.docx
│   └── Table_4_Stage_Refinement.docx
├── figures/
│   ├── Figure_1_Two_Stage_Workflow.tiff     # 300 DPI
│   ├── Figure_2_Two_Stage_Refinement.tiff   # 300 DPI
│   ├── Figure_3_Gold_Standard_Recall.tiff   # 300 DPI
│   └── Figure_4_Performance_Metrics.tiff    # 300 DPI
├── supplementary_materials/
│   └── supplementary_materials.docx    # Supplementary Tables S1-S4
├── supplementary_figures/
│   ├── Supplementary_Figure_1_Two_Stage_Comparison.tiff
│   ├── Supplementary_Figure_2_Per_Criterion_Evaluation.tiff
│   └── Supplementary_Figure_3_Stage2_Error_Correction.tiff
├── supplementary_data/
│   ├── screening_configs/              # YAML configuration files
│   │   ├── sebastin_2011_screening.yaml
│   │   ├── arshad_2016_screening.yaml
│   │   ├── ling_2012_screening.yaml
│   │   └── fattah_2015_screening.yaml
│   ├── gold_standards/                 # Verified gold standard PMIDs
│   │   ├── sebastin_2011_gold_standard.yaml
│   │   ├── arshad_2016_gold_standard.yaml
│   │   ├── ling_2012_gold_standard.yaml
│   │   └── fattah_2015_gold_standard.yaml
│   ├── validation_results/             # Complete screening results
│   │   ├── screening_decisions.csv     # 6,673 decisions with reasoning
│   │   └── gold_standard_pmids.csv     # 110 gold standard PMIDs
│   └── analysis_scripts/
│       └── calculate_metrics.py        # Reproducibility script
└── response_to_reviewers/
    ├── Response_to_Reviewers_Revision2.md    # Detailed responses
    └── Response_to_Reviewers_Revision2.docx  # Word format
```

---

## File Descriptions

### Manuscript
- **manuscript_2025-11_PRS_FINAL.docx**: Complete manuscript formatted per PRS guidelines

### Tables (separate files per PRS requirements)
- **Table 1**: Systematic review characteristics (topic, databases, years, gold standard)
- **Table 2**: AI screening performance metrics (recall, NPV, specificity, F1)
- **Table 3**: False negative analysis with criterion failed
- **Table 4**: Stage-by-stage performance refinement

### Figures (300 DPI TIFF)
- **Figure 1**: Expert-configured two-stage AI screening workflow architecture
- **Figure 2**: Two-stage refinement (recall comparison and confidence improvement)
- **Figure 3**: Gold standard recall per review (final screening sensitivity)
- **Figure 4**: Performance metrics panel (recall, NPV, specificity, F1)

### Supplementary Materials
- **Table S1**: Complete prompt example (Sebastin 2011)
- **Table S2**: Configuration requirements by review type
- **Table S3**: LLM specifications (versions, costs, parameters)
- **Table S4**: Detailed stage-by-stage metrics

### Supplementary Figures
- **Figure S1**: Two-stage comparison across reviews
- **Figure S2**: Per-criterion evaluation breakdown
- **Figure S3**: Stage 2 error correction analysis

### Supplementary Data Files
- **Screening configurations**: YAML files with inclusion/exclusion criteria
- **Gold standards**: Verified PMIDs from each original review
- **Validation results**: Complete screening decisions with AI reasoning
- **Analysis scripts**: Python code for metric calculation

---

## Checklist for Submission

- [x] Manuscript formatted per PRS Author Guidelines
- [x] Abstract ≤250 words
- [x] Tables as separate Word files
- [x] Figures 300 DPI TIFF format
- [x] Supplementary materials separate from main manuscript
- [x] Response to Reviewers complete
- [x] Cover letter updated
- [x] All 27 citations properly formatted

---

## Contact

**Corresponding Author:**
Richard J. Redett, MD
Department of Plastic and Reconstructive Surgery
Johns Hopkins University School of Medicine
Email: rredett1@jhmi.edu
