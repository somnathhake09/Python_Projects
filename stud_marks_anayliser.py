from functools import reduce

# Step 1: Student data
students = [
    {"name": "Somnath", "marks": [85, 90, 78]},
    {"name": "Dikshu", "marks": [92, 88, 95]},
    {"name": "Athrava", "marks": [45, 60, 55]},
    {"name": "Bhavana", "marks": [70, 65, 72]},
    {"name": "Diksha", "marks": [95, 98, 92]},
]

# Step 2: Lambda functions for total & percentage
calculate_total = lambda marks: sum(marks)
calculate_percentage = lambda marks: (sum(marks) / (len(marks) * 100)) * 100

# Step 3: map() to add total & percentage
students = list(map(lambda s: {**s, "total": calculate_total(s["marks"]),
                                "percentage": calculate_percentage(s["marks"])}, students))

# Step 4: Grade assign karne ke liye lambda + map
get_grade = lambda pct: "A" if pct >= 90 else "B" if pct >= 75 else "C" if pct >= 60 else "F"
students = list(map(lambda s: {**s, "grade": get_grade(s["percentage"])}, students))

# Step 5: filter() se toppers aur fail students
toppers = list(filter(lambda s: s["percentage"] >= 90, students))
failed = list(filter(lambda s: s["grade"] == "F", students))

# Step 6: reduce() se class topper aur average
class_topper = reduce(lambda a, b: a if a["percentage"] > b["percentage"] else b, students)
total_percentage_sum = reduce(lambda acc, s: acc + s["percentage"], students, 0)
class_average = total_percentage_sum / len(students)

# Step 7: sorted() mein lambda key se ranking
ranked_students = sorted(students, key=lambda s: s["percentage"], reverse=True)

# Step 8: Print results
print("=== Student Marks Analyzer ===\n")
for rank, s in enumerate(ranked_students, start=1):
    print(f"{rank}. {s['name']} - Total: {s['total']}, Percentage: {s['percentage']:.2f}%, Grade: {s['grade']}")

print(f"\nClass Topper: {class_topper['name']} with {class_topper['percentage']:.2f}%")
print(f"Class Average: {class_average:.2f}%")
print(f"\nToppers (>=90%): {[s['name'] for s in toppers]}")
print(f"Failed Students: {[s['name'] for s in failed]}")