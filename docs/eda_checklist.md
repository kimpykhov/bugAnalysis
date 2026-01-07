# EDA Checklist
## 0. Preparation
- [ ] Dataset loads without errors
- [ ] One _CSV_ version is used
- [ ] All subsequent inferences are based solely on this dataset

## 1. General Structure
- [ ] Dataset Size (rows, columns)
- [ ] Column names match data_design
- [ ] Data types are correct (`datetime`, `int`, `category`, `string`)
- [ ] `bug_id` is unique

## 2. Missing Data and Validity
For each column:
- [ ] Are there any missing data?
- [ ] Are they expected?
- [ ] Are there any empty rows or strange values?
Specifically check:
- [ ] `created_at`
- [ ] `closed_at`
- [ ] `days_to_close`

## 3. Temporal Logic
- [ ] `closed_at >= created_at` for all rows
- [ ] No negative `days_to_close`
- [ ] No zero `days_to_close`
- [ ] No extreme outliers (far outside expectations)

## 4. Target: days_to_close
- [ ] Min / Median / Mean / Max
- [ ] Distribution histogram
- [ ] Skewness check
- [ ] Long tail?

## 5. FAST / MEDIUM / SLOW classes (if applicable)
- [ ] Thresholds defined
- [ ] Class distribution
- [ ] Is there a strong imbalance?
- [ ] Are there logical conflicts (FAST with huge days_to_close?)?

## 6. Categorical features - distributions
Check for each:
- [ ] priority
- [ ] severity
- [ ] component
- [ ] assignee_id
- [ ] number of labels per bug

View:
- frequencies
- rare categories
- unexpected biases

## 7. Feature-target relationships (aggregates)
For each feature:
- [ ] mean / median days_to_close
- [ ] FAST / MEDIUM / SLOW by groups
Minimum set:
- priority → days_to_close
- severity → days_to_close
- component → days_to_close
- assignee_id → days_to_close
- label_count → days_to_close

## 8. Checking data_design assumptions
Explicitly check:
- [ ] Higher priority ≠ always faster, but on average yes
- [ ] Blocker + Infra → rarely FAST
- [ ] Performance label → slowest
- [ ] Backend faster Performance
- [ ] Multiple labels → more often MEDIUM / SLOW
- [ ] Assignees differ in speed

## 9. Noise and realism
- [ ] Are there any exceptions to the rules?
- [ ] Is there any class overlap?
- [ ] Is the problem solved by rules (if yes, it's bad)

## 10. Risks and conclusions
Record:
- Dominating features
- Potential leaks
- Weaknesses of synthetics
- What can break in real data

11. Solution after EDA
- [ ] Leave the data design unchanged
- [ ] / Amplify the noise
- [ ] / Adjust the generation
- [ ] Move on to modeling