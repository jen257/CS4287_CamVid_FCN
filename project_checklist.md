# CS4287 Assignment: CamVid Semantic Segmentation Project Checklist

## Phase 1: Infrastructure & Dummy Data Testing
- [ ] **Task 1:** Develop Dummy Data Placeholder DataLoader
- [ ] **Task 2:** Implement FCN-32s without Skip Connections and Test Forward Pass with Dummy Data
- [ ] **Task 3:** Implement mIoU Calculation Function and Basic Training Loop, Test Backpropagation with Dummy Data

## Phase 2: Core Module Development & Real Training
- [ ] **Task 4:** Map RGB Colors to Class IDs, Load Real CamVid Images, and Apply Synchronized Data Augmentation
- [ ] **Task 5:** Extract Pool3/Pool4 Feature Maps and Implement FCN-8s via Addition Fusion
- [ ] **Task 6:** Implement K-Fold Splitting, Weighted Cross-Entropy/Dice Loss, Model Saving, and Plot Loss Curves

## Phase 3: Independent Experiments & Metric Collection
- [ ] **Task 7:** Conduct Data Augmentation Ablation Study to Verify Overfitting Suppression
- [ ] **Task 8:** Conduct Segmentation Performance Comparison: FCN-32s vs. FCN-8s
- [ ] **Task 9:** Execute Full 5-Fold Cross-Validation on Optimal Configuration and Summarize Final Metrics

## Phase 4: Final Reporting & Submission
- [ ] **Task 10:** Write "Dataset Analysis and Preprocessing" Report Section and Clean Up Code Comments
- [ ] **Task 11:** Draw Network Architecture Diagram and Write "Network Structure" and "Difficulty Assessment" Sections
- [ ] **Task 12:** Compile Literature Benchmarks, Write "Results and Evaluation" Section, and Verify Generative_AI_Log.md
- [ ] **Task 13:** Jointly Verify Notebook and Submit Assignment
