# f = open("fahim2.txt","w")


# a = f.write("My age is 7 years old!")

# print(a) #to see how many letters i've written in the line

# #outputs 22

# f.close()


'''
Your code isn’t working because of a couple of fundamental mistakes in how file handling works in Python. Let’s fix them step by step.

---

### 🔴 Problem 1: Wrong file mode (`"w"`)

You opened the file with:

```python
f = open("fahim2.txt", "w")
```

* `"w"` = **write mode only**
* You **cannot read** from a file opened in `"w"` mode

---

### 🔴 Problem 2: Wrong usage of `read()`

```python
content = f.read("fahim2.txt","t")
```

* `read()` **does NOT take filename or mode as arguments**
* It only optionally takes a number of bytes (like `read(10)`)

---

### 🔴 Problem 3: File pointer position

After writing, the cursor is at the **end of the file**, so even if reading worked, it would return empty unless you move it.

---

## ✅ Correct Version (Option 1: Use `w+`)

```python
f = open("fahim2.txt", "w+")

f.write("My age is 7 years old!")
f.seek(0)   # move cursor to beginning

content = f.read()
print(content)

f.close()
```

---

## ✅ Correct Version (Option 2: Better practice)

```python
# Write first
with open("fahim2.txt", "w") as f:
    f.write("My age is 7 years old!")

# Then read
with open("fahim2.txt", "r") as f:
    content = f.read()
    print(content)
```

---

### 💡 Key Takeaways

* `"w"` → write only
* `"r"` → read only
* `"w+"` → write + read
* `read()` → no filename inside
* Use `seek(0)` to go back to start

---

If you want, I can show you a **clean pattern for file handling in exams/interviews** so you don’t lose marks 👍

'''


# for both reading and write both 

f = open("fahim2.txt", "r+")

print(f.read())

f.write("Thank You!")