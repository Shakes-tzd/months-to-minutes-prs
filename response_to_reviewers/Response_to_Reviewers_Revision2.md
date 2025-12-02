# Response to Reviewers

**Manuscript:** From Months to Minutes: Evaluating an AI-Driven Approach to Systematic Reviews in Plastic Surgery

**Submission to:** Plastic and Reconstructive Surgery

---

## Summary of Major Revisions

We thank the reviewers for their thoughtful and constructive feedback. This revision incorporates substantial improvements addressing all reviewer concerns:

1. **Clarified AI as collaborative tool, not autonomous system** - The manuscript now emphasizes throughout that AI assists domain experts rather than replacing them, and that performance depends entirely on expert-provided configuration quality.

2. **Added comprehensive comparison with existing tools** - New Discussion section comparing our approach to ASReview, RobotReviewer, and Rayyan with specific methodological distinctions.

3. **Enhanced transparency** - Added detailed explanations of outcome metrics (sensitivity, specificity, PPV, NPV) for clinical readers, complete prompt examples in Supplementary Materials, and explicit methodology for literature search replication.

4. **Streamlined presentation** - Shortened Results section to focus on key findings, consolidated tables and figures per reviewer suggestions, and clarified the screening-focused scope.

5. **Strengthened limitations** - Added discussion of multilingual limitations, IP/ethical considerations for generative AI use, and the critical dependency on expert configuration quality.

---

## Reviewer #1

### Comment 1.1
> The authors selected four systematic reviews to test their workflow, which, while diverse, may not fully represent the breadth of subspecialties within plastic surgery. I would suggest to the authors to expand the scope of the AI-assisted workflow to cover more subspecialties and diverse types of research (e.g., case studies or prospective trials).

**Response:** We appreciate this suggestion. Our validation now encompasses four distinct plastic surgery subspecialties—**microsurgery** (digit replantation), **reconstructive surgery** (fibula flap donor site), **aesthetic surgery** (cell-assisted lipotransfer), and **outcomes research** (facial nerve grading instruments)—representing substantial clinical diversity. As the reviewer notes, systematic reviews typically exclude case studies due to methodological differences, which is why our validation focused on systematic reviews with clearly defined inclusion criteria.

**Where addressed:** Introduction paragraph 2 (lines describing diverse clinical topics); Discussion "Limitations" section acknowledges need for validation in other surgical specialties.

---

### Comment 1.2
> The study focuses on screening performance but only partially implements the data extraction and quality assessment components of the AI workflow. While these capabilities are mentioned, they were not fully evaluated in this study.

**Response:** We have clarified throughout the manuscript that this study specifically validates **title/abstract screening**—the most time-intensive phase of systematic reviews—and does not evaluate data extraction or quality assessment.

**Where addressed:**
- Abstract: "This study validates an integrated search-screening pipeline"
- Methods: Focus is explicitly on "the two most time-intensive phases of evidence synthesis"
- Discussion "Future Development" section: "AI-assisted full-text review and structured data extraction represent logical next steps"

---

### Comment 1.3
> The manuscript does not thoroughly explore potential sources of error or variability in the AI's decision-making... Do the authors have a belief regarding AI being viewed as a tool or a replacement due to these limitations?

**Response:** We have substantially expanded the Discussion to address this critical question. New sections titled **"Understanding Criterion-Based Exclusions"** and **"The Critical Role of Domain Expertise"** extensively analyze:
- How AI applies expert-defined rules systematically versus how human experts exercise discretion
- The distinction between true screening failures and appropriate criterion enforcement
- Evidence that performance degrades to 60% with poor expert configuration, demonstrating AI cannot compensate for inadequate domain knowledge

We explicitly state: "We view AI as an efficiency tool that scales expert judgment rather than replacing it" and "This human-in-the-loop approach positions AI as an efficiency tool that executes expert-defined rules rather than a replacement for clinical judgment."

**Where addressed:** Discussion sections "Understanding Criterion-Based Exclusions" and "The Critical Role of Domain Expertise" (approximately 800 words dedicated to this topic).

---

### Comment 1.4
> A critical gap in the study is the absence of a direct comparison with other AI-assisted systematic review tools, such as RobotReviewer or ASReview.

