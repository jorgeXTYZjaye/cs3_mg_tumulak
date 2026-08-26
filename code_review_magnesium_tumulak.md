### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: \_Magnesium\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_         Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name:\_Jorgiena Tumulak\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	Date: \_\_\_\_\_\_\_\_\_\_\_\_\_**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

The Binary search is faster than the Linear search when dealing with very large lists. This difference in speed comes down to how both of them navigate the search space. Linear search checks all numbers one by one from left to right, while Binary search starts in the middle.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ | How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

At first glance, Linear search looks easier to understand. It is easier because the code is simple and short, using a simple for loop that checks one element at a time. Binary search is harder to follow because you have to keep track of multiple changing variable.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Linear search would be easier to update. Its structure is very straightforward, with only one simple condition checking for the target. You can change what happens when the item is found without risking breaking complex loop variables,making errors much less likely. In Binary search it uses multiple pointers and conditions making it hard to update, modifying logic inside the while loop can easily break how the search splits the list, and there is also a higher risk of bugs like infinite loops.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ | ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Linear search is easier to test with different inputs. It works on any list without requiring the data to be sorted first. It also has fewer conditions to check, making it simpler to test and less logic errors. Binary search is harder to test because it requires the input to be presorted. However, it is easier to test performance with very large inputs because it runs so much faster.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ | ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

To avoid errors, both Linear search and Binary search should check if the list is empty and verify that inputs are valid data types, while Binary search needs to check that the list is already sorted before running.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search?~~ | ~~Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search?~~ |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

I would choose Binary search for this problem because it is faster and more efficient when dealing with large data sets. However, Linear search would be more suitable if the list is small, unsorted, or continuously changing, as it doesnt require presorting and is simpler to read,test, and modify.