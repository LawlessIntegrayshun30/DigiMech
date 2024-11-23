## ui.py
import tkinter as tk
from tkinter import messagebox
from diagnostics import Diagnostics

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vehicle Diagnostic System")
        self.diagnostics = Diagnostics()
        self.create_widgets()

    def start_ui(self):
        """
        Start the user interface.
        """
        self.root.mainloop()

    def create_widgets(self):
        """
        Create the UI widgets.
        """
        # Text box for user to enter symptoms
        self.symptoms_entry_label = tk.Label(self.root, text="Enter Symptoms:")
        self.symptoms_entry_label.pack()
        self.symptoms_entry = tk.Text(self.root, height=5, width=50)
        self.symptoms_entry.pack()

        # Button to diagnose symptoms
        self.diagnose_button = tk.Button(self.root, text="Diagnose Symptoms", command=self.on_diagnose_symptoms)
        self.diagnose_button.pack()

        # Button to diagnose OBD data
        self.diagnose_obd_button = tk.Button(self.root, text="Diagnose OBD Data", command=self.on_diagnose_obd_data)
        self.diagnose_obd_button.pack()

        # Output area for diagnosis results
        self.results_label = tk.Label(self.root, text="Diagnosis Results:")
        self.results_label.pack()
        self.results_text = tk.Text(self.root, height=15, width=50, state=tk.DISABLED)
        self.results_text.pack()

    def on_diagnose_symptoms(self):
        """
        Handle the event when the 'Diagnose Symptoms' button is clicked.
        """
        symptoms = self.symptoms_entry.get("1.0", tk.END).strip()
        if symptoms:
            diagnosis = self.diagnostics.diagnose_symptoms(symptoms)
            self.display_results(diagnosis)
        else:
            messagebox.showwarning("Warning", "Please enter symptoms before diagnosing.")

    def on_diagnose_obd_data(self):
        """
        Handle the event when the 'Diagnose OBD Data' button is clicked.
        """
        diagnosis = self.diagnostics.diagnose_obd_data()
        self.display_results(diagnosis)

    def display_results(self, results: str):
        """
        Display the diagnostic results in the results text area.

        :param results: A string with the diagnosis result.
        """
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete("1.0", tk.END)
        self.results_text.insert(tk.END, results)
        self.results_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    ui = UI()
    ui.start_ui()