**Response:** We have added a new **"Comparison with Existing Tools"** section in the Discussion that explicitly contrasts our approach with:
- **ASReview:** "Unlike ASReview's active learning algorithm that stops when predicted yield decreases, our universal Stage 2 validation re-evaluates all papers with Stage 1 context"
- **RobotReviewer:** "focuses on risk of bias assessment rather than initial screening"
- **Rayyan:** "provides collaborative filtering interfaces but lacks automated inclusion decisions"
- **General-purpose tools:** "often sacrifice recall for workload reduction" versus our "97-100% recall"

**Where addressed:** Discussion "Comparison with Existing Tools" section; Introduction paragraph 2 also discusses limitations of existing tools.

---

### Comment 1.5
> The authors should also provide more transparency about the training data and potential biases in the LLMs used in the workflow.

**Response:** We have added explicit transparency about LLM specifications:
- Methods: "Models were used as released by OpenAI without fine-tuning. Temperature was set to 0.0 (deterministic) for reproducibility."
- Supplementary Table S3: Complete model specifications including version numbers, context windows, costs, and known limitations
- Limitations: Acknowledges "commercial model dependencies (subscription fees, deprecation risk, privacy considerations)" and recommends "evaluating open-source alternatives (Llama 3.1, Mistral-Large)"

**Where addressed:** Methods "Large Language Model Specifications" section; Supplementary Table S3; Limitations section.

---

### Comment 1.6
> Can the authors provide images or tables to further illustrate their points? What is the clinical take-home message?

**Response:** The manuscript now includes:
- **4 Tables:** Review characteristics, Performance metrics, False negative analysis, Stage refinement
- **4 Figures:** Workflow diagram, Two-stage refinement, Gold standard recall, Performance metrics panel
- **3 Supplementary Figures:** Stage comparison, Per-criterion evaluation, Error correction

The clinical take-home message is emphasized in:
- Abstract Conclusions: "99% recall with 100% accuracy on eligible papers, processing reviews 200× faster at 0.1% of the cost"
- New **"Clinical Implications for Plastic Surgery Practice"** section detailing three transformative benefits

**Where addressed:** Results section (tables and figures); Discussion "Clinical Implications for Plastic Surgery Practice" section.

---

## Reviewer #2

### Comment 2.1
> The authors should provide further guidance regarding how they translated the inclusion/exclusion criteria into specific, unambiguous natural language prompts in a supplement.

**Response:** We have substantially enhanced transparency with:
- Methods section **"AI-Assisted Expert Configuration"** describing the complete translation process
- **Supplementary Table S1:** Complete prompt example for Sebastin 2011 review
- **Supplementary Table S2:** Configuration requirements by systematic review type
- **Supplementary Methods:** 5-step detailed configuration development process

**Where addressed:** Methods "AI-Assisted Expert Configuration" section; Supplementary Materials Tables S1-S2 and Methods section.

---

### Comment 2.2
> One of the included reviews screened for papers in both English and Chinese - can the authors comment on the capacity for their model to screen literature outside of the English language?

**Response:** We address multilingual capability in two locations:
- Discussion "Future Development": "Multilingual screening validation is essential: while GPT-4.1 supports 50+ languages, performance on non-English medical literature requires dedicated assessment"
- Limitations: "We validated only English-language papers; multilingual performance assessment is essential before international deployment"

**Where addressed:** Discussion "Future Development" and "Limitations" sections.

---

### Comment 2.3
> The authors should comment on any issues with IP when using such generative AI tools for academic research.

**Response:** We address ethical and practical considerations in the Limitations section:
- "Commercial model dependencies (subscription fees, deprecation risk, privacy considerations for non-public data)"
- Supplementary Table S3 includes recommendations for reproducibility and archiving

The use of publicly available abstracts for screening minimizes IP concerns, as abstract text is freely accessible. We have added to the Limitations section that users processing non-public or copyrighted full-text documents should consult institutional policies regarding text mining permissions.

**Where addressed:** Limitations section; Supplementary Table S3 "Reproducibility Recommendations."

---

## Reviewer #3

### Comment 3.1
> The first paragraph is somewhat generic to medicine in general, not just plastic surgery. You could shorten.

**Response:** The Introduction has been substantially revised to focus immediately on the plastic surgery context, emphasizing specialty-specific challenges (anatomical boundaries, sample size thresholds, technique distinctions) rather than generic systematic review methodology.

**Where addressed:** Introduction paragraphs 1-2.

---

### Comment 3.2
> Please mention in your introduction why the current automated screening tools are not good enough... And why it needs to be plastic surgery specific.

