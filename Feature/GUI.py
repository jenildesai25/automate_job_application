import tkinter as tk
from tkinter import filedialog
from Feature import LinkedInEasyApply


class GUI:

    def __init__(self, master):
        self.master = master
        master.title = "Job apply"
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, rowspan=13, columnspan=3, sticky='nsew')
        self._create_var_field_for_text_area()
        self._validate_text_area_field()
        self._create_email_component()
        self._create_linkedin_component()
        self._create_desired_job_component()
        self._create_city_entry_component()
        self._create_state_entry_component()
        self._create_phone_number_component()
        self._create_num_loops_component()
        self._create_resume_path_component()
        self._create_submit_button_component()

    def _create_var_field_for_text_area(self):
        self.email_address_var = tk.StringVar(self.master)
        self.email_password_var = tk.StringVar(self.master)
        self.linkedin_username_var = tk.StringVar(self.master)
        self.linkedin_password_var = tk.StringVar(self.master)
        self.desired_job_title_var = tk.StringVar(self.master)
        self.location_city_var = tk.StringVar(self.master)
        self.location_state_var = tk.StringVar(self.master)
        self.phone_number_var = tk.StringVar(self.master)
        self.page_limit_var = tk.StringVar(self.master)
        self.resume_path_var = tk.StringVar(self.master)

    def _validate_text_area_field(self):
        self.email_address_var.trace("w", self.validate)
        self.email_password_var.trace("w", self.validate)
        self.linkedin_username_var.trace("w", self.validate)
        self.linkedin_password_var.trace("w", self.validate)
        self.desired_job_title_var.trace("w", self.validate)
        self.location_city_var.trace("w", self.validate)
        self.location_state_var.trace("w", self.validate)
        self.phone_number_var.trace("w", self.validate)
        self.page_limit_var.trace("w", self.validate)
        self.resume_path_var.trace("w", self.validate)
        # self.stringvar10 = tk.StringVar(self.master)

    def _create_email_component(self):
        self.email_entry = tk.Entry(self.frame, textvariable=self.email_address_var)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.email_entry_label = tk.Label(self.frame, text="Email Address:")
        self.email_entry_label.grid(row=0, column=0, sticky=tk.W)

        self.email_pass_entry = tk.Entry(self.frame, textvariable=self.email_password_var)
        self.email_pass_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.email_pass_label = tk.Label(self.frame, text="Email Password:")
        self.email_pass_label.grid(row=1, column=0, sticky=tk.W)

    def _create_linkedin_component(self):
        self.linkedin_username_entry = tk.Entry(self.frame, textvariable=self.linkedin_username_var)
        self.linkedin_username_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.linkedin_username_label = tk.Label(self.frame, text="LinkedIn Username:")
        self.linkedin_username_label.grid(row=2, column=0, sticky=tk.W)

        self.linkedin_password_entry = tk.Entry(self.frame, textvariable=self.linkedin_password_var)
        self.linkedin_password_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.linkedin_password_label = tk.Label(self.frame, text="LinkedIn Password:")
        self.linkedin_password_label.grid(row=3, column=0, sticky=tk.W)

    def _create_desired_job_component(self):
        self.desired_job_title_entry = tk.Entry(self.frame, textvariable=self.desired_job_title_var)
        self.desired_job_title_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.desired_job_title_label = tk.Label(self.frame, text="Desired Job Title:")
        self.desired_job_title_label.grid(row=4, column=0, sticky=tk.W)

    def _create_city_entry_component(self):
        self.city_entry = tk.Entry(self.frame, textvariable=self.location_city_var)
        self.city_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.city_label = tk.Label(self.frame, text="Location City:")
        self.city_label.grid(row=6, column=0, sticky=tk.W)

    def _create_state_entry_component(self):
        self.state_entry = tk.Entry(self.frame, textvariable=self.location_state_var)
        self.state_entry.grid(row=7, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.state_label = tk.Label(self.frame, text="Location State:")
        self.state_label.grid(row=7, column=0, sticky=tk.W)

    def _create_phone_number_component(self):
        self.phone_number_entry = tk.Entry(self.frame, textvariable=self.phone_number_var)
        self.phone_number_entry.grid(row=8, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.phone_label = tk.Label(self.frame, text="Your Phone Number:")
        self.phone_label.grid(row=8, column=0, sticky=tk.W)

    def _create_num_loops_component(self):
        self.num_loops_label = tk.Label(self.frame, text="Page Limit:")
        self.num_loops_label.grid(row=9, column=0, sticky=tk.W)
        self.num_loops = tk.Entry(self.frame, textvariable=self.page_limit_var)
        self.num_loops.grid(row=9, column=1, sticky=tk.N + tk.S + tk.E + tk.W, padx=5, pady=5)

    def _create_resume_path_component(self):
        self.resume_path = tk.Entry(self.frame, textvariable=self.resume_path_var)
        self.resume_path.grid(row=10, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)
        self.resume_path_label = tk.Label(self.frame, text="Resume Path:")
        self.resume_path_label.grid(row=10, column=0, sticky=tk.W)
        self.resume_path.configure(state="readonly")
        self._create_resume_button_component()

    def _create_resume_button_component(self):
        self.resume_button = HoverButton(self.frame, text='Browse Resume', activebackground='lightgrey',
                                         command=self.askopenfileResume)
        self.resume_button.grid(row=10, column=2, sticky=tk.N + tk.S + tk.E + tk.W, padx=5, pady=5)

    def _create_submit_button_component(self):
        self.submit_button = HoverButton(self.frame, text="Submit", activebackground='lightgrey', command=self.apply,
                                         state=tk.DISABLED)
        self.submit_button.grid(row=12, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W, padx=5, pady=5)

    def askopenfileResume(self):
        f = filedialog.askopenfile(mode='r')
        if f:
            filename = f.name

            self.resume_path.configure(state="normal")
            self.resume_path.delete(0, 'end')
            self.resume_path.insert(0, filename)
            self.resume_path.configure(state="readonly")
            print(filename)

    def validate(self, *args):
        email_address_validate = self.email_address_var.get()
        email_password_validate = self.email_password_var.get()
        linkedin_username_validate = self.linkedin_username_var.get()
        linkedin_password_validate = self.linkedin_password_var.get()
        desired_job_title_validate = self.desired_job_title_var.get()
        location_city_validate = self.location_city_var.get()
        location_state_validate = self.location_state_var.get()
        phone_number_validate = self.phone_number_var.get()
        page_limit_validate = self.page_limit_var.get()
        resume_path_validate = self.resume_path_var.get()

        if email_address_validate and email_password_validate and \
                linkedin_username_validate \
                and linkedin_password_validate \
                and desired_job_title_validate and \
                location_city_validate and \
                location_state_validate and \
                phone_number_validate and \
                page_limit_validate and \
                resume_path_validate:
            self.submit_button.config(state='normal')
        else:
            self.submit_button.config(state='disabled')

    def apply(self):
        print('in apply function')
        linkedin_easy_apply_obj = LinkedInEasyApply.LinkedInEasyApply(email_address=self.email_address_var.get(),
                                                                      email_password=self.email_password_var.get(),
                                                                      linkedin_username=self.linkedin_username_var.get(),
                                                                      linkedin_password=self.linkedin_password_var.get(),
                                                                      desired_job_title=self.desired_job_title_var.get(),
                                                                      city=self.location_city_var.get(),
                                                                      state=self.location_state_var.get(),
                                                                      phone_number=self.phone_number_var.get(),
                                                                      page_limit=self.page_limit_var.get(),
                                                                      resume_path=self.resume_path_var.get())
        linkedin_easy_apply_obj.login()
        linkedin_easy_apply_obj.search_for_jobs()


class HoverButton(tk.Button):
    """HoverButton class to change color of button when hovering.

    Attributes:
        defaultBackground: Background instance of window
        defaultForeground: Foreground instance of window
        bind: Event to trigger color change of button

    """

    def __init__(self, master, **kw):
        """Inits SampleClass with master widget."""
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """Hover over button event"""
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        """Hover off button event"""
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

# if __name__ == '__main__':
#     root = tk.tk()
#     obj_ = MyGUI(root)
#     root.mainloop()
