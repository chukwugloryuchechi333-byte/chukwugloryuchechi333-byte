# Glory's AI Memory - Day 4
print("--- Glory's AI Classroom Memory ---")

students = []

for i in range(1, 4):
    name = input(f"Enter student {i} name: ")
    students.append(name)
    print(f" -> AI memorized: {name}")

print(f"\nAI now remembers {len(students)} students:")
for s in students:
    print(f" - {s}")

search = input("\nSearch for student: ")
if search in students:
    print(f"✅ Found {search} in AI memory!")
else:
    print(f"❌ {search} not found")

print(f"\nFirst student: {students[0]}")
print(f"Last student: {students[-1]}")
print("\nGlory's AI brain is working!")
