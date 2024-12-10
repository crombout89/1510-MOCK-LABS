# Voting System

## Objective
This program analyzes a voting system to determine:
1. How many **registered voters** actually voted.
2. How many **registered voters** didn’t vote.
3. How many **unregistered people** tried to vote.

---

## Strategy
We use **sets** to efficiently compare registered voters and votes cast. Sets allow us to find overlaps and differences between the groups using simple operations like intersections and subtractions.

---

## Methodology
### 1. Inputs
- `registered_voters`: A set of IDs of voters who are registered.
- `votes_cast`: A set of IDs of people who tried to vote.

### 2. Steps to Solve
1. **Validate the inputs**:
   - Ensure both inputs are sets.
   - If they are not, raise an error so that invalid inputs are not processed.

2. **Find registered voters who voted**:
   - Use the **intersection** of `registered_voters` and `votes_cast` to find IDs that appear in both sets.

3. **Find registered voters who didn’t vote**:
   - Subtract `votes_cast` from `registered_voters` to get IDs that exist only in `registered_voters`.

4. **Find unregistered people who tried to vote**:
   - Subtract `registered_voters` from `votes_cast` to get IDs that exist only in `votes_cast`.

5. **Return results** as a dictionary:
   - `"voted_count"`: Number of registered voters who voted.
   - `"non_voters_count"`: Number of registered voters who didn’t vote.
   - `"unregistered_voters_count"`: Number of unregistered people who tried to vote.

---

## Example
### Input:
```python
registered_voters = {"Alice", "Bob", "Charlie"}
votes_cast = {"Alice", "Eve", "Charlie", "Frank"}

...
# OUTPUT
{
    "voted_count": 2,
    "non_voters_count": 1,
    "unregistered_voters_count": 2
}
```
---
### Key Concepts to Remember
- Sets are powerful for comparing groups of data.
- Intersection (&) finds common elements.
- Difference (-) finds elements in one set but not the other.

---
