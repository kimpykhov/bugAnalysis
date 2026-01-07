# EDA Plan
## 1. EDA Goal
Verify that the synthetic dataset:
- is internally consistent
- reflects the underlying assumptions
- contains no logical inconsistencies or leaks
- is suitable for solving the ML problem of predicting bug closure times

EDA is not aimed at:
- model selection
- metric optimization
- feature engineering

## 2. Data Structure Checks (Sanity Checks)
### 2.1 Dataset Size and Shape
- Number of Rows
- Number of Columns
- Data Types by Column

**Expectations:**
- Each Row = One Bug
- No Duplicate Bug_IDs

### 2.2 Gap Checks
For each field:
- Percentage of Nulls / Empty
- Are gaps allowed according to the data design?

**Expectations:**
- Required fields (created_at, closed_at, priority, severity, component, assignee_id) without gaps
- text fields may be empty

## 3. Temporal Logic
### 3.1 Date Validation
- closed_at >= created_at for all records
- no future dates relative to the generation time
- no abnormally large days_to_close values

**Expectations:**
- no negative values
- days_to_close > 0

### 3.2 Close Time Distribution
- days_to_close histogram
- min / median / mean / max

**Goal:**
- understand whether there is:
- strong skewness
- outliers
- multimodality

## 4. Target Variable Analysis
### 4.1 Class Validation (if classification is used)
- FAST / MEDIUM / SLOW distribution
- Class balance

**Expectations:**
- no extreme skewness (e.g., 90% FAST)

### 4.2 Regression → Classification Relationship
- days_to_close ranges correspond to classes
- absence Overlaps or logical conflicts

## 5. Categorical Feature Analysis
### 5.1 Distributions
For each feature:
- priority
- severity
- component
- assignee_id
- labels (number per bug)

**Checks:**
- conformity to expected frequencies
- are there any categories that occur 1-2 times?

### 5.2 Impact of Features on the Target
Aggregate-Level Analysis:
- mean / median days_to_close by:
    - priority
    - severity
    - component
    - assignee_id

- FAST / MEDIUM / SLOW for the same groups

**Goal:**
- Verify that the assumed dependencies are met on average, rather than perfectly.

## 6. Data Design Assumptions Testing
Explicit testing of the following hypotheses:
- High / Critical → faster on average, but not always
- Blocker + Infra → rarely FAST
- Performance Label → slowest
- Backend faster Performance
- Multiple labels → higher probability of MEDIUM / SLOW
- Assignees vary in speed

**Important:**
- Exceptions are allowed
- A trend, not determinism, is important

## 7. Checking noise and realism
- Are there any cases:
    - low priority, but SLOW
    - critical, but slow
- Are there any intersections between classes

**Goal:**
- Confirm that the problem cannot be solved by rules

## 8. Risks and limitations identified by EDA
Based on the EDA, record:
- Which features are dominant
- Where target leakage is possible
- Where synthetics appear too "clean"
- Which aspects of reality are poorly modeled

## 9. Decision on the next step
Based on the EDA, a decision is made:
- Whether to keep the current data design
- Whether to amplify noise
- Whether move to:
    - regression
    - classification
    - or do both