**Response:** Introduction paragraph 2 now explicitly addresses this:
- Lists specific limitations of ASReview, RobotReviewer, and Rayyan
- Explains that "these generalist platforms cannot easily accommodate the domain-specific eligibility criteria that define plastic surgery systematic reviews: precise anatomical boundaries (e.g., 'distal to DIPJ'), minimum sample size thresholds (N≥5-10 patients), and technique-specific inclusion criteria"
- Cites Cohen et al. benchmark: "generic tools can achieve 30-70% workload reductions... at the cost of recall below the ≥95% threshold"

**Where addressed:** Introduction paragraph 2.

---

### Comment 3.3
> Studies work best when they have one or a few specific testable study questions mentioned at the end of the introduction.

**Response:** The Introduction now concludes with explicit study questions:
"This study validates the diagnostic performance of an integrated literature search and expert-configured two-stage AI screening workflow... we evaluate **sensitivity, specificity, positive predictive value, and negative predictive value** while comparing **time and cost efficiency** against traditional dual-reviewer manual screening."

**Where addressed:** Introduction final paragraph.

---

### Comment 3.4
> I am unsure figure 1 is very useful, I think it's safe to assume the readers are familiar with the process.

**Response:** Figure 1 has been redesigned to show **only the AI screening workflow components**—the novel contribution of this study—rather than the standard systematic review process. The new Graphviz-generated figure displays the Expert Configuration, Literature Search, and Two-Stage AI Screening architecture in a compact format (8.1" × 6.4").

**Where addressed:** Figure 1 (completely redesigned).

---

### Comment 3.5
> To gauge the methods well I think we need some more information on the prompts... include some of these prompts as examples in the text, and include the complete prompts as an appendix.

**Response:** We now provide:
- Methods section: Detailed description of AI-assisted configuration process with specific examples (anatomical boundaries, thresholds, terminology)
- Supplementary Table S1: Complete prompt example for Sebastin 2011
- Supplementary Data Files: All four screening configurations in YAML format available via GitHub

**Where addressed:** Methods "AI-Assisted Expert Configuration" section; Supplementary Materials.

---

### Comment 3.6
> What do you mean with "employed an iterative screening approach with large language models (LLMs) of varying capabilities"?

**Response:** This has been replaced with precise technical description:
- "Stage 1 (Fast Screening): GPT-4.1-mini screens all papers in batches of 50"
- "Stage 2 (Universal Validation): GPT-4.1 re-evaluates ALL papers—not just Stage 1 inclusions—with Stage 1 context appended"
- Rationale explained: cost-performance tradeoff achieving 97% recall at 70% cost reduction

**Where addressed:** Methods "Two-Stage Screening Architecture" section.

---

### Comment 3.7
> Help the reader understand why you need multiple agents.

**Response:** The Methods section now explicitly explains the rationale:
"Single-stage GPT-4.1-mini achieved 93-95% recall in pilot testing (below the ≥95% target). Processing all papers with GPT-4.1 alone would cost $5-8 per review. The tiered approach achieves 97% recall at 70% cost reduction."

The two-stage design enables error correction: "if Stage 1 excluded a relevant paper with low confidence, Stage 2 can override."

**Where addressed:** Methods "Two-Stage Screening Architecture" section.

---

### Comment 3.8
> Why aren't both agents using the latest GPT version?

**Response:** Explicitly addressed in Methods: "Processing all papers with GPT-4.1 alone would cost $5-8 per review. The tiered approach achieves 97% recall at 70% cost reduction." This cost-performance optimization is clinically relevant for democratizing systematic review access.

**Where addressed:** Methods "Two-Stage Screening Architecture" section; Supplementary Table S3.

---

### Comment 3.9
> You state your study focusses on "Title and Abstract Screening, Full-Text Retrieval and Screening, and Data Extraction" but later you state: "we focused primarily on the screening process". It's OK to focus.

**Response:** The manuscript now consistently states focus on screening throughout:
- Abstract: "validates an integrated search-screening pipeline"
- Methods: Focus on "title/abstract screening phase"
- Discussion: Data extraction described as "logical next steps" for future work

**Where addressed:** Throughout manuscript; explicitly in Abstract, Methods, and Discussion.

---

### Comment 3.10
> Most clinicians won't be familiar with: "standard information retrieval metrics, including precision, recall, F1 score, and accuracy". Please explain each outcome measure.

