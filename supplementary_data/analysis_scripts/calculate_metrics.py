#!/usr/bin/env python3
"""
Calculate screening performance metrics from validation results.

This script reproduces the performance metrics reported in the manuscript.
"""

import pandas as pd
from pathlib import Path


def calculate_confusion_matrix(decisions_df, gold_pmids):
    """Calculate confusion matrix for a review."""
    # Get final decisions (stage2 if available, otherwise stage1)
    final_decisions = decisions_df.sort_values('stage').groupby('pmid').last().reset_index()

    included = set(final_decisions[final_decisions['decision'] == 'include']['pmid'].astype(str))
    excluded = set(final_decisions[final_decisions['decision'] == 'exclude']['pmid'].astype(str))
    gold_set = set(str(pmid) for pmid in gold_pmids)

    # Calculate metrics
    tp = len(included & gold_set)
    fn = len(gold_set - included)
    fp = len(included - gold_set)
    tn = len(excluded - gold_set)

    return tp, fn, fp, tn


def calculate_metrics(tp, fn, fp, tn):
    """Calculate performance metrics from confusion matrix."""
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return {
        'recall': recall,
        'precision': precision,
        'specificity': specificity,
        'npv': npv,
        'f1': f1
    }


def main():
    # Load screening decisions
    decisions_path = Path(__file__).parent.parent / 'validation_results' / 'screening_decisions.csv'
    df = pd.read_csv(decisions_path)

    # Gold standard PMIDs (from manuscript)
    gold_standards = {
        'sebastin_2011': [
            # Add 30 PMIDs from Sebastin 2011 review
        ],
        'arshad_2016': [
            # Add 11 PMIDs from Arshad 2016 review
        ],
        'ling_2012': [
            # Add 36 PMIDs from Ling 2012 review
        ],
        'fattah_2015': [
            # Add 32 searchable PMIDs from Fattah 2015 review
        ]
    }

    print("=" * 60)
    print("AI SCREENING PERFORMANCE METRICS")
    print("=" * 60)

    for review, gold_pmids in gold_standards.items():
        if not gold_pmids:
            print(f"\n{review}: Gold standard not loaded - add PMIDs to script")
            continue

        review_df = df[df['review'].str.contains(review, case=False, na=False)]
        if review_df.empty:
            print(f"\n{review}: No decisions found")
            continue

        tp, fn, fp, tn = calculate_confusion_matrix(review_df, gold_pmids)
        metrics = calculate_metrics(tp, fn, fp, tn)

        print(f"\n{review.upper()}")
        print("-" * 40)
        print(f"Papers screened: {len(review_df['pmid'].unique())}")
        print(f"Gold standard: {len(gold_pmids)}")
        print(f"True Positives: {tp}")
        print(f"False Negatives: {fn}")
        print(f"Recall (Sensitivity): {metrics['recall']:.1%}")
        print(f"Specificity: {metrics['specificity']:.1%}")
        print(f"NPV: {metrics['npv']:.1%}")
        print(f"F1 Score: {metrics['f1']:.3f}")


if __name__ == '__main__':
    main()
