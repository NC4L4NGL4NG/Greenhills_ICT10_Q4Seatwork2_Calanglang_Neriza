from pyscript import display, document

classmates = [
    {"name": "Adrianna", "section": "Sapphire", "subject": "Math"},
    {"name": "Sca", "section": "Sapphire", "subject": "English"},
    {"name": "Jaiyanah", "section": "Ruby", "subject": "Math"},
    {"name": "Michaela", "section": "Sapphire", "subject": "SS"},
    {"name": "Harvey", "section": "Sapphire", "subject": "Science"},
]

def add_classmate(event):
    name_input = document.getElementById("nameInput")
    section_input = document.getElementById("sectionInput")
    subject_input = document.getElementById("subjectInput")
    
    name = name_input.value
    section = section_input.value
    subject = subject_input.value

    if name and section and subject:
        new_person = {
            "name": name,
            "section": section,
            "subject": subject
        }
        classmates.append(new_person)
        
        name_input.value = ""
        section_input.value = ""
        subject_input.value = ""
        
        display(f"✅ {name} is now added!", target="listOutput", append=False)

def show_list(event):
    output_div = document.getElementById("listOutput")
    output_div.innerHTML = "<h3>📋 Classmate List</h3>"
    
    for i, person in enumerate(classmates, 1):
        formatted_entry = f"{i}) {person['name']}, {person['section']}, I love {person['subject']}"
        display(formatted_entry, target="listOutput", append=True)