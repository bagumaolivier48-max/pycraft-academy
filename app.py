from flask import Flask, render_template, request

app = Flask(__name__)

MODULES = {
    "beginner-python": {
        "title": "Beginner Python",
        "description": "Master the absolute core fundamentals of Python programming.",
        "lessons": [
            {
                "id": "variables",
                "title": "Variables and Data Types",
                "content": "Variables are containers for storing data values. Python has no command for declaring a variable; a variable is created the moment you first assign a value to it.",
                "code_example": '# Creating variables\nname = "Alice"\nage = 16\nis_student = True\n\nprint(name)\nprint(age)',
            },
            {
                "id": "strings",
                "title": "Strings and String Types",
                "content": "Strings in Python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as \"hello\".",
                "code_example": 'single_quote = \'Hello\'\ndouble_quote = "World"\nprint(single_quote + double_quote)',
            },
            {
                "id": "string-methods",
                "title": "String Methods",
                "content": "Python has built-in methods like .upper(), .lower(), .strip(), and .replace() to manipulate text easily.",
                "code_example": 'text = "  Hello, Python!  "\nprint(text.strip())\nprint(text.upper())\nprint(text.replace("Python", "World"))',
            },
            {
                "id": "loops",
                "title": "Loops (for and while)",
                "content": "Python has two primitive loop commands: 'for loops' for iterating over a sequence, and 'while loops' for repeating as long as a condition is true.",
                "code_example": "# For loop\nfor i in range(3):\n    print('Counting')\n\n# While loop\ncount = 0\nwhile count < 2:\n    print('Looping')\n    count += 1",
            },
            {
                "id": "functions",
                "title": "Functions",
                "content": "A function is a block of code which only runs when called. Use the 'def' keyword to create a function.",
                "code_example": 'def greet_student(name):\n    return f"Welcome, {name}!"\n\nprint(greet_student("Olivier"))',
            },
        ],
    },
    "flask-basics": {
        "title": "Flask Basics",
        "description": "Learn how to build dynamic web applications using Python and Flask.",
        "lessons": [
            {
                "id": "intro-flask",
                "title": "Setting Up Flask",
                "content": "Flask is a lightweight WSGI web application framework in Python designed to make getting started quick and easy.",
                "code_example": "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)",
            }
        ],
    },
    "html-css-challenges": {
        "title": "HTML/CSS Challenges",
        "description": "Understand the structure and design layers behind web pages.",
        "lessons": [
            {
                "id": "html-structure",
                "title": "Building Web Elements",
                "content": "HTML uses tags like <h1>, <p>, and <a> to structure text and links in a browser.",
                "code_example": "<!DOCTYPE html>\n<html>\n  <body>\n    <h1>Welcome to PyCraft</h1>\n    <p>Learning web development step by step.</p>\n  </body>\n</html>",
            }
        ],
    },
}

@app.route("/")
def index():
    return render_template("index.html", modules=MODULES)

@app.route("/lesson/<module_id>/<lesson_id>")
def lesson(module_id, lesson_id):
    mod = MODULES.get(module_id)
    if not mod:
        return "Module not found", 404
    
    current_lesson = next((l for l in mod["lessons"] if l["id"] == lesson_id), None)
    if not current_lesson:
        return "Lesson not found", 404
        
    return render_template("lesson.html", module=mod, lesson=current_lesson, module_id=module_id)

@app.route("/practice", methods=["GET", "POST"])
def practice():
    output = None
    user_code = ""
    if request.method == "POST":
        user_code = request.form.get("code", "")
        try:
            if "print(" in user_code:
                output = "Code executed successfully! Simulated output:\n" + user_code.split("print(")[-1].split(")")[0].strip('"\'')
            else:
                output = "Code ran successfully with no print output."
        except Exception as e:
            output = f"Error in code execution: {str(e)}"
            
    return render_template("practice.html", output=output, user_code=user_code)

if __name__ == "__main__":
    app.run(debug=True)