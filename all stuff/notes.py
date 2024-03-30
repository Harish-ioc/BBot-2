def add_note(note):
    with open('notes.txt', 'a') as file:
        file.write(note + '\n')

def list_notes():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            print("List of Notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note}")
        else:
            print("No notes found.")

def latest_note():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            latest = notes[-1]
            print("Latest Note:")
            print(latest)
        else:
            print("No notes found.")

def oldest_note():
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
        if notes:
            oldest = notes[0]
            print("Oldest Note:")
            print(oldest)
        else:
            print("No notes found.")

def delete_note_by_number(note_number):
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
    
    if 0 < note_number <= len(notes):
        del notes[note_number - 1]
        with open('notes.txt', 'w') as file:
            file.writelines(notes)
        print("Note deleted successfully.")
    else:
        print("Note number out of range. No note deleted.")

def delete_note_by_content(content):
    with open('notes.txt', 'r') as file:
        notes = file.readlines()
    
    filtered_notes = [note for note in notes if content not in note]
    with open('notes.txt', 'w') as file:
        file.writelines(filtered_notes)
    print("Notes containing the specified content are deleted.")

def clear_notes():
    open('notes.txt', 'w').close()
    print("All notes cleared.")

while True:
    user_input = input("Enter your command (add note / what are the notes / what is the latest note / what is the oldest note / delete note by number / delete note by content / clear all notes): ")

    if user_input == 'add note':
        new_note = input("Enter your note: ")
        add_note(new_note)
    elif user_input == 'what are the notes':
        list_notes()
    elif user_input == 'what is the latest note':
        latest_note()
    elif user_input == 'what is the oldest note':
        oldest_note()
    elif user_input == 'delete note by number':
        note_num = int(input("Enter the note number to delete: "))
        delete_note_by_number(note_num)
    elif user_input == 'delete note by content':
        content_to_delete = input("Enter the content to delete: ")
        delete_note_by_content(content_to_delete)
    elif user_input == 'clear all notes':
        clear_notes()
    else:
        print("Invalid command. Please try again.")
