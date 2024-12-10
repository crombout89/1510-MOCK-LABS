# Inventory Management

## Objective
This program merges the inventories of two warehouses. If the same item exists in both warehouses, their quantities are summed up.

---

## Strategy
We use **dictionaries** to represent inventories, where the keys are item names and the values are quantities. We iterate over both dictionaries to combine the inventories efficiently.

---

## Methodology
### 1. Inputs
- `warehouse_a`: A dictionary where keys are item names and values are quantities.
- `warehouse_b`: Another dictionary with the same structure.

### 2. Steps to Solve
1. **Validate the inputs**:
   - Ensure both inputs are dictionaries.
   - If they are not, raise an error so invalid inputs are caught early.

2. **Merge the inventories**:
   - Create a new dictionary to store the combined inventory.
   - Add all items from `warehouse_a` to the new dictionary.
   - For each item in `warehouse_b`:
     - If the item already exists in the new dictionary, add its quantity to the existing value.
     - Otherwise, add the item to the new dictionary.

3. **Return the merged inventory**:
   - Return the dictionary with the combined inventory.

---

## Example
### Input:
```python
warehouse_a = {"apples": 10, "bananas": 5, "oranges": 7}
warehouse_b = {"bananas": 8, "grapes": 15, "oranges": 3}

...
# OUTPUT:
{
    "apples": 10,
    "bananas": 13,
    "oranges": 10,
    "grapes": 15
}
```

### Key Concepts to Remember
- Use a for loop to iterate through dictionary keys and values.
To combine inventories:
- If the item exists in both, sum the quantities.
- If the item exists in only one, add it directly.

---