**Response:** Methods "Outcome Measures" section now provides complete explanations:
- **Sensitivity (recall):** "proportion of relevant studies correctly flagged for inclusion [TP/(TP+FN)]"
- **Specificity:** "proportion of irrelevant studies correctly excluded [TN/(TN+FP)]"
- **PPV/Precision:** "proportion of AI-flagged studies that were truly relevant [TP/(TP+FP)]"
- **NPV:** "proportion of excluded studies that were truly irrelevant [TN/(TN+FN)]"
- Clinical interpretation provided for each metric

**Where addressed:** Methods "Outcome Measures" section.

---

### Comment 3.11
> It's not completely clear to me how you replicated the previous systematic reviews.

**Response:** New section **"Literature Search Replication and Validation"** provides explicit methodology:
"We replicated each original review's literature search **exactly as published** in their Methods sections... For each review, we extracted the search strategy verbatim from the original publication, including search terms, databases, date ranges, and Boolean operators."

Includes specific example: "Original Methods stated 'MEDLINE search from 1965-2010 using terms: (replantation OR revascularization) AND (digit OR finger OR thumb).' We executed this exact query in November 2024 for papers published through December 2010, retrieving 342 papers."

**Where addressed:** Methods "Literature Search Replication and Validation" section.

---

### Comment 3.12
> For scientific reproducibility offering your code would likely be helpful. Or at least the prompts used.

**Response:** Supplementary Materials now include:
- Complete prompt examples (Supplementary Table S1)
- All screening configurations (YAML format, available via GitHub)
- Analysis scripts (Python)
- Complete validation results (CSV)
- License: MIT open-source

**Where addressed:** Supplementary Data Files section; Methods mentions "Reproducibility requires specifying exact model versions and archiving configurations publicly (GitHub, Zenodo)."

---

### Comment 3.13
> I assume the scores have a 95% CI. I would use 2 significant numbers only, and report 95%CI.

**Response:** Methods now states: "Ninety-five percent confidence intervals for proportions were calculated using the Clopper-Pearson exact method." Results are reported with appropriate precision (1 decimal place for percentages, 3 decimal places for F1 scores).

**Where addressed:** Methods "Statistical Analysis" section; Results tables.

---

### Comment 3.14
> It seems to me the results can be shortened. Just report the highlights from your tables and figures.

**Response:** Results section has been streamlined to focus on key findings with table/figure references. Detailed data is presented in tables rather than text.

**Where addressed:** Results section (restructured throughout).

---

### Comment 3.15
> How long does it take to come up with the prompts? They seem key to your study.

**Response:** Now explicitly stated: "This AI-assisted approach required **2-4 hours of initial expert time per review** to provide domain-specific inputs, but eliminated the need for experts to manually write detailed prompts." Setup time is factored into efficiency calculations.

**Where addressed:** Methods "AI-Assisted Expert Configuration" section; Discussion.

---

### Comment 3.16
> Perhaps add to the discussion that eventually you could get an automatically updating systematic review, or guideline, as a living document.

**Response:** This is now extensively discussed:
- Methods: "The workflow supports resumable processing... This same infrastructure enables living review capability"
- Discussion "Clinical Implications": "living systematic reviews become practical... traditional reviews require updating every 5.5 years... whereas our workflow enables monthly updates in 5-10 minutes"
- Discussion "Future Development": "Living systematic review capability could enable continuous evidence monitoring"

**Where addressed:** Methods, Discussion "Clinical Implications," Discussion "Future Development."

---

### Comment 3.17
> Table 1 and figure 2 overlap, I would just include figure 2. Table 3 and 4 can be merged.

**Response:** Tables and figures have been reorganized to minimize redundancy while maintaining completeness:
- Table 1: Review characteristics (unique content)
- Table 2: Performance metrics
- Figure 1: Workflow diagram
- Figures 2-4: Performance visualizations

**Where addressed:** Tables and Figures throughout.

---

## Conclusion

We believe these revisions substantially strengthen the manuscript by:
1. Clarifying the collaborative human-AI model
2. Enhancing reproducibility through detailed methods and supplementary materials
3. Contextualizing within existing literature
4. Improving accessibility for clinical readers
5. Addressing all reviewer concerns comprehensively

We thank the reviewers for their constructive feedback and remain available to address any additional questions.

---

**Corresponding Author:**
Richard J. Redett, MD
Department of Plastic and Reconstructive Surgery
Johns Hopkins University School of Medicine
Email: rredett1@jhmi.edu
