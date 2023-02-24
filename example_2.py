import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview

app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
colors = app.style.colors

main_frame = ttk.Frame(app, padding=(20,10))
main_frame.pack(fill=BOTH, expand=YES)

data=[]

 # form variables
name_val = ttk.StringVar(value="")
student_id_val = ttk.StringVar(value="")
course_name_val = ttk.StringVar(value="")
final_score_val = ttk.IntVar(value=0)

# form header
instruction_text = "Please enter your contact information" 
instruction = ttk.Label(app, text=instruction_text, width=50)
instruction.pack(fill=X, pady=10)

def initialize_meter(app, int_variable):
    meter = ttk.Meter(
    metersize=100,
    padding=5,
    amounttotal=100,
    amountused=50,
    metertype="full",
    subtext="Final Score",
    interactive=True,
    )

    meter.pack()

    final_score_label = ttk.Label(text="Final Score: ", width=10)
    final_score_label.pack(side=LEFT, padx=5)

    int_variable.set(meter.amountusedvar)

    final_score_input = ttk.Entry(textvariable=meter.amountusedvar)
    final_score_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

    return meter

def initialize_table(app, data):
    coldata = [
        {"text": "Name"},
        {"text": "Student ID", "stretch": False},
        {"text": "Course Name"},
        {"text": "Final Score", "stretch": False}
    ]

    dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=data,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
    return

def create_form_entry(app, label, string_variable):
    form_field_container = ttk.Frame(app)
    form_field_container.pack(fill=X, expand=YES, pady=5)

    form_field_label = ttk.Label(master=form_field_container, text=label.title(), width=10)
    form_field_label.pack(side=LEFT, padx=5)

    form_input = ttk.Entry(master=form_field_container, textvariable=string_variable)
    form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

def on_submit(app):
        """Print the contents to console and return the values."""
        name = name_val.get()
        student_id = student_id_val.get()
        course_name = course_name_val.get()
        final_score = final_score_val.get()


        print("Name:", name)
        print("Student ID: ", student_id)
        print("Course Name:", course_name)
        print("Final Score:", final_score)

        toast = ToastNotification(
        title="Submission successful!",
        message="Your data has been successfully submitted.",
        duration=3000,
        )

        toast.show_toast()

        data.append((name, student_id, course_name, final_score))

        return name, student_id, course_name, final_score

def on_cancel(app):
    """Cancel and close the application."""
    app.quit()

def create_buttonbox(app):
    button_container = ttk.Frame(app)
    button_container.pack(fill=X, expand=YES, pady=(15, 10))

    submit_btn = ttk.Button(
        master=button_container,
        text="Submit",
        command=on_submit(app),
        bootstyle=SUCCESS,
        width=6,
    )
    submit_btn.pack(side=RIGHT, padx=5)
    submit_btn.focus_set()

    cancel_btn = ttk.Button(
        master=button_container,
        text="Cancel",
        command=on_cancel(app),
        bootstyle=DANGER,
        width=6,
    )

    cancel_btn.pack(side=RIGHT, padx=5)

# form entries
create_form_entry(app, "Name: ", name_val)
create_form_entry(app, "Student ID: ", student_id_val)
create_form_entry(app, "Course Name: ", course_name_val)
# update the amount used with another widget
meter = initialize_meter(app, final_score_val)

app.mainloop()