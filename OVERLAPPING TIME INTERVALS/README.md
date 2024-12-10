---

### **Lab 2: Time Interval Overlap**
#### **README.md**
```markdown
# Time Interval Overlap

## Objective
This program determines if two employees' work shifts overlap. If they do, it calculates the **total overlapping time** in minutes.

---

## Strategy
We treat the work shifts as intervals on a number line. To find the overlap:
1. The overlap **starts** at the later of the two start times.
2. The overlap **ends** at the earlier of the two end times.

If the start time of the overlap is greater than or equal to the end time, there is no overlap.

---

## Methodology
### 1. Inputs
- `shift_a`: A tuple representing the start and end times of Employee A’s shift (in hours, 24-hour format).
- `shift_b`: A tuple representing the start and end times of Employee B’s shift.

### 2. Steps to Solve
1. **Validate the inputs**:
   - Ensure both inputs are tuples of size 2.
   - Ensure the values are integers representing hours.

2. **Find the overlap interval**:
   - Overlap starts at the later of the two start times: `max(start_a, start_b)`.
   - Overlap ends at the earlier of the two end times: `min(end_a, end_b)`.

3. **Check if there is an overlap**:
   - If the overlap start time is less than the overlap end time, calculate the duration as:
     ```python
     overlap_minutes = (overlap_end - overlap_start) * 60
     ```

4. **Return the result**:
   - Return the total overlapping time in minutes.
   - If there is no overlap, return `0`.

---

## Example
### Input:
```python
shift_a = (9, 17)  # 9 AM to 5 PM
shift_b = (13, 21) # 1 PM to 9 PM

...
# OUTPUT
240  # 4 hours of overlap (13:00 to 17:00), converted to minutes
```
---
### Key Concepts to Remember
- max(start_a, start_b): Finds the later start time.
- min(end_a, end_b): Finds the earlier end time.
- If the overlap start is greater than or equal to the overlap end, there is no overlap.